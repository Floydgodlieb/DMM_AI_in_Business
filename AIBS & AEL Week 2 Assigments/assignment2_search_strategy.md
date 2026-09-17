# Assignment 2 — Search strategies and quality criteria

Aäron Bos · AIBS/AEL minor, "AI in Business" · 17 September 2026

Question: what are good-quality reports on the geopolitics of the AI race — the United States, China, Europe — and how do you find them.

## 1. Quality criteria (written before searching)

Assignment 1 showed the failure mode: three confident, well-written, contradictory answers to "who leads," none of which stated its own scope. These criteria are built to rule that failure mode out. A source passes only if it meets all seven.

| # | Criterion | Why it matters |
|---|---|---|
| 1 | Names a measurable dimension of "leadership" (compute, investment, chip supply, model benchmark, regulation, adoption) instead of an undefined global ranking | This is exactly where all three AI-generated articles failed — each silently picked a different scoreboard |
| 2 | States its methodology and the exact date/scope of the underlying data — what is counted, what is excluded, as of when | A number with no "as of" and no "counting what" cannot be checked or compared |
| 3 | Traceable to a named author or institution, not an unsigned aggregator page | Accountability: someone stands behind the claim and can be checked against their other work |
| 4 | Discloses (or makes obvious) whose interest sits behind the claim — government body, vendor, VC-backed lab, law firm, think tank funding | A vendor blog and a parliamentary briefing can cite the same fact and deserve different weight |
| 5 | Corroborated by at least one independently produced source measuring something similar | One source is a claim; two independent sources agreeing is a fact worth using |
| 6 | Recent and dated explicitly — within roughly 12 months, given how fast chip export rules, funding rounds and the AI Act's phase-in move | AI geopolitics in 2026 is not a stable topic; an undated or 2023 figure is close to worthless here |
| 7 | Relevant to the reader's actual decision, not just to "who is winning" — for the handbook page, that means: which vendor, hosted where, under whose law | The geopolitics question only matters to the SME owner once it turns into a vendor and a duty |

## 2. Search strategy (written before judging results)

**The one rule the strategy exists to enforce: never search "who leads the AI race."** That query rewards exactly the confident, single-scoreboard writing assignment 1 produced. Instead, the race was split into the dimensions criterion 1 asks for, and each was searched separately, in English (the handbook is English-only per house style; the Dutch-language angle belongs to the sector-scan strand of the team's own methodology, not this desk-research question).

Search sequence actually run:

1. **Compute and private investment** — `Stanford HAI AI Index Report 2025/2026`, `Epoch AI compute trends`. Stanford's and Epoch's own landing pages turned out to be navigation shells with no figures in the crawlable text; a secondary summary was used instead but traced back to the primary report it cited (see appraisal, source S1) rather than trusted on its own word.
2. **Chips and export controls** — `China AI compute chip export controls Nvidia DeepSeek`. Deliberately searched for a claim and its rebuttal in the same pass, because a policy this contested needs two institutions reading the same facts, not one.
3. **Europe's adoption and regulation** — `Draghi report AI adoption gap Europe`, then the European Commission's own "one year after" page, to get both an independent read and the institution's self-report of its own progress side by side.
4. **Vendor and cloud dependency** — `EU cloud sovereignty dependency Microsoft Azure Amazon Google market share`, aimed at parliamentary/policy-department output rather than opinion pieces, because this is the figure the handbook page actually needs.
5. **A live counter-example** — `Mistral AI European sovereign AI funding 2025 2026`, then checked that the headline figure (€3bn, Samsung-led, €21bn valuation) appeared consistently across three independently reported outlets before treating it as safe to use.
6. **The legal duties named in the team's own context.md** — `EU AI Act deployer obligations SME 2026`, `EU Regulation 833/2014 sanctions due diligence`, aimed at the regulation text itself and an EU Commission FAQ first, commercial commentary second.

Two generic queries (`OECD.AI investment by country`, `Epoch AI compute trends US China`) returned only Wikipedia links and a content-free dashboard page — evidence, in itself, that the easy query returns weak sources and the criteria-driven one is doing real work.

## 3. AI-assisted analysis of what was found

The assistant was given the strategy above as an explicit instruction — search dimension by dimension, require a named author/institution and a dated methodology, disclose the interest behind each source, and corroborate before using a number — rather than being asked to just "find sources on AI geopolitics." Its first-pass appraisal of what came back:

| ID | Source | Author / institution, date | Credibility (1–3) | Relevance (1–3) | Recency (1–3) | One line on why to believe them |
|---|---|---|---|---|---|---|
| S1 | ScienceBlog, "US-China AI investment / Arena gap" | "The Long View," ed. L. Brown, 30 Aug 2026 | 2 | 3 | 3 | Secondary aggregator, but discloses its counting rules in full and names its primary source (Stanford AI Index 2026) — use for the figure, cite the primary report, not this page, as the authority |
| S2 | CSIS, "DeepSeek, Huawei, Export Controls…" | Gregory C. Allen, 7 Mar 2025 | 3 | 3 | 2 | Named security-policy analyst at a major DC think tank; gives GPU-hour and dollar figures with sourcing, not just a conclusion |
| S3 | Brookings, "Ball game's over…" | Mark MacCarthy, 17 Jun 2026 | 3 | 3 | 3 | Same institutional tier as S2, reaches a different interpretation of the same export-control facts — used as the deliberate second read, not a duplicate |
| S4 | HCSS, "The Draghi Report Revisited: AI" | S. Romansky & J. Kommandeur, 10 Oct 2025 | 3 | 3 | 2 | Named authors at a European strategic-studies institute independent of the EU institutions it is assessing |
| S5 | European Commission, "One year after" the Draghi report | European Commission, 16 Sept 2025 | 2 | 2 | 3 | Primary and official, but self-reporting its own progress — read as company/institution-reported, not independently verified |
| S6 | European Parliament (ITRE Committee) briefing | Gineikyte-Kanclere, Eggert, Skiotyte, Dec 2025 | 3 | 3 | 2 | Parliamentary policy department, not the Commission being assessed — independent of the institution whose plan it evaluates; carries the cloud-market figures the handbook page actually needs |
| S7 | TechCrunch, Mistral funding | Anna Heim, 8 Sept 2026 | 2 | 3 | 3 | Single named journalist at a trade outlet, but the core figures (€3bn, Samsung-led, €21bn valuation) were cross-checked against two other independently reported outlets before use |
| S8 | artificialintelligenceact.eu, Article 50 | Reference compilation of the AI Act text | 2 | 3 | 3 | Not the Official Journal itself, but a widely used, accurately quoted legal-reference mirror; used for wording, not as the sole authority |
| S9 | Goodwin Procter LLP, transparency-obligations alert | Goodwin Procter, 3 Aug 2026 | 2 | 3 | 3 | Credible for the compliance reading, but a law firm's client alert has a commercial interest in flagging new obligations — corroborated against S8 rather than used alone |
| S10 | European Commission, consolidated sanctions FAQ | European Commission (DG FISMA), n.d., current as of 2026 | 3 | 3 | 2 | Primary, official interpretation of Regulation 833/2014 — the highest-authority source in this set for the legal duty itself |
| S11 | Sayari blog, Article 12gb due diligence | Ben Power, 1 Apr 2026 | 1 | 2 | 3 | Vendor content from a company that sells sanctions-screening software — used only for how it structures the due-diligence categories, flagged as commercially interested, never as the sole support for a claim |

**What this first pass already shows, before a second reader touches it:** the number that best answers "who leads" (S1's $286bn vs $12.4bn) and the number that best answers what a Dutch SME owner should actually worry about (S6's 70% non-EU cloud market share) are not the same number, and neither the US-investment story nor the China-efficiency story from assignment 1 mentions vendor dependency at all. That gap — between "who's spending the most" and "who do I actually depend on" — is what the handbook page is built to close, and it is only visible because the search was split by criterion 1 and 7 instead of asked as one question.

**What this analysis does not settle.** This is a first pass by one person with AI assistance, not the team's appraisal step: S1 was read only through a secondary summary (the Stanford AI Index 2026 report itself should be opened directly before any of its figures enter a `claims_en.md`-equivalent record), and S5, S9 and S11 all carry a disclosed interest that a second reader should weigh independently rather than take on this appraisal's word.

**The bar this meets.** Another team could take section 2's six searches, in the order given, and land on the same eleven sources — because the strategy names the exact query, the reason for it, and what was rejected, not just what was kept.
