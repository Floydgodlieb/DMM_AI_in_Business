---
name: translate
description: Stage 3 of the handbook pipeline. Add claims to claims_en.md for use-sources that have none yet, and repair FAIL claims, with verbatim original_nl and an English translation_en. Use when asked to translate, extract claims or update claims_en.md.
---

# Stage 3 — Translate (new and failed only)

Read `context.md` first. Shape: `templates/claims_en.example.md`.

## Steps
1. Run `python .claude/scripts/gates.py todo`. Work only on "use-sources without claims" and "FAIL claims to repair". Existing claims from earlier weeks stay — they are the library's claims, reused by Draft.
2. For each sentence the page could rely on, add one claim block. Next free id with this week's prefix (`W<week>-0xx`, week from `question.md`); never renumber existing claims.
3. `original_nl`: **one** verbatim stretch copied from the source's `excerpt:`, character for character. Use `...` only to drop words inside that stretch. Never join two passages, never add words outside the quotes.
4. Quote the value with double quotes; if the sentence itself contains `"`, use single quotes around the whole value instead.
5. `translation_en`: plain English for the reader in context.md §1. Every number in it must appear in `original_nl`, `location` or the source title.
6. Set `kind`, `evidence`, `scope`, `translated_by: tool`. Leave `verified_by: ""`; do not write `auto_verified`.
7. Repairing a FAIL claim: if only `translation_en`, labels or quoting are wrong, fix those fields. If `original_nl` itself is not verbatim, do **not** edit it: add a new claim with the next free id and a verbatim `original_nl`, and add `superseded_by: <new id>` to the old block. The old claim stays as the record; Draft may no longer cite it.

## Never
- Fill `verified_by`, or touch a block with `translated_by: person`.

## Then
Run `python .claude/scripts/verify_claims.py --write --changed` (only new or changed claims are re-fetched) and report its summary line.
