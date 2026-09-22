# context.md — the shared desk

version: 2.0
date: 2026-09-22
owner: product manager
change rule: bump the version and add a line under "Changes" for every edit; every part reads this file before acting; no part holds its own copy.

## 1. Who we write for

Primary reader: the owner or commercial manager of a Dutch trader in used commercial vehicles, trailers and machinery — 10 to 50 staff, no IT function, selling B2B and multilingual into mostly non-EU markets. They read one page to decide on one next step with AI.

Secondary reader: BAS World commercial and operations management, who host the case.

## 2. The case, and what it is not

BAS World (Veghel, BAS Group, 450+ staff, AI Search in production) is a frontier case: it shows what stays hard once budget and IT are no longer the limit. It does not describe the sector on average. Every claim carries a scope label: `case` or `sector`.

**Week 3 addition.** The one BAS World-specific technical claim available (its AI agents' architecture) comes only from its implementation partner's own marketing case study (`S-012`, week 2), which is undated and was already flagged at appraisal as failing gate G2 (no date) and weak on G5 (not the vendor's own filed documentation). Week 3 does not lean on it for new claims: a page about trust should not rest its own case evidence on a source it cannot fully trust either. Where BAS World is mentioned this week, it is as the named case, not as a source of new technical fact.

## 3. Quality criteria (PRD v2.1 §3 — verbatim)

Floor, from the handbook template: clear to a non-technical reader; accurate against appraised sources; covers responsible use of AI; useful to an owner.

1. Names a step in the sales or documentation chain (lead → quotation → contract → payment → export document), never a category of tool. *(checked by: reader)*
2. Keeps time-saving automation apart from automation that touches the customer, and says which each recommendation is. *(reader)*
3. Names the duty that applies (AI Act, GDPR, sanctions screening / Regulation 833/2014), the evidence for it, and any outside supplier's hosting location. *(tool: presence; reader: correctness)*
4. Labels every figure `company-reported` or `independently-verifiable`, and `case` or `sector`. *(tool)*
5. Labels every recommendation by complexity: `bought tooling`, `named process owner`, or `in-house build` (the last flagged as a warning). *(reader)*
6. Closes with one next step: an owner, a rough cost, and a three-month check. *(reader)*

## 4. Out of scope

- No screen or app beyond the command line.
- Nothing is published without a human check.
- English only.
- No AI model is trained on BAS World material.
- Interview material never reaches a model service (blueprint §6, the line).
- No claim enters a draft without a source and a quoted sentence.

## 5. House style

- Plain English, short sentences, no jargon an owner would have to look up.
- Every statement carries a `[claim-id]` that exists in `claims_en.md`.
- Every number: `company-reported` or `independently-verifiable`; every claim: `case` or `sector`.
- Recommendations name a step and a complexity label, never "use an AI tool".
- Each page states how much checking was done.
- Each page ends with one next step: owner, rough cost, three-month check.
- The disclaimer of the handbook template appears on every page: educational, not consultancy.

## 6. Week 3 theme (new)

**Theme: trust and AI safety.** Week 3's page answers the course's own framing question — *"can I trust this — with my data, with its answers, and with my people?"* — in the three parts the course brief names:

1. What leaves the building when the firm uses AI, and could it run the model itself?
2. When may an AI tool act on the firm's behalf, and when may it only advise?
3. What happens when staff use AI and do not say so?

**Question-diversity rule (new this week, PM decision, 2026-09-22).** After week 2's feedback questioned how reliable some of that week's sources were, this week's stopping rule adds one more check: for each of the three parts above, run at least one neutral search and one differently-angled rephrasing of the same question before appraising anything, and log both in `searchlog.md` even when one line finds nothing new — a source list built from only the first, most obvious phrasing of a question is exactly the failure mode assignment 1 already taught this team to distrust. See `searchlog.md` §"Rephrasing test" for what this surfaced.

**Source-reliability rule (new this week, PM decision, 2026-09-22).** Week 2's feedback is read as: too many `use` decisions rested on undated marketing pages held up only by a human override (S-012, S-014, S-017). This week raises the bar in practice, not just on paper: marketing-only sources are used, if at all, only to illustrate a vendor claim explicitly labelled as such, never as the sole support for a duty or a figure a reader would act on. Prefer official/regulatory text, independent research-institute output corroborated by a second source, or a named primary legal record over vendor copy.

## Changes

- 1.0 (2026-09-17): first version, from PRD v2.1 and blueprint v1.0.
- 2.0 (2026-09-22): week 3 theme added (§6); BAS World case-evidence caveat added (§2); question-diversity and source-reliability rules added in response to week-2 feedback.
