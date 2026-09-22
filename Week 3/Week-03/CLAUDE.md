# CLAUDE.md — Academic Pipeline (per-assignment orchestrator)

This governs one instance of the pipeline — one copy of `_template/`, one week's work
(`week-01/`, `week-02/`, …, per `scripts/new_assignment.py`). It is separate from, and more
detailed than, the build-repo's own root `CLAUDE.md`, which governs *building* this pipeline,
not running it.

Full rationale for every decision here lives in `docs/pipeline_spec.md`, `docs/build_plan.md`
and `docs/build_log.md` in the build repo. This file is the operative summary agents and Floyd
actually work from.

## What this is

A multi-agent pipeline for HAN minor Data Driven Decision Making (AI in Business) coursework.
Each instance produces one weekly handbook page through 8 stages, stage by stage, with an
approval gate after each one. All pipeline output is in English.

## Global rules — apply to every agent, every stage

1. **Stop-and-ask.** Never assume missing or ambiguous information. Add it to `status.md` under
   "Open questions" and ask Floyd. Don't guess and move on.
2. **Gates.** After each stage, update `status.md` and stop. Proceed only after Floyd types
   `approved`. See "Two different kinds of gate" below — this is the internal one.
3. **English output.** Non-English quotes keep the original plus a faithful English translation,
   side by side — never translation-only.
4. **Context management.** Every stage writes its output to files, and every stage starts by
   reading the relevant previous files — not chat history. A stage that needs to know what an
   earlier stage decided reads that stage's output file.
5. **Sources.** Only sources whose full text exists as a file in `02_sources/pdf/` may be quoted.
   Quotes are copied verbatim from the file with a page number. Nothing is ever quoted from
   memory — if an agent can't point to the file and page, it doesn't quote it.
6. **Privacy.** No agent may read `03_data/private/`. Never put identifiable personal or company
   data in any output. Enforced by `.claude/settings.json` (deny `Read` on `03_data/private/**`)
   as a backstop — but the rule holds regardless of what the settings file catches.
7. **Versioning.** Never overwrite a file that represents a revision. Save as `_v1`, `_v2`, etc.
   Platform documents in `platform_docs/` follow the same rule (`prd_v1.md`, `prd_v2.md`, …).
8. **Manual fallback.** Every automated step documents how Floyd can do it by hand. Every script
   under `scripts/` ships a short fallback note. `quality-assurance` (stage 7) checks each one is
   present, not just that it once existed.
9. **Progress tracking.** `scripts/progress.py` (copied in from the build repo) tracks the 8
   stages as phases in `progress.json`, broken into tasks when a stage starts. Timestamps come
   only from the system clock — never estimated. `scripts/progress.py report` regenerates the
   progress table inside `status.md` (between the `PROGRESS_TABLE_START`/`END` markers) at every
   gate, so Floyd can see per stage what was done, its status, and time spent.
10. **AI-use disclosure.** Every deliverable (handbook page, platform document, portfolio
    evidence) states what AI drafted and what a human checked. This is a course requirement, not
    an optional nicety — `format.md` carries the required disclosure block, and
    `quality-assurance` checks for it.

## Git safety

**Before any destructive git operation** — `git filter-repo`, `git reset --hard`, `git clean`,
`git push --force`, `git checkout -- .` (or any other form that discards uncommitted or already-
pushed work), `git restore` on uncommitted files — commit or stash whatever is currently
uncommitted first, explain in plain language exactly what the operation will do and what could be
lost, and wait for explicit approval before running it. `.claude/settings.json` asks for
confirmation on these as a technical backstop, but the rule holds regardless of what the settings
file catches. Same incident and rationale as the build repo's own root `CLAUDE.md` — see the
build repo's `docs/build_log.md`, phase 8 follow-up.

## Two different kinds of gate — don't conflate them

- **This pipeline's own gate** (rule 2 above): internal, after each of the 8 stages, blocking —
  nothing proceeds until Floyd types `approved`.
- **The course's two gates** (Socratic tutor, peer team): external, weekly, run by the course
  itself on whatever the team has published — and **informational only**, not blocking. Nothing
  in this pipeline should wait on them or treat them as a pass/fail check. Their only home here is
  as *input*: log what they asked and what changed in response, so `portfolio_evidence.md` can
  compile it factually. See rule on the portfolio below.

## What this pipeline does NOT produce

- **The six AEL platform documents** (PRD, blueprint, knowledge architecture, build plan, two
  evaluations) are a separate, deliberately separate track — not one of the 8 stages below. They
  live in the root `platform_docs/` folder (sibling to every week instance, not nested inside
  one), versioned per revision. A dedicated skill (phase 7) carries their templates. The pipeline
  may help draft them, but **a team member reviews and posts every one** — no auto-publish, ever.
- **The individual portfolio** (30% of both course marks) is never AI-drafted. This pipeline only
  ever compiles the *factual record* a portfolio entry is written from —
  `scripts/portfolio_evidence.py` (phase 5) fills in `portfolio_evidence.md` with what was
  published, the gate questions received, what changed in response, and task times. Floyd writes
  the actual entry himself. No agent produces reflection text about Floyd's own contribution.

## The 8 stages

Each stage: reads specific files (rule 4), writes specific files, then updates `status.md` and
stops for approval (rule 2).

1. **Requirements & Constraints** — `requirements-analyst`. Reads `00_input/`. Writes
   `checklist.md` (hard/soft requirements, assessment rubric, word budgets per section, the
   course's AI-use and disclosure rules), `source_criteria.md` (inclusion criteria derived from
   the requirements and output type), `format.md` (format, deadline, individual/group, citation
   style, length, AI-disclosure block — asks Floyd if any of these are missing). Checks
   `_skill_material/` for a published course criteria page matching this week's deliverable
   before deriving criteria from scratch.
2. **Research & Source Bank** — `lead-researcher`. Builds search strings, searches OpenAlex,
   Semantic Scholar, Crossref. Writes candidates with DOIs to `to_download.md`. Downloads
   open-access versions via Unpaywall. Marks paywalled items for Floyd to fetch via HAN access
   with Zotero, then pauses until confirmed. Runs the sync script. Writes `source_bank.md`
   (APA 7 reference, file name, page, verbatim quote, English translation, findings/methodology,
   relevance, quality score with justification).
3. **Own Data Intake** — `data-intake`, optional. Runs only if `03_data/consent_checklist.md` is
   fully checked. Works only on `03_data/anonymized/` — never `03_data/private/`. Flags any
   remaining personal data it finds. Produces a data summary and analysis. Interview audio itself
   is handled *before* this stage even starts: transcribed locally, then anonymized, then
   translated — see `03_data/consent_checklist.md` for the full chain and why.
4. **Argument Architecture & Drafting** — `academic-writer`. 4a: `outline.md` mapped to rubric
   criteria with word budgets — its own approval gate before 4b starts. 4b: full draft using only
   the source bank and anonymized data, APA 7 in-text citations for every claim, written to the
   course's handbook chapter format (not a generic essay — see the `report-formats` skill).
5. **Review & Verification** — `reviewer-factchecker`. Pass 1: rubric audit. Pass 2: run
   `scripts/verify_quotes.py` and check every claim follows from its cited source. Writes
   `issue_log.md` and `verification.md`. Max 2 iterations. Done = no open critical or major
   issues.
6. **Humanization & Deliverables** — `academic-editor`. Applies the style guide (banned words:
   delve, tapestry, pivotal, spearhead, testimony, multifaceted, dynamic, seamlessly; vary
   sentence length; avoid repetitive "Transition, clause" openings). Produces deliverables only if
   requested, in the format from `format.md`.
7. **Final QA** — `quality-assurance`. Grammar, formatting, word count vs. budgets, full checklist
   audit, manual-fallback-note presence per script, AI-disclosure block presence. Reference list
   checked both ways and against the Zotero export. Final output to `06_final/`.
8. **Feedback Integration** — `revision-specialist`. Revision matrix
   (`Feedback item | Location | Action taken | Updated text`), version 2.0, rubric re-score.

## Agent tool restrictions (built out in phase 6)

| Agent | Tools | Model |
|---|---|---|
| requirements-analyst | minimum needed, read `00_input/`, write `01_requirements/`, `progress.py` | Sonnet |
| lead-researcher | web search/fetch, bash, read/write `02_sources/`, `progress.py` | Sonnet |
| data-intake | read `03_data/anonymized/` only, write data summary, `progress.py` | Sonnet |
| academic-writer | **no web access**; reads `01_`, `source_bank.md`, `03_data/anonymized/`; writes `04_draft/`; `progress.py` | **Opus** |
| reviewer-factchecker | **read-only**, plus bash limited to `scripts/verify_quotes.py`; writes `05_review/` only; `progress.py` | **Opus** |
| academic-editor | minimum needed, read `04_draft/`/`05_review/`, write deliverables, `progress.py` | Sonnet |
| quality-assurance | minimum needed, read broadly, write `06_final/`, `progress.py` | Sonnet |
| revision-specialist | minimum needed, read `07_feedback/`, write `07_feedback/`, `progress.py` | Sonnet |
| platform-doc-drafter (extra, finding 2) | reads `platform-documents.html`-derived skill templates + this week's context; writes `platform_docs/` drafts only, never posts; `progress.py` | Sonnet |

Default model is Sonnet; Opus is reserved for the two stages where getting it wrong is most
costly (drafting the actual academic argument, and catching what's wrong with it). Haiku is for
mechanical, non-judgment tasks (text extraction, formatting, word counts) inside scripts/skills,
not a full agent role of its own. Keep token use lean — every agent reads files, never full chat
history (rule 4), regardless of model.

No agent gets more than what its stage needs. `03_data/private/` is off-limits to all of them
(rule 6).

## Folder reference

```
CLAUDE.md                  this file
.claude/agents/            stage agents (phase 6)
.claude/skills/             shared skills (phase 7)
.claude/settings.json       permission deny rules
00_input/                   course docs, rubric, brief — filled in by hand per week
01_requirements/             checklist.md, source_criteria.md, format.md
02_sources/pdf/               AuthorYear_ShortTitle.pdf
02_sources/text/               extracted text per page
02_sources/to_download.md, source_bank.md
03_data/private/                raw data + anonymization key — agents blocked, git-ignored
03_data/anonymized/
03_data/consent_checklist.md
04_draft/                        outline.md, draft_vX.md
05_review/                        issue_log.md, verification.md
06_final/
07_feedback/                       feedback + revision_matrix.md
status.md                  current stage, approvals, open questions, progress table
progress.json               this week's progress tracker
portfolio_evidence.md        factual record for Floyd's own (manual) portfolio entry
scripts/                     progress.py (copied in) + phase-5 scripts
```

`platform_docs/` and (later) `consolidation/` are **not** inside this folder — they're siblings,
shared across all weeks. `scripts/new_assignment.py` creates `platform_docs/` on first run if it
doesn't already exist.

## Scripts (phase 5 builds these; `progress.py` already works)

- `progress.py` — task tracker. Already copied in and working.
- `sync_sources.py` — pulls new items/PDFs from Zotero's local API, renames to
  `AuthorYear_ShortTitle.pdf`, checks PDF matches DOI, exports APA metadata. Unpaywall email:
  `fr.godlieb@student.han.nl`.
- `extract_text.py` — per-page text extraction into `02_sources/text/`.
- `verify_quotes.py` — checks each quote exists at its stated page, normalizing whitespace, line
  breaks, hyphenation, ligatures, curly quotes.
- `anonymize.py` — LOCAL, no AI. Replaces names/terms from a mapping file in `03_data/private/`,
  writes to `03_data/anonymized/`.
- `transcribe_translate.py` — local transcription (`faster-whisper`/`openai-whisper`) of interview
  audio, output to `03_data/private/`; translation is a separate later step, done via Claude on
  the *anonymized* transcript only, after `anonymize.py` has run. See
  `03_data/consent_checklist.md`.
- `wordcount.py` — words per section vs. budgets.
- `portfolio_evidence.py` — compiles `portfolio_evidence.md` from gate logs, the issue log, the
  revision matrix, and `progress.json`. Never drafts reflection text.

Every script above ships a manual-fallback note (rule 8).

## Starting a new week

From the build repo root: `python scripts/new_assignment.py week-NN`. Copies `_template/` into
`week-NN/`, seeds `status.md` with the week name and today's date, and creates root-level
`platform_docs/` if it doesn't exist yet. See that script's own `--help` for options.
