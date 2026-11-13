"""Build and execute docs/posts/<post>/notebook.ipynb.

Sources (nothing is written by hand in the notebook):
  article.md       title block, TL;DR, Result, Numerical check table
  code/check.py    split into cells at top-level "# N. ..." comments
  code/figures.py  optional; run last, in the same namespace
Usage: python3 scripts/make_notebook.py <post>
(run after scripts/tex2md.py, which writes article.md).
"""
import re
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

root = Path(__file__).resolve().parent.parent
post = sys.argv[1]
pdir = root / "docs" / "posts" / post
md = (pdir / "article.md").read_text()


def section(name):
    m = re.search(r"^## %s\n(.*?)(?=^## |\Z)" % re.escape(name), md, re.S | re.M)
    return m.group(1).strip() if m else ""


head = md.split("\n## ", 1)[0]
title_block = head.split("\n> ", 1)[0].strip()
title_block = title_block.replace("(pdf/", "(pdf/").replace("[Notebook](notebook.ipynb) · ", "")
title_block = title_block.replace("[LaTeX source](main.tex)", "[Article](article.md) · [LaTeX source](main.tex)")
tldr = "\n".join(l for l in head.splitlines() if l.startswith(">"))
result = section("Result")
check = section("Numerical check").split("**Code.**", 1)[0].strip()

cells = [nbformat.v4.new_markdown_cell(title_block + "\n\n" + tldr),
         nbformat.v4.new_markdown_cell("## Result\n\n" + result),
         nbformat.v4.new_markdown_cell(
             "## Numerical check\n\nThe cells below are `code/check.py`, split at its "
             "numbered sections; together they print every number in this table.\n\n" + check)]

src = (pdir / "code" / "check.py").read_text()
parts = re.split(r"(?m)^(?=# \d+(?:-\d+)?\. )", src)
cells.append(nbformat.v4.new_markdown_cell("### Setup"))
cells.append(nbformat.v4.new_code_cell(parts[0].strip()))
for p in parts[1:]:
    first = p.splitlines()[0]
    heading = re.sub(r"^# ", "", first)
    cont = []
    for line in p.splitlines()[1:]:
        if line.startswith("# ") and not cont:
            heading += " " + line[2:].strip()
        else:
            cont.append(line)
    cells.append(nbformat.v4.new_markdown_cell("### " + heading.strip()))
    cells.append(nbformat.v4.new_code_cell(p.strip()))

fig = pdir / "code" / "figures.py"
if fig.exists():
    cells.append(nbformat.v4.new_markdown_cell(
        "## Figures\n\n`code/figures.py`: matplotlib versions of the PDF's figures."))
    cells.append(nbformat.v4.new_code_cell(fig.read_text().strip()))

nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3",
                             "language": "python"}
nb.metadata["language_info"] = {"name": "python"}
NotebookClient(nb, timeout=900, kernel_name="python3",
               resources={"metadata": {"path": str(pdir / "code")}}).execute()
nbformat.write(nb, pdir / "notebook.ipynb")
print(pdir / "notebook.ipynb")
