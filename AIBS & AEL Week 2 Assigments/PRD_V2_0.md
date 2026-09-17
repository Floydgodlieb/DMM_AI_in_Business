# Product Requirements Document

## A research and publishing tool for the BAS World handbook

| **Team**        | Aäron Bos, Floyd Godlieb, Ivan van Vreeswijk, Baran Yapici |
| --------------- | ---------------------------------------------------------- |
| **Build roles** | Product manager, developer, tester, deployer               |
| **Version**     | 1.2                                                        |
| **Status**      | Revised after week 1 feedback                              |
| **Date**        | 14 September 2026                                          |

## 1\. What we build and why

**Who uses the tool.**

Our team of four people from the minor 'Data Driven Decision Making in Business' at the HAN University of Applied Science.

**Who reads the result.**

The owner or commercial manager of a Dutch trader in this sector, roughly 10 to 50 staff, with no IT function. They read a page to decide on a next step with AI. 

A second type of reader is management at BAS World in sales and operations, who host the case and get the findings back.

**What we deliver.**

The handbook discusses how AI can be applied within SMEs in the Dutch used commercial vehicles and machinery sector, with BAS World as case. One handbook page each week for six weeks. Each page is built from Dutch and/or international sources.

To build the handbook we will also use at least one case company that is interviewed. The handbook will be produced for SME's in the sector Dutch trade in used commercial vehicles and machinery, with BAS World as case.

**The problem.**

This work takes a long time just by hand. We use AI to extend our research. We judge whether a source is reliable, and then we translate the Dutch parts. Then we write the page.

**How certain we are.**

The time problem is our expectation and not a measurement. Section 9 explains how we turn it into a real number in week 2.

## 2\. What the tool does step by step

| **Step**                 | **What we do**                                                           | **What the tool does**                                                                                              |
| ------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| 1\. Find sources         | we type the question you want answered                                   | It searches in Dutch and in English. It saves each result with the web address and the date.                        |
| 2\. Judge sources        | We read the rating. We change it when we disagree                        | It rates each source on reliability, and it writes down the reason.                                                 |
| 3\. Handle the interview | We upload the recording or transcript. We confirm that consent was given | It writes out the text, and it replaces names with job roles                                                        |
| 4\. Write a draft        | We choose the angle and edit the text                                    | It summarizes the material and writes a draft. Every statement gets a source and a quoted sentence from that source |
| 5\. Check                | We answer the questions on the checklist                                 | It tests the draft against the six points in section 3                                                              |
| 6\. Publish              | We approve and finalize the page                                         | It places the page on the course website                                                                            |

**What we build first.**

We start with the search and the language work. The checklist comes later. We cannot test a checklist before we can produce a page.

## 3\. What a good page looks like

Four basic requirements come from the handbook template. A page is clear for a reader without technical knowledge. It is accurate. It covers responsible use of AI. It is useful for a manager.

We add six points of our own.

| **#** | **A good page**                                                                                                       | **Who checks it** |
| ----- | --------------------------------------------------------------------------------------------------------------------- | ----------------- |
| 1     | Points each piece of advice to a named step in the sales or document process. It does not point to a type of software | Reader            |
| 2     | Separates advice that saves time from advice that touches contact with the customer                                   | Reader            |
| 3     | Names the rule that applies to each piece of advice                                                                   | Tool              |
| 4     | Marks each number as company reported or independently confirmed                                                      | Tool              |
| 5     | Explains what a company with 10 to 50 staff need for a smaller version would                                          | Reader            |
| 6     | Ends with one next step. It names an owner and a rough cost                                                           | Reader            |

**Who checks the points marked 'Reader'.**

The tool cannot judge these four points. A second person from our team reads every page. That person is never the author. The role moves to another team member each week. The checklist asks about the four points one at a time. Each answer is a pass or a failure with one line of explanation. A page with failure is not published. The author repairs it first. The product manager decides when the two readers disagree. The six points above match section 4 of our research proposal.

## 4\. What limits us

- We instruct an AI assistant through the command line in plain language. We write no software ourselves.
- We use the course website that already exists. We build nothing new.
- Somebody without programming knowledge must be able to run the tool.
- Each automatic step has a manual back-up: **find sources, rate sources, interview, translation,** **write a draft, publish.**

## 5\. How we build it

| **Phase** | **What we build**                             | **How we test it**                                                                                           | **Where it runs** |
| --------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------- |
| Sources   | Storage, search and rating                    | We use ten sources that we already know. The tool must save them correctly.                                  | Our laptops       |
| Language  | Interview text, translation and number checks | We take twenty numbers and three quotes from Dutch sources. Each one must match the original                 | Our laptops       |
| Page      | Summary, draft, checklist and publishing      | One page goes live. Every statement can be traced to a source. The checklist finds at least one real mistake | Course website    |

**Who does what.** The developer builds and keeps a log of the problems. The tester writes and runs the tests. The deployer publishes the page. The product manager decides on the scope.

## 6\. How we know that the tool works

The tests in section 6 show that the separate parts work. They do not show whether one week is enough time. We follow three numbers each week from week 2.

| **What we measure**                             | **How we measure it**                                | **What we aim for**                                                                |
| ----------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Hours the team spends on one page               | Each person notes the time per step                  | The same as the manual result of week 2 or lower. The number should drop each week |
| Steps done by hand instead of by the tool       | We count them during the review. There are six steps | One or none from week 4                                                            |
| Statements that can be traced to a saved source | We count them during the review                      | All of them                                                                        |

**Where a page can still go wrong.** We watch two cases. In the first case a statement has no source behind it. The tool writes readable text even when the summary does not support the statement. In the second case a statement points to a source that does not contain it. The reference looks correct and our third measure would still show a good result. The second case is harder to notice for that reason. We handle both cases in four ways.

- Every statement carries a quoted sentence from the original source. A statement without such a quote does not enter the draft.
- We check every number and every date. We take no samples here.
- The second reader picks five other statements. That person opens the original source and checks the quote.
- A rating can also be wrong. Each rating has a written reason. The reader can change it.

**What does this not cover.**

Five checks out of roughly forty statements will not find every mistake. We note on each page how much checking was done.

## 7\. What we do not build

We build no screen or app beyond the command line. We publish nothing without a human check. We keep the interview recording inside our own environment. We publish in English only. We train no AI models on BAS World material.

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
