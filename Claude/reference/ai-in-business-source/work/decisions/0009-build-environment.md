# ADR-0009: The AEL build environment — students bring their own agentic CLI

## Status

Proposed

## Context

Under ADR-0006 every AEL team builds its own research platform, and the LRD
commits AEL to the technical level of the third redesign sketch: harness
design, knowledge architecture, an evaluation pipeline and the full agent
development lifecycle. The sketch names its own setup — Python, an agent SDK,
a vector store, an eval platform — and its own risk: it needs a
coding-confident intake. The LRD softens that to "coding-confident by choice".

Two facts have since become clear. The minor's intake is predominantly
business-management students, most with no coding or engineering background,
and under the LRD's default pairing they all take AEL. And there is no
programme budget for model usage. An agent SDK bills every token to an API key
the programme would have to own; at list price at the time of writing, ten
teams over seven weeks come to several thousand dollars once interactive
building, platform runs and evaluation are added up, and the figure is
open-ended because it scales with how hard the teams work.

So the question is not which SDK to teach. It is how a non-coding cohort with
no token budget reaches the sketch's six outcomes at all. The outcomes survive:
none of them is "write Python fluently". What has to change is how students
build, and what the build runs on.

Three constraints from earlier records bind the answer. The platform must stay
the team's tool and never the handbook's precondition (ADR-0006, NFR-08). Where
student-built tooling may hold interview data is a course-team decision, not a
team's (ADR-0005, NFR-09). And the shared hosting platform must reuse the
existing AI Wiki / Quartz site rather than stand up new infrastructure (NFR-02).

## Options considered

**An agent SDK on a programme-funded API key, as the sketch assumes.** The
most direct mapping to the wiki's vocabulary, headless runs in CI, and one
workspace per team with a spend cap gives clean cost control. But the cost is
real and open-ended, there is no budget for it, and an SDK application cannot
run on a consumer subscription, so the cost cannot be shifted to students
either. It also asks a non-coding cohort to write and debug SDK code, which is
the sketch's own named risk.

**No-code agent platforms, as in the first sketch.** Free tiers exist and every
student ships something. But the harness layers, the knowledge-architecture
choice and the evaluation pipeline are exactly what those platforms hide, so
the module would be teaching the first sketch's outcomes under the third
sketch's name.

**Subscription seats bought by the programme.** A team plan gives central
billing and admin control, and a seat is a predictable cost rather than an
open-ended one. But it is still a cost the programme does not have, and it
buys interactive use only — a headless platform still needs a key.

**Students direct an agentic CLI they bring themselves.** The student does not
write the platform; they specify it, constrain it, evaluate it and direct an
agentic coding CLI that writes it. The platform is the repository's harness
configuration — instruction files, hooks, skills, MCP servers and an
evaluation config — run interactively by the researcher on the student's own
account. At least one capable CLI is free on a personal account at a daily
quota that comfortably covers a student's use, and it exposes the full harness
surface: project context files, lifecycle hooks before and after each tool
call, MCP and extensions. Students who prefer a paid CLI may bring one at
their own expense, at a price below a textbook. Nothing headless, nothing
billed to the programme.

## Decision

Students build their team's research platform by directing an agentic coding
CLI they bring themselves, and the platform is the repository's harness
configuration rather than an application built on an agent SDK.

Concretely:

- **The harness is the CLI's own.** The four layers of the wiki's harness
  model map onto files a business student can read and edit: the project
  context file is the Context layer, hooks are the Constraints layer, the
  evaluation config is the Contracts layer, and memory and skills are the
  Compounding layer. Building a harness means writing prose in the right
  places, and every layer is visible.
- **A free CLI is the guaranteed baseline.** The module names one CLI that is
  free on a personal account with hooks, MCP and project context files, and
  every exercise and every piece of course material is written against it.
  Any other agentic CLI with an equivalent surface is allowed, at the
  student's own cost, and the student maps it to the baseline themselves.
- **Evaluation is configuration, not test code.** Rubrics are written in a
  declarative eval tool's config against the shared quality bar (LRD §6.2),
  with a judge model drawn from the same free quota. The tester role owns them.
- **The platform is used through MCP, not through a built interface.** A
  team exposes its tools as MCP servers and the researchers use them from the
  CLI they already have. No team builds a user interface.
- **The shared infrastructure stays on the education-tier services the
  cohort already has.** Cloud development environments through the
  programme's classroom organisation, the AI Wiki on Quartz on GitHub Pages,
  and the gate dashboard as a static file the wiki renders. The
  infrastructure build-group's outcome (LRD §3.3 #6) is unchanged.
- **The Socratic tutor is the one exception.** It is owner-built, evaluates
  students, and must not depend on any student's account or free tier. It
  runs on a course-owned key with a hard spend cap — the single model-usage
  line the programme funds.
- **No personal data through a free tier.** Free tiers may use submitted
  content to improve the vendor's products. The data-tier rule that NFR-09
  requires therefore becomes absolute: public sources and the team's own
  writing may pass through the harness; interview material may not, in any
  form, unless the course team has explicitly decided otherwise for a named
  tool. Transcript processing is done by the manual route.

This is chosen over the SDK because it is the only option that reaches the
sketch's outcomes with this intake at this budget, and because directing an
agent against a specification, then judging the result, is precisely the
agentic-engineering discipline the fifth outcome asks for. The intake stops
being a risk and becomes the point.

## Consequences

- The technical module's setup section in the LRD, the AEL prior-knowledge
  row in its Part 4 and the "agent SDK" wording it inherits from the sketch
  are now wrong and must be revised, with a version bump and a logbook entry.
  The sketch itself stays as written; it is a source document.
- The wiki's harness vocabulary was written with one vendor's CLI in view.
  The baseline CLI has the same layers under different names, and the module
  owes students a one-page mapping between the two before week 2.
- The week-3 exercise of swapping the model behind the team's platform is
  lost: a free CLI is single-vendor. It is replaced by a comparison exercise —
  the same task through the baseline CLI and through a student-funded
  alternative, judged by the same rubric — which needs at least one student per
  cohort to have brought the alternative.
- The module now depends on a vendor's free tier, which the vendor can
  withdraw or shrink at any time, including mid-cohort. That is the very
  dependency the AIBS week-3 theme warns SMEs about, and the module should
  say so in the room rather than hide it. The mitigation is the same as
  ADR-0006's: every step keeps a manual route, and the platform is judged on
  whether it works, not on whether the handbook came out of it.
- Daily request quotas become a design constraint. A hook that fires on every
  tool call spends the quota fastest, so the deployer role watches consumption
  and the ratchet retrospective asks which constraint cost the most requests.
- Headless, scheduled runs are gone. The platform runs when a researcher runs
  it. Under FR-12 that is the intended state anyway.
- Evaluation has to arrive earlier than the AEL calendar currently places it.
  A cohort that directs an agent rather than reading its code cannot tell a
  working platform from one that looks working without a rubric, so the first
  eval config is due in week 2, not week 4.
- Whether students may use a consumer account with an external vendor for
  coursework at all is a data-protection question for the institution, not
  for the module. If the answer is no, this record is superseded and the
  subscription-seat option returns with a budget request attached.
- Students who bring a paid CLI pay for it themselves. The module must make
  clear that the paid route confers no advantage in assessment, and the
  criteria must be written so that it does not.
