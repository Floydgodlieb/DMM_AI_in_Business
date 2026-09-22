# checklist.md — week 3, AIBS handbook page

Derived from `00_input/week3_course_brief.md` (course site), `00_input/team_context.md` (the
team's own research proposal v2 and PRD v2.1), and the published chapter template/quality bar in
`_skill_material/ai-in-business-source/site/handbook.html`, per `rubric-decomposition`.

## Hard requirements

- [ ] Answers the course's own framing question in three parts: what leaves the building /
      could the firm run the model itself; when AI may act vs. only advise; what happens when
      staff use AI without saying so.
- [ ] Written for the SME the research proposal describes (the sector-owner persona in
      `00_input/team_context.md`), not a generic business. **Revised by Floyd, 2026-09-22: the
      real case company's name stays out of the page itself** (see the dedicated hard
      requirement below) — this item is satisfied by sector-level specificity (the actual
      chain steps, the trader's size and market), not by naming the company.
- [ ] Follows the chapter template referenced by the brief — **which shape, exactly, is an open
      question**, see `format.md`.
- [ ] Every claim traces to an appraised source, each with a one-line reason to believe it
      (`source_criteria.md`).
- [ ] States explicitly what the platform (AI) drafted and what a human on the team checked —
      the course's own AI-use disclosure line, and rule 10 in `CLAUDE.md`.
- [ ] Ends in something the owner can do (one next step: owner, rough cost, check-in).
- [ ] Carries the handbook disclaimer, verbatim: "This handbook offers inspiration and starting
      points, not commercial advice or guarantees... Decisions about a firm remain the firm's
      own."
- [ ] Is a **new** page — never an edit of week 2's published page (course versioning rule,
      restated in `report-formats`).
- [ ] Published on the shared course site itself by the hand-in deadline — a repo link or a
      Google Doc "cannot be read, and counts as not handed in" (course brief, verbatim).
- [ ] Team's own criterion 1: every recommendation names a step in the lead → quotation →
      contract → payment → export document chain, never a category of tool.
- [ ] Team's own criterion 3: names the duty that applies, its evidence, and any outside
      supplier's hosting location, wherever a duty is invoked.
- [ ] **Strict maximum one A4 page** (Floyd, 2026-09-22) — operationalized as ~500–550 words of
      body text; see "Word budgets" below.
- [ ] **Do not name the real case company (BAS World) in the page text** (Floyd, 2026-09-22) —
      sector-level description ("a Dutch trader in used commercial vehicles and machinery")
      stays; the company name doesn't. Applies to the published page itself, not to internal
      working files (`00_input/`, `Platform/`) which stay traceable to the real research.

## Soft requirements (rubric-scored)

**Note on weighting — see "Assessment rubric" below: this page is not itself assigned numeric
marks.** These are still scored, but on the partner-team's informational gate and, indirectly,
through the portfolio entry ("what did the gates ask, and what did you change"), not as a
percentage of a grade on the page itself.

- [ ] Clarity for a non-technical reader (floor criterion 1).
- [ ] Accuracy against appraised sources — nothing overclaimed beyond what a source actually
      supports (floor criterion 2). Includes getting the *scope* of a legal duty right, not just
      quoting it — e.g. not stating an AI Act duty applies more broadly than its actual
      high-risk-only scope.
- [ ] Responsible-AI coverage across all three of the week's parts, not just the one easiest to
      source (floor criterion 3).
- [ ] Usefulness to an owner — the recommendations are things a 10–50 staff firm with no IT
      function could actually start (floor criterion 4).
- [ ] Team's own criterion 2: keeps time-saving automation apart from customer-touching
      automation, stated per recommendation.
- [ ] Team's own criterion 4: every figure labelled `company-reported`/`independently-
      verifiable` and `case`/`sector`.
- [ ] Team's own criterion 5: every recommendation labelled by complexity, with `in-house build`
      flagged as a warning where used.
- [ ] Team's own criterion 6: the next step names an owner, a rough cost, and a three-month
      check — not left generic.

## Assessment rubric

| Criterion | Weight | What "good" looks like |
|---|---|---|
| Clarity | not numerically weighted — see note below | An owner with no technical background can read it once and understand what to do |
| Accuracy | not numerically weighted | Every claim matches its source; every legal duty stated at its actual, correct scope |
| Responsible-AI coverage | not numerically weighted | All three of the week's required parts are genuinely covered, not just gestured at |
| Usefulness | not numerically weighted | The next step and recommendations are concrete and affordable for this reader |

**Open finding, not a guess filled in as if it were fact:** the course brief does not give this
page a percentage-weighted mark allocation, unlike a typical rubric `rubric-decomposition`
expects to decompose. Per the course's own hand-in section: *"The page and the architecture are
not marked. They are evidence for your final interview... Your portfolio is the part that
carries a mark: 30% of both your marks."* The four criteria above are a qualitative bar checked
by the partner-team gate (informational, non-blocking — see `CLAUDE.md`'s "two kinds of gate"),
not a scored rubric in the usual sense. Word budgets below are therefore proportioned by content
weight (how much each part needs to say), not by mark percentage, since there is no mark
percentage to track.

## Word budgets

**Resolved by Floyd, 2026-09-22: strict maximum one A4 page.** Not a soft target — "strict
maximum" is read as a hard requirement, moved from the soft/rubric list to the hard-requirements
list above. Translating "one A4 page" into a word count is this stage's own operational estimate
(normal margins, ~11–12pt, single spacing, allowing room for the title, headings, the
recommendations list and the disclaimer): **~500–550 words of body text**, not counting the
title line itself. Flagged as an estimate, not a number the course published — if the actual
published page runs long or short of one physical page at stage 7's QA pass, that's the real
test, not this word count.

The existing draft in `Platform/draft.md` (~1,330 words) is roughly **2.5× over budget** and
needs a substantial rewrite at stage 4, not a trim. Budget below is reallocated by content
priority (which of the three required parts and the recommendation needs the fewest words to
still be true and useful), not by carrying forward the existing draft's proportions:

| Section | New budget (words) |
|---|---|
| Intro (1–2 sentences) | 30 |
| Part 1 — what leaves the building / self-hosting | 90 |
| Part 2 — act or only advise | 110 |
| Part 3 — staff using AI without saying so | 60 |
| Recommendations (down from 4 to the strongest 3) | 140 |
| Next step | 30 |
| Disclaimer (verbatim, required) | 25 |
| **Total** | **~485** |

At this length, most individual claim citations from `Platform/claims_en.md` cannot all survive
into the page text — stage 4 selects the strongest one or two per part rather than citing every
appraised claim. The full source set stays valuable as the evidence base even where a specific
citation doesn't make the final cut; nothing forces `Platform/appraised.md` itself to shrink.

**Clarified by Floyd, 2026-09-22: inline citation tags (`[S-0NN, evidence-label]`) do not count
toward the ~485-word body total.** Only the prose does. This gives more room per section than the
figures above imply on a literal word-processor count, but the physical one-A4-page constraint
is still the real, stricter test — citation tags still take visible space on the printed page,
so stage 4 keeps them terse rather than treating this as licence to lengthen the prose to match.

## AI-use and disclosure

The course requires the page to state, explicitly, what the platform (AI) drafted and what a
human on the team checked — "a reader who cannot tell will trust the whole page less" (course
brief, verbatim). This is not satisfied by a vague "AI was used" line. The existing draft's
process note and checking-note line (stating plainly that no second human reader has yet
confirmed any claim) are a start, but stage 6/7 must turn this into the disclosure block the
course expects on the finished, published page — not leave it as an internal process note.
