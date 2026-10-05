---
name: wiki-query
description: Answer a question from the wiki (wiki/), citing claim-ids, and file the answer back as a page when it is worth keeping. Use when asked what the library says about something, to compare sources, or to prepare the ground for a new week's question.
argument-hint: "<question>"
allowed-tools: Bash(python .claude/scripts/wiki.py:*), Read, Write, Edit, Glob, Grep
---

# Wiki query

Read `context.md`, then `wiki/SCHEMA.md`.

1. Read `wiki/index.md`. Open the pages that bear on `$ARGUMENTS`, then follow their links one step. Use Grep on `wiki/` for terms the index does not show.
2. Check each claim you will rely on in `claims_en.md` (the source page's generated block shows its status).
3. Answer in plain English. Every fact carries its `[claim-id]`. Say what the library does **not** cover, and which claims still await a person check.
4. If the answer is worth keeping (a comparison, a gap analysis, groundwork for a week's question), ask once, then file it as `wiki/answers/<today>-<kebab-name>.md` with front matter (SCHEMA.md). Link it from each topic page it draws on, run `wiki.py refresh` and `wiki.py lint` until 0 errors, and `wiki.py log query "<question>" "<answer page>"`.

Never answer from your own knowledge; an uncovered point is a gap, not a guess.
