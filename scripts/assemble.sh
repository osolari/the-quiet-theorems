#!/usr/bin/env bash
# Assemble a self-contained, Overleaf-ready tree for one post:
#   skeleton/ (template + series layer) + STANDARD.md + docs/posts/<post>/
# Usage: scripts/assemble.sh <post-dir-name> [out-dir]
#   e.g. scripts/assemble.sh 01-debruijn  ->  build/01-debruijn/
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
post="${1:?usage: assemble.sh <post> [out]}"
src="$root/docs/posts/$post"
out="${2:-$root/build/$post}"
[ -d "$src" ] || { echo "no such post: $src" >&2; exit 1; }
rm -rf "$out"; mkdir -p "$out"
# skeleton, minus the new-post starter
( cd "$root/skeleton" && tar cf - --exclude=./new-post . ) | ( cd "$out" && tar xf - )
mv "$out/TEMPLATE_README.md" "$out/README.md"
cp "$root/STANDARD.md" "$out/STANDARD.md"
# post-specific files
cp "$src/main.tex" "$src/project.tex" "$src/post.txt" "$src/tweet.txt" "$out/"
mkdir -p "$out/code" "$out/pdf" "$out/shared/bibliography"
cp "$src/code/check.py" "$out/code/"
cp "$src/references.bib" "$out/shared/bibliography/references.bib"
[ -d "$src/pdf" ] && cp "$src/pdf/"*.pdf "$out/pdf/" 2>/dev/null || true
[ -d "$src/figures" ] && cp -r "$src/figures" "$out/figures" || true
echo "$out"
