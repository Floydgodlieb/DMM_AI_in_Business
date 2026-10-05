# DIAIA Redesign + Technical Sister Module — Three Paired Sketches

> Written when the modules were still called DIAIA and AEAIS. They are now AIBS (AI in Business & Society) and AEL (Agent Engineering Lab) — see ADR-0008 in `work/decisions/`. The names below are left as they were.

*A design document for the Minor Data Driven Decision Making (HAN University of Applied Sciences). Three alternative ways to split the current DIAIA module into a refocused business/economic/societal module plus a new, more technical sister module. Grounded in the AI Wiki — browse it at [businessdatasolutions.github.io/ai-wiki](https://businessdatasolutions.github.io/ai-wiki). Every "Wiki grounding" below links to its source page; a full index sits at the end.*

---

## 1. Why this redesign, and the shared design logic

### The problem

The current module **DATDRD05-T05 – Decision Intelligence and AI Agents (DIAIA)** tries to do two jobs in seven weeks. It teaches the **business, strategic and ethical framing** of AI-supported decision-making, *and* it pushes students toward **building** a working agent prototype. The prototype is currently optional — it is only rewarded at grades 7–10, where the rubric asks for a working, and then an advanced, agent. Yet the module is explicitly aimed at business students — *"not on building pipelines for programmers or AI Engineers"*. The build ambition therefore sits awkwardly against the audience: the students best placed to score top marks are the ones who can already code, which is not who the module is for.

### The fix

Add a **more technical sister module** and let DIAIA refocus cleanly on what it does best: the **business, economic and societal** aspects of AI. The build work moves next door, where it can be taught properly and at an appropriate technical level.

### The seam we cut along

The AI Wiki splits naturally into three teaching domains:

| Wiki domain | Goes to |
| --- | --- |
| **Strategic / Organisational** (strategy, adoption, maturity, foresight, firm boundaries) | **DIAIA** |
| **Economic / Labour** (employment effects, deskilling, durable skills, productivity) | **DIAIA** |
| **Engineering / Practitioner** (agents, harnesses, RAG, evals, the build lifecycle) | **Sister module** |

This is exactly the seam the redesign needs. DIAIA keeps the first two domains; the sister module takes the third.

### What DIAIA keeps and what it sheds

- **Keeps:** the **CRISP-DM** spine and the **"intern analogy"** — the AI agent as a smart, autonomous intern that works through an agentic workflow while humans retain accountability (overview line 7). These are pedagogically strong and audience-appropriate; they stay.
- **Sheds:** the *build-the-prototype* track (it moves to the sister module) and the *BI-tool mechanics* — the Tableau and Power BI tutorials in weeks 5–7 (overview lines 72, 74–78). The strategic *interpretation* of BI/dashboards can remain as a discussion topic, but the click-through tooling does not belong in a strategy/society module.

### Continuity to exploit

DIAIA's current **Week 3** already features Microsoft 365 Copilot agents (Lisa Crosbie) and practitioner guest speakers who built agentic solutions for real companies (overview lines 65–66). That is a natural seed for the **low-code sister module** in Sketch 1, and the guest speakers transplant cleanly into whichever module fits their story.

### The pairing logic

The three sketches climb a **technical-ambition ladder**: no-code → light-Python → full agentic engineering. There is a deliberate coupling: **the more the sister module builds, the more decisively DIAIA can become a pure strategy/economics/society course.** So DIAIA's own redesign shifts across the three sketches — most "build-aware" in Sketch 1, purely conceptual in Sketch 3.

> **Reading the two tracks separately.** Section 5 decouples the pairings: §5.2 compares the **three DIAIA designs** week-by-week, and §5.3 compares the **three sister modules** week-by-week — so each track can be evaluated on its own.

---

## 2. Sketch 1 — "Accessible Builder"

> **Philosophy.** Every business student can ship a *working* AI agent without writing a line of code. The sister module uses no-code / low-code platforms; DIAIA stays close enough to the build that students can connect strategy to a thing they actually made.

### 2a. Sister module — *"AI Agents in Practice"* (no-code / low-code)

**Platforms:** Microsoft Copilot Studio, n8n, Flowise, custom GPTs. (Copilot Studio gives strong continuity with DIAIA's existing Week 3 material.)

**Learning outcomes.** After this module, students can: 1. Configure a working AI agent on a no-code platform and explain the **agent loop** — an LLM using tools in a loop toward a goal *(wiki: [`ai-agents`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-agents))*. 2. Connect an agent to tools and knowledge sources (file upload, web search, connectors). 3. Apply **prompt and instruction design** to shape agent behaviour reliably. 4. Test an agent with simple pass/fail checks and add **human-in-the-loop** guardrails. 5. Deploy an agent to a real surface (Teams, web) and demonstrate it. 6. Document an agent's **limitations, failure modes and guardrails** honestly.

**Weekly programme (7 weeks):**

| Week | Topic | Wiki grounding |
| --- | --- | --- |
| 1 | Platform landscape; what an agent *is* — LLM + tools + loop; chatbot → agent → multi-agent | [`ai-agents`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-agents), [`foundation-models`](https://businessdatasolutions.github.io/ai-wiki/concepts/foundation-models) |
| 2 | Prompt & instruction design; giving the agent a role (the "intern" briefing) | [`ai-agents`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-agents) |
| 3 | Connecting tools & knowledge — no-code RAG, file upload, connectors | [`is-rag-dead`](https://businessdatasolutions.github.io/ai-wiki/syntheses/is-rag-dead), [`knowledge-architectures-for-llm-agents`](https://businessdatasolutions.github.io/ai-wiki/syntheses/knowledge-architectures-for-llm-agents) |
| 4 | Multi-step flows & triggers; keeping it simple; when *not* to automate | [`agent-harness`](https://businessdatasolutions.github.io/ai-wiki/concepts/agent-harness) (constraints, simplified) |
| 5 | Testing & guardrails — destructive-action checks, human-in-the-loop, intent validation | [`responsible-ai`](https://businessdatasolutions.github.io/ai-wiki/concepts/responsible-ai) (constraints layer) |
| 6 | Deploy & integrate (Teams / web); monitoring what the agent does | [`agent-development-lifecycle`](https://businessdatasolutions.github.io/ai-wiki/concepts/agent-development-lifecycle) (deploy/monitor) |
| 7 | Demo day + reflection on limitations and responsible use | — |

**Assessment.** A working no-code agent + a short "build log" documenting role definition, tools connected, tests run, and guardrails. Demo + Q&A. Mirrors DIAIA's criterion-based interview style so the two modules feel coherent.

### 2b. DIAIA redesign — business-aware, build still nearby

**Learning outcomes.** After DIAIA, students can: 1. Frame a decision problem and build a convincing **business case** for AI support. 2. Apply an AI **strategy framework** to position an initiative. 3. Assess an organisation's **AI adoption maturity**. 4. Analyse the **labour and economic impact** of an AI deployment. 5. Evaluate **responsible-AI risks** and propose mitigations. 6. Recommend a **build / buy boundary** for an AI capability.

**Weekly programme (7 weeks):**

| Week | Topic | Wiki grounding |
| --- | --- | --- |
| 1 | Decision framing & the intern analogy; what an AI decision agent is and is *not* | overview spine |
| 2 | Strategy & value | [`strategy`](https://businessdatasolutions.github.io/ai-wiki/concepts/strategy) — Theory of Winning (Martin); Value Stick (Oberholzer-Gee) |
| 3 | Adoption & maturity | [`enterprise-ai-adoption`](https://businessdatasolutions.github.io/ai-wiki/concepts/enterprise-ai-adoption) — MIT CISR 4 stages; Cisco 5 foundations; Augmented Learners (Ransbotham) |
| 4 | The micro-productivity trap & reinvention | [`micro-productivity-trap`](https://businessdatasolutions.github.io/ai-wiki/concepts/micro-productivity-trap) — Bain/OpenAI 4-step; offering/process lock-in |
| 5 | AI & work — the economics | [`automation-vs-augmentation`](https://businessdatasolutions.github.io/ai-wiki/concepts/automation-vs-augmentation), [`durable-skills`](https://businessdatasolutions.github.io/ai-wiki/concepts/durable-skills) — Brynjolfsson "Canaries" |
| 6 | Responsible AI & governance | [`responsible-ai`](https://businessdatasolutions.github.io/ai-wiki/concepts/responsible-ai), [`jagged-frontier`](https://businessdatasolutions.github.io/ai-wiki/concepts/jagged-frontier) (Dell'Acqua); incident data |
| 7 | Build / Compose / Collaborate / Buy + presentations | [`enterprise-ai-adoption`](https://businessdatasolutions.github.io/ai-wiki/concepts/enterprise-ai-adoption) — Nishar & Nohria firm-boundary model |

**Assessment.** CRISP-DM-structured report on a decision-agent business case (no build required) + criterion-based interview. Students may reference the agent they built next door in *"AI Agents in Practice"* as their worked example, creating a satisfying link between the two modules.

**Best fit.** Maximum inclusivity — no prerequisites, every student ships something. **Risk.** Platform lock-in; the transferable technical skill is thinner, and students do not see "under the hood".

---

## 3. Sketch 2 — "Light-Code Practitioner"

> **Philosophy.** Students write *scaffolded* Python against LLM APIs — real engineering on a gentle ramp. The sister module teaches enough code to build and evaluate a small LLM application; DIAIA becomes the partner that reads the technical signal and turns it into a decision.

### 3a. Sister module — *"Building LLM Applications"* (light Python)

**Setup:** Jupyter/Colab notebooks, an LLM API (e.g. Anthropic / OpenAI), a hosted vector store. Heavily scaffolded — students fill in blanks, they do not start from a blank file.

**Learning outcomes.** After this module, students can: 1. Call an LLM API from Python and design prompts **in code** with structured output *(wiki: [`software-3.0`](https://businessdatasolutions.github.io/ai-wiki/concepts/software-3.0))*. 2. Implement **tool-calling / function use** so the model can act. 3. Build a simple **RAG pipeline** — chunk, embed, retrieve *(wiki: [`is-rag-dead`](https://businessdatasolutions.github.io/ai-wiki/syntheses/is-rag-dead))*. 4. Write **basic evaluations** — LLM-as-judge with binary pass/fail rubrics, reading TPR/TNR. 5. Reason about **cost, latency and failure handling** in an LLM app. 6. Package and demo a small working application.

**Weekly programme (7 weeks):**

| Week | Topic | Wiki grounding |
| --- | --- | --- |
| 1 | LLM APIs & the agent loop in Python; Software 3.0 — the context window *is* the program | [`software-3.0`](https://businessdatasolutions.github.io/ai-wiki/concepts/software-3.0), [`ai-agents`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-agents) |
| 2 | Prompting in code; structured / JSON output; system vs user roles | [`ai-agents`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-agents) |
| 3 | Tool-calling & function use; introducing contracts (what counts as success) | [`agent-harness`](https://businessdatasolutions.github.io/ai-wiki/concepts/agent-harness) (contracts intro) |
| 4 | RAG fundamentals — chunking, embeddings, vector search; "RAG is dead" debate | [`is-rag-dead`](https://businessdatasolutions.github.io/ai-wiki/syntheses/is-rag-dead), [`knowledge-architectures-for-llm-agents`](https://businessdatasolutions.github.io/ai-wiki/syntheses/knowledge-architectures-for-llm-agents) |
| 5 | Evaluation — LLM-as-judge, binary pass/fail beats 1–5 scales, TPR/TNR | [`ai-benchmarks`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-benchmarks); Husain |
| 6 | Guardrails, cost & observability; basic tracing | [`agent-development-lifecycle`](https://businessdatasolutions.github.io/ai-wiki/concepts/agent-development-lifecycle) (monitor/govern) |
| 7 | Mini-project demo + write-up | — |

**Assessment.** A small working LLM app (notebook or simple script) + an **eval report** showing the rubrics used and pass/fail results + a short reflection on cost and limitations.

### 3b. DIAIA redesign — bridges to the code next door

Same strategic/economic/societal backbone as Sketch 1, with **one deliberate twist**: DIAIA explicitly teaches students to **read technical artifacts** (a RAG design, an eval report) and turn them into business judgements.

**Learning outcomes.** As Sketch 1's six outcomes, **plus**: 7. Interpret a technical artifact (RAG design, eval report) and judge **feasibility and risk** for a business decision.

**Weekly programme.** Identical to Sketch 1 except **Week 4 is reframed** as *"Reading the technical signal"*: instead of (or alongside) the micro-productivity trap, students use the sister module's RAG/eval concepts to judge whether an AI initiative is feasible, and apply the **Anand–Wu 2×2** (cost-of-errors × type of knowledge) to decide *where* AI should be deployed.

| Week | Topic | Wiki grounding |
| --- | --- | --- |
| 1 | Decision framing & the intern analogy | overview spine |
| 2 | Strategy & value | [`strategy`](https://businessdatasolutions.github.io/ai-wiki/concepts/strategy) — Martin; Oberholzer-Gee |
| 3 | Adoption & maturity | [`enterprise-ai-adoption`](https://businessdatasolutions.github.io/ai-wiki/concepts/enterprise-ai-adoption) — CISR; Cisco; Ransbotham |
| 4 | **Reading the technical signal** — feasibility from RAG/eval reports; where to deploy | [`jagged-frontier`](https://businessdatasolutions.github.io/ai-wiki/concepts/jagged-frontier), [`micro-productivity-trap`](https://businessdatasolutions.github.io/ai-wiki/concepts/micro-productivity-trap) — Anand–Wu 2×2 |
| 5 | AI & work — the economics | [`automation-vs-augmentation`](https://businessdatasolutions.github.io/ai-wiki/concepts/automation-vs-augmentation), [`durable-skills`](https://businessdatasolutions.github.io/ai-wiki/concepts/durable-skills) — Brynjolfsson |
| 6 | Responsible AI & governance | [`responsible-ai`](https://businessdatasolutions.github.io/ai-wiki/concepts/responsible-ai), [`jagged-frontier`](https://businessdatasolutions.github.io/ai-wiki/concepts/jagged-frontier) — Dell'Acqua |
| 7 | Build / Compose / Collaborate / Buy + presentations | [`enterprise-ai-adoption`](https://businessdatasolutions.github.io/ai-wiki/concepts/enterprise-ai-adoption) — Nishar & Nohria |

**Assessment.** CRISP-DM report where the **Modelling** and **Evaluation** sections are evidenced by the artifact the student built in *"Building LLM Applications"* — the two modules share one running project.

**Best fit.** Students willing to code a little; **strongest business↔engineering bridge** of the three. **Risk.** The coding ramp may exclude the least technical students; needs lab/TA support.

---

## 4. Sketch 3 — "Agentic Engineer"

> **Philosophy.** A genuine technical track. The sister module teaches harness design, knowledge architectures, evaluation pipelines and the full agent development lifecycle — the closest of the three to the wiki's actual depth. Freed entirely from the build, DIAIA becomes a sharp strategy / economics / society course.

### 4a. Sister module — *"Agentic Engineering & AI Systems"* (full)

**Setup:** Python, an agent framework/SDK (e.g. LangGraph or the Claude Agent SDK), a vector store and/or graph DB, an eval platform (e.g. Braintrust / LangSmith). Assumes coding confidence.

**Learning outcomes.** After this module, students can: 1. Design an **agent harness** across its four layers — Context, Constraints, Contracts, Compounding *(wiki: [`agent-harness`](https://businessdatasolutions.github.io/ai-wiki/concepts/agent-harness))*. 2. Choose and implement a **knowledge architecture** — RAG vs LLM-Wiki vs Fat-Skills — and justify the choice *(wiki: [`knowledge-architectures-for-llm-agents`](https://businessdatasolutions.github.io/ai-wiki/syntheses/knowledge-architectures-for-llm-agents))*. 3. Build an **evaluation pipeline** with rubrics, LLM-as-judge and benchmark awareness *(wiki: [`ai-benchmarks`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-benchmarks))*. 4. Instrument **deployment and monitoring** across the agent development lifecycle (Chase/LangChain). 5. Apply **agentic-engineering discipline** — spec-first, the ratchet principle, owning the harness while renting the model *(wiki: [`agentic-engineering`](https://businessdatasolutions.github.io/ai-wiki/concepts/agentic-engineering), [`vibe-coding`](https://businessdatasolutions.github.io/ai-wiki/concepts/vibe-coding))*.

**Weekly programme (7 weeks):**

| Week | Topic | Wiki grounding |
| --- | --- | --- |
| 1 | Software 3.0 & agent fundamentals; brain / hands / session decomposition | [`software-3.0`](https://businessdatasolutions.github.io/ai-wiki/concepts/software-3.0), [`ai-agents`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-agents) (Karpathy) |
| 2 | The harness — Context & Constraints layers; pre/post-tool hooks | [`agent-harness`](https://businessdatasolutions.github.io/ai-wiki/concepts/agent-harness) |
| 3 | Knowledge architectures — RAG / LLM-Wiki / Fat-Skills decision framework; GraphRAG, hybrid search, chunking | [`knowledge-architectures-for-llm-agents`](https://businessdatasolutions.github.io/ai-wiki/syntheses/knowledge-architectures-for-llm-agents), [`knowledge-graphs`](https://businessdatasolutions.github.io/ai-wiki/concepts/knowledge-graphs) |
| 4 | Contracts & evaluation — rubrics, LLM-as-judge, binary scoring, benchmarks | [`ai-benchmarks`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-benchmarks); eval synthesis |
| 5 | The agent development lifecycle — build / test / deploy / monitor / iterate / govern | [`agent-development-lifecycle`](https://businessdatasolutions.github.io/ai-wiki/concepts/agent-development-lifecycle) (Chase) |
| 6 | Agentic engineering vs vibe coding; production discipline; the ratchet | [`agentic-engineering`](https://businessdatasolutions.github.io/ai-wiki/concepts/agentic-engineering), [`vibe-coding`](https://businessdatasolutions.github.io/ai-wiki/concepts/vibe-coding) |
| 7 | Capstone agent demo + ratchet retrospective (trace failures back to constraints) | — |

**Assessment.** A capstone agent built to the agentic-engineering discipline: spec → harness → knowledge architecture → eval pipeline → deploy/monitor, presented with a **ratchet retrospective** tracing each guardrail back to a specific failure it prevents.

### 4b. DIAIA redesign — pure strategy / economics / society

With the sister module owning all building, DIAIA drops every build reference and deepens into seminar/case work.

**Learning outcomes.** After DIAIA, students can: 1. Frame a decision problem and articulate a **theory of winning** for an AI initiative. 2. Apply **dynamic-capabilities** and **strategic-foresight** thinking to AI strategy. 3. Diagnose **adoption maturity** and the **micro-productivity trap**. 4. Analyse the **economic and labour-market** effects of AI. 5. Critically evaluate **responsible-AI and societal** risks. 6. Recommend **firm-boundary** decisions for AI capabilities.

**Weekly programme (7 weeks):**

| Week | Topic | Wiki grounding |
| --- | --- | --- |
| 1 | Decision framing & the intern analogy | overview spine |
| 2 | Strategy & the infinite game | [`strategy`](https://businessdatasolutions.github.io/ai-wiki/concepts/strategy), [`infinite-game`](https://businessdatasolutions.github.io/ai-wiki/concepts/infinite-game) — Martin; Sinek |
| 3 | Dynamic capabilities & foresight | [`dynamic-capabilities`](https://businessdatasolutions.github.io/ai-wiki/concepts/dynamic-capabilities), [`warner-wager-process-model`](https://businessdatasolutions.github.io/ai-wiki/concepts/warner-wager-process-model), [`strategic-foresight`](https://businessdatasolutions.github.io/ai-wiki/concepts/strategic-foresight) — Teece; Webb; MGI arenas |
| 4 | Adoption, maturity & the productivity trap | [`enterprise-ai-adoption`](https://businessdatasolutions.github.io/ai-wiki/concepts/enterprise-ai-adoption), [`micro-productivity-trap`](https://businessdatasolutions.github.io/ai-wiki/concepts/micro-productivity-trap) — CISR; Ransbotham; Bain/OpenAI; Kiron–Schrage |
| 5 | Economics & labour | [`ai-employment-effects`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-employment-effects), [`ai-deskilling`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-deskilling), [`durable-skills`](https://businessdatasolutions.github.io/ai-wiki/concepts/durable-skills) — Brynjolfsson; MGI skill-change index |
| 6 | Responsible AI & society | [`responsible-ai`](https://businessdatasolutions.github.io/ai-wiki/concepts/responsible-ai), [`jagged-frontier`](https://businessdatasolutions.github.io/ai-wiki/concepts/jagged-frontier) — identity-threat; misinformation |
| 7 | Firm-boundary decisions & capstone case | [`enterprise-ai-adoption`](https://businessdatasolutions.github.io/ai-wiki/concepts/enterprise-ai-adoption) — Nishar & Nohria |

**Assessment.** A strategic case study + criterion-based interview, assessed on quality of strategic reasoning, economic analysis and ethical critique — no build component.

**Best fit.** Building a real technical track and letting DIAIA become a genuinely sharp strategy/society course. **Risk.** The sister module needs a **coding-confident intake** — a prerequisite or self-selection — which is in tension with the minor's business-student profile. May suit only a subset of the cohort.

---

## 5. Comparison

### 5.1 At a glance

| Dimension | Sketch 1 — Accessible Builder | Sketch 2 — Light-Code Practitioner | Sketch 3 — Agentic Engineer |
| --- | --- | --- | --- |
| **Sister module** | *AI Agents in Practice* (no-code) | *Building LLM Applications* (light Python) | *Agentic Engineering & AI Systems* (full) |
| **Tooling** | Copilot Studio, n8n, Flowise, GPTs | Notebooks, LLM APIs, vector store | Agent SDK, vector/graph DB, eval platform |
| **Coding required** | None | Scaffolded Python | Confident Python |
| **Prerequisites** | None | Willingness to code | Coding background or self-selection |
| **DIAIA stance** | Build-aware (shares the agent) | Bridge (reads the technical signal) | Pure strategy/society |
| **Shared project across the pair?** | Loose (reference the agent) | Tight (one running project) | None (independent) |
| **Who it suits** | Whole cohort, max inclusivity | Mixed cohort wanting a real bridge | A technically inclined subset |
| **Main strength** | Everyone ships something real | Best business↔engineering integration | Genuine, transferable depth |
| **Main risk** | Platform lock-in, shallow skill | Coding ramp excludes some; needs labs | Intake tension with business profile |
| **Wiki depth used** | Surface (agents, RAG, guardrails) | Mid (RAG, evals, lifecycle basics) | Deep (harness, knowledge architectures, full ADLC) |

### 5.2 DIAIA module designs compared (week by week)

*The three DIAIA variants, read independently of their sister modules. Wiki groundings link to source pages.*

| Week | Sketch 1 DIAIA — Build-aware | Sketch 2 DIAIA — Bridge | Sketch 3 DIAIA — Pure strategy/society |
| --- | --- | --- | --- |
| 1 | Decision framing & the intern analogy | Decision framing & the intern analogy | Decision framing & the intern analogy |
| 2 | Strategy & value — [`strategy`](https://businessdatasolutions.github.io/ai-wiki/concepts/strategy) (Martin; Oberholzer-Gee) | Strategy & value — [`strategy`](https://businessdatasolutions.github.io/ai-wiki/concepts/strategy) (Martin; Oberholzer-Gee) | Strategy & **the infinite game** — [`strategy`](https://businessdatasolutions.github.io/ai-wiki/concepts/strategy), [`infinite-game`](https://businessdatasolutions.github.io/ai-wiki/concepts/infinite-game) (Martin; Sinek) |
| 3 | Adoption & maturity — [`enterprise-ai-adoption`](https://businessdatasolutions.github.io/ai-wiki/concepts/enterprise-ai-adoption) (CISR; Cisco; Ransbotham) | Adoption & maturity — [`enterprise-ai-adoption`](https://businessdatasolutions.github.io/ai-wiki/concepts/enterprise-ai-adoption) (CISR; Cisco; Ransbotham) | **Dynamic capabilities & foresight** — [`dynamic-capabilities`](https://businessdatasolutions.github.io/ai-wiki/concepts/dynamic-capabilities), [`warner-wager-process-model`](https://businessdatasolutions.github.io/ai-wiki/concepts/warner-wager-process-model), [`strategic-foresight`](https://businessdatasolutions.github.io/ai-wiki/concepts/strategic-foresight) (Teece; Webb) |
| 4 | The micro-productivity trap & reinvention — [`micro-productivity-trap`](https://businessdatasolutions.github.io/ai-wiki/concepts/micro-productivity-trap) (Bain/OpenAI) | **Reading the technical signal** — feasibility from RAG/eval; where to deploy — [`jagged-frontier`](https://businessdatasolutions.github.io/ai-wiki/concepts/jagged-frontier), [`micro-productivity-trap`](https://businessdatasolutions.github.io/ai-wiki/concepts/micro-productivity-trap) (Anand–Wu 2×2) | Adoption, maturity & the productivity trap — [`enterprise-ai-adoption`](https://businessdatasolutions.github.io/ai-wiki/concepts/enterprise-ai-adoption), [`micro-productivity-trap`](https://businessdatasolutions.github.io/ai-wiki/concepts/micro-productivity-trap) (Ransbotham; Kiron–Schrage) |
| 5 | AI & work — the economics — [`automation-vs-augmentation`](https://businessdatasolutions.github.io/ai-wiki/concepts/automation-vs-augmentation), [`durable-skills`](https://businessdatasolutions.github.io/ai-wiki/concepts/durable-skills) (Brynjolfsson) | AI & work — the economics — [`automation-vs-augmentation`](https://businessdatasolutions.github.io/ai-wiki/concepts/automation-vs-augmentation), [`durable-skills`](https://businessdatasolutions.github.io/ai-wiki/concepts/durable-skills) (Brynjolfsson) | **Economics & labour (deeper)** — [`ai-employment-effects`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-employment-effects), [`ai-deskilling`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-deskilling), [`durable-skills`](https://businessdatasolutions.github.io/ai-wiki/concepts/durable-skills) (MGI skill-change index) |
| 6 | Responsible AI & governance — [`responsible-ai`](https://businessdatasolutions.github.io/ai-wiki/concepts/responsible-ai), [`jagged-frontier`](https://businessdatasolutions.github.io/ai-wiki/concepts/jagged-frontier) (Dell'Acqua) | Responsible AI & governance — [`responsible-ai`](https://businessdatasolutions.github.io/ai-wiki/concepts/responsible-ai), [`jagged-frontier`](https://businessdatasolutions.github.io/ai-wiki/concepts/jagged-frontier) (Dell'Acqua) | Responsible AI & **society** — [`responsible-ai`](https://businessdatasolutions.github.io/ai-wiki/concepts/responsible-ai), [`jagged-frontier`](https://businessdatasolutions.github.io/ai-wiki/concepts/jagged-frontier) (identity-threat; misinformation) |
| 7 | Build/Compose/Collaborate/Buy + presentations — [`enterprise-ai-adoption`](https://businessdatasolutions.github.io/ai-wiki/concepts/enterprise-ai-adoption) (Nishar & Nohria) | Build/Compose/Collaborate/Buy + presentations — [`enterprise-ai-adoption`](https://businessdatasolutions.github.io/ai-wiki/concepts/enterprise-ai-adoption) (Nishar & Nohria) | Firm-boundary decisions & capstone case — [`enterprise-ai-adoption`](https://businessdatasolutions.github.io/ai-wiki/concepts/enterprise-ai-adoption) (Nishar & Nohria) |

**What changes across the three DIAIA designs:**
- **Sketch 1 → Sketch 2:** only **Week 4** changes (the micro-productivity trap is reframed as *Reading the technical signal*) plus one extra learning outcome (interpret a technical artifact). The strategic/economic/societal backbone is otherwise identical.
- **Sketch 2 → Sketch 3:** strategy **expands** (Week 2 adds the infinite game; Week 3 becomes dynamic capabilities & foresight, pushing adoption/maturity into Week 4), economics **deepens** (Week 5 adds deskilling and the MGI skill-change index), and **all build references are dropped** — DIAIA becomes a pure seminar/case course.

### 5.3 Technical sister modules compared (week by week)

*The three sister modules, read independently of DIAIA. Note how each week escalates in technical depth from left to right.*

| Week | Sketch 1 — *AI Agents in Practice* (no-code) | Sketch 2 — *Building LLM Applications* (light Python) | Sketch 3 — *Agentic Engineering & AI Systems* (full) |
| --- | --- | --- | --- |
| 1 | Platform landscape; agent loop; chatbot→agent→multi-agent — [`ai-agents`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-agents), [`foundation-models`](https://businessdatasolutions.github.io/ai-wiki/concepts/foundation-models) | LLM APIs & the agent loop in Python; Software 3.0 — [`software-3.0`](https://businessdatasolutions.github.io/ai-wiki/concepts/software-3.0), [`ai-agents`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-agents) | Software 3.0 & agent fundamentals; brain/hands/session — [`software-3.0`](https://businessdatasolutions.github.io/ai-wiki/concepts/software-3.0), [`ai-agents`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-agents) |
| 2 | Prompt & instruction design (the "intern" briefing) — [`ai-agents`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-agents) | Prompting in code; structured / JSON output — [`ai-agents`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-agents) | The harness — Context & Constraints; pre/post-tool hooks — [`agent-harness`](https://businessdatasolutions.github.io/ai-wiki/concepts/agent-harness) |
| 3 | Connecting tools & knowledge — no-code RAG, file upload — [`is-rag-dead`](https://businessdatasolutions.github.io/ai-wiki/syntheses/is-rag-dead), [`knowledge-architectures-for-llm-agents`](https://businessdatasolutions.github.io/ai-wiki/syntheses/knowledge-architectures-for-llm-agents) | Tool-calling & function use; contracts intro — [`agent-harness`](https://businessdatasolutions.github.io/ai-wiki/concepts/agent-harness) | Knowledge architectures — RAG / LLM-Wiki / Fat-Skills; GraphRAG — [`knowledge-architectures-for-llm-agents`](https://businessdatasolutions.github.io/ai-wiki/syntheses/knowledge-architectures-for-llm-agents), [`knowledge-graphs`](https://businessdatasolutions.github.io/ai-wiki/concepts/knowledge-graphs) |
| 4 | Multi-step flows & triggers; keep it simple — [`agent-harness`](https://businessdatasolutions.github.io/ai-wiki/concepts/agent-harness) | RAG fundamentals — chunk, embed, vector search — [`is-rag-dead`](https://businessdatasolutions.github.io/ai-wiki/syntheses/is-rag-dead), [`knowledge-architectures-for-llm-agents`](https://businessdatasolutions.github.io/ai-wiki/syntheses/knowledge-architectures-for-llm-agents) | Contracts & evaluation — rubrics, LLM-as-judge, benchmarks — [`ai-benchmarks`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-benchmarks) |
| 5 | Testing & guardrails — destructive-action checks, HITL — [`responsible-ai`](https://businessdatasolutions.github.io/ai-wiki/concepts/responsible-ai) | Evaluation — LLM-as-judge, binary pass/fail, TPR/TNR — [`ai-benchmarks`](https://businessdatasolutions.github.io/ai-wiki/concepts/ai-benchmarks) | The agent development lifecycle — build/test/deploy/monitor/iterate/govern — [`agent-development-lifecycle`](https://businessdatasolutions.github.io/ai-wiki/concepts/agent-development-lifecycle) |
| 6 | Deploy & integrate (Teams/web); monitoring — [`agent-development-lifecycle`](https://businessdatasolutions.github.io/ai-wiki/concepts/agent-development-lifecycle) | Guardrails, cost & observability; basic tracing — [`agent-development-lifecycle`](https://businessdatasolutions.github.io/ai-wiki/concepts/agent-development-lifecycle) | Agentic engineering vs vibe coding; production discipline; the ratchet — [`agentic-engineering`](https://businessdatasolutions.github.io/ai-wiki/concepts/agentic-engineering), [`vibe-coding`](https://businessdatasolutions.github.io/ai-wiki/concepts/vibe-coding) |
| 7 | Demo day + reflection on limitations | Mini-project demo + write-up | Capstone agent demo + ratchet retrospective |

### 5.4 A note on sequencing

All three pairings are **7 weeks each**, matching DIAIA's current shape so they can run **sequentially** (DIAIA → sister, or sister → DIAIA) or **in parallel** within the minor. Sketch 2's tight shared-project design works best **in parallel**; Sketch 3's independent design works either way.

---

## 6. Recommended next steps (on request)

- A **one-page comparison** for the faculty board to choose a direction.
- For the chosen sketch: a **full assessment rubric** (CRISP-DM-aligned for DIAIA; spec/eval-aligned for the sister) on the existing 0–10 scale.
- Mapping each module's learning outcomes to the **minor's formal assessment regulations** and the broader MDD programme outcomes.
- A **reading list / source pack** drawn from the wiki's 138 sources, per week.

---

## Wiki source index

All groundings link into the AI Wiki at **[businessdatasolutions.github.io/ai-wiki](https://businessdatasolutions.github.io/ai-wiki)**. Pages cited in this document:

| Page | Type | URL |
| --- | --- | --- |
| ai-agents | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/ai-agents> |
| foundation-models | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/foundation-models> |
| software-3.0 | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/software-3.0> |
| agent-harness | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/agent-harness> |
| agent-development-lifecycle | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/agent-development-lifecycle> |
| ai-benchmarks | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/ai-benchmarks> |
| agentic-engineering | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/agentic-engineering> |
| vibe-coding | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/vibe-coding> |
| knowledge-graphs | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/knowledge-graphs> |
| responsible-ai | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/responsible-ai> |
| strategy | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/strategy> |
| enterprise-ai-adoption | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/enterprise-ai-adoption> |
| dynamic-capabilities | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/dynamic-capabilities> |
| warner-wager-process-model | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/warner-wager-process-model> |
| strategic-foresight | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/strategic-foresight> |
| infinite-game | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/infinite-game> |
| micro-productivity-trap | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/micro-productivity-trap> |
| jagged-frontier | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/jagged-frontier> |
| automation-vs-augmentation | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/automation-vs-augmentation> |
| durable-skills | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/durable-skills> |
| ai-deskilling | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/ai-deskilling> |
| ai-employment-effects | concept | <https://businessdatasolutions.github.io/ai-wiki/concepts/ai-employment-effects> |
| is-rag-dead | synthesis | <https://businessdatasolutions.github.io/ai-wiki/syntheses/is-rag-dead> |
| knowledge-architectures-for-llm-agents | synthesis | <https://businessdatasolutions.github.io/ai-wiki/syntheses/knowledge-architectures-for-llm-agents> |

*Current module facts cited from the existing module description for DATDRD05-T05, recorded in Appendix A of the internal integrated LRD.*

*Author/organisation names (Martin, Oberholzer-Gee, Ransbotham, Brynjolfsson, Teece, Sinek, Webb, Dell'Acqua, Nishar & Nohria, Kiron–Schrage, Anand–Wu, Husain, Chase, Karpathy) have their own entity pages in the wiki under `/entities/`.*
