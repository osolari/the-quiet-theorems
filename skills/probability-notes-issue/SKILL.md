---
name: probability-notes-issue
description: Build a complete Probability Notes post (PDF source + A4/screen PDFs, Markdown article, Jupyter notebook, X thread and tweet, Overleaf zip, GitHub Pages) in the probability-notes repo to the accepted No. 00 standard.
---

# Probability Notes: building a full post

Reference: No. 00, Hoeffding's covariance identity (package `pn_00_hoeffding.zip`, accepted 9 Nov 2026). Every post must match it in structure, tone, rigour, formats, packaging and links. British English, no em-dashes, terse.

## 0. Where things are

- **Repo** `probability-notes`: on the author's Mac at `~/workspace/projects/probability-notes`; on GitHub once a remote exists. Read `README.md`, `STANDARD.md` and `docs/POST_GUIDE.md` first; the guide is the step-by-step procedure and wins over this summary on details.
- **Backlog doc** (live, ranked, status dropdowns, draw log): https://claude.ai/artifact/4i9oRaXXahj9CRiEAvSVUH ; snapshot in `BACKLOG.md`. Take the highest-ranked Queued topic unless told otherwise; respect noted dependencies (e.g. SURE needs Stein's lemma).
- **claude.ai Project "prob notes"**: `reference/pn-00-STANDARD.md`, `reference/pn-00-main.tex`, `claude/HANDOFF.md`.
- If the repo is not in the session, ask the user to connect `~/workspace/projects` or attach the latest repo or zip; never rebuild the skeleton from memory.

Repo layout (do not change it):

```
skeleton/                 SAIM blog template v1.2 + series layer, shared by every post
skeleton/new-post/        starter files for `make new`
docs/posts/NN-slug/       ALL issue-specific files
docs/POST_GUIDE.md        full procedure        docs/HANDOFF.md   session handoff
scripts/                  assemble.sh tex2md.py figures.py make_notebook.py verify_formats.py
                          build_site.py publish_pages.sh wlen.py
.github/workflows/pages.yml   builds the site on push to main, deploys to gh-pages
BACKLOG.md README.md STANDARD.md requirements.txt (pinned) Makefile
```

Never edit `skeleton/saim-blog.cls`, `skeleton/shared/brand/*`, other `skeleton/shared/components/*`, `Makefile`/`latexmkrc`/`main-screen.tex`/`people.tex` in the skeleton. `shared/components/math.tex` (appended notation) and `theorems.tex` may only gain macros, never change existing ones; record additions in `STANDARD.md`.

## 1. Per-post files: what goes where

| File | Source | Rule |
|---|---|---|
| `main.tex` | hand | skeleton in section 2 |
| `project.tex` | hand | title = name of the result; subtitle = claim in words; `\ProjectIssue{No. NN}` (two digits); reading time ≈ words excl. code / 230; 4 to 6 substantive subject tags (not "derivations"); date; keywords incl. the result's name. Author bio block, `\ProjectAuthorPostnominal{, Ph.D.}` and empty `\ProjectLinks` untouched |
| `references.bib` | hand | section 3 |
| `code/check.py` | hand | section 4 |
| `code/figures.py` | hand | matplotlib twin of each PDF figure, same order and meaning, palette constants; runs after check.py in the notebook namespace |
| `post.txt`, `tweet.txt` | hand | section 5 |
| `meta.json` | hand | `issue`, `slug`, `status` (draft/accepted/published), `date`, `links` {x_thread, x_tweet, substack, pages} |
| `README.md` | hand | status, file map, published-links table, open points, references |
| `pdf/pn-NN-slug.pdf`, `pdf/pn-NN-slug-screen.pdf` | `make pdfs` | never hand-made |
| `img/figure-N.png` | `make formats` | TikZ pictures inside `figure` environments, in order |
| `article.md` | `make formats` | MathJax maths, embedded `img/`, numbered results, references, code inline |
| `notebook.ipynb` | `make formats` | executed; title, TL;DR, Result, check table, check.py by `# N.` sections, figures |

Never edit generated files: fix the source (or the script, for every post) and regenerate.

## 2. main.tex skeleton (fixed order, none dropped or renamed)

Preamble exactly as `skeleton/new-post/main.tex`. Then:

1. `\maketitle`, then `tldr`: three plain sentences (familiar fact; the result, attributed to originator with year; what it means).
2. `\SecSetup`: probability space, symbol table (`\SAIMTableHead`, booktabs, `\small`), numbered `assumption`s, one sentence noting when a commonly quoted condition is stronger than needed, definitions of words used later.
3. `\SecResult`: one `mainresult` box holding the theorem `[Originator, Year]`; equivalent or variant forms as remarks with one-line proofs.
4. `\SecProof`: lemmas first (with proofs), then `\begin{proof}[Proof of \cref{thm:main}]` in `\step{...}` paragraphs. Every interchange of limit/integral/expectation/derivative gets an `\interchange{...}` paragraph stating the dominating function or Tonelli bound and joint measurability. Spell out product-space constructions and why cross terms factorise. Optional "Alternative route (sketch)." paragraph.
5. `\SecInsight`: `enumerate` of 2 to 4 bold-led items (what it says; comparison; role of the structure; sign or equality cases), then one `pullquote`.
6. `\SecUses`: one opening sentence on how the consequences follow; each consequence a `\subsection` with a precise statement and a proof (state any extra condition).
7. `\SecExample`: one fully explicit computation (prefer a counterexample or extreme case), a table, and a TikZ figure in `figure[tbp]` using palette colours (Primary, Secondary, Warning, Rule, RuleDark, Ink, Muted) with an informative caption, referenced via `\cref`. Only pictures inside `figure` are exported to `img/`.
8. `\SecCheck`: one sentence on the method per row; Case / Exact / Numerical table; exact values not proved in the PDF carry a dagger citing the source and "not proved here"; prefer exact arithmetic to Monte Carlo; end with `\paragraph{Code.}` pointing to `\cref{lst:check}` and `python3 code/check.py`.
9. `\SecNotes`: originator history only: who, when, original title (with translation if not English), what the original contains, how it reached a wide audience. Then `\bibliographystyle{plainnat}` and `\bibliography{shared/bibliography/references}` (no `\nocite` padding).
10. Author card, exactly:
```
{\let\SAIMplainauthors\ProjectAuthorsPlainDisplay
 \renewcommand{\ProjectAuthorsPlainDisplay}{\SAIMplainauthors\ProjectAuthorPostnominal}%
 \postauthorcard}
```
11. `\clearpage\appendix\section{Code}` and
`\lstinputlisting[style=python,basicstyle=\ttfamily\footnotesize\color{Ink},caption={Numerical check (\texttt{code/check.py}).},label={lst:check}]{code/check.py}`.

Conventions: sections unnumbered; refer with `\cref` only, never to sections by number. Label lemmas, corollaries, remarks with their type (`\label[lemma]{...}`; the class loads cleveref before amsthm). `\interchange`, never `\justify` (ragged2e). Notation: capitals for random variables, F_X, F_{X,Y}, \bar F_X, f_X, Z/\varphi/\Phi, copies X_1, X_2, `\E \Prob \Var \Cov \Corr \ind{} \dd \eqd \indep \iid \Normal \Unif \Expo`, `\dd x` at the end of integrals. Display long formulas with `aligned`.

## 3. Names, credit, references

- Prose names only the originators of the post's result. Everyone else is credited by citation where their work is used (`\citet`, `\citep`); side results are named descriptively ("rank correlation", "copula bounds", "association inequality"). Standard tool names (Cauchy–Schwarz, Fubini–Tonelli, Jensen) are fine.
- Unproved facts: `\citep[not proved here; see][]{key}`.
- References: peer-reviewed papers, books, monographs, theses, arXiv only; never X posts, blogs, newspapers. Every work whose definitions, proofs or results are used is listed. Check each entry (authors, original-language title, venue, volume, number, pages, year) against a primary record via web search; list details verified only through secondary sources as open points.

## 4. code/check.py

Docstring "Probability Notes No. NN: numerical check.", what it prints, minimum and tested versions, run command. Lines ≤ 60 characters. Top-level sections start `# N. ...` (or `# 1-2. ...`); the notebook is split there. One labelled print per table number. Exact arithmetic (fractions) where possible, quadrature otherwise. The table copies the output digit for digit.

## 5. Posts on X (no Premium)

Weighted length: code points 0-4351, 8192-8205, 8208-8223, 8242-8247 count 1; everything else (minus U+2212, ≤, ∬, subscript digits) counts 2; a URL or `[link]` counts 23. Check with `make tweets` (`scripts/wlen.py`).
- `post.txt`: thread headed `1/2` and `2/2`, each ≤ 280. Tweet 1: familiar fact, question, "Originator (Year)" and the formula on its own line, one line on symbols. Tweet 2: meaning in words, one consequence with attribution, "Proofs, examples and code: [link]".
- `tweet.txt`: ≤ 280: fact, formula with originator and year, one-line meaning, "Probability Notes No. NN (proofs and code): [link]".
- Plain text, Unicode maths, no hashtags, emoji or @-mentions. `[link]` becomes the Pages article URL only at publication.

## 6. Commands (in order)

```sh
make new P=NN-slug       # start the post (meta.json gets issue and slug)
make check P=NN-slug     # numbers for the table
make qa P=NN-slug        # A4+screen build, zero warnings/boxes/undefined, Type 1 fonts, tweet weights
make pdfs P=NN-slug      # PDFs into docs/posts/NN-slug/pdf/
make formats P=NN-slug   # img/, article.md, notebook.ipynb (executed)
make verify P=NN-slug    # article links and conversion, notebook outputs == check.py, meta.json
make zip P=NN-slug       # dist/pn_NN_slug.zip (Overleaf: main.tex A4, main-screen.tex screen, PDFs in pdf/)
make all                 # qa + verify for every post
make site [SITE_ALL=1]   # site/ preview; drafts only with SITE_ALL=1
make pages [PUSH=1]      # commit site/ to the gh-pages branch (orphan); PUSH=1 pushes
```

QA gate also includes: render every PDF page to PNG and look (`mainresult` not split, author card not orphaned (cut text, never touch the template), figure labels clear, listing not wrapping, cross-reference names right); read `article.md` rendered once; unzip `dist/pn_NN_slug.zip` into an empty folder and run `make`; proofread for overclaims (every claim proved or flagged, minimal conditions, correct equality cases).

## 7. Links and status to update (all must agree)

| Place | Draft | Accepted | Published |
|---|---|---|---|
| `meta.json` status | draft | accepted | published (+ all four links) |
| post `README.md` | status row, open points | status | status + Published links table |
| `README.md` Issues table | add row | status | status |
| `BACKLOG.md` | Drafted (No. NN) | Accepted (No. NN) | Published (No. NN) |
| backlog doc | Status dropdown Drafted, Draw log row | update row | Status Posted, links in row |
| `docs/HANDOFF.md` | status table | status table | status table |
| `post.txt`, `tweet.txt` | `[link]` | `[link]` | `https://<owner>.github.io/<repo>/posts/NN-slug/` |

The site shows only accepted and published posts. Commit after each status change with the session attribution lines. From a Claude session, git in the Mac folder needs delete permission (lock files); otherwise commit in a cloud copy and transfer with `tar --overwrite`, or ask the user to commit.

## 8. Workflow

Phased, one consolidated approval gate per post: deliver the zip, both PDFs, `article.md`, the notebook and the posts, list open points (unverified reference details, unproved facts, layout trade-offs), and wait for approval before setting `accepted`.
