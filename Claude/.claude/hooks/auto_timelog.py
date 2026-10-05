"""Automatic timelog: one timelog.csv row per stage agent run.

Wired to SubagentStart (remembers the start time) and SubagentStop (writes the row).
Only the pipeline's own agents are logged; any other subagent is ignored.
Person checks (review queue, second reader) are not agent runs: log those with /log-time.
Person name: env TIMELOG_PERSON, default "Floyd".
"""
import csv
import datetime as dt
import json
import os
import sys
from pathlib import Path

STAGE = {"source-finder": 1, "appraiser": 2, "translator": 3, "drafter": 4, "checker": 5}

root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2])
state_file = root / ".claude" / "hooks" / ".timelog_state.json"
log_file = root / "timelog.csv"


def load_state():
    try:
        return json.loads(state_file.read_text(encoding="utf-8"))
    except Exception:
        return {}


def main():
    data = json.load(sys.stdin)
    event = data.get("hook_event_name", "")
    agent_id = data.get("agent_id") or data.get("session_id") or "unknown"
    agent_type = data.get("agent_type") or data.get("subagent_type") or ""
    now = dt.datetime.now()
    state = load_state()

    if event == "SubagentStart":
        state[agent_id] = {"start": now.isoformat(timespec="minutes"), "type": agent_type}
        state_file.write_text(json.dumps(state), encoding="utf-8")
        return

    if event == "SubagentStop":
        started = state.pop(agent_id, None)
        state_file.write_text(json.dumps(state), encoding="utf-8")
        agent_type = agent_type or (started or {}).get("type", "")
        if agent_type not in STAGE:
            return
        start = dt.datetime.fromisoformat(started["start"]) if started else now
        person = os.environ.get("TIMELOG_PERSON", "Floyd")
        with log_file.open("a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([
                now.strftime("%d-%m-%Y"), person, STAGE[agent_type],
                f"{start:%H:%M}-{now:%H:%M}", "tool", f"auto: {agent_type}",
            ])


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # never block the pipeline over a log line
