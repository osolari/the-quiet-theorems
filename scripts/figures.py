"""Rasterise the TikZ figures of a post for its Substack article.

Output: docs/posts/<post>/substack/<slug>-figure.png (one figure) or
<slug>-figure-N.png (several), N = order of appearance.

Only tikzpictures inside figure environments are rendered, in order of
appearance (matching the PDF's figure numbers), with the post's own class,
colours and macros. Usage: python3 scripts/figures.py <post>
(run after `make build P=<post>`).
"""
import re
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
post = sys.argv[1]
b = root / "build" / post
out = root / "docs" / "posts" / post / "substack"
slug = post.split("-", 1)[1]
import json
meta = json.loads((root / "docs" / "posts" / post / "meta.json").read_text())
if meta.get("substack", {}).get("frozen") and "--force" not in sys.argv:
    print(f"skip: {post} Substack figures are frozen (published)")
    sys.exit(0)
tex = (b / "main.tex").read_text()
pre = tex.split("\\begin{document}", 1)[0]
figs = re.findall(r"\\begin\{figure\}.*?\\end\{figure\}", tex, re.S)
pics = []
for f in figs:
    pics += re.findall(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", f, re.S)
if not pics:
    print("no figures")
    sys.exit(0)
pre = re.sub(r"(?m)^%.*\n", "", pre)
pre = re.sub(r"(?m)^\\documentclass(\[[^\]]*\])?\{saim-blog\}",
             "\\\\RequirePackage[active,tightpage]{preview}\n"
             "\\\\documentclass{saim-blog}\n"
             "\\\\AtBeginDocument{\\\\PreviewEnvironment{tikzpicture}}\n"
             "\\\\setlength\\\\PreviewBorder{6pt}", pre)
drv = pre + "\\begin{document}\n" + "\n\n".join(pics) + "\n\\end{document}\n"
(b / "figures-driver.tex").write_text(drv)
fb = b / "figbuild"
fb.mkdir(exist_ok=True)
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory=figbuild", "figures-driver.tex"],
                   cwd=b, capture_output=True, text=True)
if r.returncode:
    sys.exit(f"figure build failed: see {fb}/figures-driver.log")
out.mkdir(parents=True, exist_ok=True)
for i in range(1, len(pics) + 1):
    subprocess.run(["pdftoppm", "-r", "220", "-png", "-singlefile",
                    "-f", str(i), "-l", str(i),
                    str(fb / "figures-driver.pdf"),
                    str(out / (f"{slug}-figure" if len(pics) == 1 else f"{slug}-figure-{i}"))],
                   check=True)
print(f"{len(pics)} figure(s) -> {out}")
