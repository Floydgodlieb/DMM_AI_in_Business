# ADR-0006: What the sister module builds — a client prototype or the research platform

## Status

Proposed

## Context

All three redesign sketches assume the same thing about the technical sister
module: students build an AI product for a client. The variants differ only in
how they build it — a no-code agent on Copilot Studio, a scaffolded Python LLM
application, or a full agentic system with a harness and an evaluation pipeline.
In each case the artefact is a prototype of something a company might use.

The research lecturer's proposal opens a different possibility. Noting that
students previously devised a simple agentic business case and built a prototype
for it, the question is put directly: is there still room for that, or should the
build effort go into *an agentic platform with which students write the handbook,
collect the data, analyse it — a socratic agent, and so on*.

That second option appears nowhere in the sketches. It is not a variation in
technical depth; it is a different answer to what the artefact is *for*. Under
ADR-0001 the module produces a handbook through team research, and that research
has real infrastructure needs: gathering and appraising sources, processing
interview transcripts, keeping citations honest, editing six teams' prose into
one voice, and challenging the authors' reasoning.

The two options also couple the modules differently. Sketch 2 couples them
through a shared *case* — the same running project seen from two sides. Building
the research platform couples them through a shared *tool*: the research track
becomes the technical track's user, with real requirements and real complaints.

## Options considered

**Client prototype, as in the sketches.** Familiar, transferable, and it gives
students something to show an employer. The client is hypothetical, so the
requirements are whatever the team decides they are, and there is no user to
disappoint. Under ADR-0003 it also means the joint interview has two artefacts
with nothing connecting them.

**The research platform.** The users are in the room and their needs are real, so
requirements engineering stops being a paper exercise. It produces the tightest
possible integration between the tracks, and it is a genuinely current thing to
build — agentic tooling for knowledge work is the subject the module teaches.
But a tool the cohort depends on cannot be allowed to fail, which is a hard
constraint to put on a seven-week student project; and if it does fail, it takes
the handbook with it. It also narrows the domain: everyone builds a variation on
document processing.

**Both.** The proposal notes the impression that both may be wanted. Seven weeks
does not hold two build tracks, and attempting it produces two unfinished
artefacts.

**Client prototype, with the research platform as the running case study.** The
platform is specified, designed and partially built as the teaching vehicle, but
the handbook does not depend on it.

## Decision

The sister module builds the research platform, with the module's own research
work as its client — but the handbook must not depend on it.

The dependency is the whole difficulty, and it is separable from the benefit. The
value is that the users are real, the requirements are real, and the feedback is
immediate; none of that requires the handbook to be unrecoverable if the platform
does not work. Teams therefore keep a manual route for every step the platform
automates, and the platform is judged on whether it works, not on whether the
handbook came out of it.

This is chosen over the client prototype because a hypothetical client produces
hypothetical requirements, and requirements are the part of building that
business students most need to practise and least get to.

## Consequences

- The technical module needs a specification before it starts: what the research
  track actually needs, in enough detail that teams can build against it. Writing
  it is work, and it belongs to both lecturers.
- Every team builds in the same domain. The portfolio piece is less varied than a
  free-choice prototype, which matters for students using it in applications.
- The manual fallback must be genuinely maintained, not nominal. If the platform
  becomes the only practical route mid-module, the safeguard has failed.
- Under ADR-0003 the joint interview gains an obvious spine: the student can be
  asked about the same object from the technical and the research side.
- Teams handling interview data through their own tooling raises the data
  protection question in ADR-0005 with more force — student-built software
  processing personal data needs a decision about where that data may live.
- The asymmetric calendars in ADR-0002 matter here: the platform is needed early
  in the research module but is not finished until late in the technical one.
  Either the dependency is genuinely optional, as decided above, or the calendars
  have to change.

This record depends on ADR-0001.
