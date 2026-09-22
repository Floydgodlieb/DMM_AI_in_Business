#!/usr/bin/env python3
"""Extract per-page text from every PDF in 02_sources/pdf/ into 02_sources/text/.

For each 02_sources/pdf/<Name>.pdf, writes one file per page to
02_sources/text/<Name>/page_0001.txt, page_0002.txt, ... using pymupdf. This
is what lets verify_quotes.py (and any agent) check "does this quote exist
on page N" by reading exactly one small file, never the whole PDF.

Idempotent / rerunnable: a PDF whose text folder already has the same page
count as the PDF is skipped, so a weekly rerun only extracts new PDFs. Use
--force to re-extract everything.

MANUAL FALLBACK: if pymupdf isn't installed or a PDF won't open, extract by
hand: open the PDF, select and copy each page's text in turn (or use
Adobe Acrobat / Preview's "Export as Text"), and save each page as
02_sources/text/<Name>/page_0001.txt (one file per page, four-digit
zero-padded number, matching the PDF's own page numbers).

Usage:
    python extract_text.py
    python extract_text.py --force
    python extract_text.py --pdf 02_sources/pdf/Smith2024_SomeTitle.pdf
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import pymupdf as fitz
except ImportError:
    fitz = None

ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = ROOT / "02_sources" / "pdf"
TEXT_DIR = ROOT / "02_sources" / "text"


def extract_one(pdf_path: Path, force: bool) -> None:
    out_dir = TEXT_DIR / pdf_path.stem
    doc = fitz.open(pdf_path)
    page_count = doc.page_count

    if out_dir.exists() and not force:
        existing = sorted(out_dir.glob("page_*.txt"))
        if len(existing) == page_count:
            print(f"  {pdf_path.name}: already extracted ({page_count} pages) — skipped")
            doc.close()
            return

    out_dir.mkdir(parents=True, exist_ok=True)
    for i, page in enumerate(doc, start=1):
        text = page.get_text()
        (out_dir / f"page_{i:04d}.txt").write_text(text, encoding="utf-8")
    doc.close()
    print(f"  {pdf_path.name}: extracted {page_count} page(s) to {out_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--force", action="store_true", help="Re-extract even if already done")
    parser.add_argument("--pdf", help="Extract only this one PDF (path)")
    args = parser.parse_args()

    if fitz is None:
        sys.exit("pymupdf is not installed (pip install pymupdf). See the manual fallback in this script's header.")

    if args.pdf:
        pdfs = [Path(args.pdf)]
        if not pdfs[0].exists():
            sys.exit(f"{pdfs[0]} not found.")
    else:
        if not PDF_DIR.exists():
            sys.exit(f"{PDF_DIR} not found.")
        pdfs = sorted(PDF_DIR.glob("*.pdf"))

    if not pdfs:
        print(f"No PDFs found in {PDF_DIR}.")
        return

    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"{len(pdfs)} PDF(s) to check.")
    for pdf_path in pdfs:
        extract_one(pdf_path, args.force)


if __name__ == "__main__":
    main()
