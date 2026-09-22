# source_criteria.md — week 3, AIBS handbook page

Derived from the requirements in `checklist.md` and the output type (a handbook page whose every
claim must trace to an appraised source). Two layers: the course's own published framework, and
the team's own established operationalization of it — used instead of this pipeline's generic
`source-evaluation` skill's High/Medium/Low scale, for the reason given below.

## The course's own framework (published, `_skill_material/`, week 3 session content)

Both desk research and field research — including an AI-assisted search method a team designs
itself — are held to the same three questions: **is it reliable, is it valid, is it
transparent?** (`source-evaluation` skill, sourced from the week-3 session material). Every
source below is checked against all three before use.

## The team's own operationalization (`00_input/team_context.md`; full detail in
`Platform/appraised.md`, `Platform/sources/*.md`)

**Chosen over this pipeline's generic High/Medium/Low scale.** The team already has a more
specific, working version of the same three-question framework — five pass/fail gates plus a
1–3 scale — used consistently since week 2 and already applied to every source in
`Platform/`. Per `rubric-decomposition`'s own instruction to pull in published/established
criteria before deriving new ones, this stage adopts the team's version rather than introducing
a second, incompatible scale.

**Gates (pass/fail; maps to "is it transparent" and part of "is it reliable"):**

| Gate | Test |
|---|---|
| G1 Attributable | A named author or institution stands behind it. Anonymous or AI-generated text fails. |
| G2 Dated | A publication date is visible, and it is recent, unless it is a regulation or a foundational/precedent record (exempted explicitly, not silently). |
| G3 Evidenced | It cites data, documents, or a named case/record that could in principle be opened. "Experts say" fails. |
| G4 Ownership disclosed | Who owns or funds the publisher is findable. A source with a commercial interest is used only as corroboration, never as sole support for a duty or figure. |
| G5 Primary where it matters | For a figure about a vendor, or a legal duty, the source is the vendor's own documentation, an official regulator/court record, or an independent named study — not a secondary summary. |

**Scale (1–3 each; maps to "is it valid" and the rest of "is it reliable"):**

| Dimension | 1 | 2 | 3 |
|---|---|---|---|
| Credibility | trade press, vendor/consultancy blog, opinion | named-author think tank, law firm thought leadership, disclosed-interest vendor documentation | regulation text, official statistics/regulator body, primary court/tribunal record, vendor's own contractual documentation |
| Relevance | about AI trust/safety in general | about this sector's AI vendors, agency, or disclosure risk | about what this specific reader (10–50 staff, no IT, this sector) depends on or is bound by |
| Recency | pre-2024 or undated, not otherwise exempted | 2025 | 2026, or the relevant law/reform as currently in force |

## This week's two additions (new, `Platform/context.md` §6, PM decision 2026-09-22)

- **Question-diversity rule.** For each of the three required parts, at least one neutral and
  one differently-angled or differently-worded search must be logged before appraising sources
  for that part — logged even when the second search finds nothing new. Rationale and results:
  `Platform/question.md` and `Platform/searchlog.md`.
- **Source-reliability rule, raised this week.** Written in direct response to the concern that
  week 2's sourcing leaned too often on undated marketing pages carried by a human override.
  A source failing G2 or G4 is not disqualified outright, but it may never be the *sole* support
  for a duty or a figure a reader would act on — it needs either a second, independent source
  making the same point, or explicit labelling in the draft that the claim is a single vendor's
  own, unverified word.

## Target count and scope

- **No fixed target count is published for this deliverable** (unlike, say, "at least two
  sources per region" in week 2's own diversity rule, which was itself team-derived, not
  course-published). This stage does not invent one; `source_criteria.md` requires only that
  every one of the three required parts has enough appraised, gate-passing sources to support
  its claims — checked in `Platform/appraised.md`, currently 8 new sources (`S-019`–`S-027`,
  minus `S-021`'s framing-only role) plus 5 carried-forward week-2 sources across the three
  parts.
- **Languages:** English by default (house style, `checklist.md`); Dutch where the sector or
  Dutch-specific evidence is genuinely better in Dutch (as with `S-020`), translated into
  `claims_en.md` with the original kept alongside, per global rule 3.
- **Recency:** 2025–2026 preferred; a regulation or a foundational/precedent legal record may be
  older, but only if the draft says explicitly why it's still the right source (e.g. `S-026`'s
  2024 tribunal decision, kept as precedent, not as a recent event).
- **What does *not* count as a source for a claim:** an AI tool's own unattributed output, a
  single AI-generated article (this pipeline's own draft.md is exactly this kind of output, and
  is not itself a citable source for a later stage), and any source that fails G1 outright
  (no named author or institution).
