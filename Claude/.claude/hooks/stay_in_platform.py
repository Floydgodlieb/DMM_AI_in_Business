"""PreToolUse hook: the line (blueprint section 4) enforced by the tool, not only by instructions.

Blocks any file tool whose path lies outside platform/, and any shell command that names a
path outside it or climbs out with '..'. Exit code 2 = blocked; the reason goes back to Claude.
Fails closed: if this script itself errors, the call is blocked, not let through.
"""
import json, os, re, sys
from pathlib import Path

PLATFORM = Path(__file__).resolve().parents[2]
ALLOWED = [PLATFORM, Path.home() / ".claude"]  # Claude's own settings and memory; never interview material
if os.environ.get("TEMP"):
    ALLOWED.append(Path(os.environ["TEMP"]) / "claude")

FILE_TOOLS = ("Read", "Write", "Edit", "NotebookEdit", "Glob", "Grep")
SHELL_TOOLS = ("Bash", "PowerShell")


class Blocked(Exception):
    pass


def inside(p):
    try:
        p = Path(p).expanduser()
        p = (p if p.is_absolute() else Path.cwd() / p).resolve()
    except (OSError, ValueError):
        return False
    return any(p == a.resolve() or a.resolve() in p.parents for a in ALLOWED)


def to_native(p):
    m = re.match(r"^/([a-zA-Z])/(.*)", p)  # Git Bash style /c/Users/...
    return f"{m.group(1)}:/{m.group(2)}" if m else p


def check(tool, args):
    if tool in FILE_TOOLS:
        for key in ("file_path", "notebook_path", "path"):
            if args.get(key) and not inside(args[key]):
                raise Blocked(f"{tool} on {args[key]}")
    elif tool in SHELL_TOOLS:
        cmd = args.get("command", "")
        if re.search(r"(^|[\s'\"=/\\])\.\.([/\\]|$|[\s'\"])", cmd):
            raise Blocked("command climbs out of the folder with '..'")
        if re.search(r"\$HOME|%USERPROFILE%|\$env:USERPROFILE|(^|\s)~([/\\\s]|$)", cmd):
            raise Blocked("command refers to the home folder")
        candidates = re.findall(r"(?<![\w])[A-Za-z]:[\\/][^'\"|;&<>]*", cmd)          # C:\... (may contain spaces)
        candidates += re.findall(r"(?<![\w.:/])/[a-zA-Z]/[^'\"|;&<>]*", cmd)          # /c/...
        for c in candidates:
            # a path may run into following arguments; accept if any space-cut prefix is inside
            parts = c.split(" ")
            if not any(inside(to_native(" ".join(parts[:i]).rstrip())) for i in range(len(parts), 0, -1)):
                raise Blocked(f"command names a path outside platform/: {parts[0]}")


def main():
    try:
        data = json.load(sys.stdin)
        check(data.get("tool_name", ""), data.get("tool_input", {}) or {})
    except Blocked as b:
        reason = str(b)
    except Exception as e:
        reason = f"hook could not read the call ({type(e).__name__}), blocked to be safe"
    else:
        return 0
    sys.stderr.write(f"Blocked by stay_in_platform hook: {reason}. Only files inside {PLATFORM} may be used "
                     "(CLAUDE.md; blueprint section 4, the line).\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())
