---
name: quiet-theorems-post
description: Build and publish a complete post for The Quiet Theorems (formerly Probability Notes): PDF source and A4/screen PDFs, Substack article, notebook, X posts, Overleaf zip and GitHub Pages, in the the-quiet-theorems repo.
---

# The Quiet Theorems: building a full post

The series: theorems from probability, statistics and machine learning that deserve to be better known, one a week, stated with minimal conditions, proved in full and checked in code. Formerly *Probability Notes*; No. 00 was published under that name and keeps it (file prefix `pn`); every later post is *The Quiet Theorems No. NN* with prefix `qt` (`meta.json` `series`, `prefix`).

Reference: No. 00, Hoeffding's covariance identity, published on Substack 9 Nov 2026 (https://omidsolari.substack.com/p/probability-notes-no-00-hoeffdings); its files are `docs/posts/00-hoeffding/` and its published package is archived there as `pn-00-hoeffding.zip`. Every post must match it in structure, tone, rigour, formats, packaging and links. British English, no em-dashes, terse.

## 0. Where things are

- **Repo**: https://github.com/osolari/the-quiet-theorems. On the author's Mac it is `~/workspace/projects/the-quiet-theorems` with remote `git@github-personal:osolari/the-quiet-theorems.git` (the `github-personal` SSH host alias is required for this repo). Commit as `osolari <solari@berkeley.edu>` (set in the repo's git config). Site: https://osolari.github.io/the-quiet-theorems/. Read `README.md`, `STANDARD.md` and `docs/POST_GUIDE.md` first; the guide is the step-by-step procedure and wins over this summary on details.
- **Backlog doc** (live, ranked, status dropdowns, draw log): https://claude.ai/artifact/4i9oRaXXahj9CRiEAvSVUH ; snapshot in `BACKLOG.md`. Take the highest-ranked Queued topic unless told otherwise; respect noted dependencies (e.g. SURE needs Stein's lemma).
- **Substack**: https://omidsolari.substack.com (byline "Omid Solari").
- **claude.ai Project "prob notes"**: read-only copies of the No. 00 reference (`reference/`); the repo is the source of truth, no handoff packages.
- If the repo is not in the session, clone it (or ask the user to connect `~/workspace/projects`); never rebuild the skeleton from memory.

Repo layout (do not change it):

```
skeleton/                 SAIM blog template v1.2 + series layer, shared by every post
skeleton/new-post/        starter files for `make new`
docs/posts/NN-slug/       ALL issue-specific files
docs/POST_GUIDE.md        full procedure
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
| `meta.json` | hand | `issue`, `slug`, `series`, `prefix`, `package_frozen`, `status` (draft/accepted/published), `date`, `links` {x_thread, x_tweet, substack, pages}, `substack` {url, published, audience, editor, draft_id, pdf_attachment, pdf_attached, images, byline, frozen} |
| `README.md` | hand | status, file map, published-links table, open points, references |
| `pdf/qt-NN-slug.pdf`, `pdf/qt-NN-slug-screen.pdf` | `make pdfs` | never hand-made |
| `qt-NN-slug.zip` | archived at publication | the published Overleaf package; `make zip` copies it (`package_frozen: true`) |
| `substack/article.md` | `make formats` draft, then hand-finished; frozen when published | Substack house style (section 5a) |
| `substack/<slug>-figure.png` (`-N.png` if several) | `make formats` | TikZ pictures inside `figure` environments, in order; uploaded to Substack |
| `notebook.ipynb` | `make formats` | executed; title, TL;DR, Result, check list, check.py by `# N.` sections, figures |

Never edit generated files: fix the source (or the script, for every post) and regenerate. Exception: `substack/article.md` is hand-finished after drafting and frozen on publication (`meta.json` `substack.frozen: true`; `make formats` then skips it and its figures).

## 2. main.tex skeleton (fixed order, none dropped or renamed)

Preamble exactly as `skeleton/new-post/main.tex`. Then:

1. `\maketitle`, then `tldr`: three plain sentences (familiar fact; the result, attributed to originator with year; what it means).
2. `\SecSetup`: probability space, symbol table (`\SAIMTableHead`, booktabs, `\small`), numbered `assumption`s, one sentence noting when a commonly quoted condition is stronger than needed, definitions of words used later.
3. `\SecResult`: one `mainresult` box holding the theorem `[Originator, Year]`; equivalent or variant forms as remarks with one-line proofs.
4. `\SecProof`: lemmas first (with proofs), then `\begin{proof}[Proof of \cref{thm:main}]` in `\step{...}` paragraphs. Every interchange of limit/integral/expectation/derivative gets an `\interchange{...}` paragraph stating the dominating function or Tonelli bound and joint measurability. Spell out product-space constructions and why cross terms factorise. Optional "Alternative route (sketch)." paragraph.
5. `\SecInsight`: `enumerate` of 2 to 4 bold-led items (what it says; comparison; role of the structure; sign or equality cases), then one `pullquote`.
6. `\SecUses`: one opening sentence on how the consequences follow; each consequence a `\subsection` with a precise statement and a proof (state any extra condition).
7. `\SecExample`: one fully explicit computation (prefer a counterexample or extreme case), a table, and a TikZ figure in `figure[tbp]` using palette colours (Primary, Secondary, Warning, Rule, RuleDark, Ink, Muted) with an informative caption, referenced via `\cref`. Only pictures inside `figure` are exported (to `substack/`).
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

Docstring "The Quiet Theorems No. NN: numerical check.", what it prints, minimum and tested versions, run command. Lines ≤ 60 characters. Top-level sections start `# N. ...` (or `# 1-2. ...`); the notebook is split there. One labelled print per table number. Exact arithmetic (fractions) where possible, quadrature otherwise. The table copies the output digit for digit.

## 5. Posts on X (no Premium)

Weighted length: code points 0-4351, 8192-8205, 8208-8223, 8242-8247 count 1; everything else (minus U+2212, ≤, ∬, subscript digits) counts 2; a URL or `[link]` counts 23. Check with `make tweets` (`scripts/wlen.py`).
- `post.txt`: thread headed `1/2` and `2/2`, each ≤ 280. Tweet 1: familiar fact, question, "Originator (Year)" and the formula on its own line, one line on symbols. Tweet 2: meaning in words, one consequence with attribution, "Proofs, examples and code: [link]".
- `tweet.txt`: ≤ 280: fact, formula with originator and year, one-line meaning, "The Quiet Theorems No. NN (proofs and code): [link]".
- Plain text, Unicode maths, no hashtags, emoji or @-mentions. `[link]` becomes the post's Substack URL only at publication.

## 5a. Substack article (house style of the published No. 00)

- Head: `# The Quiet Theorems No. NN: <Title>`, italic subtitle, then `Published <date>: <url>` once published.
- TL;DR blockquote, then `[PDF attachment: *The Quiet Theorems No. NN: <Title> (PDF)*. Full proofs, references and the numerical-check code.]`; in the editor this becomes the A4 PDF file block right after the TL;DR.
- Same eight sections as the PDF; no author card, no appendix. No tables (Substack has none): symbol table and check table become numbered lists ("Case. Exact x; numerical y.").
- Result heads in bold, a kind numbered only if there are several, each kind on its own counter ("**Theorem (Hoeffding, 1940).**", "**Lemma.**", "**Corollary 1** (Lehmann, 1966)**.**"); proof steps "**Step k: name.**"; "*Justification (...).*"; ∎.
- LaTeX maths in `$...$` / `$$...$$`; only referenced equations numbered, typed `\qquad (k)`; `\,\mathrm{d}x` for differentials.
- Pull quote as a bold blockquote followed by "(pull quote)"; figure as `![caption](<slug>-figure.png)` plus italic caption.
- Numerical check: method sentence, numbered list, "**Code.** Every number above is printed by the script below (Python 3, NumPy, SciPy); its docstring gives the requirements.", full `check.py`, "**Output:**" with its exact output.
- Author–year citations in text (up to three authors in full, then "et al."); `### References` at the end, alphabetical: `Surname, I. (Year). Title. *Journal*, vol(no), pages.` The PDF keeps numeric citations.

## 5b. Publishing on Substack

Paste the finished article (title `The Quiet Theorems No. NN: <Title>`) on https://omidsolari.substack.com; drag the A4 PDF in after the TL;DR (no file button; the block's "Replace" swaps the file); upload figures with captions; audience everyone; publish. Never edit one draft in two browsers or tabs (the stale one gets HTTP 409 and Publish fails silently; reload first). The "may be truncated in some email clients" banner is only a warning. Then record in `meta.json`: `links.substack` and the whole `substack` block (url, published time, audience, editor URL, draft id, attached-PDF URL, which build was attached, image URLs by file name, byline), set `frozen: true`, add the `Published <date>: <url>` line to the article head, and archive the published package as `docs/posts/NN-slug/qt-NN-slug.zip` with `package_frozen: true`.

## 6. Commands (in order)

```sh
make new P=NN-slug       # start the post (meta.json gets issue and slug)
make check P=NN-slug     # numbers for the table
make qa P=NN-slug        # A4+screen build, zero warnings/boxes/undefined, Type 1 fonts, tweet weights
make pdfs P=NN-slug      # PDFs into docs/posts/NN-slug/pdf/
make formats P=NN-slug   # substack/<slug>-figure.png, substack/article.md draft, notebook.ipynb (executed)
make verify P=NN-slug    # article links, PDF line, Output == check.py, notebook == check.py, meta.json
make zip P=NN-slug       # dist/qt-NN-slug.zip (Overleaf: main.tex A4, main-screen.tex screen, PDFs in pdf/)
make all                 # qa + verify for every post
make site [SITE_ALL=1]   # site/ preview; drafts only with SITE_ALL=1
make pages [PUSH=1]      # commit site/ to the gh-pages branch (orphan); PUSH=1 pushes
```

QA gate also includes: render every PDF page to PNG and look (`mainresult` not split, author card not orphaned (cut text, never touch the template), figure labels clear, listing not wrapping, cross-reference names right); read `substack/article.md` rendered once (rebuild the notebook after hand-finishing it); unzip `dist/qt-NN-slug.zip` into an empty folder and run `make`; proofread for overclaims (every claim proved or flagged, minimal conditions, correct equality cases).

## 7. Links and status to update (all must agree)

| Place | Draft | Accepted | Published |
|---|---|---|---|
| `meta.json` status | draft | accepted | published (+ links and the `substack` block, frozen) |
| post `README.md` | status row, open points | status | status + Published links table |
| `README.md` Issues table | add row | status | status |
| `BACKLOG.md` | Drafted (No. NN) | Accepted (No. NN) | Published (No. NN) |
| backlog doc | Status dropdown Drafted, Draw log row | update row | Status Posted, links in row |
| Substack post | (none) | (none) | published with the PDF attached |
| `post.txt`, `tweet.txt` | `[link]` | `[link]` | the Substack post URL |

The site shows only accepted and published posts. Commit after each status change, as `osolari <solari@berkeley.edu>`, with the session attribution lines. From a Claude session, git in the Mac folder needs delete permission (lock files), and pushing needs the Mac's `github-personal` SSH key: if the session cannot push, leave the commits in place and ask the user to run `git push origin main gh-pages`.

## 8. Workflow

Phased, one consolidated approval gate per post: deliver the zip, both PDFs, the finished `substack/article.md` with its figures, the notebook and the posts, list open points (unverified reference details, unproved facts, layout trade-offs), and wait for approval before setting `accepted`.
