#!/usr/bin/env bash
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
# ./install.sh [--claude|--codex|--all|--check]
# Optional isolated destinations: IEEE_CLAUDE_DIR, IEEE_CODEX_DIR.
# Installs links and adapters; never edits project/global AGENTS files.
set -eu
ROOT=$(dirname "$(readlink -f "$0")")
TARGET="${1:---claude}"
if [ $# -gt 1 ]; then
  echo "ERROR: usage: install.sh [--claude|--codex|--all|--check]" >&2
  exit 2
fi

link_skills() {
  local dest="$1" name target
  mkdir -p "$dest"
  for name in ieee-write ieee-polish ieee-review ieee-style; do
    target="$dest/$name"
    if [ -e "$target" ] && [ ! -L "$target" ]; then
      echo "ERROR: preserving existing non-symlink skill: $target" >&2
      return 1
    fi
    ln -sfn "$ROOT/skills/$name" "$target"
    echo "linked: $target -> $ROOT/skills/$name"
  done
}

install_claude() {
  local base="${IEEE_CLAUDE_DIR:-$HOME/.claude}"
  link_skills "$base/skills"
}

install_codex() {
  local base="${IEEE_CODEX_DIR:-$HOME/.codex}"
  local pdir="$base/prompts" f name tmp target
  link_skills "$base/skills"
  mkdir -p "$pdir"
  for f in "$ROOT"/adapters/codex/prompts/*.md; do
    name=$(basename "$f")
    target="$pdir/$name"
    tmp=$(mktemp)
    # Literal replacement avoids treating special path characters as sed syntax.
    python3 - "$f" "$ROOT" "$tmp" <<'PYPROMPT'
from pathlib import Path
import sys
Path(sys.argv[3]).write_text(Path(sys.argv[1]).read_text().replace('{{IEEE_SKILL_ROOT}}', sys.argv[2]))
PYPROMPT
    if [ -f "$target" ] && ! cmp -s "$tmp" "$target"; then
      mkdir -p "$pdir/.ieee-suite-backups"
      cp -p "$target" "$(mktemp "$pdir/.ieee-suite-backups/$name.XXXXXX")"
    fi
    if [ ! -f "$target" ] || ! cmp -s "$tmp" "$target"; then
      cp "$tmp" "$target"
    fi
    rm -f "$tmp"
    echo "installed prompt: $target"
  done
  mkdir -p "$ROOT/local"
  python3 - "$ROOT" <<'PYSNIPPET'
from pathlib import Path
import sys
root = Path(sys.argv[1])
(root/'local/AGENTS-snippet.filled.md').write_text((root/'adapters/codex/AGENTS-snippet.md').read_text().replace('{{IEEE_SKILL_ROOT}}', str(root)))
PYSNIPPET
  echo "Optional AGENTS snippet: $ROOT/local/AGENTS-snippet.filled.md"
  echo "No AGENTS file was changed. Restart a host session if its skill list is cached."
}

# Self-test: required files, script syntax, every relative Markdown link,
# and a smoke run of the three Python helpers. Exit 1 on any failure.
check() (
  local fail=0 f py tmpdir rc
  tmpdir=$(mktemp -d)
  trap 'rm -rf "$tmpdir"' EXIT
  export PYTHONPYCACHEPREFIX="$tmpdir/cache"
  for f in core/WORKFLOW.md QUICK_REFERENCE.md README.md README.zh-CN.md \
           core/rules/voice-and-positioning.md core/rules/paragraph-architecture.md \
           core/rules/sentence-craft.md core/rules/lexicon.md \
           core/rules/translation-discipline.md core/rules/revising.md \
           core/rules/review-loops.md core/rules/terminology-and-notation.md \
           core/rules/layout-and-build.md core/rules/figure-standards.md \
           core/rules/prose-rules.md core/rules/verification-protocol.md \
           core/checklists/pre-delivery.md core/checklists/polish-round.md \
           core/checklists/submission.md core/templates/proposal-card.md \
           core/templates/paragraph-card.md \
           scripts/prose_lint.py scripts/pronoun_check.py scripts/review_page.py; do
    [ -f "$ROOT/$f" ] || { echo "MISSING: $f"; fail=1; }
  done
  for f in skills/{ieee-write,ieee-polish,ieee-review,ieee-style}/SKILL.md; do
    [ -f "$ROOT/$f" ] || { echo "MISSING: $f"; fail=1; }
  done
  for py in prose_lint pronoun_check review_page; do
    python3 -m py_compile "$ROOT/scripts/$py.py" 2>/dev/null || { echo "SYNTAX: scripts/$py.py"; fail=1; }
  done
  # Relative links in shipped Markdown must resolve.
  python3 - "$ROOT" <<'PYSELF' || fail=1
import re, sys
from pathlib import Path
root = Path(sys.argv[1])
bad = []
skip_dirs = {'.git', '.codebase-memory', 'local', 'paper', '__pycache__'}
for md in root.rglob('*.md'):
    if any(part in skip_dirs for part in md.relative_to(root).parts):
        continue
    text = md.read_text(errors='replace')
    for target in re.findall(r'\]\(([^)#\s]+)(?:#[^)]*)?\)', text):
        if target.startswith(('http://', 'https://', 'mailto:')):
            continue
        if not (md.parent / target).exists():
            bad.append(f"{md.relative_to(root)} -> {target}")
for b in bad:
    print("BROKEN LINK:", b)
sys.exit(1 if bad else 0)
PYSELF
  printf '%s\n' "This shows that it works. Because the folds hold one subject, so we repeat." > "$tmpdir/sample.tex"
  set +e
  python3 "$ROOT/scripts/prose_lint.py" "$tmpdir/sample.tex" --quiet >/dev/null 2>&1
  rc=$?
  set -e
  [ "$rc" -eq 1 ] || { echo "SMOKE: prose_lint did not flag a planted fault (rc=$rc)"; fail=1; }
  set +e
  python3 "$ROOT/scripts/pronoun_check.py" "$tmpdir/sample.tex" --quiet >/dev/null 2>&1
  rc=$?
  set -e
  [ "$rc" -le 1 ] || { echo "SMOKE: pronoun_check failed to run (rc=$rc)"; fail=1; }
  echo '{"items":[]}' > "$tmpdir/round.json"
  python3 "$ROOT/scripts/review_page.py" "$tmpdir/round.json" -o "$tmpdir/page.html" >/dev/null || fail=1
  if [ "$fail" -eq 0 ]; then
    echo "check: OK"
  else
    echo "check: FAILED" >&2
  fi
  return "$fail"
)

case "$TARGET" in
  --claude) install_claude ;;
  --codex) command -v python3 >/dev/null || { echo "ERROR: python3 required for adapters" >&2; exit 2; }; install_codex ;;
  --all) command -v python3 >/dev/null || { echo "ERROR: python3 required for adapters" >&2; exit 2; }; install_claude; install_codex ;;
  --check) command -v python3 >/dev/null || { echo "ERROR: python3 required for --check" >&2; exit 2; }; check ;;
  *) echo "ERROR: usage: install.sh [--claude|--codex|--all|--check]" >&2; exit 2 ;;
esac
echo "Done."
