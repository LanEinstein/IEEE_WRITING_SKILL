#!/usr/bin/env bash
# (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite.
# Measure only; venue bounds are explicit options, never a universal default.
# Usage: wordcount_abstract.sh [--plain] <file> [--min N] [--max N]
set -u
command -v python3 >/dev/null 2>&1 || { echo "ERROR: python3 not found" >&2; exit 2; }
exec python3 - "$@" <<'PYCOUNT'
import argparse
from pathlib import Path
import re
import sys
parser = argparse.ArgumentParser(description="Measure an abstract; apply only explicitly supplied word limits.")
parser.add_argument("file")
parser.add_argument("--plain", action="store_true", help="Input contains only the plain-text abstract")
parser.add_argument("--min", type=int, dest="minimum")
parser.add_argument("--max", type=int, dest="maximum")
args = parser.parse_args()
if (args.minimum is not None and args.minimum < 0) or (args.maximum is not None and args.maximum < 1):
    parser.error("word limits must be nonnegative (maximum must be positive)")
if args.minimum is not None and args.maximum is not None and args.minimum > args.maximum:
    parser.error("minimum exceeds maximum")
try:
    source = Path(args.file).read_text(encoding="utf-8")
except (OSError, UnicodeError) as exc:
    print(f"ERROR: cannot read input: {exc}", file=sys.stderr)
    sys.exit(2)
if args.plain:
    abstract = source
else:
    # Unescaped percent starts a TeX comment; preserve escaped percent.
    source = re.sub(r"((?:^|[^\\])(?:\\\\)*)%[^\n]*", r"\1", source, flags=re.M)
    matches = re.findall(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", source, re.S)
    if len(matches) != 1:
        print(f"ERROR: expected one abstract environment, found {len(matches)}", file=sys.stderr)
        sys.exit(1)
    abstract = matches[0]
    abstract = abstract.replace(r"\%", "%").replace(r"\&", "&").replace(r"\_", "_")
    abstract = re.sub(r"\\[a-zA-Z@]+\*?", "", abstract)
    abstract = abstract.replace("{", "").replace("}", "").replace("~", " ")
count = len(abstract.split())
if not count:
    print("ERROR: abstract is empty", file=sys.stderr)
    sys.exit(1)
print(f"abstract-words: {count}")
print("count-method: whitespace tokens (plain text or source with comments/commands stripped; macros not expanded)")
if args.minimum is None and args.maximum is None:
    print("GATE: NOT_APPLIED (no target-specific limits supplied)")
else:
    passed = (args.minimum is None or count >= args.minimum) and (args.maximum is None or count <= args.maximum)
    limits = f"minimum={args.minimum if args.minimum is not None else 'none'}, maximum={args.maximum if args.maximum is not None else 'none'}"
    print(f"GATE: {'PASS' if passed else 'FAIL'} ({limits})")
    if not passed:
        sys.exit(1)
PYCOUNT
