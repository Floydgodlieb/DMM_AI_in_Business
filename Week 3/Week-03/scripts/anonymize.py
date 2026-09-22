#!/usr/bin/env python3
"""Anonymize files from 03_data/private/ into 03_data/anonymized/.

LOCAL ONLY. No AI, no network call — a deterministic find-and-replace against
a mapping file, nothing more. This is deliberate: anonymization is the one
step in the whole pipeline that must be trustworthy by construction, not by
review, since everything downstream (data-intake, drafting) depends on it
having already happened.

The mapping file (JSON: {"real name or term": "replacement", ...}) lives in
03_data/private/ alongside the raw data — never in 03_data/anonymized/, since
the mapping is itself the re-identification key. Replacement is literal
substring matching, longest keys first (so "Jane Doe" is replaced before a
shorter "Jane" entry would have a chance to break it into "[X] Doe").

After replacing, does a best-effort residual scan for things that look like
they were missed (emails, phone-like number sequences) and prints them as
warnings — this is a safety net, not a substitute for a human checking the
output before it's trusted. It never blocks the anonymized file from being
written.

MANUAL FALLBACK: open the raw file and the mapping in a text editor, and use
Find & Replace for each mapping entry by hand (longest terms first, same
reason as above), saving the result into 03_data/anonymized/ yourself.

Usage:
    python anonymize.py --map 03_data/private/anonymization_map.json --all
    python anonymize.py --map 03_data/private/anonymization_map.json --input 03_data/private/interview_raw.txt
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRIVATE_DIR = ROOT / "03_data" / "private"
ANON_DIR = ROOT / "03_data" / "anonymized"

RESIDUAL_PATTERNS = {
    "email address": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"),
    "phone-like number": re.compile(r"(?:\+?\d[\d\s().-]{7,}\d)"),
}


def load_map(map_path: Path) -> dict[str, str]:
    mapping = json.loads(map_path.read_text(encoding="utf-8-sig"))
    if not isinstance(mapping, dict) or not mapping:
        sys.exit(f"{map_path} should be a non-empty JSON object of {{real term: replacement}}.")
    return mapping


def anonymize_text(text: str, mapping: dict[str, str]) -> str:
    # Longest keys first so a short entry can't fragment a longer one it's a
    # substring of (e.g. "Jane" inside "Jane Doe").
    for term in sorted(mapping, key=len, reverse=True):
        text = text.replace(term, mapping[term])
    return text


def residual_flags(text: str) -> list[str]:
    flags = []
    for label, pattern in RESIDUAL_PATTERNS.items():
        hits = pattern.findall(text)
        if hits:
            flags.append(f"{label}: {len(hits)} possible instance(s) still present, e.g. {hits[0]!r}")
    return flags


def anonymize_one(src: Path, mapping: dict[str, str]) -> None:
    text = src.read_text(encoding="utf-8-sig")
    result = anonymize_text(text, mapping)

    dest = ANON_DIR / src.relative_to(PRIVATE_DIR)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(result, encoding="utf-8")

    flags = residual_flags(result)
    print(f"  {src.name} -> {dest.relative_to(ROOT)}")
    for f in flags:
        print(f"    WARNING: {f} — check before trusting this file")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--map", required=True, help="Path to the JSON anonymization mapping file")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true", help="Anonymize every file in 03_data/private/ (except the map itself)")
    group.add_argument("--input", help="Anonymize just this one file")
    args = parser.parse_args()

    map_path = Path(args.map)
    if not map_path.exists():
        sys.exit(f"{map_path} not found.")
    mapping = load_map(map_path)

    if args.input:
        targets = [Path(args.input)]
    else:
        if not PRIVATE_DIR.exists():
            sys.exit(f"{PRIVATE_DIR} not found.")
        targets = [
            p for p in PRIVATE_DIR.rglob("*")
            if p.is_file() and p.resolve() != map_path.resolve() and not p.name.startswith(".")
        ]

    if not targets:
        print(f"No files to anonymize in {PRIVATE_DIR}.")
        return

    ANON_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Anonymizing {len(targets)} file(s) with {len(mapping)} mapping entries.")
    for t in targets:
        anonymize_one(t, mapping)


if __name__ == "__main__":
    main()
