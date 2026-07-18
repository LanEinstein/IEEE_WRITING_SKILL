#!/usr/bin/env bash
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
# Installer. Idempotent.
#   ./install.sh            # Claude Code (symlinks into ~/.claude/skills/)
#   ./install.sh --codex    # Codex CLI (prompts + AGENTS snippet, path-filled)
#   ./install.sh --all      # both
set -u

ROOT=$(dirname "$(readlink -f "$0")")
TARGET="${1:---claude}"

install_claude() {
  local dest="$HOME/.claude/skills"
  mkdir -p "$dest"
  local name
  for name in ieee-write ieee-polish ieee-review; do
    ln -sfn "$ROOT/skills/$name" "$dest/$name"
    echo "linked: $dest/$name -> $ROOT/skills/$name"
  done
  echo "NOTE: the links resolve to $ROOT. When editing suite files, edit the"
  echo "      real paths under $ROOT (some editors refuse writes through"
  echo "      symlinks); 'readlink -f' shows the real path."
}

install_codex() {
  local pdir="$HOME/.codex/prompts"
  mkdir -p "$pdir"
  local f base
  for f in "$ROOT"/adapters/codex/prompts/*.md; do
    base=$(basename "$f")
    sed "s|{{IEEE_SKILL_ROOT}}|$ROOT|g" "$f" > "$pdir/$base"
    echo "installed prompt: $pdir/$base"
  done
  mkdir -p "$ROOT/local"
  local snippet="$ROOT/local/AGENTS-snippet.filled.md"
  sed "s|{{IEEE_SKILL_ROOT}}|$ROOT|g" \
    "$ROOT/adapters/codex/AGENTS-snippet.md" > "$snippet"
  echo "AGENTS.md snippet with real paths written to:"
  echo "  $snippet"
  echo "Paste the snippet into your project AGENTS.md or ~/.codex/AGENTS.md."
}

case "$TARGET" in
  --claude) install_claude ;;
  --codex)  install_codex ;;
  --all)    install_claude; install_codex ;;
  *) echo "ERROR: usage: install.sh [--claude|--codex|--all]" >&2; exit 2 ;;
esac
echo "Done."
