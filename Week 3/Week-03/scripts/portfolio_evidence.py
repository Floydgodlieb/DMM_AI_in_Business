#!/usr/bin/env python3
"""Compile portfolio_evidence.md from this week's actual records.

NEVER drafts reflection text — Floyd writes the real portfolio entry himself,
elsewhere, from what this file shows him. This script only pulls together
facts that already exist in other files:

  - what was published: whatever's in 06_final/ (or 04_draft/ if nothing's
    final yet)
  - gate feedback received: 07_feedback/gate_log.json (a plain list of
    {"date", "source": "socratic"|"peer", "text"} entries — append to this
    by hand as feedback arrives; there's no script for that part, since it's
    just copying down what the tutor/peer team sent)
  - what changed in response: parsed from 05_review/issue_log.md and
    07_feedback/revision_matrix.md's own tables
  - task times: from progress.json

Fully regenerates portfolio_evidence.md every run — nothing in that file is
meant to be hand-edited, so there's nothing to preserve between runs.

MANUAL FALLBACK: read the same four source locations yourself and fill in
portfolio_evidence.md's sections by hand; the file's headings describe
exactly what goes in each one.

Usage:
    python portfolio_evidence.py
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GATE_LOG = ROOT / "07_feedback" / "gate_log.json"
ISSUE_LOG = ROOT / "05_review" / "issue_log.md"
REVISION_MATRIX = ROOT / "07_feedback" / "revision_matrix.md"
PROGRESS_JSON = ROOT / "progress.json"
OUT = ROOT / "portfolio_evidence.md"


def published_files() -> list[Path]:
    for d in (ROOT / "06_final", ROOT / "04_draft"):
        if d.exists():
            files = sorted(p for p in d.glob("*") if p.is_file() and p.name != ".gitkeep")
            if files:
                return files
    return []


def load_gate_log() -> list[dict]:
    if not GATE_LOG.exists():
        return []
    return json.loads(GATE_LOG.read_text(encoding="utf-8-sig"))


def parse_md_table(path: Path) -> list[dict]:
    """Parse a pipe-delimited Markdown table into a list of {header: cell}."""
    if not path.exists():
        return []
    lines = [l for l in path.read_text(encoding="utf-8-sig").splitlines() if l.strip().startswith("|")]
    if len(lines) < 2:
        return []
    headers = [c.strip() for c in lines[0].strip("|").split("|")]
    rows = []
    for line in lines[2:]:  # skip header + separator row
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != len(headers):
            continue
        rows.append(dict(zip(headers, cells)))
    return rows


def stage_time_summary() -> tuple[list[str], float]:
    if not PROGRESS_JSON.exists():
        return [], 0.0
    data = json.loads(PROGRESS_JSON.read_text(encoding="utf-8-sig"))
    lines = []
    total = 0.0
    for phase in data.get("phases", []):
        tasks = [t for t in phase["tasks"] if t.get("minutes", 0) > 0 or t["status"] != "todo"]
        if not tasks:
            continue
        phase_minutes = sum(t.get("minutes", 0) for t in phase["tasks"])
        total += phase_minutes
        lines.append(f"- **Stage {phase['id']} ({phase['title']})**: {phase_minutes:.1f} min")
        for t in tasks:
            lines.append(f"  - {t['id']} {t['title']} — {t['status']}, {t.get('minutes', 0):.1f} min")
    return lines, total


def build() -> str:
    lines = ["# Portfolio evidence", "", "Factual record only — compiled by `scripts/portfolio_evidence.py`, "
             "not drafted. Write the actual portfolio entry yourself, from this.", ""]

    lines.append("## What was published this week")
    lines.append("")
    files = published_files()
    if files:
        for f in files:
            lines.append(f"- `{f.relative_to(ROOT).as_posix()}`")
    else:
        lines.append("_Nothing in 06_final/ or 04_draft/ yet._")
    lines.append("")

    lines.append("## Gate feedback received")
    lines.append("")
    gate_entries = load_gate_log()
    if gate_entries:
        for e in gate_entries:
            lines.append(f"- **{e.get('date', '?')} ({e.get('source', '?')})**: {e.get('text', '')}")
    else:
        lines.append(f"_No entries in `{GATE_LOG.relative_to(ROOT).as_posix()}` yet — append to it by hand as feedback arrives._")
    lines.append("")

    lines.append("## What changed in response")
    lines.append("")
    issues = parse_md_table(ISSUE_LOG)
    revisions = parse_md_table(REVISION_MATRIX)
    if issues:
        lines.append(f"From `{ISSUE_LOG.relative_to(ROOT).as_posix()}`:")
        for row in issues:
            lines.append(f"- [{row.get('Status', '?')}] {row.get('Issue', '')} — {row.get('Location', '')}")
    if revisions:
        lines.append(f"From `{REVISION_MATRIX.relative_to(ROOT).as_posix()}`:")
        for row in revisions:
            lines.append(f"- {row.get('Feedback item', '')} -> {row.get('Action taken', '')}")
    if not issues and not revisions:
        lines.append("_No issue log or revision matrix entries yet._")
    lines.append("")

    lines.append("## Task times this week")
    lines.append("")
    time_lines, total = stage_time_summary()
    if time_lines:
        lines.extend(time_lines)
        lines.append(f"\n**Total: {total:.1f} min**")
    else:
        lines.append("_No task times recorded yet — see progress.json._")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.parse_args()
    OUT.write_text(build(), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
