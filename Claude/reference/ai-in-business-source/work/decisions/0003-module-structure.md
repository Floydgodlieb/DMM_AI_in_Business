# ADR-0003: Module structure — two separate modules or one co-taught module

## Status

Proposed

## Context

The redesign sketches propose splitting the current module in two: a refocused
AIBS covering business, economic and societal aspects, and a new technical
sister module owning the build work. Each is a module in its own right, with its
own learning outcomes and its own assessment.

The research lecturer's proposal describes something closer to one course with
two faces: students work in teams of four, hold build roles with the technical
lecturer (product manager, developer, tester, deployer) and the role of
independent researcher with the research lecturer, and are assessed in a single
criterion-based interview conducted by **both lecturers at once**, each
questioning from their own perspective — technical and research.

Read generously the two are compatible: two modules whose teams and timetable
happen to coincide. But the joint CBI is not a coincidence. If one interview
produces one judgement, there is one assessment, and two modules that share an
assessment are administratively one module. If they stay two modules, each needs
a defensible mark of its own, and the joint interview becomes two interviews in
one room.

The examination regulations force this to be explicit rather than left pleasantly
vague.

## Options considered

**Two separate modules, separate assessment.** Clean administratively. Each
module carries its own outcomes and its own mark, students can pass one and fail
the other, and the sister module can be offered to students outside the minor.
The cost is that the integration lives only in the students' heads: nothing in
the assessment rewards connecting the research to the thing they built.

**One co-taught module, one joint CBI.** Assessment matches how the work is
actually done, and the joint interview is genuinely stronger — a student who can
answer the technical lecturer and the research lecturer in the same breath has
demonstrated something neither could establish alone. The cost is that a student
who is strong on one side and weak on the other gets one mark, both lecturers
must be present for every interview, and the module cannot be unbundled.

**Two modules, one shared assessment moment, two marks.** The joint interview
happens, both lecturers question, but each awards a mark against their own
module's criteria. Keeps the administrative separation and most of the
integration benefit. The risk is halo: it is hard to mark a strong technical
answer down on research grounds having just heard it.

## Decision

Two separate modules with separate marks, assessed in a single joint
criterion-based interview in which each lecturer awards their own module's mark
against their own criteria.

Separate marks are kept because the alternative removes a student's ability to
pass the research work while failing the build, which given the intake the
sketches describe — business students, not programmers — is a real and
foreseeable outcome rather than an edge case. The joint interview is kept
because the integration between the two tracks is the point of the pairing, and
an assessment that never tests it will not produce it.

The halo risk is accepted and mitigated by writing the two criterion sets
separately and scoring independently before comparing.

## Consequences

- Two sets of assessment criteria must be written, and they must be genuinely
  distinct — not one rubric with a technical and a research column.
- Both lecturers must attend every interview, which roughly doubles the
  assessment load in contact hours and constrains the timetable.
- The modules can be timetabled with different week counts (see ADR-0002) as long
  as the interview lands after both have finished.
- The sister module remains offerable to students outside the pairing, though its
  assessment would then need a single-examiner variant.
- Scoring independently before comparing must be an explicit instruction in the
  assessment procedure, or the halo risk is unmitigated in practice.

This record depends on ADR-0001, which establishes that AIBS is a research
module with a distinct perspective worth examining separately.

