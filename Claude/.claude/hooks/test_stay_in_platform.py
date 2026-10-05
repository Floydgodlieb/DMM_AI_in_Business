"""Run: python .claude/hooks/test_stay_in_platform.py  — prints one line per case, FAIL if a case is wrong."""
import json, subprocess, sys
from pathlib import Path

HOOK = Path(__file__).with_name("stay_in_platform.py")
P = str(HOOK.resolve().parents[2])                  # the platform folder
PARENT = str(Path(P).parent)
GB = "/" + P[0].lower() + P[2:].replace("\\", "/")  # Git Bash form

cases = [  # (expect_blocked, tool, input)
    (False, "Read", {"file_path": P + "\\context.md"}),
    (False, "Read", {"file_path": "sources/S-001.md"}),
    (True, "Read", {"file_path": PARENT + "\\interview.txt"}),
    (True, "Read", {"file_path": P + "\\..\\interview.txt"}),
    (True, "Glob", {"pattern": "*", "path": str(Path.home() / "Documents")}),
    (False, "Grep", {"pattern": "x"}),
    (False, "Bash", {"command": "python .claude/scripts/verify_claims.py --write"}),
    (True, "Bash", {"command": "cat ../transcript.txt"}),
    (True, "Bash", {"command": "cat " + "/" + "c/Users/floyd/Documents/x.txt"}),
    (False, "Bash", {"command": f'cd "{GB}" && ls sources'}),
    (True, "Bash", {"command": f'cat "{PARENT}\\rec.txt"'}),
    (True, "PowerShell", {"command": "Get-Content " + "$env:" + "USERPROFILE\\Downloads\\rec.txt"}),
    (False, "Bash", {"command": "curl -s https://www.cbs.nl/nl-nl/x"}),
    (False, "WebFetch", {"url": "https://example.org"}),
]
bad = 0
for expect, tool, inp in cases:
    r = subprocess.run([sys.executable, str(HOOK)], input=json.dumps({"tool_name": tool, "tool_input": inp}),
                       capture_output=True, text=True)
    blocked = r.returncode == 2
    ok = blocked == expect and r.returncode in (0, 2)
    bad += not ok
    print(("ok  " if ok else "FAIL"), "blocked" if blocked else "allowed", tool, json.dumps(inp)[:90])
r = subprocess.run([sys.executable, str(HOOK)], input="not json", capture_output=True, text=True)
print("ok  " if r.returncode == 2 else "FAIL", "garbage input -> exit", r.returncode)
sys.exit(1 if bad or r.returncode != 2 else 0)
