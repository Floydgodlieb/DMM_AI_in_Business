# format.md — week 3, AIBS handbook page

## Format

**A handbook chapter/page**, per the course brief. **Resolved by Floyd, 2026-09-22: does not
need to follow the 7-part CRISP-DM anatomy.** Option B below is confirmed.

**Option A — the published 7-part CRISP-DM anatomy** (`handbook.html#chapter`, also this
pipeline's own `report-formats` skill): question narrowed to an SME type → plain-language
theory → one worked example through CRISP-DM's six phases → recommended tooling (no-code first,
cost noted) → responsible-AI & trust section → first five steps for an owner → sources, plus a
metadata block (team/cohort/version/named-or-persona SME/date sources last appraised).

**Option B — the team's own already-published shape** (week 2's live `HandbookPage.md`, and this
week's existing `Platform/draft.md`, built to match it): why this matters → the evidence,
organised by the week's own sub-questions rather than CRISP-DM phases → the duties that apply →
recommendations (step, customer-touching or not, complexity label) → next step → disclaimer.

**Why this matters, not just a formality:** a trust/safety topic has no data-modelling task to
run through CRISP-DM's six phases — there is no dataset, no model being built or evaluated. Option
A's "worked example (CRISP-DM)" and "recommended tooling, no-code first" slots do not fit this
week's actual content the way they fit, say, a demand-forecasting chapter. Option B is also what
the team has actually published once already and had reviewed — now confirmed as the shape to
use, consistent with precedent and with `rubric-decomposition`'s "pull in published criteria
before deriving your own."

## Deadline

**Monday 28 September 2026**, start of the next session — from the course brief. Hand-in is by
publishing the page live on the shared course site; a repository link or a document that "cannot
be read... counts as not handed in" (course brief, verbatim).

## Individual or group

**Group** — "one published handbook page per team" (course brief). The team: Aäron Bos, Floyd
Godlieb, Ivan van Vreeswijk, Baran Yapici (`00_input/team_context.md`).

## Citation style

**Resolved by Floyd, 2026-09-22: keep the convention already implemented.** Inline
`[claim-id, evidence-label, scope-label]` tags (e.g. `[W2-001, independently-verifiable,
sector]`) tracing to `claims_en.md`/`appraised.md`, no separate APA-formatted reference list on
the page itself — not this pipeline's generic `apa7` default. Neither the course brief nor
`handbook.html` mandates APA specifically; the brief's own language ("every claim carries an
appraised source") is satisfied at least as well by a claim-id a reader can trace straight to
the exact quote and appraisal.

## Length

**Resolved by Floyd, 2026-09-22: strict maximum one A4 page.** Operationalised in
`checklist.md`'s word-budget table as ~500–550 words of body text — the existing draft
(~1,330 words) is roughly 2.5× over and needs a substantial rewrite at stage 4, not a trim.

## AI-disclosure block

Required by the course brief, restated as global rule 10. Not yet a proper block on the page
itself — currently only an internal process note and a checking-note line in `Platform/draft.md`.
Stage 6 (`academic-editor`) must turn this into the disclosure the course expects on the
*published* page, not leave it as process-only commentary. Recorded here so stage 6 doesn't
have to rediscover the requirement.
