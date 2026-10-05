# platform/ — the BAS World handbook pipeline

One handbook page per week, every fact traced to a saved source. Start with `context.md` (who we write for, the quality bar), then `docs/RUNBOOK.md` (how a week runs).

```
platform/
├── CLAUDE.md          rules for the CLI assistant + stage table
├── context.md         the shared desk: reader, criteria, who checks what, house style
├── timelog.csv        minutes per stage, all weeks
├── library/           carries over between weeks
│   ├── sources/       S-0xx.md (+ PDF/, incoming/ during a search)
│   ├── appraised.md   ratings
│   ├── claims_en.md   every claim: verbatim original + English
│   ├── searchlog.md   every search query
│   └── review_queue.md  the sources a person must open
├── weeks/
│   ├── week-02/       question.md, draft.md
│   └── week-04/       question.md, draft.md, check.md (page.md after publish-prep)
├── templates/         the shape of each stage's output, question template, manual check
├── docs/              PRD, blueprint, assignment 2 write-up, RUNBOOK
├── wiki/              interlinked synthesis of the library (start at wiki/overview.md)
├── reference/         copy of the course-site repository; not part of the pipeline
└── .claude/           skills, agents, scripts, hooks, settings
```

New week: `python .claude/scripts/gates.py new-week <NN>`, fill in `weeks/week-NN/question.md`, then `/run-page`.
What is left to do: `python .claude/scripts/gates.py todo`.
