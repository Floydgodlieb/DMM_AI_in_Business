#!/usr/bin/env bash
# Two link rules, both guarding against rot that nothing else would notice.
#
# 1. Publication gate — every relative link in site/ must resolve INSIDE site/.
#    This is what stops a draft still living in work/ from being linked into the
#    public handbook. A link that escapes via ../ counts as escaping: it would
#    404 on Pages, because nothing outside site/ is ever uploaded.
#
# 2. Repo docs — every relative link in README.md, CLAUDE.md and work/ must
#    point at something that exists. These files describe the repo to whoever
#    picks it up next, and they go stale the moment a file is moved.
#
# Run it before you push.
set -uo pipefail

fail=0
err() { echo "::error file=$1::$2"; fail=1; }

# Collapse . and .. textually. The target need not exist — that is the thing
# being tested — so this cannot go through realpath.
norm() {
  printf '%s\n' "$1" | awk -F/ '{
    n = 0
    for (i = 1; i <= NF; i++) {
      if ($i == "" || $i == ".") continue
      if ($i == "..") { if (n > 0) n--; continue }
      st[++n] = $i
    }
    s = ""
    for (i = 1; i <= n; i++) s = s (i > 1 ? "/" : "") st[i]
    print s
  }'
}

# Relative link targets in a file: markdown [](target "title") and html href/src.
targets() {
  {
    grep -oE '\]\([^)]*\)' "$1" | sed -E 's/^\]\(//; s/\)$//; s/[[:space:]]+"[^"]*"$//'
    grep -oE '(href|src)="[^"]*"' "$1" | sed -E 's/^(href|src)="//; s/"$//'
  } 2>/dev/null \
    | grep -vE '^(https?:|mailto:|data:|tel:|javascript:|#|//)' \
    | sed -E 's/[#?].*$//' \
    | grep -v '^$' \
    | sort -u
}

# --- 1. Publication gate ----------------------------------------------------

while IFS= read -r page; do
  while IFS= read -r t; do
    case "$t" in
      /*) resolved="site$t" ;;                    # site-root-relative
      *)  resolved="$(dirname "$page")/$t" ;;
    esac
    n=$(norm "$resolved")

    if [ ! -e "$n" ]; then
      err "$page" "broken link -> $t (not found in site/)"
    else
      case "$n" in
        site|site/*) ;;
        *) err "$page" "link leaves site/ -> $t (resolves to $n, which is never published)" ;;
      esac
    fi
  done < <(targets "$page")
done < <(find site -type f \( -name '*.html' -o -name '*.md' \) 2>/dev/null | sort)

# --- 2. Repo docs -----------------------------------------------------------

while IFS= read -r doc; do
  [ -f "$doc" ] || continue
  while IFS= read -r t; do
    n=$(norm "$(dirname "$doc")/$t")
    [ -e "$n" ] || err "$doc" "broken link -> $t"
  done < <(targets "$doc")
done < <({ ls README.md CLAUDE.md 2>/dev/null
           find work -name '*.md' 2>/dev/null; } | sort -u)

# ----------------------------------------------------------------------------

if [ "$fail" -eq 0 ]; then
  echo "All relative links resolve: site/ stays inside site/, and the repo docs point at real files."
fi
exit $fail
