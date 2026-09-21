# Product Requirements Document

## A research and publishing tool for the BAS World handbook

| **Team**        | Aäron Bos, Floyd Godlieb, Ivan van Vreeswijk, Baran Yapici |
| --------------- | ---------------------------------------------------------- |
| **Build roles** | Product manager, developer, tester, deployer               |
| **Version**     | 2.1                                                        |
| **Status**      | Revised after blueprint v1.0 (17 September) and the week-2 feedback |
| **Date**        | 21 September 2026                                          |

**Version history.** v1.2 — week 1 (before 17 September 2026). v2.1, 17 September 2026 — after blueprint v1.0: interview moved outside the tool (§2); sector scan of 20–30 traders added to step 1 (§2; research proposal v2 §5 strand 2); translation made an explicit step 3 (§2). 21 September 2026, same version — week-2 feedback: six criteria listed again (§3); manual back-up named for Check (§4); open points moved to blueprint §7 (§8).

## 1. What we build and why

**Who uses the tool.** Our team of four from the minor 'Data Driven Decision Making in Business' at HAN University of Applied Sciences.

**Who reads the result.** The owner or commercial manager of a Dutch trader in used commercial vehicles, trailers and machinery, roughly 10–50 staff, no IT function. They read one page to decide on one next step with AI. A second reader is BAS World's sales and operations management, who host the case.

**What we deliver.** One English handbook page per week for six weeks, on how AI can be applied within SMEs in this sector, with BAS World as case.

**The problem.** This work takes too long by hand — our expectation, not yet a measurement; section 8 turns it into a real number in week 2. We use AI to extend our research: it finds and rates sources, translates the Dutch parts and drafts; we judge, correct and approve.

## 2. What the tool does step by step

| **Step** | **What we do** | **What the tool does** | **File it hands on** |
|----------|--------------------|------------------------------|-----------|
| 1. Find sources | We type the research question. | Searches in Dutch and English, including the visible channels of 20–30 smaller traders (research proposal v2 §5, strand 2). Saves each result with web address, date and language. | `source.md` |
| 2. Judge sources | We read the rating and change it when we disagree; the change is recorded with our name and reason. | Rates each source on credibility, relevance and recency and writes down the reason. | `appraised.md` |
| 3. Translate | We verify every number and quoted sentence against the original. | Turns each Dutch sentence we will use into an English claim, keeping the original sentence, the source and the location. | `claims_en.md` |
| 4. Write a draft | We choose the angle and edit the text. | Writes a draft from `claims_en.md` only. Every statement carries a claim-id; a statement without a source and a quoted sentence does not enter the draft. | `draft.md` |
| 5. Check | The second reader answers the points marked 'Reader' in section 3. | Tests the draft on the points marked 'Tool' in section 3 and on traceability, and returns pass/fail per statement. | `check.md` |
| 6. Publish | We approve. | Places the page on the course website with a version and a checking note. | `page.md` |

**The interview is not a tool step.** A person transcribes the BAS World recording, replaces names with job roles, and writes the claims we will use into `claims_en.md` by hand, labelled company-reported and case. The recording and both transcripts stay on one team laptop outside the tool and are deleted after the module.

**What we build first.** Steps 1 to 3: search and the language work. The checklist comes later; we cannot test one before we can produce a page.

## 3. What a good page looks like

Four basic requirements come from the handbook template: clear for a reader without technical knowledge; accurate against appraised sources; covers responsible use of AI; useful to an owner. Blueprint §3 names who checks each.

We add six criteria of our own, as in research proposal v2 §4; the full wording is in `context.md` §3b.

| **#** | **Criterion (short name)** | **Checked by** |
|--|------------------------------------|--------------|
| 1 | Names a step in the sales or documentation chain, not a tool category | Reader |
| 2 | Keeps time-saving automation apart from customer-touching automation | Reader |
| 3 | Names the duty that applies, its evidence and any supplier's hosting location | Tool (presence), Reader (correctness) |
| 4 | Labels every figure and claim: company-reported or independently-verifiable; case or sector | Tool |
| 5 | Labels every recommendation by complexity | Reader |
| 6 | Closes with one next step: owner, rough cost, three-month check | Reader |

**Who checks the points marked 'Reader'.** The tool cannot judge these. A second person from our team reads every page and is never the author; the role rotates weekly. Each reader-checked point gets a pass/fail with one line. A page with a failure is not published; the author repairs it first; the product manager decides when two readers disagree.

## 4. What limits us

- We instruct an AI assistant through the command line in plain language. We write no software: wherever a document says a part could run as "code," read "nothing."
- We use the course website that already exists. We build nothing new.
- Somebody without programming knowledge must be able to run the tool.
- Each automatic step has a manual back-up, a person doing the same by hand. For Check, the tester fills the same `check.md` columns by hand from the saved files (blueprint §1).

## 5. How we build it

| **Phase** | **What we build** | **How we test it** | **Where it runs** |
|-------|------------------|----------------------------|-----------|
| Sources | Storage, search and rating (steps 1–2) | Ten sources we already know must be saved and rated correctly, with a reason each. | Our laptops |
| Language | Translation and number checks (step 3) | Twenty numbers and three quotes from Dutch sources must match the original in `claims_en.md`. Dutch sources are appraised in Dutch first. | Our laptops |
| Page | Draft, checklist and publishing (steps 4–6) | One page goes live. Every statement traces to a claim-id. The checklist finds at least one real mistake. | Course website |

**Who does what.** The developer builds and keeps a log of the problems. The tester writes and runs the tests. The deployer publishes the page. The product manager decides on the scope. Who does what in weeks 2–3: blueprint §1.

## 6. How we know the tool works

The tests in section 5 show the parts work, not whether one week is enough. From week 2 we follow three numbers weekly: hours per page, how many of the six tool steps were done by hand (the interview is never counted — it is manual by design), and the share of statements that trace to a saved source.

Two ways a page can go wrong: a statement with no source behind it, or a statement pointing to a source that does not actually contain it — the harder one to notice, since the third measure above still looks good. Four safeguards: every statement needs a quoted source sentence to enter the draft; every number and date is checked, no sampling; the second reader opens five statements of their choice against the original, and the claim-ids opened are recorded in `check.md`; every rating carries a written reason and can be overridden. Five openings out of roughly forty statements will not catch everything — each page states how much was checked.

## 7. What we do not build

We build no screen or app beyond the command line. We publish nothing without a human check. We publish in English only. We train no AI model on BAS World material.

**The line:** the interview recording, its transcript and the anonymised transcript never reach a model service. They stay outside the tool on one laptop, and only files inside the tool's folder can be sent to a model. A person carries what we use from the interview into `claims_en.md`.

## 8. Open points

| **Our statement** | **What we have now** | **What we still need** |
|-----------------|-----------------|----------------|
| The work does not fit in one week | Week-1 experience; one logged run (17 Sept, 43 min), not yet a baseline | A measured result from week 2 |
| A page cannot be traced back to its sources | Seen in our own week-1 documents: no source named per statement | Nothing further |

We first produce one page by hand. That result shows whether the tool is worth building and becomes the comparison for section 6; a short manual result would lead us to build less.

**What we assume.** An interview with a BAS World professional, ideally someone from export documentation. The AI services we already use are good enough. No extra budget is needed.

**Still open:** tracked in blueprint §7 only, so the two documents don't drift apart.
