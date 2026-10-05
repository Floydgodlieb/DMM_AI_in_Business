"""Mechanical bookkeeping for the handbook pipeline: the jobs that need rules, not a model.

Usage (from the platform/ folder):
  python .claude/scripts/gates.py library          every saved source: id, type, publisher, url, decision, claims
  python .claude/scripts/gates.py intake           move parallel Find output from library/sources/incoming/ into
                                                   library/sources/: next free ids, duplicates set aside, searchlog merged
  python .claude/scripts/gates.py todo             what each stage still has to do (only the new work)
  python .claude/scripts/gates.py publish-gate     every condition /publish-prep needs; exit 1 if any fails
  python .claude/scripts/gates.py new-week <NN>    open weeks/week-NN/ with a question.md to fill in
  python .claude/scripts/gates.py allow-domains    load .claude/source-domains.txt into .claude/settings.json

The library is library/; this week's files are in the highest weeks/week-NN/ (see verify_claims.py).
"""
import json, re, sys, urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from verify_claims import CRED3_TYPES, LIB, SOURCES_DIR, WEEK, WEEKS, load_appraised, load_claims, load_source, queue_results, person_ok, route_of  # noqa: E402

ROOT = Path.cwd()
SOURCES, INCOMING = SOURCES_DIR, SOURCES_DIR / "incoming"


def source_ids():
    return sorted(p.stem for p in SOURCES.glob("S-[0-9][0-9][0-9].md") if p.stem != "S-000")


def norm_url(url):
    """Same document, different spelling: scheme, www, trailing slash, fragment, tracking parameters."""
    u = urllib.parse.urlsplit(url.strip().lower())
    host = u.netloc.removeprefix("www.")
    query = "&".join(q for q in u.query.split("&") if q and not q.startswith(("utm_", "fbclid", "gclid")))
    return f"{host}{u.path.rstrip('/')}" + (f"?{query}" if query else "")


def front(path):
    text = path.read_text(encoding="utf-8")
    return dict((k, v.strip().strip('"')) for k, v in re.findall(r"^(\w+):[ \t]*(.*)$", text.split("excerpt:")[0], re.M))


# ---------- library ----------

def library():
    appraised = load_appraised(LIB / "appraised.md")
    claims = load_claims(LIB / "claims_en.md") if (LIB / "claims_en.md").exists() else []
    print("| id | type | lang | publisher | title | url | decision | claims |")
    print("|---|---|---|---|---|---|---|---|")
    for sid in source_ids():
        f = front(SOURCES / f"{sid}.md")
        n = sum(c.get("source_id") == sid for c in claims)
        dec = appraised.get(sid, {}).get("decision", "not appraised")
        print(f"| {sid} | {f.get('type', '')} | {f.get('language', '')} | {f.get('publisher', '')[:50]} | "
              f"{f.get('title', '')[:60]} | {f.get('url', '')} | {dec} | {n} |")


# ---------- intake ----------

def intake():
    files = sorted(p for p in INCOMING.glob("*.md") if not p.name.startswith("searchlog-")) if INCOMING.exists() else []
    known = {norm_url(front(SOURCES / f"{s}.md").get("url", "")): s for s in source_ids()}
    next_n = max([int(s[2:]) for s in source_ids()] or [0]) + 1
    mapping, dup_dir = {}, INCOMING / "_duplicates"
    for p in files:
        placeholder, url = p.stem, front(p).get("url", "")
        key = norm_url(url)
        if not url or key in known:
            dup_dir.mkdir(exist_ok=True)
            p.replace(dup_dir / p.name)
            mapping[placeholder] = f"dup of {known[key]}" if url else "no url, set aside"
            continue
        sid = f"S-{next_n:03d}"
        next_n += 1
        text = re.sub(r"(?m)^id:.*$", f"id: {sid}", p.read_text(encoding="utf-8"), count=1)
        (SOURCES / f"{sid}.md").write_text(text, encoding="utf-8")
        p.unlink()
        known[key], mapping[placeholder] = sid, sid

    logs = sorted(INCOMING.glob("searchlog-*.md")) if INCOMING.exists() else []
    added = []
    for log in logs:
        for line in log.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("|") and not re.match(r"\|\s*-+", line) and "exact query" not in line:
                for ph, sid in sorted(mapping.items(), key=lambda kv: -len(kv[0])):
                    line = re.sub(rf"\b{re.escape(ph)}\b", sid, line)
                added.append(line)
        log.unlink()
    if added:
        with (LIB / "searchlog.md").open("a", encoding="utf-8") as fh:
            fh.write("\n".join(added) + "\n")

    new = [v for v in mapping.values() if v.startswith("S-")]
    print(f"intake: {len(new)} new source(s): {', '.join(new) or 'none'}")
    for ph, v in mapping.items():
        if not v.startswith("S-"):
            print(f"  {ph}: {v} (in sources/incoming/_duplicates/)")
    print(f"searchlog.md: {len(added)} line(s) added")


# ---------- todo ----------

def todo():
    appraised = load_appraised(LIB / "appraised.md")
    claims = load_claims(LIB / "claims_en.md") if (LIB / "claims_en.md").exists() else []
    with_claims = {c.get("source_id") for c in claims}
    ids = source_ids()

    unrated = [s for s in ids if s not in appraised]
    cap = [s for s in ids if appraised.get(s, {}).get("credibility") == 3
           and load_source(s)["type"] not in CRED3_TYPES and not appraised[s]["override"]]
    untranslated = [s for s in ids if appraised.get(s, {}).get("decision") == "use" and s not in with_claims]
    unverified = [c["claim_id"] for c in claims if not route_of(c) and c.get("translated_by") != "person"]
    failed = [c["claim_id"] for c in claims if route_of(c) == "FAIL" and not c.get("superseded_by")]
    queue = queue_results(LIB / "review_queue.md")
    open_queue = [s for s, r in queue.items() if not (person_ok(r) or "discard" in r.lower())]

    print("This week's folder:", WEEK.relative_to(ROOT).as_posix())
    print("Stage 2 Appraise - rate only these (new):", ", ".join(unrated) or "none")
    print("Stage 2 Appraise - credibility 3 not allowed for this type, re-rate:", ", ".join(cap) or "none")
    print("Stage 3 Translate - use-sources without claims:", ", ".join(untranslated) or "none")
    print("Stage 3 Translate - FAIL claims to repair:", ", ".join(failed) or "none")
    print("Verify - claims never verified:", ", ".join(unverified) or "none")
    print("Person - review_queue.md sources still open:", ", ".join(open_queue) or "none")


# ---------- publish gate ----------

def publish_gate():
    problems = []
    check = (WEEK / "check.md").read_text(encoding="utf-8") if (WEEK / "check.md").exists() else ""
    if not check:
        problems.append("check.md missing")
    final = re.search(r"(?m)^## Final:(.*)$", check)
    if not final or not re.search(r"\bpublish\b", final.group(1)) or "return to draft" in final.group(1) \
            or re.search(r"decided by:\s*_+", final.group(1)):
        problems.append("check.md final line does not say publish with a person's name (and only publish)")
    for line in check.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if re.fullmatch(r"W\d+-\d{3}", cells[0] if cells else "") and "pass" not in cells:
            problems.append(f"check.md: {cells[0]} is not pass")
    sr = check.split("## Second reader", 1)[1].split("## Final", 1)[0] if "## Second reader" in check else ""
    for crit in ("1 names", "2 time-saving", "5 complexity", "6 one next step"):
        row = next((l for l in sr.splitlines() if crit in l), "")
        if not re.search(r"\|\s*pass\s*\|", row, re.I):
            problems.append(f"second reader: criterion {crit.split()[0]} not pass")
    duty = check.split("## Duty named", 1)[1].split("##", 1)[0] if "## Duty named" in check else ""
    for line in duty.splitlines():
        if re.match(r"\|\s*\d+\.", line) and not re.search(r"\|\s*pass\s*\|\s*$", line):
            problems.append("duty per recommendation: " + line.split("|")[1].strip()[:50] + " not pass")
    queue = queue_results(LIB / "review_queue.md")
    for s, r in queue.items():
        if not (person_ok(r) or "discard" in r.lower()):
            problems.append(f"review_queue.md: {s} still open")
    draft = (WEEK / "draft.md").read_text(encoding="utf-8")
    for ph in ("[no claim found", "(awaiting source check)", "[CHECKING NOTE", "[DISCLAIMER", "[fill in"):
        if ph in draft:
            problems.append(f"draft.md still contains '{ph}'")
    print("publish-gate:", "OPEN - all conditions met" if not problems else f"CLOSED - {len(problems)} problem(s)")
    for p in problems:
        print("  -", p)
    return 1 if problems else 0


# ---------- new week ----------

def new_week(n):
    """Open weeks/week-NN/ with a question.md to fill in; the library carries over untouched."""
    folder = WEEKS / f"week-{int(n):02d}"
    if folder.exists():
        print(f"{folder.relative_to(ROOT).as_posix()} already exists; nothing changed")
        return 1
    folder.mkdir(parents=True)
    template = (ROOT / "templates" / "question.template.md").read_text(encoding="utf-8")
    (folder / "question.md").write_text(template.replace("<NN>", str(int(n))), encoding="utf-8")
    print(f"{folder.relative_to(ROOT).as_posix()}/question.md created: fill it in, then run /run-page")


# ---------- web allowlist ----------

def allow_domains():
    """source-domains.txt is the one list; settings.json's WebFetch entries are rebuilt from it."""
    hosts = []
    for line in (ROOT / ".claude" / "source-domains.txt").read_text(encoding="utf-8").splitlines():
        h = line.split("#")[0].strip().lower()
        if h and h not in hosts:
            if not re.fullmatch(r"[a-z0-9.-]+\.[a-z]{2,}", h):
                print(f"skipped, not a host name: {h}")
                continue
            hosts.append(h)
    path = ROOT / ".claude" / "settings.json"
    settings = json.loads(path.read_text(encoding="utf-8"))
    allow = settings.setdefault("permissions", {}).setdefault("allow", [])
    kept = [a for a in allow if not a.startswith("WebFetch(domain:")]
    settings["permissions"]["allow"] = kept + [f"WebFetch(domain:{h})" for h in hosts]
    path.write_text(json.dumps(settings, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"settings.json: {len(hosts)} sites allowed for WebFetch (restart Claude Code to load)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "new-week" and len(sys.argv) == 3 and sys.argv[2].isdigit():
        sys.exit(new_week(sys.argv[2]) or 0)
    jobs = {"library": library, "intake": intake, "todo": todo, "publish-gate": publish_gate,
            "allow-domains": allow_domains}
    if cmd not in jobs:
        print(__doc__)
        sys.exit(2)
    sys.exit(jobs[cmd]() or 0)
