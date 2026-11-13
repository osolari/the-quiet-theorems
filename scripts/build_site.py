"""Build the GitHub Pages site into site/.

Only posts whose meta.json status is "accepted" or "published" are
included (pass --all to preview drafts locally). Per post:
  site/posts/<post>/index.html   substack/article.md rendered (pandoc + MathJax)
  site/posts/<post>/notebook.html, notebook.ipynb, pdf/, code/, figures
  site/posts/<post>/pn_<NN>_<slug>.zip   Overleaf-ready package
Usage: python3 scripts/build_site.py [--all] [--repo owner/name]
--repo (or $PAGES_REPO) adds GitHub source and Colab links.
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
site = root / "site"
args = sys.argv[1:]
show_all = "--all" in args
repo = os.environ.get("PAGES_REPO", "")
if "--repo" in args:
    repo = args[args.index("--repo") + 1]

CSS = """
:root{--ink:#17131F;--muted:#6F6879;--rule:#D8D3E1;--primary:#32127A;
--panel:#F5F2FA;--blue:#2E5C8A}
body{font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif;
color:var(--ink);max-width:46rem;margin:2.5rem auto;padding:0 1.2rem;
line-height:1.6}
a{color:var(--primary)}h1,h2,h3{color:var(--primary);line-height:1.25}
h1{font-size:2rem;margin-bottom:.2rem}
blockquote{border-left:4px solid var(--primary);background:var(--panel);
margin:1.2rem 0;padding:.6rem 1rem}
table{border-collapse:collapse;margin:1rem 0;font-size:.92rem}
th,td{border-bottom:1px solid var(--rule);padding:.35rem .6rem;text-align:left}
th{color:var(--primary)}img{max-width:100%}
pre{background:#F4F2F8;padding:.8rem;overflow-x:auto;font-size:.85rem}
.eyebrow{text-transform:uppercase;letter-spacing:.08em;color:var(--muted);
font-size:.8rem}.links a{margin-right:1rem}
.card{border:1px solid var(--rule);padding:1rem 1.2rem;margin:1rem 0}
.card h2{margin:.2rem 0}.muted{color:var(--muted)}
footer{margin-top:3rem;color:var(--muted);font-size:.85rem;
border-top:1px solid var(--rule);padding-top:1rem}
"""
FOOT = ("<footer>Probability Notes · Omid Shams Solari, Ph.D. · sAIm Labs"
        "</footer>")


def project_field(tex, name):
    m = re.search(r"\\newcommand\{\\%s\}\{(.*?)\}\s*(%%|\n)" % name, tex)
    return m.group(1).strip() if m else ""


def run(cmd, **kw):
    subprocess.run(cmd, check=True, **kw)


def main():
    if site.exists():
        shutil.rmtree(site)
    (site / "posts").mkdir(parents=True)
    (site / "style.css").write_text(CSS)
    (site / ".nojekyll").write_text("")
    cards = []
    for pdir in sorted((root / "docs" / "posts").glob("[0-9]*")):
        meta = json.loads((pdir / "meta.json").read_text())
        if meta["status"] not in ("accepted", "published") and not show_all:
            continue
        post = pdir.name
        nn, slug = meta["issue"], meta["slug"]
        out = site / "posts" / post
        out.mkdir(parents=True)
        for sub in ("pdf", "code"):
            if (pdir / sub).exists():
                shutil.copytree(pdir / sub, out / sub)
        for f in ("notebook.ipynb", "main.tex"):
            if (pdir / f).exists():
                shutil.copy(pdir / f, out / f)
        for f in (pdir / "substack").iterdir():
            shutil.copy(f, out / f.name)
        # Overleaf-ready package
        run(["make", "-s", "zip", f"P={post}"], cwd=root,
            stdout=subprocess.DEVNULL)
        shutil.copy(root / "dist" / f"pn_{nn}_{slug}.zip", out)
        # notebook as HTML (outputs already stored)
        run(["jupyter", "nbconvert", "--to", "html", "--output",
             "notebook", str(out / "notebook.ipynb")],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # article page
        md = (pdir / "substack" / "article.md").read_text()
        bar = [f"[PDF (A4)](pdf/pn-{nn}-{slug}.pdf)",
               f"[PDF (screen)](pdf/pn-{nn}-{slug}-screen.pdf)",
               "[Notebook](notebook.html)", "[LaTeX source](main.tex)",
               f"[Overleaf package](pn_{nn}_{slug}.zip)"]
        names = {"substack": "Substack", "x_thread": "X thread",
                 "x_tweet": "X post"}
        for k in ("x_tweet", "x_thread", "substack"):
            if meta["links"].get(k):
                bar.insert(0, f"[{names[k]}]({meta['links'][k]})")
        if repo:
            gh = f"https://github.com/{repo}/blob/main/docs/posts/{post}"
            colab = ("https://colab.research.google.com/github/"
                     f"{repo}/blob/main/docs/posts/{post}/notebook.ipynb")
            bar += [f"[Source]({gh})", f"[Open in Colab]({colab})"]
        md = re.sub(r"(?m)^\[PDF attachment:.*$", " · ".join(bar), md,
                    count=1)
        tmp = out / "_article.md"
        tmp.write_text(md)
        title = project_field((pdir / "project.tex").read_text(),
                              "ProjectTitle")
        run(["pandoc", str(tmp), "-f", "gfm+tex_math_dollars", "-t",
             "html5", "-s",
             "--mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js", "--css", "../../style.css",
             "--metadata", f"pagetitle={title} · Probability Notes",
             "-A", "/dev/stdin", "-o", str(out / "index.html")],
            input=(f'<p><a href="../../">All issues</a></p>{FOOT}'),
            text=True)
        tmp.unlink()
        proj = (pdir / "project.tex").read_text()
        sub = project_field(proj, "ProjectSubtitle")
        date = project_field(proj, "ProjectDate")
        tag = "" if meta["status"] != "draft" else " (draft)"
        cards.append(
            f'<div class="card"><div class="eyebrow">No. {nn} · '
            f'{html.escape(date)}{tag}</div><h2><a href="posts/{post}/">'
            f'{html.escape(title)}</a></h2><p>{html.escape(sub)}</p>'
            f'<p class="links"><a href="posts/{post}/">Article</a>'
            f'<a href="posts/{post}/pdf/pn-{nn}-{slug}.pdf">PDF</a>'
            f'<a href="posts/{post}/notebook.html">Notebook</a>'
            f'<a href="posts/{post}/pn_{nn}_{slug}.zip">Overleaf zip</a>'
            f'</p></div>')
    index = (
        '<!doctype html><html lang="en-GB"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Probability Notes</title><link rel="stylesheet" '
        'href="style.css"></head><body><div class="eyebrow">sAIm Labs</div>'
        "<h1>Probability Notes</h1><p class=\"muted\">One result in "
        "probability or statistics a week: the statement, a complete proof, "
        "insights, uses, a worked example and a numerical check.</p>"
        + "".join(reversed(cards)) + FOOT + "</body></html>")
    (site / "index.html").write_text(index)
    print(f"{len(cards)} post(s) -> {site}")


if __name__ == "__main__":
    main()
