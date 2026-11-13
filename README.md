# The Quiet Theorems

*Theorems from probability, statistics and machine learning that deserve to be better known: one a week, stated with minimal conditions, proved in full, and checked in code.*

Each post takes one result (a classical identity, an inequality, a characterisation, or a theorem behind a modern machine-learning method) and gives the precise statement, a complete proof with every interchange of limits justified, what it means, what follows from it, a worked example and a numerical check. It ships as a Substack post with the PDF attached, an X thread and a single post linking to it, a derivation PDF (A4 and screen layouts) with its Overleaf-ready LaTeX source, an executed Jupyter notebook, and a page on the GitHub Pages site. The posts are written to be collected into a book of the same name.

Author: Omid Shams Solari, Ph.D. (sAIm Labs). The series was called *Probability Notes* until 13 Nov 2026; No. 00 was published under that name and is kept as published.

## Start here

1. Clone: `git clone git@github-personal:osolari/the-quiet-theorems.git` (the `github-personal` SSH host alias; commits as `osolari <solari@berkeley.edu>`)
2. Read [`docs/POST_GUIDE.md`](docs/POST_GUIDE.md) (full procedure, file map, Substack style, link checklist) and [`STANDARD.md`](STANDARD.md) (PDF standard).
3. For Claude: load the `quiet-theorems-post` skill (copy in [`skills/quiet-theorems-post/SKILL.md`](skills/quiet-theorems-post/SKILL.md)). Status lives in this README, `BACKLOG.md` and each post's `meta.json`; no handoff package is needed.

## Links

| What | Where |
|---|---|
| Repository | <https://github.com/osolari/the-quiet-theorems> |
| Site (GitHub Pages, `gh-pages` branch) | <https://osolari.github.io/the-quiet-theorems/> |
| Substack publication | <https://omidsolari.substack.com> |
| Topic backlog (live, ranked, status dropdowns) | <https://claude.ai/artifact/4i9oRaXXahj9CRiEAvSVUH> |
| Backlog snapshot | [`BACKLOG.md`](BACKLOG.md) |
| Series standard (bundled into every package) | [`STANDARD.md`](STANDARD.md) |
| How to make a post | [`docs/POST_GUIDE.md`](docs/POST_GUIDE.md) |

## Posts

| No. | Topic | Status | Substack article | PDF | Notebook |
|---|---|---|---|---|---|
| 00 | Hoeffding's covariance identity | Published 9 Nov 2026 as *Probability Notes* No. 00 ([Substack](https://omidsolari.substack.com/p/probability-notes-no-00-hoeffdings)) | [article](docs/posts/00-hoeffding/substack/article.md) | [A4](docs/posts/00-hoeffding/pdf/pn-00-hoeffding.pdf), [screen](docs/posts/00-hoeffding/pdf/pn-00-hoeffding-screen.pdf) | [ipynb](docs/posts/00-hoeffding/notebook.ipynb) |
| 01 | De Bruijn's identity | Draft, awaiting approval | [draft](docs/posts/01-debruijn/substack/article.md) | [A4](docs/posts/01-debruijn/pdf/qt-01-debruijn.pdf), [screen](docs/posts/01-debruijn/pdf/qt-01-debruijn-screen.pdf) | [ipynb](docs/posts/01-debruijn/notebook.ipynb) |

Published links (Substack, X, Pages) and Substack details are pinned in each post's `meta.json` and `README.md`. No. 00 is the reference post.

## Layout

```
skeleton/            SAIM blog template v1.2 + series layer (shared by every post)
  saim-blog.cls  shared/  Makefile  latexmkrc  main-screen.tex  people.tex  .gitignore  figures/
  shared/components/math.tex       series notation (appended block)
  shared/components/theorems.tex   theorem system, section skeleton, mainresult box
  new-post/          starter files for a new post
docs/posts/NN-slug/  one folder per post: only what is post-specific
  hand-written: main.tex project.tex references.bib code/check.py code/figures.py
                post.txt tweet.txt meta.json README.md
  generated:    pdf/ notebook.ipynb
  substack/:    article.md (drafted, hand-finished, frozen on publication) + <slug>-figure.png
  published:    <prefix>-NN-slug.zip (the Overleaf package as published)
docs/POST_GUIDE.md   full procedure, file map, Substack style, link/status checklist
scripts/assemble.sh  skeleton + STANDARD.md + post -> self-contained Overleaf tree
scripts/figures.py   TikZ figures -> substack/<slug>-figure.png
scripts/tex2md.py    main.tex -> substack/article.md draft (Substack house style)
scripts/make_notebook.py  substack/article.md + code/ -> executed notebook.ipynb
scripts/verify_formats.py checks article, Output block, notebook == check.py, meta.json
scripts/build_site.py     site/ for GitHub Pages (accepted/published posts only)
scripts/publish_pages.sh  commit site/ to the gh-pages branch (--push to push)
scripts/wlen.py      weighted X length checker (limit 280, URL = 23)
.github/workflows/pages.yml  on push to main: build site, deploy to gh-pages
skills/quiet-theorems-post/SKILL.md  Claude skill for building posts
```

File names use the prefix `qt` (`qt-01-debruijn.pdf`, `qt-01-debruijn.zip`); No. 00 keeps its published prefix `pn`. Never edit the template files in `skeleton/`; the series layer files may only gain new macros (record them in `STANDARD.md`).

## Usage

```sh
make new P=02-sure          # start a post from skeleton/new-post
make check P=02-sure        # run its numerical check
make qa P=02-sure           # build A4 + screen, zero-warning scan, Type 1 fonts, tweet weights
make pdfs P=02-sure         # copy built PDFs into docs/posts/02-sure/pdf/
make formats P=02-sure      # Substack draft + figure, notebook.ipynb (executed)
make verify P=02-sure       # article/notebook/meta checks
make zip P=02-sure          # dist/qt-02-sure.zip, Overleaf-ready (set main-screen.tex as main document for the screen layout)
make all                    # qa + verify for every post
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
- Manual: `make pages PUSH=1 PAGES_REPO=osolari/the-quiet-theorems`.
- Only posts whose `meta.json` status is `accepted` or `published` are on the site; each page renders the post's `substack/article.md` with links to the PDFs, notebook, LaTeX source and the Substack and X posts; the index links the Substack publication. The Overleaf zip is not on the site (build it with `make zip`). Drafts are still visible on `main` if the repository is public.
