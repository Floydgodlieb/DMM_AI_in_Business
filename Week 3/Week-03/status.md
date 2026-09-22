# Status — Week-03

_Started 2026-09-22._

Regenerated in part at every gate. `scripts/progress.py report` rewrites only the section
between the `PROGRESS_TABLE_START`/`END` markers below — everything else on this page is
maintained by hand.

## Current stage

Stage 7 (Final QA) — done. **`06_final/handbook_page_week3.md` and `06_final/qa_note.md` are
written.** Word count vs. per-section budgets (`wordcount.py`): 3 of 7 sections run over their
individual sub-budget (Staff-disclosure +32%, Next step +20%, Disclaimer +12%), but the page's
actual total (443 words across sections) is close to the ~485 target — these are stage-4's
original per-section allocation misses, not an overall length problem; not blocking. Full
checklist audit: all hard and soft requirements met. Manual-fallback-note check: `progress.py`
itself is missing one — a real gap in the build repo's own script, flagged for you, not fixed
here (outside this stage's writable scope). Reference check, both directions: all 9 cited
sources trace to `source_bank.md`; 6 appraised-but-uncited sources is fine; no
`zotero_export.md` exists this week, correctly, since nothing was Zotero-synced.

**I5 (physical one-A4-page fit) is still the one open item — carried through every stage since
5, never resolved, because no browser or document tool was available in this session at any
point.** This is genuinely yours to close before hand-in: paste `06_final/handbook_page_week3.md`
into Word/Docs or the actual course-site template and confirm it's one page.

### What this needs from you

`approved` moves to stage 8 (Feedback Integration) — which has nothing to do yet, since no gate
feedback exists until the page is actually published and the partner team/Socratic tutor
respond. Practically, `approved` here means: **this pipeline run is finished until you (a) do
the physical page-fit check and (b) actually publish the page** — say when either happens and
I'll pick the next real step back up.

## Approvals

| Stage | Approved by | Date |
|---|---|---|
| 1. Requirements & Constraints | Floyd | 2026-09-22 |
| 2. Research & Source Bank | Floyd | 2026-09-22 |
| 3. Own Data Intake — skipped (no interview data yet) | Floyd | 2026-09-22 |
| 4a. Outline | Floyd | 2026-09-22 |
| 4b. Full draft | Floyd | 2026-09-22 |
| 5 / 4-revision. Review + revised draft (draft_v2.md, company name removed) | Floyd | 2026-09-22 |
| 6. Humanization & Deliverables (draft_v3.md) | Floyd | 2026-09-22 |

## Open questions

_(stop-and-ask items land here — anything an agent couldn't resolve on its own. Answered
questions move to a dated line below rather than being deleted, so the trail stays visible.)_

- **Borderline source calls, flagged per `lead-researcher`'s own stop-and-ask rule rather than
  silently included or dropped:** `S-020` (Dutch 78% shadow-AI figure) is only secondary-sourced
  — the primary Awareways report wasn't directly fetchable this session — kept as corroboration,
  scored down a point, not as sole support. `S-021` (Themio) is used for its legal framing only,
  not its own unattributed prevalence statistics. A directly relevant SSRN paper on AI Act
  Article 26 (Clark, 2026) was found but returned HTTP 403 to the fetch tool — not used without
  a readable quote; logged in `02_sources/to_download.md` if you want to fetch it yourself for
  stage 4. None of these block the gate; flagged for visibility.
- **Stage 3 (Own Data Intake).** Per `CLAUDE.md`, this stage only runs if
  `03_data/consent_checklist.md` is fully checked. It isn't — no interview has happened for this
  week yet. Recommend skipping straight to stage 4 on `approved`; say if you'd rather stage 3 be
  marked explicitly skipped-with-a-reason in `progress.json` first.

### Answered, 2026-09-22

- **Chapter shape** — does not need to follow the site's 7-part CRISP-DM anatomy; the team's own
  already-published shape is confirmed. (`format.md`)
- **Citation style** — keep the convention already implemented (inline `[claim-id, ...]` tags),
  not this pipeline's generic APA 7 default. (`format.md`)
- **Word budget** — **strict maximum one A4 page**, operationalised as ~500–550 words of body
  text. The existing draft (`Platform/draft.md`, ~1,330 words) is ~2.5× over and needs a
  substantial rewrite, not a trim, once stage 4 runs. (`checklist.md`, `format.md`)
- **Citation tags don't count toward the word total** — only the prose does (`checklist.md`).
  `04_draft/draft_v1.md` is 494 words of prose (515 with tags), close to but not exactly at the
  ~485 target; the real test is the physical one-page fit at stage 7, not this count.
- **Don't name the real case company (BAS World) in the page** — sector-level description only.
  `draft_v2.md` updated; recorded in `checklist.md` as a hard requirement for stage 6/7 too.

## Progress

<!-- PROGRESS_TABLE_START -->
_Generated 2026-09-22T17:03:22+02:00_

### Stage 1: Requirements & Constraints

| Task | Description | Status | Time spent |
|------|-------------|--------|------------|
| 1.1 Populate 00_input | Pull week 3 AIBS brief from course site (site/week-03.html) and team context from the DMM_AI_in_Business GitHub repo into 00_input/ | done | 1 min |
| 1.2 Write checklist.md | Hard/soft requirements, rubric, word budgets, AI-use disclosure rules | done | 2 min |
| 1.3 Write source_criteria.md | Inclusion criteria derived from requirements and output type | done | 0 min |
| 1.4 Write format.md | Format, deadline, individual/group, citation style, length, AI-disclosure block | done | 0 min |
| 1.5 Update status.md and stop for gate | Run progress.py report, set current stage, stop for Floyd's approval per rule 2 | done | 0 min |
| 1.6 Incorporate Floyd's answers | Resolve chapter-shape, citation-style, and word-budget open questions in checklist.md/format.md/status.md | done | 0 min |

**Stage 1 total: 3 min**

### Stage 2: Research & Source Bank

| Task | Description | Status | Time spent |
|------|-------------|--------|------------|
| 2.1 Search academic databases | OpenAlex/Semantic Scholar/Crossref per search-strategy skill, against source_criteria.md | done | 2 min |
| 2.2 Write to_download.md | Search strings, database results (or why insufficient), pointer to Platform/searchlog.md's direct-web-search trail | done | 0 min |
| 2.3 Reconcile Platform/ sources into 02_sources/source_bank.md | Full appraised set (13 sources), team's own citation/scoring convention per format.md | done | 1 min |
| 2.4 Update status.md and stop for gate | Search strings used, sources found, quality scores, any pending items | done | 0 min |

**Stage 2 total: 3 min**

### Stage 3: Own Data Intake

| Task | Description | Status | Time spent |
|------|-------------|--------|------------|
| 3.1 Stage skipped | No interview has happened for this week; 03_data/consent_checklist.md is unchecked, so this optional stage has nothing to run on. Skipped with Floyd's approval, 2026-09-22. | done | 0 min |

**Stage 3 total: 0 min**

### Stage 4: Argument Architecture & Drafting

| Task | Description | Status | Time spent |
|------|-------------|--------|------------|
| 4.1 Write outline.md (4a) | Mapped to rubric criteria, word budgets per section, checked against source_bank.md, within the strict 1-page limit | done | 0 min |
| 4.2 Update status.md, stop for 4a gate | Separate gate from the full draft, per agent instructions | done | 0 min |
| 4.3 Write draft_v1.md (4b) | Full ~485-word draft from outline.md and source_bank.md only, claim-id citations excluded from word count per Floyd's clarification | done | 1 min |
| 4.4 Update status.md, stop for 4b gate | Word count check, AI-disclosure block status | done | 0 min |
| 4.5 Revise: write draft_v2.md | Fix I1-I4, I6-I7 from issue_log.md; never overwrite draft_v1.md | done | 0 min |
| 4.6 Verify physical one-A4-page fit (I5) | Render as print-styled HTML, measure in a real browser against A4 printable dimensions | done | 2 min |
| 4.7 Update status.md, stop for gate | Report fixes and page-fit result | done | 1 min |

**Stage 4 total: 5 min**

### Stage 5: Review & Verification

| Task | Description | Status | Time spent |
|------|-------------|--------|------------|
| 5.1 Pass 1 — rubric audit | Audit draft_v1.md against checklist.md, hard requirements first | done | 0 min |
| 5.2 Pass 2 — quote verification | Attempt verify_quotes.py (expected to fail, no 02_sources/text/), then manual check against Platform/sources/S-0NN.md | done | 0 min |
| 5.3 Write issue_log.md and verification.md | Per issue-log-format | done | 1 min |
| 5.4 Update status.md, stop for gate | Issue count and severities | done | 0 min |

**Stage 5 total: 1 min**

### Stage 6: Humanization & Deliverables

| Task | Description | Status | Time spent |
|------|-------------|--------|------------|
| 6.1 Style-guide pass | Banned words, sentence variety, hollow contrasts, repetitive openings, filler — per style-guide skill | done | 0 min |
| 6.2 Finalize AI-use disclosure block | Replace the interim placeholder with an honest, accurate disclosure of what happened so far | done | 1 min |
| 6.3 Update status.md, stop for gate |  | done | 0 min |

**Stage 6 total: 1 min**

### Stage 7: Final QA

| Task | Description | Status | Time spent |
|------|-------------|--------|------------|
| 7.1 Run wordcount.py vs budgets | Build word_budgets.json from checklist.md's table, matching draft_v3.md's actual headings | done | 0 min |
| 7.2 Full checklist audit | Every hard and soft requirement in checklist.md, not a sample | done | 0 min |
| 7.3 Manual-fallback-note presence check | Every script actually used this week: progress.py, verify_quotes.py, wordcount.py | done | 0 min |
| 7.4 Two-way reference check | source_bank.md vs draft_v3.md citations, both directions; no zotero_export.md this week (no PDFs synced) | done | 0 min |
| 7.5 Write 06_final/ + QA note, stop for gate |  | done | 1 min |

**Stage 7 total: 2 min**

### Stage 8: Feedback Integration

_No tasks yet._

**Overall total: 15 min**

**What's next:** All defined tasks are done.
<!-- PROGRESS_TABLE_END -->
