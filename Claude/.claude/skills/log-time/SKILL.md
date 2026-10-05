---
name: log-time
description: Append one row to timelog.csv for a pipeline stage. Use when a person says they started or finished a stage, or asks to log time.
argument-hint: "<person> <stage 1-6> <start-end, e.g. 13:55-14:16> <tool|hand|both> [note]"
---

# Log time

Append exactly one line to `timelog.csv`, matching its header:
`date,person,stage,minutes,done_by (tool|hand|both),note`

- date: today as DD-MM-YYYY (the format already in the file).
- minutes: the time range as given (e.g. `13:55-14:16`), as the existing rows do.
- note: free text; wrap in double quotes if it contains a comma. Record checks done by hand from `review_queue.md` as `note: person-checked S-0xx, S-0yy`.
- If any field is missing from `$ARGUMENTS`, ask for it. Never guess a person or a time.

Do not edit or reorder existing rows.
