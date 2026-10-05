"""Mechanical claim verification for the handbook pipeline (context.md §3c).

For every claim in claims_en.md it checks, without any model in the loop:
  - the verbatim sentence (original_nl) is in the saved excerpt (library/sources/S-xxx.md)
  - the same sentence is in the live document at the source URL
  - every number in translation_en also appears in original_nl
  - the source is `decision: use` in appraised.md, its credibility, and any FLAG in the source file
and routes each claim: AUTO-PASS, PERSON (T1 less trustworthy / T2 document not found), or FAIL.

Usage (from the platform/ folder):
  python .claude/scripts/verify_claims.py                    report only (fetches every live document)
  python .claude/scripts/verify_claims.py --write            also write auto_verified + review_queue.md
  python .claude/scripts/verify_claims.py --write --changed  same, but skip the live fetch for claims whose
                                                             claim, excerpt and rating are unchanged since the last run
  python .claude/scripts/verify_claims.py --draft draft.md --precheck
                                                             drafter's quick self-check, no network: labels, ids, routes
  python .claude/scripts/verify_claims.py --draft draft.md --check-md check.md
                                                             Stage 5: fresh live run + the whole tool part of check.md

Where files live: the library (sources, appraised, claims, review queue) in library/; this week's files
(question, draft, check, page) in weeks/week-NN/, the highest NN unless HANDBOOK_WEEK=NN says otherwise.
A bare filename such as `draft.md` means this week's copy.
"""
import argparse, datetime, hashlib, html, io, json, os, re, sys, unicodedata, urllib.error, urllib.request
from pathlib import Path

import yaml

ROOT = Path.cwd()
TODAY = datetime.date.today().isoformat()
CRED3_TYPES = {"regulation", "statistics", "vendor-contract-doc"}


# ---------- where files live (shared by gates.py and wiki.py) ----------

LIB = ROOT / "library"
SOURCES_DIR = LIB / "sources"
WEEKS = ROOT / "weeks"


def current_week():
    env = os.environ.get("HANDBOOK_WEEK", "").strip()
    if env:
        return WEEKS / (env if env.startswith("week-") else f"week-{int(env):02d}")
    dirs = sorted(d for d in WEEKS.glob("week-[0-9][0-9]") if d.is_dir())
    return dirs[-1] if dirs else WEEKS / "week-01"


WEEK = current_week()


def week_file(name):
    """A bare filename is this week's copy; anything with a folder in it is relative to platform/."""
    p = Path(name)
    return WEEK / p if len(p.parts) == 1 else ROOT / p


# ---------- reading the platform files ----------

def load_claims(path):
    """Line-based, so one badly quoted value cannot hide every other claim from Check."""
    text = path.read_text(encoding="utf-8")
    m = re.search(r"```yaml\n(.*?)```", text, re.S)
    claims = []
    for line in (m.group(1) if m else "").splitlines():
        kv = re.match(r"\s*(-\s*)?(\w+):\s?(.*)$", line)
        if not kv:
            continue
        if kv.group(1):
            claims.append({})
        if not claims:
            continue
        raw = kv.group(3).strip()
        q = raw[:1] if raw[:1] in "\"'" else ""
        value = raw if q else re.sub(r"\s+#.*$", "", raw).strip()
        if q:
            try:
                value = yaml.safe_load(value)
            except yaml.YAMLError:
                claims[-1].setdefault("_yaml_errors", []).append(kv.group(2))
                value = value[1:value.rfind(q)] if value.count(q) >= 2 else value[1:]
        claims[-1][kv.group(2)] = value if value is not None else ""
    return claims


def load_appraised(path):
    rows = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 7 and re.fullmatch(r"S-\d{3}", cells[0]):
            rows[cells[0]] = {"credibility": int(cells[1]) if cells[1].isdigit() else 0,
                              "override": cells[5], "decision": cells[-1].lower()}
    return rows


def load_source(sid):
    p = SOURCES_DIR / f"{sid}.md"
    if not p.exists():
        return None
    text = p.read_text(encoding="utf-8")
    front = dict(re.findall(r"^(\w+):[ \t]*(.*)$", text.split("excerpt:")[0], re.M))
    excerpt = text.split("excerpt:", 1)[1] if "excerpt:" in text else ""
    return {"url": front.get("url", "").strip(), "type": front.get("type", "").strip(),
            "title": front.get("title", "").strip(),
            "excerpt": excerpt, "flagged": "FLAG FOR HUMAN REVIEW" in text}


# ---------- matching ----------

def norm(s):
    s = unicodedata.normalize("NFKC", html.unescape(s)).lower()
    s = re.sub(r"[‘’‚′`]", "'", s)
    s = re.sub(r"[“”„″]", '"', s)
    s = re.sub(r"[‐‑‒–—―]", "-", s)
    return re.sub(r"[\s\"'­​]", "", s)  # whitespace, quotes, soft hyphens


def fragments(sentence):
    parts = re.split(r"\.\.\.|…", sentence)
    return [norm(p) for p in parts if len(norm(p)) >= 4]


def contains(haystack_norm, sentence):
    frags = fragments(sentence)
    return bool(frags) and all(f in haystack_norm for f in frags)


def numbers(s):
    return {n.replace(",", ".") for n in re.findall(r"\d+(?:[.,]\d+)?", s)}


_live_cache = {}


def live_text(url):
    """Returns (status, normalised_text). status: 'ok' or a short reason it could not be read."""
    if url in _live_cache:
        return _live_cache[url]
    result = ("not fetched", "")
    try:
        # Sites differ in which client they accept (CBS refuses a browser-like header, others need one),
        # and slow official sites time out now and then; neither means "not found". Try each, twice.
        agents = ["Mozilla/5.0 (handbook-verify)",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"]
        last = None
        for agent in agents:
            for _ in range(2):
                try:
                    req = urllib.request.Request(url, headers={"User-Agent": agent, "Accept-Language": "nl,en;q=0.8"})
                    with urllib.request.urlopen(req, timeout=45) as r:
                        body, ctype = r.read(), r.headers.get("Content-Type", "")
                    last = None
                    break
                except (TimeoutError, urllib.error.URLError) as e:
                    last = e
            if last is None:
                break
        if last is not None:
            raise last
        if "pdf" in ctype or url.lower().endswith(".pdf"):
            try:
                import pypdf
                pages = pypdf.PdfReader(io.BytesIO(body)).pages
                result = ("ok", norm(" ".join(p.extract_text() or "" for p in pages)))
            except ImportError:
                result = ("pdf, no reader installed", "")
        else:
            raw = body.decode("utf-8", errors="replace")
            visible = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", raw)
            visible = re.sub(r"<[^>]+>", " ", visible)
            everything = re.sub(r"<[^>]+>", " ", raw)  # keeps text embedded in scripts (JS-rendered pages)
            result = ("ok", norm(visible) + "\n" + norm(everything))
    except Exception as e:  # any failure to read the document is a T2 route, never a crash
        result = (f"fetch failed: {type(e).__name__} {getattr(e, 'code', '')}".strip(), "")
    _live_cache[url] = result
    return result


# ---------- routing ----------

def fingerprint(claim, src, row):
    """Changes whenever anything the route depends on changes, except the live page itself."""
    parts = [claim.get(k, "") or "" for k in ("original_nl", "translation_en", "location", "source_id")]
    if src:
        parts += [src["url"], src["type"], src["excerpt"], str(src["flagged"])]
    if row:
        parts += [str(row["credibility"]), row["decision"]]
    return hashlib.sha1("\x1f".join(parts).encode("utf-8")).hexdigest()[:10]


def cached_live(claim, fp):
    """Live result from the previous run, only if nothing changed and the page was actually read then."""
    m = re.search(r"\[h:(\w+)\|live:([^\]]*)\]", claim.get("auto_verified", "") or "")
    if m and m.group(1) == fp and m.group(2) in ("match", "NO MATCH"):
        return m.group(2)
    return None


def verify(claim, appraised, offline, changed_only=False):
    cid, sid = claim.get("claim_id"), claim.get("source_id")
    orig, tr = claim.get("original_nl", "") or "", claim.get("translation_en", "") or ""
    out = {"claim_id": cid, "source_id": sid, "kind": claim.get("kind"), "triggers": [], "fails": []}

    if claim.get("translated_by") == "person":
        out.update(route="PERSON-ENTERED", detail="interview/person claim: entered and verified by a person")
        return out

    if claim.get("_yaml_errors"):
        out["fails"].append("malformed YAML quoting in: " + ", ".join(claim["_yaml_errors"]))

    src, row = load_source(sid), appraised.get(sid)
    out["fp"] = fingerprint(claim, src, row)
    if src is None:
        out["fails"].append(f"no library/sources/{sid}.md")
    if row is None:
        out["fails"].append(f"{sid} not in appraised.md")
    elif row["decision"] != "use":
        out["fails"].append(f"{sid} decision is '{row['decision']}'")

    # A number may come from the quoted sentence, the claim's location ("Article 26") or the source title;
    # one found only elsewhere in the excerpt needs a person; one found nowhere is a fail.
    extra = numbers(tr) - numbers(orig) - numbers(claim.get("location", "") or "") - numbers(src["title"] if src else "")
    elsewhere = extra & numbers(src["excerpt"]) if src else set()
    if extra - elsewhere:
        out["fails"].append("numbers in translation not in source: " + ", ".join(sorted(extra - elsewhere)))
    if elsewhere:
        out["triggers"].append("T2 number not in the quoted sentence: " + ", ".join(sorted(elsewhere)))

    if src:
        out["excerpt"] = "match" if contains(norm(src["excerpt"]), orig) else "NO MATCH"
        if out["excerpt"] != "match":
            out["triggers"].append("T2 sentence not in saved excerpt")
        if offline:
            out["live"] = "skipped (--offline)"
            out["triggers"].append("T2 live document not checked")
        elif changed_only and cached_live(claim, out["fp"]):
            out["live"] = cached_live(claim, out["fp"])
            out["live_cached"] = True
        else:
            status, text = live_text(src["url"])
            out["live"] = ("match" if contains(text, orig) else "NO MATCH") if status == "ok" else status
            if out["live"] != "match":
                out["triggers"].append(f"T2 live document: {out['live']}")
        if src["flagged"]:
            out["triggers"].append("T1 source file carries a FLAG FOR HUMAN REVIEW")
    if row:
        out["credibility"] = row["credibility"]
        if row["credibility"] < 3:
            out["triggers"].append(f"T1 credibility {row['credibility']}")
        elif src and src["type"] not in CRED3_TYPES:
            out["triggers"].append(f"T1 credibility 3 but type '{src['type']}' cannot score 3")

    if out["fails"]:
        out["route"] = "FAIL"
    elif out["triggers"]:
        out["route"] = "PERSON"
    else:
        out["route"] = "AUTO-PASS"
    return out


def draft_label_check(draft_path, claims_by_id):
    """Every [W2-xxx, evidence, scope] bracket in the draft: id exists, labels match claims_en.md."""
    problems, cited = [], []
    for m in re.finditer(r"\[(W\d+-\d{3})([^\]]*)\]", draft_path.read_text(encoding="utf-8")):
        cid, rest = m.group(1), m.group(2)
        cited.append(cid)
        c = claims_by_id.get(cid)
        if not c:
            problems.append(f"{cid}: cited in draft but not in claims_en.md")
            continue
        for field in ("evidence", "scope"):
            if c.get(field) and c[field] not in rest:
                problems.append(f"{cid}: draft label lacks {field} '{c[field]}'")
    return sorted(set(cited)), sorted(set(problems))


# ---------- writing ----------

def auto_line(r):
    tag = f" [h:{r.get('fp')}|live:{r.get('live', '')}]"
    if r["route"] == "AUTO-PASS":
        return f"{TODAY} AUTO-PASS: excerpt+live match, numbers ok, credibility {r.get('credibility')}" + tag
    if r["route"] == "PERSON":
        return f"{TODAY} PERSON: " + "; ".join(r["triggers"]) + tag
    if r["route"] == "FAIL":
        return f"{TODAY} FAIL: " + "; ".join(r["fails"]) + tag
    return ""


def queue_results(path):
    """source_id -> what a person wrote in review_queue.md's result column."""
    old = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 5 and re.fullmatch(r"S-\d{3}", cells[0]):
                old[cells[0]] = cells[4]
    return old


def person_ok(result_cell):
    """A queue result counts as closed-ok when it reads like 'Name, 2026-10-02: ok'."""
    return bool(re.search(r":\s*ok\b", result_cell or "", re.I))


# ---------- drafter self-check (no network) ----------

def route_of(claim):
    av = (claim.get("auto_verified", "") or "").split("[")[0]
    for r in ("AUTO-PASS", "PERSON", "FAIL"):
        if r in av:
            return r
    return ""


def precheck(draft_path, claims_by_id):
    cited, problems = draft_label_check(draft_path, claims_by_id)
    text = draft_path.read_text(encoding="utf-8")
    for cid in cited:
        c = claims_by_id.get(cid)
        if not c:
            continue
        route = route_of(c)
        if c.get("superseded_by"):
            problems.append(f"{cid}: superseded by {c['superseded_by']} - cite that claim instead")
        elif route == "FAIL":
            problems.append(f"{cid}: claim is FAIL in claims_en.md - it may not be in the draft")
        elif not route and c.get("translated_by") != "person":
            problems.append(f"{cid}: not verified yet - run /verify-claims first")
        elif route == "PERSON" and not c.get("verified_by"):
            if not re.search(re.escape(cid) + r"[^\]]*\]\s*\(awaiting source check\)", text):
                problems.append(f"{cid}: awaits a person's source check - add '(awaiting source check)' after its bracket")
    return cited, sorted(set(problems))


# ---------- Stage 5: the tool part of check.md ----------

def recommendations(draft_text):
    """Numbered recommendations in the draft: '1. **step - what.**' -> short titles."""
    sec = re.split(r"(?im)^##\s+.*recommendation.*$", draft_text, maxsplit=1)
    body = re.split(r"(?m)^##\s", sec[1])[0] if len(sec) > 1 else ""
    return [m.group(1).strip() for m in re.finditer(r"(?m)^\d+\.\s+\*\*(.+?)\*\*", body)]


def write_check_md(path, draft_path, results, claims_by_id, label_problems, appraised):
    queue = queue_results(LIB / "review_queue.md")
    draft_text = draft_path.read_text(encoding="utf-8")
    labels_bad = {p.split(":")[0] for p in label_problems}
    week = re.search(r"^week:\s*(\S+)", (WEEK / "question.md").read_text(encoding="utf-8"), re.M)
    ctx = re.search(r"^version:\s*(\S+)", (ROOT / "context.md").read_text(encoding="utf-8"), re.M)
    drafted = datetime.date.fromtimestamp(draft_path.stat().st_mtime).isoformat()

    rows, n_pass = [], 0
    for r in results:
        c = claims_by_id.get(r["claim_id"], {})
        vb = (c.get("verified_by") or "").strip()
        if r["route"] == "AUTO-PASS":
            verified = "auto"
        elif r["route"] == "PERSON" and vb and person_ok(queue.get(r["source_id"])):
            verified = f"person: {vb}"
        elif r["route"] == "PERSON-ENTERED" and vb:
            verified = f"person: {vb} (interview)"
        else:
            verified = "open"
        dec = appraised.get(r["source_id"], {}).get("decision", "missing")
        numbers_ok = not any(f.startswith("numbers") for f in r["fails"])
        excerpt, labels = r.get("excerpt", "n/a"), "NO" if r["claim_id"] in labels_bad else "yes"
        ok = (r["route"] != "FAIL" and verified != "open" and numbers_ok and labels == "yes" and dec == "use"
              and (excerpt in ("match", "n/a") or verified.startswith("person")))
        n_pass += ok
        note = "; ".join(r["fails"] + r["triggers"])
        rows.append(f"| {r['claim_id']} | yes | {excerpt} | {r.get('live', 'n/a')} | {'yes' if numbers_ok else 'NO'} | "
                    f"{labels} | {'yes' if dec == 'use' else f'NO ({dec})'} | {verified} | {'pass' if ok else 'FAIL'} | {note} |")
    for p in label_problems:
        if "not in claims_en.md" in p:
            rows.append(f"| {p.split(':')[0]} | NO | | | | | | open | FAIL | {p} |")

    closed = [sid for sid in queue if person_ok(queue[sid]) or "discard" in queue[sid].lower()]
    recs = recommendations(draft_text)

    keep = ""
    if path.exists():
        old = path.read_text(encoding="utf-8")
        if "<!-- generated by verify_claims.py -->" in old and "## Second reader" in old:
            keep = "## Second reader" + old.split("## Second reader", 1)[1]
    if not keep:
        keep = "\n".join([
            "## Second reader: ______ (not the author)",
            "| criterion | pass/fail | one line |", "|-----------|-----------|----------|",
            "| 1 names a step, not a tool | | |", "| 2 time-saving vs customer-touching, stated | | |",
            "| 5 complexity label per recommendation | | |", "| 6 one next step: owner, cost, 3-month check | | |", "",
            "## Final: publish / return to draft · decided by: ______ · date: ______", ""])

    body = [
        f"# check.md — week {week.group(1) if week else '__'} · draft of {drafted} · context version: {ctx.group(1) if ctx else '__'}",
        "<!-- generated by verify_claims.py -->",
        "",
        f"## Tool checks (one row per [claim-id] in draft.md) — {n_pass} of {len(rows)} pass · live documents fetched {TODAY}",
        "| claim_id | claim exists | quote in saved source | live document | numbers match | labels present (crit 4) | source `decision: use` | verified (auto / person / open) | pass/fail | note |",
        "|----------|--------------|-----------------------|---------------|---------------|--------------------------|------------------------|---------------------------------|-----------|------|",
        *rows,
        "",
        "## Duty named per recommendation (crit 3) — checker fills",
        "| recommendation | duty named with claim-id (AI Act / GDPR / sanctions) | supplier hosting named or 'not known' | pass/fail |",
        "|----------------|------------------------------------------------------|----------------------------------------|-----------|",
        *[f"| {i}. {t} | | | |" for i, t in enumerate(recs, 1)],
        *(["| (no numbered recommendations found in draft.md) | | | FAIL |"] if not recs else []),
        "",
        "## Person source checks (context.md §3c)",
        f"`review_queue.md`: {len(closed)} of {len(queue)} sources closed · open: {', '.join(s for s in queue if s not in closed) or 'none'}",
        "",
        keep.rstrip() + "\n",
    ]
    path.write_text("\n".join(body), encoding="utf-8")
    return n_pass, len(rows)


def write_auto_verified(path, results):
    lines, by_id, cur = path.read_text(encoding="utf-8").splitlines(), {r["claim_id"]: r for r in results}, None
    out = []
    for line in lines:
        m = re.match(r"\s*-\s*claim_id:\s*(\S+)", line)
        if m:
            cur = m.group(1)
        if re.match(r"\s+auto_verified:", line) and cur in by_id:
            continue  # replaced below, after verified_by
        out.append(line)
        if re.match(r"\s+verified_by:", line) and cur in by_id and auto_line(by_id[cur]):
            indent = re.match(r"(\s+)", line).group(1)
            out.append(f'{indent}auto_verified: "{auto_line(by_id[cur])}"   # tool-filled; never a person\'s name')
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def write_queue(path, results, appraised):
    old = queue_results(path)  # keep what people already wrote in the result column
    per_source = {}
    for r in results:
        if r["route"] == "PERSON":
            s = per_source.setdefault(r["source_id"], {"triggers": set(), "claims": []})
            s["triggers"].update(t.split(":")[0] if t.startswith("T2 live") else t for t in r["triggers"])
            s["claims"].append(r["claim_id"])
    rows = []
    for sid in sorted(per_source):
        s = per_source[sid]
        todo = "open the source; confirm rating + each listed sentence; put your name in verified_by of each claim that holds"
        rows.append(f"| {sid} | {'; '.join(sorted(s['triggers']))} | {', '.join(s['claims'])} | {todo} | {old.get(sid, '')} |")
    fails = [f"- {r['claim_id']} ({r['source_id']}): {'; '.join(r['fails'])}" for r in results if r["route"] == "FAIL"]
    auto = [r["claim_id"] for r in results if r["route"] == "AUTO-PASS"]
    body = [
        "# review_queue.md — the only source checks a person does (context.md §3c)",
        "",
        f"generated: {TODAY} by verify_claims.py · rerun overwrites everything except the result column",
        "",
        "| source_id | why a person (trigger) | claims to check | what to do | result (who, date: ok / fix / discard) |",
        "|-----------|------------------------|-----------------|------------|-----------------------------------------|",
        *rows,
        "",
        f"## Back to Translate (tool fails, not a person check): {len(fails)}",
        *(fails or ["- none"]),
        "",
        f"## Auto-verified, no person needed: {len(auto)}",
        ", ".join(auto) or "none",
        "",
    ]
    path.write_text("\n".join(body), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--claims", default="library/claims_en.md")
    ap.add_argument("--appraised", default="library/appraised.md")
    ap.add_argument("--draft")
    ap.add_argument("--only", help="comma-separated claim ids")
    ap.add_argument("--offline", action="store_true", help="skip live fetch (every claim then routes to a person)")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--changed", action="store_true", help="reuse last run's live result for unchanged claims")
    ap.add_argument("--precheck", action="store_true", help="with --draft: no network; labels, ids and routes only")
    ap.add_argument("--check-md", help="with --draft: write the tool part of this check file")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    claims = load_claims(ROOT / a.claims)
    by_id = {c["claim_id"]: c for c in claims}
    appraised = load_appraised(ROOT / a.appraised)

    if (a.precheck or a.check_md) and not a.draft:
        ap.error("--precheck and --check-md need --draft")
    if a.write and (a.only or a.draft):
        ap.error("--write needs the full claim set (no --only / --draft), or review_queue.md would lose rows")

    if a.precheck:
        cited, problems = precheck(week_file(a.draft), by_id)
        print(f"precheck: {len(cited)} claim-ids cited, {len(problems)} problem(s)")
        for p in problems:
            print("FIX:", p)
        return 1 if problems else 0

    cited, label_problems = ([], [])
    if a.draft:
        cited, label_problems = draft_label_check(week_file(a.draft), by_id)
    wanted = set(a.only.split(",")) if a.only else (set(cited) if a.draft else None)
    results = [verify(c, appraised, a.offline, a.changed) for c in claims if wanted is None or c["claim_id"] in wanted]

    if a.write:
        write_auto_verified(ROOT / a.claims, results)
        write_queue(LIB / "review_queue.md", results, appraised)
    if a.check_md:
        n_pass, n = write_check_md(week_file(a.check_md), week_file(a.draft), results, by_id, label_problems, appraised)
        print(f"check.md written: {n_pass} of {n} claim rows pass")

    if a.json:
        print(json.dumps({"results": results, "draft_label_problems": label_problems}, ensure_ascii=False, indent=1))
        return
    print("| claim | source | cred | excerpt | live | route | why |")
    print("|---|---|---|---|---|---|---|")
    for r in results:
        why = "; ".join(r["fails"] + r["triggers"]) or r.get("detail", "")
        print(f"| {r['claim_id']} | {r['source_id']} | {r.get('credibility', '')} | {r.get('excerpt', '')} | {r.get('live', '')} | {r['route']} | {why} |")
    counts = {k: sum(r["route"] == k for r in results) for k in ("AUTO-PASS", "PERSON", "FAIL", "PERSON-ENTERED")}
    cached = sum(bool(r.get("live_cached")) for r in results)
    print("\n" + " · ".join(f"{k}: {v}" for k, v in counts.items()) + (f" · live reused (unchanged): {cached}" if cached else ""))
    for p in label_problems:
        print("DRAFT LABEL:", p)


if __name__ == "__main__":
    sys.exit(main())
