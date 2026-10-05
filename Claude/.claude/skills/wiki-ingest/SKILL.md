---
name: wiki-ingest
description: Fold new or changed sources and claims from the library into the wiki (wiki/), updating source, topic and entity pages and the overview, every fact cited by claim-id. Use after Translate adds claims, or when asked to ingest, update or build the wiki.
argument-hint: "[optional: S-ids to ingest; default: whatever wiki.py status lists]"
allowed-tools: Bash(python .claude/scripts/wiki.py:*), Read, Write, Edit, Glob, Grep
---

# Wiki ingest

Read `context.md`, then `wiki/SCHEMA.md`. Raw files (`library/sources/`, `appraised.md`, `claims_en.md`) are read-only here.

## Steps
1. Run `python .claude/scripts/wiki.py refresh`, then `python .claude/scripts/wiki.py status`. Work on the S-ids in `$ARGUMENTS`, or else on "source pages still to ingest" and the sources behind "claims not yet used". Nothing else.
2. Read `wiki/index.md` and `wiki/overview.md` so you know which pages exist.
3. For each source: read `library/sources/S-0xx.md` and its claims in `claims_en.md`. On `wiki/sources/S-0xx.md` write:
   - `summary:` one line (what the source is and what it adds), `updated:` today;
   - *What it says*: 3-6 sentences, each ending with its `[claim-id]`. A source with no usable claims: say what it is and that nothing from it may be stated yet;
   - *Where it fits*: links to the topic and entity pages it feeds.
4. Update every topic and entity page the source touches. Add the new cited facts where they belong, add the source to `sources:` and *Sources*, and rewrite the lead if the picture changed. Create a page when a topic or organisation shows up in two or more sources.
5. Flag every disagreement with a `> [!contradiction]` callout (SCHEMA.md). A `case` claim never contradicts a `sector` claim.
6. Update `wiki/overview.md` if the overall picture moved.
7. Run `wiki.py refresh` and `wiki.py lint`. Fix every ERROR and every "number without a claim-id". Repeat until 0 errors.
8. `python .claude/scripts/wiki.py log ingest "<S-ids>" "<pages created / updated>"`.

## Never
- State a fact without a claim-id, or from your own knowledge.
- Cite a superseded, FAIL or discarded claim.
- Edit the generated block, `index.md` by hand, or any file outside `wiki/`.

Report: pages created, pages updated, contradictions flagged, and gaps worth a search line.
