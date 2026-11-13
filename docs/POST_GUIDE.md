# How to make a Probability Notes post

The complete procedure, from picking a topic to publishing. Follow it in order; every post must come out with the same files, structure and links. `STANDARD.md` governs the content of the PDF; this guide governs everything around it.

## 0. One post = these files

Everything issue-specific lives in `docs/posts/NN-slug/` (NN two digits, slug lower-case, one or two words, e.g. `02-sure`). Nothing else in the repo is edited per post except the link and status places in step 9.

| File | Written by | Purpose |
|---|---|---|
| `main.tex` | hand | PDF body (eight-section skeleton, `STANDARD.md`) |
| `project.tex` | hand | title, subtitle, issue, reading time, tags, date, keywords; author block untouched |
| `references.bib` | hand | every work used; checked against primary records |
| `code/check.py` | hand | prints every number in the check table; sections start `# N. ` |
| `code/figures.py` | hand | matplotlib versions of the PDF figures, for the notebook |
| `post.txt` | hand | X thread, `1/2` and `2/2`, each ≤ 280 weighted |
| `tweet.txt` | hand | single X post, ≤ 280 weighted |
| `meta.json` | hand | status and published links (machine-readable source of truth) |
| `README.md` | hand | status, file map, published links, open points, references |
| `pdf/pn-NN-slug.pdf`, `pdf/pn-NN-slug-screen.pdf` | `make pdfs` | the two PDF layouts |
| `img/figure-N.png` | `make formats` | the PDF's TikZ figures, rasterised |
| `article.md` | `make formats` | Markdown article with MathJax maths and embedded figures |
| `notebook.ipynb` | `make formats` | executed notebook: result, check table, check code, figures |

Never edit generated files by hand: change the source and regenerate.

## 1. Pick the topic

1. Open the backlog doc (link in `README.md`); take the highest-ranked Queued topic unless the user says otherwise. Note dependencies flagged in `BACKLOG.md` (e.g. SURE needs Stein's lemma).
2. `make new P=NN-slug`. This copies `skeleton/new-post/` (main.tex, project.tex, references.bib, code/check.py, code/figures.py, post.txt, tweet.txt, meta.json with issue and slug filled in).

## 2. Research and references

- Identify the originator(s) and the original publication; read what it contains.
- Every work whose definitions, proofs or results are used goes in `references.bib`: peer-reviewed papers, books, theses, arXiv only. No X posts, blogs, newspapers.
- Check authors, original-language title, venue, volume, number, pages and year against a primary record (publisher page, index, DOI). List anything verified only via secondary sources as an open point in the post README.

## 3. Write the PDF source

- `project.tex`: title = name of the result; subtitle = claim in words; `No. NN`; reading time ≈ words excluding code / 230; 4 to 6 subject tags; date. Do not touch the author block.
- `main.tex`: follow `skeleton/new-post/main.tex` and `STANDARD.md` exactly: TL;DR; Setup and notation; Result in one `mainresult` box; Proof (lemmas, `\step`, `\interchange` for every limit/integral/expectation swap); Insights + one pull quote; Uses and consequences; Worked example + TikZ figure in a `figure` environment; Numerical check (Case / Exact / Numerical) + `\paragraph{Code.}`; Notes (originator history only) + bibliography; author card wrapper; `\clearpage` appendix with the listing.
- Prose names only the originators; everyone else by citation; side results named descriptively. Unproved facts: `\citep[not proved here; see][]{key}`.
- Labels: `\label[lemma]{lem:x}`, `\label[corollary]{cor:x}`, `\label[remark]{rem:x}`; theorems and equations plain `\label`. Refer with `\cref` only; never to sections by number.
- Figures: put every TikZ picture inside `\begin{figure}...\end{figure}` (only those are exported to `img/`), palette colours only (Primary, Secondary, Warning, Rule, RuleDark, Ink, Muted).

## 4. Write the code

- `code/check.py`: docstring (what it prints, minimum and tested versions, run command); lines ≤ 60 characters; exact arithmetic where possible; one labelled `print` per table number; top-level sections as `# 1. ...`, `# 2. ...` (or `# 1-2. ...`). The notebook is split at these headers.
- `code/figures.py`: one matplotlib figure per PDF figure, same order and meaning, palette constants from the template file. It runs after `check.py` in the notebook's namespace, so it may use functions defined there.
- `make check P=NN-slug` and copy the printed numbers into the table digit for digit.

## 5. Write the posts

- `post.txt`: `1/2` anchor fact, question, "Originator (Year)" and the formula on its own line, one line on the symbols. `2/2` meaning in words, one consequence with attribution, "Proofs, examples and code: [link]".
- `tweet.txt`: fact, formula with originator and year, one-line meaning, "Probability Notes No. NN (proofs and code): [link]".
- Plain text, Unicode maths, no hashtags, emoji or @-mentions. `make tweets P=NN-slug`: every tweet ≤ 280 (URL or `[link]` counts 23; characters outside X's weight-1 ranges count 2).
- `[link]` is replaced by the post's Pages URL only at publication (step 10).

## 6. Build and QA the PDF

```sh
make qa P=NN-slug      # A4 + screen; zero warnings/overfull/underfull/undefined; Type 1 fonts; tweet weights
make pdfs P=NN-slug    # copies the PDFs into docs/posts/NN-slug/pdf/
```

Then look at every page (render to PNG): `mainresult` box not split, author card not orphaned on its own page, figure labels clear, code not wrapping, cross-reference names right (Lemma, Corollary, not Theorem). If the card is orphaned, cut text; do not change the template.

## 7. Generate the other formats

```sh
make formats P=NN-slug   # img/figure-N.png, article.md, notebook.ipynb (executed)
make verify P=NN-slug    # links resolve, no leftover LaTeX, notebook numbers == check.py
```

- `article.md`: converted from `main.tex` by `scripts/tex2md.py` (numbers and citations from the build's `.aux`, references from `references.bib`, figures from `img/`, code inline at the end). Read it once on GitHub to confirm the maths renders. If something converts badly, fix `main.tex` (or the converter for everyone), never the Markdown.
- `notebook.ipynb`: built by `scripts/make_notebook.py` from `article.md` (title, TL;DR, Result, check table) and the code files; executed with stored outputs.

## 8. Package

```sh
make zip P=NN-slug       # dist/pn_NN_slug.zip: Overleaf-ready, A4 main.tex + main-screen.tex, PDFs in pdf/
```

Unzip into an empty folder and run `make` there once to confirm it builds cleanly.

## 9. Approval gate: update status everywhere

Deliver the zip, both PDFs, `article.md`, the notebook and the posts, with the open points listed. Then update these places so they agree:

| Place | Draft delivered | Accepted | Published |
|---|---|---|---|
| `docs/posts/NN-slug/meta.json` `status` | `draft` | `accepted` | `published` |
| `docs/posts/NN-slug/README.md` status row | Draft, awaiting approval | Package accepted DATE | Published DATE |
| `README.md` Issues table | add row | update status | update status |
| `BACKLOG.md` status column | Drafted (No. NN) | Accepted (No. NN) | Published (No. NN) |
| Backlog doc: Status dropdown | Drafted | Drafted | Posted |
| Backlog doc: Draw log row | add row | update Post/PDF cells | add post links |
| `docs/HANDOFF.md` status table | update | update | update |

Commit after each change of status (`git add -A && git commit`), with the session attribution lines.

## 10. Publish

1. Push `main`; the Pages workflow rebuilds the site and deploys it to `gh-pages` (or run `make pages PUSH=1 PAGES_REPO=owner/name` locally). Only `accepted` and `published` posts appear on the site.
2. The article URL is `https://<owner>.github.io/<repo>/posts/NN-slug/`. Put it in place of `[link]` in `post.txt` and `tweet.txt`, rerun `make tweets`, then post on X.
3. Fill `meta.json` `links` (`x_thread`, `x_tweet`, `substack`, `pages`) and the post README's "Published links" table with the same URLs, set status `published`, update the places in step 9, commit and push (the site then shows the X and Substack links on the article page).

## 11. Final checks (all must hold)

- `make all` passes (QA and verify for every post).
- `dist/pn_NN_slug.zip` builds from a clean unzip.
- Links agree across `meta.json`, the post README, `README.md`, the backlog doc and the site.
