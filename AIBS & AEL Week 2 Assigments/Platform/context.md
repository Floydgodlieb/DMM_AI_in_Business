# context.md — the shared desk

version: 1.0
date: 2026-09-17
owner: product manager
change rule: bump the version and add a line under "Changes" for every edit; every part reads this file before acting; no part holds its own copy.

## 1. Who we write for

Primary reader: the owner or commercial manager of a Dutch trader in used commercial vehicles, trailers and machinery — 10 to 50 staff, no IT function, selling B2B and multilingual into mostly non-EU markets. They read one page to decide on one next step with AI.

Secondary reader: BAS World commercial and operations management, who host the case.

## 2. The case, and what it is not

BAS World (Veghel, BAS Group, 450+ staff, AI Search in production) is a frontier case: it shows what stays hard once budget and IT are no longer the limit. It does not describe the sector on average. Every claim carries a scope label: `case` or `sector`.

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

## Changes

- 1.0 (2026-09-17): first version, from PRD v2.1 and blueprint v1.0.
