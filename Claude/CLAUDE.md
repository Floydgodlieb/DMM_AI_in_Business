# Instructions for the CLI assistant (rename to CLAUDE.md / AGENTS.md)

Read `context.md` before every task. It is the only source of the target reader, the six quality criteria, who checks what (§3c), the out-of-scope list and the house style. Do not keep your own copy of any of it.

Rules that hold for every stage:
- Work only with files inside this `platform/` folder. Never read, request or reference any recording, transcript or file outside it. Interview material is entered by a person; you never process it. (`.claude/hooks/stay_in_platform.py` blocks tool calls that leave the folder.)
- Every fact you write down carries a source id and the verbatim sentence it rests on. If you cannot point to a sentence in `library/sources/`, write nothing.
- Never edit `original_nl`. Never fill `verified_by`; a person does. `auto_verified` is written only by `verify_claims.py`, never by hand.
- Never change a rating a person has overridden.
- Never publish. Stage 6 is done by a person; `/publish-prep` only prepares `page.md` when the deployer runs it.
- Output only the file the stage asks for, in the exact shape of its template. No prose around it.

Each stage has a skill (`.claude/skills/`) and, where a separate context or a cheaper model pays off, an agent (`.claude/agents/`). Bookkeeping that needs rules, not judgement, is done by `.claude/scripts/` (no model, no credits).

| Stage | Skill | Agent (model) | Script | Writes |
|---|---|---|---|---|
| 1 Find | `/find-sources` (coordinator) | source-finder ×n in parallel (sonnet) | `gates.py library`, `intake` | `library/sources/S-0xx.md`, `searchlog.md` |
| 2 Appraise | `/appraise` | appraiser (sonnet) | `gates.py todo` | `appraised.md` (new rows) |
| 3 Translate | `/translate` → `/verify-claims` | translator (sonnet) | `verify_claims.py --write --changed` | `claims_en.md`, `review_queue.md` |
| 4 Draft | `/draft` | drafter (opus) | `verify_claims.py --precheck` | `draft.md` |
| 5 Check | `/check` (by hand: `templates/check.manual.md`) | checker (haiku) | `verify_claims.py --check-md` | `check.md` |
| 6 Publish | `/publish-prep` (deployer only) | none | `gates.py publish-gate` | `page.md` |

`library/sources/`, `appraised.md` and `claims_en.md` are a library that carries over between weeks: each stage only does what `gates.py todo` lists as new. `/run-page` walks the stages with the gates; `/log-time` writes `timelog.csv`.

## Where files live

| Folder | Holds | Carries over between weeks? |
|---|---|---|
| `library/` | `sources/` (+ `incoming/`, `PDF/`), `appraised.md`, `claims_en.md`, `searchlog.md`, `review_queue.md` | Yes |
| `weeks/week-NN/` | `question.md`, `draft.md`, `check.md`, `page.md` for that week | No: one folder per week |
| `templates/` | The shape of every stage's output, `question.template.md`, `check.manual.md` | Yes |
| `docs/` | PRD, blueprint, assignment 2 write-up, `RUNBOOK.md` | Yes |
| `wiki/` | The wiki (see below) | Yes |
| `reference/` | Course-site repository copy; not part of the pipeline, never edit | n/a |

This week = the newest `weeks/week-NN/` (`gates.py todo` prints it; `HANDBOOK_WEEK=NN` overrides). A new week starts with `python .claude/scripts/gates.py new-week <NN>`. Scripts take bare names (`draft.md`) and resolve them; when you read or write a file yourself, use the full path. `context.md`, `CLAUDE.md` and `timelog.csv` stay at the top.

## The wiki (beside the stages, not one of them)

`wiki/` is a persistent, interlinked synthesis of the library, maintained by the assistant: source, topic and entity pages, filed answers, an overview. Its rules are in `wiki/SCHEMA.md`. Every fact in it ends with a claim-id from `claims_en.md`. It never edits the library and is never a source for Draft; Draft may use it only to find the right claims.

| Operation | Skill | Agent (model) | Script | Writes |
|---|---|---|---|---|
| Ingest (after Translate) | `/wiki-ingest` | wiki-keeper (sonnet) | `wiki.py refresh`, `status`, `lint`, `log` | `wiki/` pages |
| Query | `/wiki-query <question>` | none | `wiki.py lint`, `log` | `wiki/answers/` (if kept) |
| Lint | `/wiki-lint` | wiki-keeper (sonnet) | `wiki.py lint` | fixes in `wiki/`, candidate search lines |
