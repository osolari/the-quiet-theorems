# Probability Notes

A weekly post on one result in probability or statistics. Each issue ships as an X thread and a single tweet, a derivation PDF (A4 and screen layouts) with its Overleaf-ready LaTeX source, a Markdown article with embedded figures, an executed Jupyter notebook, and a page on the GitHub Pages site. Every PDF follows one fixed structure: setup and notation, the result, a complete proof, insights, uses, a worked example, a numerical check, and the history of the result.

Author: Omid Shams Solari, Ph.D. (sAIm Labs)

## Links

| What | Where |
|---|---|
| Topic backlog (live, ranked, status dropdowns) | <https://claude.ai/artifact/4i9oRaXXahj9CRiEAvSVUH> |
| Backlog snapshot | [`BACKLOG.md`](BACKLOG.md) |
| Series standard (bundled into every package) | [`STANDARD.md`](STANDARD.md) |
| Claude skill used to build issues | [`skills/probability-notes-issue/SKILL.md`](skills/probability-notes-issue/SKILL.md) |
| How to make a post (full procedure) | [`docs/POST_GUIDE.md`](docs/POST_GUIDE.md) |
| Session handoff notes | [`docs/HANDOFF.md`](docs/HANDOFF.md) |
| Site (GitHub Pages, `gh-pages` branch) | `https://<owner>.github.io/<repo>/` once the remote exists |

## Issues

| No. | Topic | Status | Article | PDF | Notebook |
|---|---|---|---|---|---|
| 00 | Hoeffding's covariance identity | Package accepted 9 Nov 2026 | [article](docs/posts/00-hoeffding/article.md) | [A4](docs/posts/00-hoeffding/pdf/pn-00-hoeffding.pdf), [screen](docs/posts/00-hoeffding/pdf/pn-00-hoeffding-screen.pdf) | [ipynb](docs/posts/00-hoeffding/notebook.ipynb) |
| 01 | De Bruijn's identity | Draft, awaiting approval | [article](docs/posts/01-debruijn/article.md) | [A4](docs/posts/01-debruijn/pdf/pn-01-debruijn.pdf), [screen](docs/posts/01-debruijn/pdf/pn-01-debruijn-screen.pdf) | [ipynb](docs/posts/01-debruijn/notebook.ipynb) |

Published links (X, Substack, Pages) are pinned in each post's `meta.json` and `README.md`.

## Layout

```
skeleton/            SAIM blog template v1.2 + series layer (shared by every post)
  saim-blog.cls  shared/  Makefile  latexmkrc  main-screen.tex  people.tex
  shared/components/math.tex       series notation (appended block)
  shared/components/theorems.tex   theorem system, section skeleton, mainresult box
  new-post/          starter files for a new issue
docs/posts/NN-slug/  one folder per issue: only what is issue-specific
  hand-written: main.tex project.tex references.bib code/check.py code/figures.py
                post.txt tweet.txt meta.json README.md
  generated:    pdf/ img/ article.md notebook.ipynb
docs/POST_GUIDE.md   full procedure, file map, link/status checklist
scripts/assemble.sh  skeleton + STANDARD.md + post -> self-contained Overleaf tree
scripts/figures.py   TikZ figures -> img/figure-N.png
scripts/tex2md.py    main.tex -> article.md (MathJax, numbered results, references)
scripts/make_notebook.py  article.md + code/ -> executed notebook.ipynb
scripts/verify_formats.py checks article links, leftover LaTeX, notebook == check.py, meta.json
scripts/build_site.py     site/ for GitHub Pages (accepted/published posts only)
scripts/publish_pages.sh  commit site/ to the gh-pages branch (--push to push)
scripts/wlen.py      weighted X length checker (limit 280, URL = 23)
.github/workflows/pages.yml  on push to main: build site, deploy to gh-pages
skills/probability-notes-issue/SKILL.md  Claude skill for building posts
```

`scripts/assemble.sh 00-hoeffding` reproduces the accepted `pn_00_hoeffding.zip` file for file, so the skeleton is the single source for all shared files. Never edit the template files in `skeleton/`; the series layer files may only gain new macros (record them in `STANDARD.md`).

## Usage

```sh
make new P=02-sure          # start an issue from skeleton/new-post
make check P=02-sure        # run its numerical check
make qa P=02-sure           # build A4 + screen, zero-warning scan, Type 1 fonts, tweet weights
make pdfs P=02-sure         # copy built PDFs into docs/posts/02-sure/pdf/
make formats P=02-sure      # img/, article.md, notebook.ipynb (executed)
make verify P=02-sure       # article/notebook/meta checks
make zip P=02-sure          # dist/pn_02_sure.zip, Overleaf-ready (set main-screen.tex as main document for the screen layout)
make all                    # qa + verify for every issue
make site                   # site/ preview (SITE_ALL=1 includes drafts)
make pages PUSH=1           # commit site/ to gh-pages and push
```

## Requirements (pinned)

| Tool | Version used for published numbers |
|---|---|
| Python | 3.13 |
| NumPy | 2.5.3 (see `requirements.txt`) |
| SciPy | 1.18.1 (see `requirements.txt`) |
| TeX | TeX Live 2023, pdfTeX 1.40.25, BibTeX, latexmk 4.83 |
| Notebooks and figures | matplotlib 3.11.2, nbformat 5.11.1, nbclient 0.11.0, nbconvert 7.17.2, ipykernel 7.4.0 (see `requirements.txt`) |
| Conversion and site | pandoc 3.1 |
| Tools | `make`, `zip`, `pdffonts`/`pdftoppm` (poppler-utils) |

```sh
python3 -m pip install -r requirements.txt
```

Each `code/check.py` states its own minimum versions in its docstring; the pins above are the versions its printed numbers were produced with.

## GitHub Pages

The site is built from committed artefacts (no TeX needed) and lives only on the `gh-pages` branch.

- Automatic: pushing `main` runs `.github/workflows/pages.yml`, which builds `site/` and force-pushes it to `gh-pages`. In the repository settings set Pages to "Deploy from a branch", `gh-pages`, `/ (root)`.
- Manual: `make pages PUSH=1 PAGES_REPO=<owner>/<repo>`.
- Only posts whose `meta.json` status is `accepted` or `published` are on the site. Note that drafts are still visible in `main` if the repository is public.
