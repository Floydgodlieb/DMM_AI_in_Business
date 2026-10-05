---
name: wiki-lint
description: Health-check the wiki (wiki/) - broken links, bad citations, orphans, unflagged contradictions, missing pages - fix what can be fixed, and list gaps as candidate search lines. Use when asked to lint, check or tidy the wiki, or at the start of a week.
allowed-tools: Bash(python .claude/scripts/wiki.py:*), Read, Write, Edit, Glob, Grep
---

# Wiki lint

Read `context.md`, then `wiki/SCHEMA.md`.

1. Run `python .claude/scripts/wiki.py refresh`, then `python .claude/scripts/wiki.py lint`. Fix every ERROR. Fix each warning, or say why it stands.
2. Then read for what the script cannot see:
   - claims on different pages that disagree but carry no `[!contradiction]` flag;
   - a newer claim that overtakes an older one (later year, same measure);
   - a topic or organisation named on three or more pages without its own page;
   - pages that should link to each other and do not;
   - an `overview.md` that no longer matches the topic pages.
3. Gaps: for each topic, what the reader (context.md §1) would need that no claim covers. Write each as a candidate search line: `<line code from /find-sources> - <what to look for> - <why>`. Do not search.
4. Run `wiki.py lint` again until 0 errors, then `wiki.py log lint "<date> pass" "<what was fixed; gaps listed>"`.

Report: what you fixed, open warnings, and the candidate search lines.
