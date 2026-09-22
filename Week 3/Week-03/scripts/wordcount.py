#!/usr/bin/env python3
"""Count words per section of a Markdown draft and check against budgets.

Splits the draft on Markdown headings (## Section Name — level 2 by default,
configurable) and counts words in each section's body (heading lines and
fenced code blocks excluded from the count). Compares each to a budget from
a JSON file ({"Section Name": 300, ...}, matching format.md's word budgets)
and flags anything over by more than a tolerance (10% by default).

MANUAL FALLBACK: select each section's text in a word processor and read
its own word count off the status bar, then compare by hand to the budget
in 01_requirements/format.md.

Usage:
    python wordcount.py --draft 04_draft/draft_v1.md --budgets 01_requirements/word_budgets.json
    python wordcount.py --draft 04_draft/draft_v1.md --budgets 01_requirements/word_budgets.json --tolerance 0.15
    python wordcount.py --draft 04_draft/draft_v1.md --budgets 01_requirements/word_budgets.json --level 3
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def split_sections(text: str, level: int) -> dict[str, str]:
    text = strip_code_blocks(text)
    marker = "#" * level
    pattern = re.compile(rf"^{marker} +(.+?) *$", re.MULTILINE)

    matches = list(pattern.finditer(text))
    sections: dict[str, str] = {}
    for i, m in enumerate(matches):
        name = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        # A repeated heading name appends rather than overwrites, so budgets
        # can be checked even if a section is (unusually) split in two.
        sections[name] = sections.get(name, "") + body
    return sections


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--draft", required=True, help="Path to the Markdown draft")
    parser.add_argument("--budgets", required=True, help="Path to a JSON file: {\"Section Name\": budget_words}")
    parser.add_argument("--level", type=int, default=2, help="Markdown heading level that marks a section (default 2, i.e. ##)")
    parser.add_argument("--tolerance", type=float, default=0.10, help="Fraction over budget before flagging (default 0.10 = 10%%)")
    args = parser.parse_args()

    draft_path = Path(args.draft)
    budgets_path = Path(args.budgets)
    if not draft_path.exists():
        sys.exit(f"{draft_path} not found.")
    if not budgets_path.exists():
        sys.exit(f"{budgets_path} not found.")

    draft_text = draft_path.read_text(encoding="utf-8-sig")
    budgets = json.loads(budgets_path.read_text(encoding="utf-8-sig"))
    sections = split_sections(draft_text, args.level)

    print(f"{'Section':<30} {'Words':>7} {'Budget':>7} {'Status':>10}")
    print("-" * 58)

    any_over = False
    total_words = 0
    for name, body in sections.items():
        words = count_words(body)
        total_words += words
        budget = budgets.get(name)
        if budget is None:
            status = "no budget"
        else:
            over = words > budget * (1 + args.tolerance)
            status = "OVER" if over else "ok"
            any_over = any_over or over
        print(f"{name:<30} {words:>7} {budget if budget is not None else '-':>7} {status:>10}")

    missing = set(budgets) - set(sections)
    if missing:
        print(f"\nBudgeted sections not found in draft: {', '.join(sorted(missing))}")

    print(f"\nTotal: {total_words} words across {len(sections)} section(s).")
    sys.exit(1 if any_over else 0)


if __name__ == "__main__":
    main()
