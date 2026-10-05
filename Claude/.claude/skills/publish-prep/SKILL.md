---
name: publish-prep
description: Stage 6 preparation, run only by the deployer. Runs the publish gate, then copies draft.md to page.md with version, date and checking note. Never publishes.
disable-model-invocation: true
argument-hint: "<version, e.g. 1.0>"
allowed-tools: Bash(python .claude/scripts/gates.py publish-gate), Read, Write
---

# Stage 6 — prepare page.md (a person publishes)

Read `context.md` first. You only prepare a file. Publishing (branch → pull request → link check → merge, then the Teams post) stays with the deployer, by hand.

## Gate
Run `python .claude/scripts/gates.py publish-gate`. If it says CLOSED, list its problems and stop. Do not argue a problem away; a person fixes it, or writes in `check.md` why a gap is accepted and fixes the gate's input.

## Then
1. Copy `draft.md` to `page.md` unchanged, apart from:
   - a first line: `version: $ARGUMENTS · date: <today> · context: <context.md version>`
   - the checking note, with counts taken from `check.md`: "<n> of <total> statements auto-verified against the live source; <k> sources checked by a person (review_queue.md); all numbers checked; second reader: <name>."
2. Tell the deployer the manual publish steps from `docs/RUNBOOK.md` Stage 6. Do not run git, do not push, do not post.
