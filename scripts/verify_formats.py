"""Check a post's derived formats are complete and consistent.

- substack/article.md exists, every image/link to a local file resolves
  (relative to substack/), no unconverted LaTeX (\\cref, \\cite, @@
  markers, ?? refs) remains, the PDF-attachment line is present, and the
  Output block equals `python3 code/check.py`
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

art = p / "substack" / "article.md"
md = art.read_text() if art.exists() else ""
if not md:
    bad.append("substack/article.md missing")
for link in re.findall(r"\]\(([^)#\s]+)\)", md):
    if not link.startswith("http") and not (art.parent / link).exists():
        bad.append(f"article.md: missing target {link}")
if md and "[PDF attachment:" not in md:
    bad.append("article.md: PDF attachment line missing")
m = re.search(r"\*\*Output:\*\*\s*```\n(.*?)```", md, re.S)
ref_out = subprocess.run([sys.executable, "check.py"], cwd=p / "code",
                         capture_output=True, text=True).stdout
if md and (not m or m.group(1).strip() != ref_out.strip()):
    bad.append("article.md: Output block differs from check.py")
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
    if printed.strip() != ref_out.strip():
        bad.append("notebook: printed numbers differ from check.py")

meta = json.loads((p / "meta.json").read_text())
if meta.get("status") not in ("draft", "accepted", "published"):
    bad.append("meta.json: bad status")
for k in ("issue", "slug", "date", "links"):
    if k not in meta:
        bad.append(f"meta.json: missing {k}")
sub = meta.get("substack", {})
if meta.get("status") == "published":
    if not meta["links"].get("substack") or not sub.get("url"):
        bad.append("meta.json: published but no Substack URL")
    if not sub.get("frozen"):
        bad.append("meta.json: published but substack.frozen is false")
    for img in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", md):
        if not img.startswith("http") and img not in sub.get("images", {}):
            bad.append(f"meta.json: no Substack URL recorded for {img}")
    if not meta["links"].get("x_post"):
        print("note: links.x_post empty (X not yet posted)")

print("\n".join(bad) if bad else f"{post}: formats OK")
sys.exit(1 if bad else 0)
