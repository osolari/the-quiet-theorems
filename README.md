# Probability Notes

A weekly post on one result in probability or statistics. Each issue is an X thread, a single tweet and a derivation PDF (A4 and screen layouts). Every PDF follows one fixed structure: setup and notation, the result, a complete proof, insights, uses, a worked example, a numerical check, and the history of the result.

Author: Omid Shams Solari, Ph.D. (sAIm Labs)

## Links

| What | Where |
|---|---|
| Topic backlog (live, ranked, status dropdowns) | <https://claude.ai/artifact/4i9oRaXXahj9CRiEAvSVUH> |
| Backlog snapshot | [`BACKLOG.md`](BACKLOG.md) |
| Series standard (bundled into every package) | [`STANDARD.md`](STANDARD.md) |
| Claude skill used to build issues | [`skills/probability-notes-issue/SKILL.md`](skills/probability-notes-issue/SKILL.md) |
| Session handoff notes | [`docs/HANDOFF.md`](docs/HANDOFF.md) |

## Issues

| No. | Topic | Status | Post folder | PDF |
|---|---|---|---|---|
| 00 | Hoeffding's covariance identity | Package accepted 9 Nov 2026 | [`docs/posts/00-hoeffding`](docs/posts/00-hoeffding) | [A4](docs/posts/00-hoeffding/pdf/pn-00-hoeffding.pdf), [screen](docs/posts/00-hoeffding/pdf/pn-00-hoeffding-screen.pdf) |
| 01 | De Bruijn's identity | Draft, awaiting approval | [`docs/posts/01-debruijn`](docs/posts/01-debruijn) | [A4](docs/posts/01-debruijn/pdf/pn-01-debruijn.pdf), [screen](docs/posts/01-debruijn/pdf/pn-01-debruijn-screen.pdf) |

Published links (X, Substack) are pinned in each post's `README.md`.

## Layout

```
skeleton/            SAIM blog template v1.2 + series layer (shared by every post)
  saim-blog.cls  shared/  Makefile  latexmkrc  main-screen.tex  people.tex
  shared/components/math.tex       series notation (appended block)
  shared/components/theorems.tex   theorem system, section skeleton, mainresult box
  new-post/          starter files for a new issue
docs/posts/NN-slug/  one folder per issue: only what is issue-specific
  main.tex  project.tex  references.bib  code/check.py  post.txt  tweet.txt  pdf/  README.md
scripts/assemble.sh  skeleton + STANDARD.md + post -> self-contained Overleaf tree
scripts/wlen.py      weighted X length checker (limit 280, URL = 23)
```

`scripts/assemble.sh 00-hoeffding` reproduces the accepted `pn_00_hoeffding.zip` file for file, so the skeleton is the single source for all shared files. Never edit the template files in `skeleton/`; the series layer files may only gain new macros (record them in `STANDARD.md`).

## Usage

```sh
make new P=02-sure          # start an issue from skeleton/new-post
make check P=02-sure        # run its numerical check
make qa P=02-sure           # build A4 + screen, zero-warning scan, Type 1 fonts, tweet weights
make pdfs P=02-sure         # copy built PDFs into docs/posts/02-sure/pdf/
make zip P=02-sure          # dist/pn_02_sure.zip, Overleaf-ready (set main-screen.tex as main document for the screen layout)
make all                    # qa for every issue
```

## Requirements (pinned)

| Tool | Version used for published numbers |
|---|---|
| Python | 3.13 |
| NumPy | 2.5.3 (see `requirements.txt`) |
| SciPy | 1.18.1 (see `requirements.txt`) |
| TeX | TeX Live 2023, pdfTeX 1.40.25, BibTeX, latexmk 4.83 |
| Tools | `make`, `zip`, `pdffonts` (poppler-utils) |

```sh
python3 -m pip install -r requirements.txt
```

Each `code/check.py` states its own minimum versions in its docstring; the pins above are the versions its printed numbers were produced with.
