# ADR-0002: Module calendar — six teaching weeks plus consolidation, or seven

## Status

Proposed

## Context

The three redesign sketches assume a uniform **seven-week** programme for both
AIBS and its sister module, chosen to match the current module's shape so the
two can run sequentially or in parallel.

The research lecturer's proposal assumes **six teaching weeks covering five
themes, with the final week spent bringing every team's content together**, and
raises the possibility of running over into week 8 with assessment in week 9.

These are not reconcilable by rounding. The consolidation week is not a spare
week: under ADR-0001 the handbook is a single collective artefact assembled from
team contributions, and that assembly is real work — reconciling overlapping
material, resolving contradictions between teams, imposing one voice, checking
sources. A module that fills all seven weeks with new themes has no slot for it
and will produce a stapled-together document.

The trade is therefore one theme's worth of content against the quality of the
artefact the module exists to produce.

## Options considered

**Seven themed weeks.** Maximum content coverage, symmetrical with the sister
module, no change to the existing timetable footprint. Consolidation happens in
students' own time or not at all. Given that the handbook is public and carries
the programme's name, "not at all" is the likely outcome under deadline
pressure.

**Six themed weeks plus a consolidation week.** One theme fewer. The handbook
gets an editorial pass while the teams who wrote it are still available and
still being supervised. Asymmetric with a seven-week sister module, which
matters only if the two run in lockstep.

**Six themed weeks, consolidation in week 7, slack in week 8, assessment in week
9.** The most comfortable, and it decouples the assessment from the deadline for
the artefact being assessed. Whether weeks 8 and 9 exist is a timetabling
constraint rather than a design choice, so this option may simply be
unavailable.

## Decision

Six teaching weeks covering five themes, with week 7 reserved for consolidating
all team contributions into one handbook.

The handbook is the module's deliverable under ADR-0001 and it is published under
the programme's name. An unedited assembly of six team documents is not a
handbook, and the difference between the two is a week of supervised editorial
work. One theme is the right price.

Whether assessment lands in week 7, or the module extends to weeks 8 and 9, is
left to the timetable and does not need to be fixed here — but the assessment
must not fall in the same week as the consolidation deadline.

## Consequences

- One of the themes identified in the redesign work does not get its own week and
  must be dropped, merged into another, or offered as optional material.
- AIBS and a seven-week sister module no longer align week for week. Under a
  tight shared-project design this creates friction; see ADR-0003 and ADR-0006.
- Week 7 needs its own didactic design — an editorial workflow, an owner for the
  final text, and a decision on what happens to material that does not make the
  cut. That is not a free week.
- Assessment cannot be scheduled in week 7 without putting the artefact and its
  assessment on the same deadline.
- If the timetable does not permit weeks 8 and 9, the consolidation week absorbs
  all remaining slack and there is no recovery room for a team that falls behind.

This record depends on ADR-0001; if the module is not built around a collective
handbook, the consolidation week loses its purpose and this decision should be
revisited.
