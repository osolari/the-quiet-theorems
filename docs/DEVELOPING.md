# The Quiet Theorems: developer guide

How the series is built: repository layout, commands, pinned toolchain and the GitHub Pages pipeline. Readers want [`../README.md`](../README.md); the step-by-step procedure for a post is [`POST_GUIDE.md`](POST_GUIDE.md).

## Start here

1. Clone: `git clone git@github-personal:osolari/the-quiet-theorems.git` (the `github-personal` SSH host alias)
2. Read [`docs/POST_GUIDE.md`](POST_GUIDE.md) (full procedure, file map, Substack style, link checklist) and [`STANDARD.md`](../STANDARD.md) (PDF standard).
3. For Claude: load the `quiet-theorems-post` skill (copy in [`skills/quiet-theorems-post/SKILL.md`](../skills/quiet-theorems-post/SKILL.md)). Status lives in this file (Posts table), `BACKLOG.md` and each post's `meta.json`; no handoff package is needed.

## Links

| What | Where |
|---|---|
| Repository | <https://github.com/osolari/the-quiet-theorems> |
| Site (GitHub Pages, `gh-pages` branch) | <https://osolari.github.io/the-quiet-theorems/> |
| Substack publication | <https://omidsolari.substack.com> |
| Backlog snapshot | [`BACKLOG.md`](../BACKLOG.md) |
| Series standard (bundled into every package) | [`STANDARD.md`](../STANDARD.md) |
| How to make a post | [`docs/POST_GUIDE.md`](POST_GUIDE.md) |

## Posts (status of every post, drafts included)

| No. | Topic | Status | Substack article | PDF | Notebook |
|---|---|---|---|---|---|
| 00 | Hoeffding's covariance identity | Published 9 Nov 2026 as *Probability Notes* No. 00 ([Substack](https://omidsolari.substack.com/p/probability-notes-no-00-hoeffdings)); revised edition (The Quiet Theorems, proofs expanded) awaiting approval, 18 Nov 2026 | [article](posts/00-hoeffding/substack/article.md) | [A4](posts/00-hoeffding/pdf/qt-00-hoeffding.pdf), [screen](posts/00-hoeffding/pdf/qt-00-hoeffding-screen.pdf) | [ipynb](posts/00-hoeffding/notebook.ipynb) |
| 01 | De Bruijn's identity | Published 18 Nov 2026 ([Substack](https://omidsolari.substack.com/p/the-quiet-theorems-no-01-de-bruijns)) | [article](posts/01-debruijn/substack/article.md) | [A4](posts/01-debruijn/pdf/qt-01-debruijn.pdf), [screen](posts/01-debruijn/pdf/qt-01-debruijn-screen.pdf) | [ipynb](posts/01-debruijn/notebook.ipynb) |

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
                post.txt meta.json README.md
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
scripts/wlen.py      X post checker (link on line 1, lead <= 280, total <= 25,000, plot present; URL = 23)
.github/workflows/pages.yml  on push to main: build site, deploy to gh-pages
skills/quiet-theorems-post/SKILL.md  Claude skill for building posts
```

File names use the prefix `qt` (`qt-01-debruijn.pdf`, `qt-01-debruijn.zip`); No. 00 keeps its published prefix `pn`. Never edit the template files in `skeleton/`; the series layer files may only gain new macros (record them in `STANDARD.md`).

## Usage

```sh
make new P=02-sure          # start a post from skeleton/new-post
make check P=02-sure        # run its numerical check
make qa P=02-sure           # build A4 + screen, zero-warning scan, Type 1 fonts, X post checks
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
- Before approval a post session previews the post's page with `make site SITE_ALL=1` (drafts included, local only); the deployed site never shows drafts.
- Only posts whose `meta.json` status is `accepted` or `published` are on the site; each page renders the post's `substack/article.md` with links to the PDFs, notebook, LaTeX source and the Substack and X posts; the index links the Substack publication. The Overleaf zip is not on the site (build it with `make zip`). Drafts are still visible on `main` if the repository is public.
