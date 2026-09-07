# Product Requirements Document — [platform name]

**Team:** [names] · **Roles:** PM / dev / tester / deployer
**Version:** 0.1 (first draft) · **Date:** [date]
**Status:** first draft — will be revised as we build

> Target length: 1–3 pages. Keep every section to what week 1 asks for. No solutions to problems we have not met yet.

---

## 1. Problem and users

*What is this platform for, and who uses it?*

- **Primary users:** our own four-person research team.
- **Downstream reader:** the SME owner who reads the handbook page.
- **The problem it solves:** [in 2–3 sentences — what is slow, error-prone or unverifiable if we do this by hand]

## 2. What it must let a user do

*The path from raw source material to a published handbook page.*

| # | Step | What the user does | What the platform does |
|---|------|--------------------|------------------------|
| 1 | Gather sources | | |
| 2 | Appraise sources (credibility, relevance, recency) | | |
| 3 | Process interview / field material | | |
| 4 | Draft the page | | |
| 5 | Check against quality criteria | | |
| 6 | Publish | | |

## 3. Output qualities

*What a good handbook page produced by this platform looks like.*

Floor criteria from the chapter template: clarity for a non-technical reader · accuracy against appraised sources · responsible-AI coverage · usefulness to an owner.

Our additions: [ ... ]

> **Cross-check:** this section must say the same thing as point 4 (quality criteria) of the research proposal. If they disagree, fix one now.

## 4. Known constraints

- We direct an agentic CLI; we do not hand-write code.
- We reuse the existing wiki and site; we do not build new infrastructure.
- A non-coder must be able to run it.
- Every automated step keeps a manual fallback: [name the fallback per step]
- [any constraint specific to our team]

## 5. Handling Dutch source material

*Regional SME sources — CBS, KvK, sector organisations, regional press, and probably our own interview recording — are in Dutch. The handbook is in English.*

- **Retrieval:** [how Dutch sources are found and pulled in]
- **Translation:** [where in the pipeline, with what]
- **Appraisal:** [how a source is judged in its original language, not after a lossy translation]
- **Why in the tool:** so language does not decide who on the team can do research.

## 6. Architectural blueprint

*The components and how they connect. A diagram plus a short paragraph is enough.*

- **Components:** [e.g. source store · retrieval/translation step · drafting step · evaluation step · publishing step]
- **Data flow:** [input → what moves between components → output]
- **What runs where:** [local CLI, repo, published site]
- **Key decision(s) already made, and why:** [ ... ]

## 7. Build plan

| Phase | Subtasks | Test — how we know it works | Deployment |
|-------|----------|-----------------------------|------------|
| Phase 1 — [name] | | | |
| Phase 2 — [name] | | | |
| Phase 3 — [name] | | | |

- **Owner per phase:** [role]
- **Failure log:** kept by the developer — what was tried, what broke, what changed.

## 8. Out of scope, for now

- [things we are deliberately not building yet, and why]

## 9. Open questions and assumptions

**Assumptions we are working on:**
- [ ... ]

**Open questions:**
- [ ... ]

---

**The bar:** a reader can tell what we are building, for whom, and how we will know it works.
