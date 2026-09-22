#!/usr/bin/env python3
"""Sync sources from a Zotero collection into 02_sources/.

Connects to Zotero's LOCAL API (Zotero desktop must be running, with
Settings > Advanced > "Allow other applications on this computer to
communicate with Zotero" enabled). Pulls items from the given collection
path (e.g. "Academic-Pipeline > week-01"), copies each item's PDF attachment
from the local Zotero storage directory into 02_sources/pdf/, renamed to
AuthorYear_ShortTitle.pdf, sanity-checks that the PDF's text actually
contains the item's DOI, and writes an APA 7 metadata export (using
Zotero's own citation engine, not a hand-rolled formatter) to
02_sources/zotero_export.md and a machine-readable 02_sources/zotero_export.json.

Idempotent / rerunnable: a manifest (02_sources/.sync_manifest.json) tracks
which Zotero item keys have already been synced, so a weekly rerun only
picks up new items and never re-downloads or renames existing files.

MANUAL FALLBACK: if the local API is unreachable or pyzotero isn't
installed, do this by hand in Zotero: select the collection, Export
Collection... > Format: CSV or Better BibTeX, and separately drag each PDF
attachment out of Zotero's storage into 02_sources/pdf/, naming each file
AuthorYear_ShortTitle.pdf yourself. Get the APA reference via right-click >
Create Bibliography from Item... > Style: APA 7th edition, and paste each
one into 02_sources/zotero_export.md by hand.

Usage:
    python sync_sources.py --collection "Academic-Pipeline > week-01"
    python sync_sources.py --collection "Academic-Pipeline > week-01" --dry-run
    python sync_sources.py --list-collections
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from pyzotero import zotero
except ImportError:
    zotero = None

try:
    import pymupdf as fitz
except ImportError:
    fitz = None

ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = ROOT / "02_sources" / "pdf"
SOURCES_DIR = ROOT / "02_sources"
MANIFEST_PATH = SOURCES_DIR / ".sync_manifest.json"
EXPORT_MD = SOURCES_DIR / "zotero_export.md"
EXPORT_JSON = SOURCES_DIR / "zotero_export.json"

ZOTERO_STORAGE = Path.home() / "Zotero" / "storage"


def connect():
    if zotero is None:
        sys.exit(
            "pyzotero is not installed (pip install pyzotero). See the manual fallback "
            "in this script's header for how to sync without it."
        )
    z = zotero.Zotero(library_id=0, library_type="user", local=True)
    try:
        z.collections(limit=1)
    except Exception as exc:  # noqa: BLE001 - surface whatever pyzotero/httpx raised
        sys.exit(
            "Could not reach Zotero's local API. Is Zotero running, with "
            "Settings > Advanced > \"Allow other applications on this computer to "
            f"communicate with Zotero\" enabled? Underlying error: {exc}"
        )
    return z


def all_collections(z) -> list[dict]:
    return z.everything(z.collections())


def resolve_collection_path(z, path_str: str) -> str:
    """Resolve "Parent > Child > ..." to a collection key, case-insensitively."""
    parts = [p.strip() for p in path_str.split(">")]
    cols = all_collections(z)
    by_id = {c["data"]["key"]: c for c in cols}

    def children_of(parent_key):
        return [
            c
            for c in cols
            if (c["data"].get("parentCollection") or False) == (parent_key or False)
        ]

    current_parent = False  # Zotero uses `false` for top-level collections
    matched = None
    for i, part in enumerate(parts):
        candidates = children_of(current_parent)
        matched = next(
            (c for c in candidates if c["data"]["name"].lower() == part.lower()), None
        )
        if matched is None:
            available = ", ".join(sorted(c["data"]["name"] for c in candidates)) or "(none)"
            trail = " > ".join(parts[:i]) or "(root)"
            sys.exit(
                f'Collection "{part}" not found under {trail}. '
                f"Available there: {available}"
            )
        current_parent = matched["data"]["key"]

    return matched["data"]["key"]


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {}


def save_manifest(manifest: dict) -> None:
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def short_title(title: str, max_words: int = 4) -> str:
    words = re.findall(r"[A-Za-z0-9]+", title or "Untitled")[:max_words]
    return "".join(w.capitalize() for w in words) or "Untitled"


def author_surname(creators: list[dict]) -> str:
    for c in creators or []:
        if c.get("creatorType") == "author":
            surname = c.get("lastName") or c.get("name") or "Unknown"
            return re.sub(r"[^A-Za-z]", "", surname) or "Unknown"
    return "Unknown"


def item_year(date_str: str) -> str:
    m = re.search(r"(19|20)\d{2}", date_str or "")
    return m.group(0) if m else "nd"


def find_pdf_attachment(z, item_key: str) -> Path | None:
    children = z.children(item_key)
    for child in children:
        data = child["data"]
        if data.get("itemType") != "attachment":
            continue
        if data.get("contentType") != "application/pdf":
            continue
        filename = data.get("filename")
        attachment_key = data["key"]
        if not filename:
            continue
        candidate = ZOTERO_STORAGE / attachment_key / filename
        if candidate.exists():
            return candidate
    return None


def check_pdf_matches_doi(pdf_path: Path, doi: str) -> str:
    if not doi:
        return "no DOI on record — skipped"
    if fitz is None:
        return "pymupdf not installed — skipped"
    try:
        doc = fitz.open(pdf_path)
        text = "".join(page.get_text() for page in doc[:3])
        doc.close()
    except Exception as exc:  # noqa: BLE001
        return f"could not read PDF: {exc}"
    doi_bare = doi.lower().replace("https://doi.org/", "").strip()
    return "match" if doi_bare in text.lower() else "NO MATCH — verify by hand"


def get_bib_entries(z, collection_key: str, item_keys: list[str]) -> dict[str, str]:
    """Ask Zotero's own citation engine for APA 7 bibliography entries.

    Deliberately NOT using pyzotero's z.item(key, content="bib", ...) here:
    pyzotero always adds format=atom whenever a `content` param is set
    (see pyzotero/_client.py's _build_query), and Zotero's LOCAL API
    rejects atom output outright ("Local API does not support Atom
    output", HTTP 501) — a real incompatibility between the library and
    local mode, not a usage mistake. The local API does support bib
    content through include=data,bib on the plain item endpoint instead,
    so this hits that directly with pyzotero's own HTTP client.
    """
    if not item_keys:
        return {}
    out: dict[str, str] = {}
    for key in item_keys:
        url = f"{z.endpoint}/{z.library_type}/{z.library_id}/items/{key}"
        try:
            resp = z.client.get(url, params={"include": "data,bib", "style": "apa"})
            resp.raise_for_status()
            html = resp.json().get("bib", "")
        except Exception:  # noqa: BLE001
            out[key] = "(APA export failed — generate by hand via Zotero's Create Bibliography)"
            continue
        text = re.sub(r"<[^>]+>", "", html or "").strip()
        out[key] = text or "(empty)"
    return out


def cmd_list_collections(args) -> None:
    z = connect()
    cols = all_collections(z)
    by_id = {c["data"]["key"]: c for c in cols}

    def path_of(c):
        parts = [c["data"]["name"]]
        parent = c["data"].get("parentCollection")
        while parent:
            parent_c = by_id.get(parent)
            if not parent_c:
                break
            parts.insert(0, parent_c["data"]["name"])
            parent = parent_c["data"].get("parentCollection")
        return " > ".join(parts)

    for c in sorted(cols, key=path_of):
        print(path_of(c))


def cmd_sync(args) -> None:
    z = connect()
    collection_key = resolve_collection_path(z, args.collection)
    items = z.everything(z.collection_items_top(collection_key))
    manifest = load_manifest()

    PDF_DIR.mkdir(parents=True, exist_ok=True)
    new_items = [it for it in items if it["data"]["key"] not in manifest]

    print(f"{len(items)} item(s) in \"{args.collection}\", {len(new_items)} new.")
    if not new_items:
        print("Nothing to sync.")
        return

    bibs = get_bib_entries(z, collection_key, [it["data"]["key"] for it in new_items])

    export_lines = []
    export_records = []

    for it in new_items:
        data = it["data"]
        key = data["key"]
        title = data.get("title", "Untitled")
        doi = data.get("DOI", "")
        fname = f"{author_surname(data.get('creators'))}{item_year(data.get('date'))}_{short_title(title)}.pdf"

        pdf_source = find_pdf_attachment(z, key)
        dest = PDF_DIR / fname
        doi_check = "no PDF attachment found"
        if pdf_source:
            if args.dry_run:
                doi_check = "(dry run — not copied)"
            else:
                dest.write_bytes(pdf_source.read_bytes())
                doi_check = check_pdf_matches_doi(dest, doi)

        record = {
            "key": key,
            "title": title,
            "doi": doi,
            "filename": fname,
            "doi_check": doi_check,
            "apa": bibs.get(key, ""),
        }
        export_records.append(record)
        export_lines.append(f"- **{fname}** — {bibs.get(key, title)}  \n  DOI check: {doi_check}")

        if not args.dry_run:
            manifest[key] = {"filename": fname, "title": title}

        print(f"  {fname}: {doi_check}")

    if args.dry_run:
        print("Dry run — no files written, manifest not updated.")
        return

    save_manifest(manifest)

    existing_json = json.loads(EXPORT_JSON.read_text(encoding="utf-8")) if EXPORT_JSON.exists() else []
    EXPORT_JSON.write_text(
        json.dumps(existing_json + export_records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    header = [] if EXPORT_MD.exists() else ["# Zotero export", ""]
    with open(EXPORT_MD, "a", encoding="utf-8") as f:
        if header:
            f.write("\n".join(header) + "\n")
        f.write("\n".join(export_lines) + "\n\n")

    print(f"Synced {len(new_items)} item(s). Updated {EXPORT_MD}, {EXPORT_JSON}, {MANIFEST_PATH}.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--collection", help='Collection path, e.g. "Academic-Pipeline > week-01"')
    group.add_argument("--list-collections", action="store_true", help="List all collection paths and exit")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without writing files")
    args = parser.parse_args()

    if args.list_collections:
        cmd_list_collections(args)
    else:
        cmd_sync(args)


if __name__ == "__main__":
    main()
