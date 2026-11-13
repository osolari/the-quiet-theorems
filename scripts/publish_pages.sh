#!/usr/bin/env bash
# Build the site and commit it to the gh-pages branch (orphan, site files only).
# Usage: scripts/publish_pages.sh [--push]
#   --push   also push gh-pages to origin (needs a GitHub remote)
# Set PAGES_REPO=owner/name for source and Colab links.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
python3 scripts/build_site.py ${PAGES_REPO:+--repo "$PAGES_REPO"}
wt="$(mktemp -d)"
trap 'git worktree remove --force "$wt" >/dev/null 2>&1 || true' EXIT
if git show-ref --verify --quiet refs/heads/gh-pages; then
  git worktree add -q "$wt" gh-pages
else
  git worktree add -q --detach "$wt"
  git -C "$wt" checkout -q --orphan gh-pages
  git -C "$wt" rm -rq --cached . >/dev/null 2>&1 || true
fi
find "$wt" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
cp -R site/. "$wt/"
git -C "$wt" add -A
src="$(git rev-parse --short HEAD)"
if git -C "$wt" diff --cached --quiet; then
  echo "gh-pages already up to date"
else
  git -C "$wt" commit -q -m "Publish site from main@$src"
  echo "committed gh-pages ($src)"
fi
if [ "${1:-}" = "--push" ]; then
  git -C "$wt" push origin gh-pages
fi
