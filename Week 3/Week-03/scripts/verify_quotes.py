#!/usr/bin/env python3
"""Verify that quoted text actually exists on its stated page.

Reads 02_sources/text/<source>/page_NNNN.txt (written by extract_text.py)
and checks each quote appears there, after normalizing whitespace, line
breaks, end-of-line hyphenation, ligatures (fi/fl/ffi/...) and curly quotes
on BOTH sides — a quote copied out of a PDF often has a hyphen break or a
curly apostrophe that the source text doesn't render the same way, and that
is not the same thing as the quote being wrong.

Two ways to check quotes:
  1. A batch file of citations (the normal, real-usage path — one run
     covers everything reviewer-factchecker needs to check):
       python verify_quotes.py --citations 05_review/citations.json
     writes 05_review/verification.md (the [Claim | Source file | Page |
     Match | Issue] table from the spec) and prints a summary.
  2. A single ad-hoc check, for testing or a quick spot-check:
       python verify_quotes.py --quote "..." --source Smith2024_Title --page 3

MANUAL FALLBACK: open 02_sources/pdf/<source>.pdf at the stated page and
read the quote against it by eye. The normalization this script does is a
convenience, not a different standard — a human check is always the
fallback of record.

Usage:
    python verify_quotes.py --citations 05_review/citations.json
    python verify_quotes.py --quote "exact text" --source Smith2024_Title --page 3
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT_DIR = ROOT / "02_sources" / "text"
VERIFICATION_MD = ROOT / "05_review" / "verification.md"

LIGATURES = {
    "ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl",
}
CURLY_QUOTES = {
    "‘": "'", "’": "'", "“": '"', "”": '"',
}


def normalize(text: str) -> str:
    for lig, plain in LIGATURES.items():
        text = text.replace(lig, plain)
    for curly, straight in CURLY_QUOTES.items():
        text = text.replace(curly, straight)
    # De-hyphenate line-end breaks: "exam-\nple" -> "example"
    text = re.sub(r"-\s*\n\s*", "", text)
    # Collapse all remaining whitespace (newlines included) to single spaces
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def load_page_text(source: str, page: int) -> str | None:
    page_path = TEXT_DIR / source / f"page_{page:04d}.txt"
    if not page_path.exists():
        return None
    return page_path.read_text(encoding="utf-8")


def check_one(quote: str, source: str, page: int) -> tuple[str, str]:
    """Returns (match|no-match|error, issue)."""
    page_text = load_page_text(source, page)
    if page_text is None:
        available = TEXT_DIR / source
        hint = (
            f"no extracted text for {source} page {page} "
            f"(run extract_text.py first; {available} "
            + ("exists" if available.exists() else "does not exist")
            + ")"
        )
        return "error", hint
    if normalize(quote) in normalize(page_text):
        return "match", ""
    return "no-match", "quote not found on stated page after normalization"


def cmd_single(args) -> None:
    status, issue = check_one(args.quote, args.source, args.page)
    print(f"{status.upper()}: \"{args.quote}\" — {args.source} p.{args.page}")
    if issue:
        print(f"  {issue}")
    sys.exit(0 if status == "match" else 1)


def cmd_batch(args) -> None:
    # utf-8-sig: strips a UTF-8 BOM if present (common from Windows editors,
    # including PowerShell's own `Out-File -Encoding utf8`), harmless if not.
    citations = json.loads(Path(args.citations).read_text(encoding="utf-8-sig"))
    rows = []
    n_match = 0
    for c in citations:
        status, issue = check_one(c["quote"], c["source"], c["page"])
        n_match += status == "match"
        rows.append(
            {
                "id": c.get("id", ""),
                "quote": c["quote"],
                "source": c["source"],
                "page": c["page"],
                "status": status,
                "issue": issue,
            }
        )
        print(f"  [{status.upper()}] {c.get('id', '')} — {c['source']} p.{c['page']}")

    VERIFICATION_MD.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Verification", "", "| Claim | Source file | Page | Match | Issue |", "|---|---|---|---|---|"]
    for r in rows:
        claim = r["quote"].replace("|", "\\|")
        lines.append(f"| {claim} | {r['source']} | {r['page']} | {r['status']} | {r['issue']} |")
    VERIFICATION_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"\n{n_match}/{len(rows)} matched. Wrote {VERIFICATION_MD}.")
    sys.exit(0 if n_match == len(rows) else 1)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--citations", help="JSON file: list of {id, quote, source, page}")
    parser.add_argument("--quote", help="A single quote to check")
    parser.add_argument("--source", help="Source PDF stem (without .pdf), for --quote")
    parser.add_argument("--page", type=int, help="Page number, for --quote")
    args = parser.parse_args()

    if args.citations:
        cmd_batch(args)
    elif args.quote and args.source and args.page:
        cmd_single(args)
    else:
        parser.error("either --citations FILE, or all of --quote/--source/--page")


if __name__ == "__main__":
    main()
