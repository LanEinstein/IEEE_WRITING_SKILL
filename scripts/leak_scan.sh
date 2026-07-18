#!/usr/bin/env bash
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
# Pre-release leak scan. Confirms the shipped tree contains:
#   1. none of the maintainer's private patterns (unpublished manuscript
#      identifiers, machine paths) listed in local/leak-patterns.txt;
#   2. no CJK characters in runtime files (README.zh-CN.md is the sole
#      documentation exception);
#   3. no absolute /home/ paths.
# A missing patterns file or a failed grep makes the run INCOMPLETE, never
# CLEAN. Usage: leak_scan.sh [repo-root]   (default: parent of this script)
set -u

ROOT="${1:-$(dirname "$(dirname "$(readlink -f "$0")")")}"
if [ ! -d "$ROOT" ]; then
  echo "ERROR: repo root '$ROOT' is not a directory" >&2
  exit 2
fi
PATTERNS="$ROOT/local/leak-patterns.txt"
FAIL=0
INCOMPLETE=0

# Shipped tree = everything except .git, local/, per-run outputs, the
# scanner itself, and the Chinese README (documentation-only exception).
GREPX=(--exclude-dir=.git --exclude-dir=local --exclude-dir=paper
       --exclude=leak_scan.sh --exclude=README.zh-CN.md -r -n)

# Optional: local/scan-excludes.txt lists non-shipped filenames (one per
# line) to exclude, e.g. machine-only development documents.
EXCLUDES="$ROOT/local/scan-excludes.txt"
if [ -f "$EXCLUDES" ]; then
  while IFS= read -r ex || [ -n "$ex" ]; do
    case "$ex" in ''|'#'*) continue;; esac
    GREPX+=("--exclude=$ex")
  done < "$EXCLUDES"
fi

# scan <label> <grep-args...> : prints hits, sets FAIL on hits and
# INCOMPLETE on grep errors (exit status > 1).
scan() {
  local label="$1"; shift
  local hits status count
  hits=$(grep "${GREPX[@]}" "$@" "$ROOT" 2>/dev/null)
  status=$?
  if [ "$status" -gt 1 ]; then
    echo "[$label] SCAN ERROR (grep exit $status)"
    INCOMPLETE=1
    return
  fi
  count=$(printf '%s' "$hits" | grep -c .)
  echo "[$label] count: $count"
  if [ "$count" -gt 0 ]; then
    printf '%s\n' "$hits" | head -10 | sed 's/^/    /'
    FAIL=1
  fi
}

echo "== Leak scan: $ROOT =="

if [ -f "$PATTERNS" ]; then
  while IFS= read -r pat || [ -n "$pat" ]; do
    case "$pat" in ''|'#'*) continue;; esac
    scan "PRIVATE '$pat'" -F -- "$pat"
  done < "$PATTERNS"
else
  echo "NOTE: $PATTERNS not found; private-pattern scan NOT RUN"
  INCOMPLETE=1
fi

# READMEs are human-reviewed documentation, never loaded at runtime, and the
# English README legitimately shows the Chinese language-switcher label; both
# stay in the private-pattern and absolute-path scans above.
scan "CJK-in-runtime-files" --exclude=README.md -P '[\p{Han}\p{Hiragana}\p{Katakana}\p{Hangul}]'
scan "absolute-home-paths" -F -- '/home/'

if [ "$INCOMPLETE" -ne 0 ]; then
  echo "RESULT: INCOMPLETE (a required input or scan failed; NOT a clean verdict)"
  exit 2
elif [ "$FAIL" -eq 0 ]; then
  echo "RESULT: CLEAN (all scans zero)"
  exit 0
else
  echo "RESULT: LEAKS FOUND (fix before any release)"
  exit 1
fi
