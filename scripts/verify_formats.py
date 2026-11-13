"""Check a post's derived formats are complete and consistent.

- article.md exists, every image/link to a local file resolves,
  no unconverted LaTeX (\\cref, \\cite, @@ markers, ?? refs) remains
- notebook.ipynb exists, has outputs, no error outputs, and its
  printed check numbers equal `python3 code/check.py` output
- meta.json has the required keys and a known status
Usage: python3 scripts/verify_formats.py <post>
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import nbformat

root = Path(__file__).resolve().parent.parent
post = sys.argv[1]
p = root / "docs" / "posts" / post
bad = []

md = (p / "article.md").read_text() if (p / "article.md").exists() else ""
if not md:
    bad.append("article.md missing")
for link in re.findall(r"\]\(([^)#]+)\)", md):
    if not link.startswith("http") and not (p / link).exists():
        bad.append(f"article.md: missing target {link}")
for pat in [r"\\cref", r"\\citep?", r"@@", r"\?\?", r"\\label", r"\\ref\{"]:
    if re.search(pat, md):
        bad.append(f"article.md: leftover {pat}")

nbp = p / "notebook.ipynb"
if not nbp.exists():
    bad.append("notebook.ipynb missing")
else:
    nb = nbformat.read(nbp, 4)
    outs = [o for c in nb.cells if c.cell_type == "code" for o in c.outputs]
    if any(o.output_type == "error" for o in outs):
        bad.append("notebook: error output")
    printed = "".join(o.get("text", "") for o in outs
                      if o.output_type == "stream")
    ref = subprocess.run([sys.executable, "check.py"], cwd=p / "code",
                         capture_output=True, text=True).stdout
    if printed.strip() != ref.strip():
        bad.append("notebook: printed numbers differ from check.py")

meta = json.loads((p / "meta.json").read_text())
if meta.get("status") not in ("draft", "accepted", "published"):
    bad.append("meta.json: bad status")
for k in ("issue", "slug", "date", "links"):
    if k not in meta:
        bad.append(f"meta.json: missing {k}")
if meta.get("status") == "published":
    for k in ("x_thread", "x_tweet", "substack", "pages"):
        if not meta["links"].get(k):
            bad.append(f"meta.json: published but links.{k} empty")

print("\n".join(bad) if bad else f"{post}: formats OK")
sys.exit(1 if bad else 0)
