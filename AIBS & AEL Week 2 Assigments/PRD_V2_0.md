# Product Requirements Document

## A research and publishing tool for the BAS World handbook

| **Team**        | Aäron Bos, Floyd Godlieb, Ivan van Vreeswijk, Baran Yapici |
| --------------- | ---------------------------------------------------------- |
| **Build roles** | Product manager, developer, tester, deployer               |
| **Version**     | 2.1                                                        |
| **Status**      | Revised after the technical blueprint (v1.0, 17 September) |
| **Date**        | 17 September 2026                                          |

## 1\. What we build and why

**Who uses the tool.**

Our team of four people from the minor 'Data Driven Decision Making in Business' at the HAN University of Applied Science.

**Who reads the result.**

The owner or commercial manager of a Dutch trader in used commercial vehicles, trailers and machinery, roughly 10 to 50 staff, no IT function. They read one page to decide on one next step with AI. A second reader is BAS World's sales and operations management, who host the case and get the findings back.

**What we deliver.**

One English handbook page per week for six weeks, on how AI can be applied within SMEs in this sector, with BAS World as case.

**The problem.**

This work takes too long by hand. We use AI to extend our research: it finds and rates sources, translates the Dutch parts and drafts; we judge, correct and approve.

**How certain we are.**

The time problem is our expectation and not a measurement. Section 8 explains how we turn it into a real number in week 2.

## 2\. What the tool does step by step

| **Step** | **What we do** | **What the tool does** | **File it hands on** |
|----------|----------------|------------------------|----------------------|
| 1. Find sources | We type the research question. | Searches in Dutch and English, including the visible channels of 20–30 smaller traders (proposal §5, strand 2). Saves each result with web address, date and language. | `source.md` |
| 2. Judge sources | We read the rating and change it when we disagree; the change is recorded with our name and reason. | Rates each source on credibility, relevance and recency and writes down the reason. | `appraised.md` |
| 3. Translate | We verify every number and quoted sentence against the original. | Turns each Dutch sentence we will use into an English claim, keeping the original sentence, the source and the location. | `claims_en.md` |
| 4. Write a draft | We choose the angle and edit the text. | Writes a draft from `claims_en.md` only. Every statement carries a claim-id; a statement without a source and a quoted sentence does not enter the draft. | `draft.md` |
| 5. Check | We answer the reader questions on the checklist. | Tests the draft on the tool-checkable points in section 3 and on traceability, and returns pass/fail per statement. | `check.md` |
| 6. Publish | We approve. | Places the page on the course website with a version and a checking note. | `page.md` |

**The interview is not a tool step.** A person transcribes the BAS World recording, replaces names with job roles, and writes the claims we will use into `claims_en.md` by hand, labelled company-reported and case. The recording and both transcripts stay on one team laptop outside the tool and are deleted after the module.

**What we build first.**

Steps 1 to 3: search and the language work. The checklist comes later; we cannot test a checklist before we can produce a page.

## 3\. What a good page looks like

Four basic requirements come from the handbook template: clear for a reader without technical knowledge; accurate against appraised sources; covers responsible use of AI; useful to an owner.

We add six points of our own, identical to research proposal v2 section 4.

| **#** | **A good page** | **Who checks it** |
|-------|-----------------|-------------------|
| 1 | Names a step in the sales or documentation chain, never a category of tool. | Reader |
| 2 | Keeps time-saving automation apart from automation that touches the customer, and says which each recommendation is. | Reader |
| 3 | Names the duty that applies (AI Act, GDPR, sanctions screening), the evidence for it, and any outside supplier's hosting location. | Tool checks that a duty is named; reader checks it is the right one |
| 4 | Labels every figure company-reported or independently verifiable, and case evidence or sector evidence. | Tool |
| 5 | Labels every recommendation by complexity: bought tooling, a named process owner, or an in-house build, flagged as a warning. | Reader |
| 6 | Closes with one next step: an owner, a rough cost, and a three-month check. | Reader |

**Who checks the points marked 'Reader'.**

The tool cannot judge these four points. A second person from our team reads every page. That person is never the author. The role moves to another team member each week. The checklist asks about the four points one at a time. Each answer is a pass or a failure with one line of explanation. A page with failure is not published. The author repairs it first. The product manager decides when the two readers disagree. The six points above match section 4 of our research proposal.

## 4\. What limits us

- We instruct an AI assistant through the command line in plain language. We write no software ourselves.
- We use the course website that already exists. We build nothing new.
- Somebody without programming knowledge must be able to run the tool.
- Each automatic step has a manual back-up: **find sources, rate sources, interview, translation,** **write a draft, publish.**

## 5\. How we build it

| **Phase** | **What we build** | **How we test it** | **Where it runs** |
|-----------|-------------------|--------------------|-------------------|
| Sources | Storage, search and rating (steps 1–2) | Ten sources we already know must be saved and rated correctly, with a reason each. | Our laptops |
| Language | Translation and number checks (step 3) | Twenty numbers and three quotes from Dutch sources must match the original in `claims_en.md`. Dutch sources are appraised in Dutch first. | Our laptops |
| Page | Draft, checklist and publishing (steps 4–6) | One page goes live. Every statement traces to a claim-id. The checklist finds at least one real mistake. | Course website |

**Who does what.** The developer builds and keeps a log of the problems. The tester writes and runs the tests. The deployer publishes the page. The product manager decides on the scope.

## 6\. How we know that the tool works

The tests in section 5 show that the parts work. They do not show whether one week is enough. We follow three numbers each week from week 2.

| **What we measure** | **How** | **Aim** |
|---------------------|---------|---------|
| Hours the team spends on one page | Each person logs time per step, by hand, outside the tool. | Equal to the manual week-2 result or lower, and dropping each week. |
| Of the six tool steps, how many were done by hand | Counted at review from `check.md` and the time log. The interview is never counted: it is by design manual. | One or none from week 4. |
| Statements that trace to a saved source | Counted by the check step. | All of them. |

**Where a page can still go wrong.** Two cases. A statement with no source behind it: readable text the material does not support. A statement pointing to a source that does not contain it: the reference looks right and our third measure still shows a good result, so it is the harder one to notice. We handle both in four ways:

- Every statement carries a quoted sentence from the original source. Without it, it does not enter the draft (step 4).
- Every number and date is checked against the source. No sampling (step 5).
- The second reader opens the original source for five statements of their choice (section 3).
- A rating can be wrong too; each carries a written reason, and the reader can change it (step 2).

**What this does not cover.** Five opened sources out of roughly forty statements will not find every mistake. Each page states how much checking was done.

## 7\. What we do not build

We build no screen or app beyond the command line. We publish nothing without a human check. We publish in English only. We train no AI model on BAS World material.

**The line: the interview recording, its transcript and the anonymised transcript never reach a model service.** They stay outside the tool on one laptop, and only files inside the tool's folder can be sent to a model. A person carries what we use from the interview into `claims_en.md`.

## 8\. Open points

**What supports our problem statement.**

| **Our statement**                           | **What we have now**                                                        | **What we still need**          |
| ------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------- |
| The work does not fit in one week           | Our experience from week 1. We kept no time log                             | A measured result from week 2   |
| A page cannot be traced back to its sources | We saw this in our own week 1 documents. They named no source per statement | Nothing further                 |

**The week 2 measurement.**

We first produce one page by hand. That result shows whether the tool is worth building. It also becomes the comparison for section 7. A short manual result would lead us to build less.

**What do we assume.**

We will have an interview with a professional from BAS World. We hope to speak with somebody about export documentation. The AI services that we already use are good enough. No extra budget is needed.

**What is still open.**

Where may we process the Dutch recording? The answer changes phase 2 and we need it before we build. Will we trust an automatic rating? A full check by hand would remove the benefit of phase 1.

## Sources

- **EU AI Act.** European rules on artificial intelligence. Transparency duty in section 3.
- **GDPR.** European data protection rules. Interview recording in sections 2 and 8.
- **EU sanctions rules on trade with Russia.** Screening duty in section 3.
- **CBS.** The Dutch statistics office. A source type in section 5.
- **KvK.** The Dutch chamber of commerce. A source type in section 5.
- **Chapter template of the handbook.** The four basic requirements in section 3.
- **Research proposal BAS World version 0.3.** The six points in section 3.
