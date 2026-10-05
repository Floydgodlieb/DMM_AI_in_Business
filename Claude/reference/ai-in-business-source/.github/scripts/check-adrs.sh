#!/usr/bin/env bash
# Keep the decision records in work/decisions/ trustworthy.
#
# Two jobs. The lint checks that every record is numbered, structured and
# cross-referenced correctly. The immutability check — which only runs when
# BASE_SHA is set — refuses a change to a record that was already accepted.
# That second one is the point: a record you can quietly rewrite is not a
# decision record, it is a document. Change your mind by superseding.
#
#   ./.github/scripts/check-adrs.sh                    # lint only
#   BASE_SHA=HEAD~1 ./.github/scripts/check-adrs.sh    # lint + immutability
set -uo pipefail

DIR="work/decisions"
fail=0

err() { echo "::error file=$1::$2"; fail=1; }

# The status is the single non-empty, non-comment line under "## Status".
status_of() {
  awk '
    /^## Status[[:space:]]*$/ { s = 1; next }
    /^## /                    { s = 0 }
    s && /^<!--/              { c = 1 }
    s && c                    { if (/-->/) c = 0; next }
    s && NF                   { print }
  '
}

# The record with its whole Status section removed, for comparing everything
# that must not have changed.
strip_status() {
  awk '
    /^## Status[[:space:]]*$/ { s = 1; next }
    /^## /                    { s = 0 }
    !s                        { print }
  '
}

valid_status() {
  case "$1" in
    Proposed|Accepted|Rejected)                            return 0 ;;
    "Superseded by ADR-"[0-9][0-9][0-9][0-9])              return 0 ;;
    *)                                                     return 1 ;;
  esac
}

if [ ! -d "$DIR" ]; then
  echo "No $DIR/ — nothing to check."
  exit 0
fi

list=$(mktemp)
trap 'rm -f "$list"' EXIT
find "$DIR" -maxdepth 1 -name '[0-9][0-9][0-9][0-9]-*.md' | sort > "$list"
total=$(grep -c . "$list" || true)

if [ "$total" -eq 0 ]; then
  echo "No decision records in $DIR/ yet."
  exit 0
fi

# --- Lint -------------------------------------------------------------------

# Nothing unnumbered pretending to be a record.
while IFS= read -r stray; do
  case "$(basename "$stray")" in
    README.md|template.md|[0-9][0-9][0-9][0-9]-*.md) ;;
    *) err "$stray" "not a decision record — name it NNNN-kebab-slug.md or move it out of $DIR/" ;;
  esac
done < <(find "$DIR" -maxdepth 1 -name '*.md')

expected=1
while IFS= read -r f; do
  base=$(basename "$f")

  if ! [[ "$base" =~ ^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$ ]]; then
    err "$f" "filename must be NNNN-kebab-slug.md"
    expected=$((expected + 1))
    continue
  fi

  num="${base:0:4}"

  if [ "$num" != "$(printf '%04d' "$expected")" ]; then
    err "$f" "expected ADR-$(printf '%04d' "$expected") — numbers must be unique and run consecutively from 0001"
  fi
  expected=$((expected + 1))

  # Line 1 titles the record and agrees with the filename.
  if ! head -n 1 "$f" | grep -qE "^# ADR-$num: .+"; then
    err "$f" "line 1 must be '# ADR-$num: <title>'"
  fi

  for section in "## Status" "## Context" "## Options considered" "## Decision" "## Consequences"; do
    if ! grep -qxF "$section" "$f"; then
      err "$f" "missing required section '$section'"
    fi
  done

  status_lines=$(status_of < "$f")
  count=$(printf '%s' "$status_lines" | grep -c . || true)
  if [ "$count" -ne 1 ]; then
    err "$f" "the Status section must hold exactly one status line, found $count"
  elif ! valid_status "$status_lines"; then
    err "$f" "invalid status '$status_lines' — use Proposed, Accepted, Rejected, or 'Superseded by ADR-NNNN'"
  fi

  # Exactly one link to this record from the index.
  if [ -f "$DIR/README.md" ]; then
    links=$(grep -cF "]($base)" "$DIR/README.md" || true)
    if [ "$links" -ne 1 ]; then
      err "$DIR/README.md" "must link to $base exactly once, found $links"
    fi
  fi
done < "$list"

if [ ! -f "$DIR/README.md" ]; then
  err "$DIR" "missing README.md — the index of records"
fi

# Every ADR-NNNN mentioned anywhere resolves to a record that exists.
while IFS= read -r f; do
  for ref in $(grep -oE 'ADR-[0-9]{4}' "$f" | sort -u); do
    if ! ls "$DIR/${ref#ADR-}"-*.md >/dev/null 2>&1; then
      err "$f" "reference to $ref, which does not exist"
    fi
  done
done < <(find "$DIR" -maxdepth 1 -name '*.md')

# Every relative markdown link in the index points at something real.
if [ -f "$DIR/README.md" ]; then
  while IFS= read -r target; do
    [ -e "$DIR/$target" ] || err "$DIR/README.md" "broken link -> $target"
  done < <(grep -oE '\]\([^)]+\.md\)' "$DIR/README.md" \
           | sed -E 's/^\]\(//; s/\)$//' \
           | grep -vE '^(https?:|//)' | sort -u)
fi

# --- Immutability -----------------------------------------------------------

if [ -n "${BASE_SHA:-}" ] && [ "$BASE_SHA" != "0000000000000000000000000000000000000000" ] \
   && git cat-file -e "$BASE_SHA^{commit}" 2>/dev/null; then

  while IFS= read -r f; do
    [ -n "$f" ] || continue

    # New record — nothing to protect yet.
    git cat-file -e "$BASE_SHA:$f" 2>/dev/null || continue

    old_status=$(git show "$BASE_SHA:$f" | status_of)

    if [ ! -f "$f" ]; then
      case "$old_status" in
        Proposed) ;;
        *) err "$f" "deleting a record with status '$old_status' is not allowed — supersede it instead" ;;
      esac
      continue
    fi

    new_status=$(status_of < "$f")

    case "$old_status" in
      Proposed)
        ;;  # a proposal may still grow
      Accepted)
        if ! [[ "$new_status" =~ ^Superseded\ by\ ADR-[0-9]{4}$ ]]; then
          err "$f" "this record is Accepted — the only change it may still receive is its status becoming 'Superseded by ADR-NNNN' (found '$new_status')"
        elif ! diff -q <(git show "$BASE_SHA:$f" | strip_status) <(strip_status < "$f") >/dev/null; then
          err "$f" "this record is Accepted — when superseding it, change the status line and nothing else"
        fi
        ;;
      *)
        if ! diff -q <(git show "$BASE_SHA:$f") "$f" >/dev/null; then
          err "$f" "this record is '$old_status' and is closed — write a new record instead"
        fi
        ;;
    esac
  done < <(git diff --name-only "$BASE_SHA" -- "$DIR" | grep -E '/[0-9]{4}-[^/]+\.md$' || true)
fi

# ----------------------------------------------------------------------------

if [ "$fail" -eq 0 ]; then
  echo "$total decision records: numbering, structure, status and cross-references all check out."
fi
exit $fail
