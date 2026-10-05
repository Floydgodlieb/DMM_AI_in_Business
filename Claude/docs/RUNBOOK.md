# RUNBOOK — producing one handbook page (week 2, by hand)

Boss this week: the product manager. One person drives the CLI assistant; the others work on the same files in parallel.
Every stage: (1) start the timer, (2) do the stage, (3) stop the timer and log it with `/log-time`, (4) commit. `/run-page` walks the stages and stops at each person gate.

## Day 1 — set up (30 min)
1. Unzip `platform.zip` so the files sit directly in
   `C:\Users\floyd\Desktop\DDM-AI in business repository\platform`
   (i.e. `...\platform\context.md`, not `...\platform\platform\context.md`). Open a terminal in that `platform` folder and start the CLI assistant there, so the folder boundary of door 2 is the folder it can see. The interview recording never goes in this repository.
2. Rename `ASSISTANT.md` to whatever your CLI assistant reads first (`CLAUDE.md` for Claude Code, `AGENTS.md` for others). It tells the assistant to read `context.md` and obey the stage rules.
3. Open the week's folder: `python .claude/scripts/gates.py new-week <NN>`, then fill `weeks/week-NN/question.md`. The library (`library/`) carries over; this week's draft, check and page go in that folder (see `CLAUDE.md`, "Where files live").
4. Every team member: open `timelog.csv` and log from the first minute.

## Stage 1 — Find sources (developer, ~2 h)
- Run the searches in `docs/03_Assignment2_Writeup.md` §2, in that order, NL first. Log every query in `searchlog.md`.
- Run `/find-sources`: it checks the source library (sources carry over between weeks), then runs one `source-finder` per search line at the same time and merges their results (`gates.py intake`, duplicates set aside). For one URL: `/find-sources <URL>`. Check URL and date of the new sources yourself.
- Stop rule: two searches in a row give nothing new, or one primary source per claim + one per region on the leadership question.
- Output: 15–25 `library/sources/S-0xx.md` files.

## Stage 2 — Appraise (tester, ~1 h)
- Run `/appraise` (rates only sources that have no row yet).
- You read only the rows at credibility 1–2 (context.md §3c; answers open question 2). Change what you disagree with; fill `human_override`. Set `decision: use/discard`. Rows at 3 stand unless you choose to override one.

## Stage 3 — Translate (developer + one verifier, ~2 h)
- Run `/translate`, then `/verify-claims`. The script checks every claim (all kinds, not a sample) against the saved excerpt and the live page, and writes `auto_verified` and `review_queue.md`.
- A second person works through `review_queue.md` only: open each listed source once, put your name in `verified_by` for each listed claim that holds, write the result in the queue. FAIL claims go back to `/translate`.
- Interview claims (if the visit has happened): a person types them in directly, `translated_by: person`.

## Stage 4 — Draft (author, ~2 h)
- Run `/draft <your angle>`. It follows `templates/draft.template.md` (stands in for the missing `04_Handbook_Page_Week2_Draft.md`) and fills each [CLAIM] slot only from claims_en.md.
- You choose the angle and edit the text. Do not add a sentence the assistant can't tie to a claim-id.

## Stage 5 — Check (tester + second reader, ~1.5 h)
- Run `/check` (by hand, if the tool is down: `templates/check.manual.md`). It re-runs the live verification and fills the tool columns.
- The second reader (never the author, rotates) answers criteria 1, 2, 5, 6 pass/fail with one line. Source opening is no longer five random statements: it is the `review_queue.md` list, which must be closed.
- Any fail → back to Stage 4. PM arbitrates disagreements.

## Stage 6 — Publish (deployer, ~1 h)
- Run `/publish-prep <version>`: it refuses unless check.md says publish, then writes `page.md` with version, date and the checking note ("x of y statements auto-verified against the live source; z sources checked by a person; all numbers checked").
- Publish on the course site by the route the session gave (branch → pull request → link check → merge). No direct push.
- Post in Teams: the page link, `docs/01_Technical_Blueprint_v1.1.md`, `docs/02_PRD_v2.1.md`, and the assignment 2 write-up wherever the session said.

## After
- Total the hours per stage from `timelog.csv`. Put the number in PRD §8 ("what we have now"). That is your baseline.
- Each person: write portfolio entry 2 after the gates answer (Mon 21 Sept).
