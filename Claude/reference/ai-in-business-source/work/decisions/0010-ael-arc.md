# ADR-0010: The AEL arc — two spines, one element a week, from vibe coding to agentic engineering

## Status

Proposed

## Context

The third redesign sketch orders AEL's seven weeks harness-first: agent
fundamentals, then the Context and Constraints layers, then knowledge
architecture, then contracts and evaluation, then the development lifecycle,
then "agentic engineering versus vibe coding" as a week-6 topic, then a capstone
with a ratchet retrospective. The LRD's week table carried that order into the
AEL column.

Two things have changed under it. ADR-0009 fixes that students direct an
agentic CLI rather than write the platform, which makes the project-management
half of building — knowing who it is for, why it matters, how it will be used
and what quality it must reach — the part of the work students actually do by
hand. And the ratchet principle the sketch ends on says every guardrail must
trace back to a specific failure it prevents; a calendar that installs the
guardrails first and meets the failures later gives the retrospective nothing
real to trace.

The two module owners also want AEL to cover the process, not only the
technique: a product requirements document first, sourced from the team's own
research in AIBS, then a technical blueprint, then the team's own decision log,
then a build plan with phases, tasks, tests and commit gates.

## Options considered

**Keep the sketch's order.** Harness layers first, vibe coding as a week-6
contrast. Familiar, and it front-loads the vocabulary. But under ADR-0009 the
first two weeks would teach layers the students have no failure to attach them
to, and the retrospective in week 7 would be reconstructed rather than lived.

**A process spine only.** PRD, blueprint, decision log, build plan, and let the
harness emerge from whatever the agent produces. It teaches the product
manager's half well and the engineer's half not at all; four of the six
outcomes go unpractised.

**Two spines, one element of each per week, starting from deliberate vibe
coding.** Week 1 is a bare CLI with no harness at all, producing something
that works once and a log of how it failed. Each following week adds one
process artefact and one harness element, chosen so that the harness element is
the mechanical answer to a failure the team has already met and the process
artefact is the document that records why. The week-7 retrospective traces each
element back to its failure through the team's own decision log. The cost is a
tight week 1 — a non-coding cohort given a bare CLI and an open brief will
freeze — and a discipline that every element be small enough to add in one
session, or teams that slip stack up.

## Decision

AEL runs two spines side by side, adding one element of each per week, and
starts from deliberate vibe coding.

| Week | Process artefact | Harness element | Owning role |
|---|---|---|---|
| 1 | PRD v0, sourced from the AIBS problem analysis | Vibe-coded spike and a failure log | Product manager |
| 2 | Technical blueprint | Context: the project context file and the spec, plus a hand-applied checklist from the shared criteria | Developer |
| 3 | Decision log opened; its first record is the knowledge-architecture choice | Knowledge: where sources and drafts live | Whole team, product manager edits |
| 4 | Build plan: phases, tasks, test gates | Contracts: the eval config with a binary judge against the shared bar | Tester |
| 5 | Commit and push gates live in CI | Constraints: hooks before and after tool calls, whose log is the monitoring | Deployer |
| 6 | Release discipline; the rules file grown from the failure log | Compounding: skills and memory | Whole team |
| 7 | Ratchet retrospective | Capstone demo | Whole team |

Three orderings are deliberate. Contracts come before constraints, reversing
the sketch, because a hook is the mechanical answer to a failure an eval has
already caught; the sequence is failure, then detection, then prevention. Hooks
double as monitoring, so week 5 carries both the Constraints layer and the
deploy-and-monitor outcome for a platform that never runs headless. And the
week-1 spike is not in tension with spec-first: it is the discovery instrument
for the PRD, which is written from the spike's failures and the AIBS problem
analysis together.

The PRD is for the team's own researchers. Under ADR-0006 the platform's user
is the team as researchers, so "who are we building for" is answered by the
team itself and "why it matters" by the research question and the SME reader.
The AIBS findings inform the PRD as domain knowledge, not as a customer; a PRD
that answers "who" with an SME has drifted back to the client prototype that
ADR-0006 rejected.

## Consequences

- The AEL column of the LRD's week table changes for every week, and the
  process artefacts become deliverables alongside the platform.
- Week 1 needs one concrete task that serves the AIBS week-1 gate — for
  example, a cited source list for the problem analysis into a file — and the
  failure log is a required artefact from day one. The wiki's vibe-coding page
  is a warning; students must hear week 1 as the baseline every engineer starts
  from, not as a week they are told off for later.
- Evaluation arrives earlier than the sketch places it: as a hand-applied
  checklist in week 2 and as configuration in week 4. A cohort that directs an
  agent rather than reading its code cannot tell a working platform from one
  that looks working without a rubric.
- Four process documents in seven weeks for non-coders can eat the build. Each
  is one page, living, and version-bumped weekly, or it becomes homework.
- The PRD depends on AIBS output that is only complete in week 1; later AIBS
  results arrive after the blueprint is written. The PRD must be allowed to
  change, and the team's decision log is where those changes are recorded.
- The joint interview gains a clean AEL half: walk the student through their
  own decision log and ask which failure each entry answers. That is the
  role-relevance question of ADR-0007 applied to the team's own history.
- The team's decision log mirrors this repository's decision records, and its
  commit gates mirror the module's Socratic and peer gates. Students build in
  miniature the process the module runs on; the module owes them a template for
  both.

This record depends on ADR-0006 and ADR-0009.
