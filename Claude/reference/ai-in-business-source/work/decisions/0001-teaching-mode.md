# ADR-0001: Teaching mode — taught curriculum or student-led research

## Status

Proposed

## Context

Two proposals for the redesigned AIBS are on the table, and they differ on an
axis neither document names.

The three redesign sketches vary the
technical ambition of a new sister module — no-code, light Python, agentic
engineering — and fill AIBS in as a **taught** course on the business, economic
and societal aspects of AI. Every week has a topic and a grounding in the AI
Wiki. The lecturer covers the material; students apply it in a CRISP-DM report.

The parallel proposal from the research lecturer casts AIBS as a **research
module**. Students learn applied-research skills — problem analysis, internal
and external analysis, source appraisal, field research, translating findings
into advice — and the handbook itself is the deliverable. Content is not fixed
per week; it is a set of research themes teams investigate.

This is the keystone decision. It determines what a "weekly programme" even
means: a lecturer covering theme X, or a team investigating theme X. Until it is
settled, the module calendar (ADR-0002), the module structure (ADR-0003) and
what the sister module builds (ADR-0006) cannot be settled either, because each
of those reads differently under the two readings.

It also decides what the sketches' carefully wiki-grounded week tables *are*: a
lecture plan, or a source pack.

## Options considered

**Taught curriculum.** A fixed weekly programme with wiki grounding, assessed by
a CRISP-DM report and a criterion-based interview. Predictable workload,
transparent for the examination board, and every student meets the same content.
But it sits badly with the stated assessment philosophy — *"we are no longer
impressed if you deliver content; we are impressed if you can show you have
gained new insights and create value for companies"* — because a taught course
mostly asks students to reproduce content. It also leaves the handbook without
authors.

**Student-led research.** Teams pick themes, do the research, write the
handbook. Matches the assessment philosophy directly and produces something that
did not exist before. But coverage becomes uneven — no guarantee any given
student meets responsible AI or firm-boundary theory — and the quality of the
handbook depends on the weakest team. Applied-research skills are themselves
substantial content that has to be taught somewhere, and the sketches allocate
no time to them.

**Hybrid: a fixed theme per week, research within it.** The week's theme is
fixed and grounded in the wiki; the lecturer opens it plenary; teams then
investigate a question inside that theme and contribute their findings to the
handbook. Coverage is guaranteed by the theme sequence, authorship by the
research work.

## Decision

AIBS becomes a research module with a fixed thematic spine: each week has a set
theme with wiki grounding, opened plenary, within which teams conduct their own
research and produce a handbook contribution.

The wiki-grounded week tables from the sketches are kept, but they are rewritten
from lecture topics into **research assignments** — each week states the theme,
the grounding sources as a starting point, and the question the team must answer
about it. The sketches' content survives; its function changes.

This is chosen over the pure options because each fails on something the other
handles. A taught course contradicts the assessment philosophy the module has
already adopted; pure student-led research cannot guarantee that a graduate of
the module has met the material the programme promises. The thematic spine costs
some of the freedom that makes research motivating, and that is the price.

## Consequences

- Every week table in the sketches must be rewritten as research assignments
  before the module can run. This is real work, not a reframing.
- Applied-research methodology becomes teaching content that must be timetabled.
  It is absent from all three sketches, so it displaces something.
- Assessment shifts from a report the lecturer specifies to a contribution the
  team defines, which makes the criteria harder to write and raises the
  attribution problem addressed in ADR-0007.
- The plenary opening plus team research implies a working format — a plenary
  block and per-team sessions — which constrains ADR-0002 and ADR-0003.
- The lecturer's role shifts from covering material to supervising research.
  Preparation goes down; contact-hour intensity goes up.
- A weak cohort produces a weak handbook, and the handbook is public. There must
  be an editorial gate before anything reaches the site.
