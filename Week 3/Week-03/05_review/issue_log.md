# issue_log.md — week 3, draft_v1.md

Format per `issue-log-format`. IDs sequential, never reused across passes.

| ID | Pass | Location | Issue | Severity | Status |
|---|---|---|---|---|---|
| I1 | 1 | Whole page | The page never names BAS World or the sector ("Dutch trader in used commercial vehicles") — it reads as generic business advice, not visibly written for the SME the research proposal names, despite using sector-specific chain language ("buyer quotes," the lead→quotation→contract→payment→export document steps). Hard requirement in `checklist.md`: "written for the SME named in the research proposal... not a generic business." | major | fixed |
| I2 | 1 | Disclaimer | Disclaimer is paraphrased ("This page offers..." / "your own") rather than verbatim, though `checklist.md`'s hard requirement says "carries the handbook disclaimer, verbatim." Meaning is unchanged; wording is not the source text. | major | fixed |
| I3 | 1 | Recommendations 1–2, headings | Recommendation headings lead with a tool/action description ("Customer-facing AI", "Translation for buyer quotes") with the chain step in parentheses second — the reverse of team criterion 1's own precedent (week 2: step name first, e.g. "Export document step — screening trading partners..."). The step is present, just not leading. | minor | fixed |
| I4 | 1 | Recommendation 3 | "A one-page AI-use policy (every step)" — "every step" is not one of the five named chain steps criterion 1 asks for. The pre-budget-cut version of this draft (`Platform/draft.md`) explicitly flagged this as a deliberate exception; that acknowledgment did not survive into `draft_v1.md`, leaving an unflagged deviation from a hard requirement. | major | fixed |
| I5 | 1 | Whole page | Word count (494 prose / 515 incl. citation tags) is close to the ~485 target but not physically verified against an actual one-A4-page render — `checklist.md` itself says the word count is an estimate and the real test is a print/export preview, which hasn't happened yet. | major | **open — see re-check below, tooling limitation** |
| I6 | 1 | Recommendations | Each recommendation states customer-touching or not, but none is explicitly labelled "time-saving" — team criterion 2's literal wording asks the draft to keep time-saving automation apart from customer-touching and state which each recommendation is; only one half of that pair is stated per recommendation. | minor | fixed |
| I7 | 2 | "Staff using AI without saying so" section | `[S-028]` is cited as confirming "a pattern" right after the `$670,000`/one-in-five figures from `[S-019]` — read literally, this implies the peer-reviewed source corroborates those specific numbers. It doesn't: `S-028` confirms shadow AI is a recognised risk category in the academic literature, not the dollar figure or the 20% rate. The citation is real and correctly used elsewhere in `Platform/`, but this sentence's phrasing overstates what it supports here. | major | fixed |

**Summary: 7 issues (5 major, 2 minor), 0 critical.** Per `reviewer-factchecker`'s own "done" rule,
this does not clear the gate as-is — 5 open major issues. All 7 are logged with enough detail to
fix directly; none requires new research or a second full iteration on its own. Recommendation:
one targeted revision pass on `draft_v1.md` (a `draft_v2.md`) addressing I1–I4, I6–I7 (all
wording/framing fixes within the existing word budget) and an actual page-fit check for I5, then
a short re-check rather than a full second pass-1/pass-2 cycle — but that's Floyd's call, not
decided here.

## Re-check, 2026-09-22 (Floyd said "revise")

| ID | Status | Note |
|---|---|---|
| I1 | fixed | `draft_v2.md` intro now names BAS World and the sector explicitly |
| I2 | fixed | Disclaimer restored to the handbook template's verbatim text |
| I3 | fixed | Recommendation headings reordered step-first |
| I4 | fixed | Recommendation 3 now flags its own step-naming exception on the page |
| I5 | **not resolved — see note** | Chrome browser tool unavailable this session (extension not connected), so no real rendered page count was obtainable. Fell back to a typographic estimate (Calibri 11pt, 2.5cm margins, 1.15 spacing): `draft_v2.md` is 526 words of prose plus 7 headings and a 3-item list — likely close to or just over one physical page at those settings, not comfortably under it the way `draft_v1.md` (494 words) was. **This is an estimate, not a verified measurement** — recommend Floyd pastes the final text into Word/Google Docs (or however it's actually published) and checks directly before hand-in. |
| I6 | fixed | Recommendation 3 now states "not a saving" alongside "not customer-touching" |
| I7 | fixed | The shadow-AI paragraph now states separately what `S-028` supports (the risk category is recognised) rather than implying it confirms the `$670K`/20% figures |

**6 of 7 fixed. I5 remains genuinely open — a tooling limitation, not a drafting one — flagged to
Floyd rather than guessed at.**
