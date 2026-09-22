#!/usr/bin/env python3
"""Progress tracker for one assignment/week instance of the Academic Pipeline.

Single source of truth: progress.json (in this assignment's root)
Human-readable output: the progress table inside status.md, between the
PROGRESS_TABLE_START/END markers — this script only ever replaces the text
between those two markers, so the rest of status.md (current stage,
approvals, open questions) is left untouched.

All timestamps come from the system clock at the moment a command runs.
Nothing here estimates or backfills time. Adapted from the build's own
scripts/progress.py (same command set, same progress.json shape) — here
"phases" are the 8 pipeline stages instead of build phases.
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROGRESS_JSON = ROOT / "progress.json"
STATUS_MD = ROOT / "status.md"

TABLE_START = "<!-- PROGRESS_TABLE_START -->"
TABLE_END = "<!-- PROGRESS_TABLE_END -->"

STATUSES = {"todo", "in progress", "blocked", "done"}


def now_iso():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def load():
    with open(PROGRESS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def save(data):
    with open(PROGRESS_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def find_phase(data, phase_id):
    for phase in data["phases"]:
        if str(phase["id"]) == str(phase_id):
            return phase
    return None


def find_task(data, task_id):
    for phase in data["phases"]:
        for task in phase["tasks"]:
            if task["id"] == task_id:
                return phase, task
    return None, None


def new_task(task_id, title, description):
    return {
        "id": task_id,
        "title": title,
        "description": description,
        "status": "todo",
        "started": None,
        "finished": None,
        "minutes": 0,
        "sessions": [],
        "notes": [],
        "block_reason": None,
    }


def cmd_add_phase(args):
    data = load()
    if find_phase(data, args.id):
        sys.exit(f"Phase {args.id} already exists.")
    data["phases"].append({"id": args.id, "title": args.title, "tasks": []})
    data["phases"].sort(key=lambda p: p["id"])
    save(data)
    print(f"Added phase {args.id}: {args.title}")


def cmd_add_task(args):
    data = load()
    phase = find_phase(data, args.phase)
    if not phase:
        sys.exit(f"Phase {args.phase} not found. Add it first with 'add phase'.")
    if find_task(data, args.id)[1]:
        sys.exit(f"Task {args.id} already exists.")
    phase["tasks"].append(new_task(args.id, args.title, args.description or ""))
    save(data)
    print(f"Added task {args.id} to phase {args.phase}: {args.title}")


def cmd_start(args):
    data = load()
    _, task = find_task(data, args.id)
    if not task:
        sys.exit(f"Task {args.id} not found.")
    if task["sessions"] and task["sessions"][-1].get("end") is None:
        sys.exit(f"Task {args.id} already has an open session (started {task['sessions'][-1]['start']}).")
    ts = now_iso()
    task["sessions"].append({"start": ts, "end": None})
    if task["started"] is None:
        task["started"] = ts
    task["status"] = "in progress"
    task["block_reason"] = None
    save(data)
    print(f"Started {args.id} at {ts}")


def _close_open_session(task, ts):
    if task["sessions"] and task["sessions"][-1].get("end") is None:
        session = task["sessions"][-1]
        session["end"] = ts
        start_dt = datetime.fromisoformat(session["start"])
        end_dt = datetime.fromisoformat(ts)
        minutes = (end_dt - start_dt).total_seconds() / 60.0
        task["minutes"] = round(task.get("minutes", 0) + minutes, 2)


def cmd_done(args):
    data = load()
    _, task = find_task(data, args.id)
    if not task:
        sys.exit(f"Task {args.id} not found.")
    ts = now_iso()
    _close_open_session(task, ts)
    task["status"] = "done"
    task["finished"] = ts
    task["block_reason"] = None
    save(data)
    print(f"Completed {args.id} at {ts} (total {task['minutes']:.1f} min)")


def cmd_block(args):
    data = load()
    _, task = find_task(data, args.id)
    if not task:
        sys.exit(f"Task {args.id} not found.")
    ts = now_iso()
    _close_open_session(task, ts)
    task["status"] = "blocked"
    task["block_reason"] = args.reason
    task["notes"].append({"time": ts, "text": f"BLOCKED: {args.reason}"})
    save(data)
    print(f"Blocked {args.id}: {args.reason}")


def cmd_note(args):
    data = load()
    _, task = find_task(data, args.id)
    if not task:
        sys.exit(f"Task {args.id} not found.")
    ts = now_iso()
    task["notes"].append({"time": ts, "text": args.text})
    save(data)
    print(f"Noted on {args.id}: {args.text}")


def fmt_minutes(m):
    if m <= 0:
        return "0 min"
    h = int(m // 60)
    mm = int(round(m % 60))
    if h:
        return f"{h}h {mm}m"
    return f"{mm} min"


def build_table_lines(data):
    lines = [f"_Generated {now_iso()}_", ""]

    overall_minutes = 0.0
    next_task = None

    for phase in data["phases"]:
        tasks = phase["tasks"]
        phase_minutes = sum(t.get("minutes", 0) for t in tasks)
        overall_minutes += phase_minutes

        lines.append(f"### Stage {phase['id']}: {phase['title']}")
        lines.append("")
        if not tasks:
            lines.append("_No tasks yet._")
            lines.append("")
            continue

        lines.append("| Task | Description | Status | Time spent |")
        lines.append("|------|-------------|--------|------------|")
        for t in tasks:
            lines.append(
                f"| {t['id']} {t['title']} | {t['description']} | {t['status']} | {fmt_minutes(t.get('minutes', 0))} |"
            )
            if next_task is None and t["status"] in ("todo", "in progress", "blocked"):
                next_task = t
        lines.append("")
        lines.append(f"**Stage {phase['id']} total: {fmt_minutes(phase_minutes)}**")
        lines.append("")

    lines.append(f"**Overall total: {fmt_minutes(overall_minutes)}**")
    lines.append("")
    if next_task:
        status_note = f" (currently {next_task['status']})" if next_task["status"] != "todo" else ""
        lines.append(f"**What's next:** {next_task['id']} {next_task['title']}{status_note}")
    else:
        lines.append("**What's next:** All defined tasks are done.")

    return lines


def cmd_report(args):
    data = load()
    table_lines = build_table_lines(data)

    if not STATUS_MD.exists():
        sys.exit(f"{STATUS_MD} not found. Copy it from _template/status.md first.")

    text = STATUS_MD.read_text(encoding="utf-8")
    if TABLE_START not in text or TABLE_END not in text:
        sys.exit(
            f"status.md is missing {TABLE_START} / {TABLE_END} markers — "
            "can't tell where to put the progress table."
        )

    pattern = re.compile(
        re.escape(TABLE_START) + r".*?" + re.escape(TABLE_END), re.DOTALL
    )
    replacement = TABLE_START + "\n" + "\n".join(table_lines) + "\n" + TABLE_END
    new_text = pattern.sub(lambda m: replacement, text, count=1)
    STATUS_MD.write_text(new_text, encoding="utf-8")
    print(f"Updated progress table in {STATUS_MD}")


def main():
    parser = argparse.ArgumentParser(description="Per-assignment progress tracker")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a phase or task")
    add_sub = p_add.add_subparsers(dest="kind", required=True)

    p_add_phase = add_sub.add_parser("phase")
    p_add_phase.add_argument("--id", required=True, type=int)
    p_add_phase.add_argument("--title", required=True)
    p_add_phase.set_defaults(func=cmd_add_phase)

    p_add_task = add_sub.add_parser("task")
    p_add_task.add_argument("--phase", required=True)
    p_add_task.add_argument("--id", required=True)
    p_add_task.add_argument("--title", required=True)
    p_add_task.add_argument("--description", default="")
    p_add_task.set_defaults(func=cmd_add_task)

    p_start = sub.add_parser("start", help="Start work on a task")
    p_start.add_argument("id")
    p_start.set_defaults(func=cmd_start)

    p_done = sub.add_parser("done", help="Mark a task done")
    p_done.add_argument("id")
    p_done.set_defaults(func=cmd_done)

    p_block = sub.add_parser("block", help="Mark a task blocked")
    p_block.add_argument("id")
    p_block.add_argument("--reason", required=True)
    p_block.set_defaults(func=cmd_block)

    p_note = sub.add_parser("note", help="Add a note to a task")
    p_note.add_argument("id")
    p_note.add_argument("--text", required=True)
    p_note.set_defaults(func=cmd_note)

    p_report = sub.add_parser("report", help="Regenerate the progress table inside status.md")
    p_report.set_defaults(func=cmd_report)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
