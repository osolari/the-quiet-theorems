# How to make a post for The Quiet Theorems

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
| `meta.json` | hand | status, published links and Substack details (machine-readable source of truth) |
| `README.md` | hand | status, file map, published links, open points, references |
| `pdf/qt-NN-slug.pdf`, `pdf/qt-NN-slug-screen.pdf` | `make pdfs` | the two PDF layouts |
| `qt-NN-slug.zip` (published posts only) | archived at publication | the exact Overleaf package that was published; `make zip` then copies it instead of rebuilding |
| `substack/article.md` | `make formats` (draft), then hand-finished; frozen once published | the Substack post: Markdown + LaTeX, house style below |
| `substack/<slug>-figure.png` (`-N.png` if several) | `make formats` | the PDF's TikZ figures, as uploaded to Substack |
| `notebook.ipynb` | `make formats` | executed notebook: title, TL;DR, result, check list, check code, figures |

Never edit generated files by hand: change the source and regenerate. Published posts are records: their Substack article, figures and Overleaf package are frozen. No. 00 was published under the series' earlier name, *Probability Notes*, with the file prefix `pn`; every later post uses *The Quiet Theorems* and the prefix `qt` (set by `series` and `prefix` in `meta.json`). The one exception to "never edit generated files" is `substack/article.md`: it is generated as a draft, finished by hand to the Substack house style, and frozen (`meta.json` `substack.frozen: true`) the moment it is published; `make formats` then leaves it and its figures untouched. The reference is No. 00 (`docs/posts/00-hoeffding/`), published on Substack on 9 Nov 2026.

## 1. Pick the topic

Scope: theorems from probability, statistics and machine learning (including results behind modern ML/AI methods) that deserve to be better known.

1. Open the backlog doc (link in `BACKLOG.md`); take the highest-ranked Queued topic unless the user says otherwise. Note dependencies flagged in `BACKLOG.md` (e.g. SURE needs Stein's lemma).
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

- The link goes at the top: the first line of tweet 1, and of the single post, is `<Title> (The Quiet Theorems No. NN): [link]`. Nothing after it repeats the link. `make tweets` fails otherwise.
- `post.txt`: `1/2` the heading line, then "Originator (Year) showed that" and the formula on its own line, then one line on the symbols and the familiar fact the result sharpens. `2/2` meaning in words and one consequence with attribution.
- `tweet.txt`: the heading line, then "Originator (Year): formula", then a one-line meaning.
- Plain text, Unicode maths, no hashtags, emoji or @-mentions. `make tweets P=NN-slug`: every tweet ≤ 280 (URL or `[link]` counts 23; characters outside X's weight-1 ranges count 2).
- `[link]` is replaced by the post's Substack URL only at publication (step 10).

## 6. Build and QA the PDF

```sh
make qa P=NN-slug      # A4 + screen; zero warnings/overfull/underfull/undefined; Type 1 fonts; tweet weights
make pdfs P=NN-slug    # copies the PDFs into docs/posts/NN-slug/pdf/
```

Then look at every page (render to PNG): `mainresult` box not split, author card not orphaned on its own page, figure labels clear, code not wrapping, cross-reference names right (Lemma, Corollary, not Theorem). If the card is orphaned, cut text; do not change the template.

## 7. Generate the other formats

```sh
make formats P=NN-slug   # substack/<slug>-figure.png, substack/article.md (draft), notebook.ipynb (executed)
make verify P=NN-slug    # links resolve, no leftover LaTeX, PDF line present, Output == check.py, notebook == check.py, meta.json
```

- `substack/<slug>-figure.png`: the TikZ pictures inside `figure` environments, rendered by `scripts/figures.py` with the post's class and macros. References and citations inside a figure (`\cref`, `\eqref`, `\citet`) resolve from the A4 build; the export fails on anything unresolved or on "??" in the rendered figure, so never work around it by deleting the reference.
- `substack/article.md`: drafted from `main.tex` by `scripts/tex2md.py`, then finished by hand against the house style in step 7a. Read it rendered once.
- `notebook.ipynb`: built by `scripts/make_notebook.py` from `substack/article.md` (title, TL;DR, Result, check list) and the code files; executed with stored outputs. Rebuild it after hand-finishing the article.

## 7a. Substack house style (from the published No. 00)

The Substack post is the same content as the PDF, adapted to what Substack can render:

- **Head:** `# The Quiet Theorems No. NN: <Title>`, the subtitle in italics, then (once published) `Published <date>: <url>`.
- **TL;DR** as a blockquote, then the line `[PDF attachment: *The Quiet Theorems No. NN: <Title> (PDF)*. Full proofs, references and the numerical-check code.]`. In the editor this line is replaced by the PDF file block (the A4 build), placed right after the TL;DR.
- **Same eight sections** as the PDF (`## Setup and notation` ... `## Notes`), same order; no author card, no appendix.
- **No tables** (Substack has none): the symbol table becomes a numbered list ("symbol for meaning"), and the check table a numbered list ("Case. Exact x; numerical y.").
- **Results:** bold run-in heads. A kind is numbered only if there is more than one of it, each kind on its own counter: "**Theorem (Hoeffding, 1940).**", "**Lemma.**", "**Corollary 1** (Lehmann, 1966)**.**". Proof steps "**Step k: name.**"; interchanges "*Justification (...).*"; proofs end with ∎.
- **Maths:** LaTeX in `$...$` and `$$...$$` blocks. Only equations that are referenced get a number, typed in the block as `\qquad (k)`; refer to them as (k). Write `\,\mathrm{d}x` for differentials.
- **Pull quote:** a blockquote in bold, followed by "(pull quote)"; set it as a pull quote in the editor.
- **Figures:** `![caption](<slug>-figure.png)` followed by the caption in italics; upload the PNG at that point.
- **Numerical check:** the method sentence, the numbered list, then "**Code.** Every number above is printed by the script below (Python 3, NumPy, SciPy); its docstring gives the requirements.", the full `check.py` in a Python code block, and "**Output:**" with its exact output in a plain code block.
- **Citations:** author–year in the text ("Lehmann (1966)", "(Slepian, 1962; not proved here)"); up to three authors in full ("Esary, Proschan and Walkup"), more as "et al.". **References** under `### References` at the end, alphabetical, in the form `Surname, I. (Year). Title. *Journal*, vol(no), pages.` (books: `*Title*, 2nd edn. Publisher, Place.`; chapters: `In Editor (ed.), *Book*, pages. Publisher.`). The PDF keeps numeric citations.
- Same wording as the PDF wherever the format allows; British English, no em-dashes.

## 7b. Publishing on Substack (procedure and lessons)

1. New post on https://omidsolari.substack.com; paste the finished `substack/article.md` section by section (LaTeX blocks for display maths, inline LaTeX for inline maths).
2. Drag `pdf/qt-NN-slug.pdf` into the editor right after the TL;DR, replacing the placeholder line. There is no file button; dragging creates a file block, and "Replace" on the block swaps the file.
3. Upload each `substack/<slug>-figure*.png` at its place, with the caption.
4. Set audience (everyone), check the preview, publish.
5. Never edit a draft in two browsers or tabs at once: the stale one gets HTTP 409 and Publish fails silently. Reload before publishing.
6. The banner "may be truncated in some email clients" is a warning only; it does not block publishing.
7. Archive the Overleaf package that matches what was published: `make zip P=NN-slug` and copy `dist/qt-NN-slug.zip` to `docs/posts/NN-slug/qt-NN-slug.zip`; set `package_frozen: true`.
8. Record in `meta.json` `substack`: `url`, `published` (ISO time), `audience`, `editor` URL and `draft_id`, `pdf_attachment` (the file URL Substack assigns), `pdf_attached` (which build), `images` (file name to Substack image URL), `byline`; set `frozen: true` and `links.substack`. Add the published-on line to the article head (it is the record of what was published).

## 8. Package

```sh
make zip P=NN-slug       # dist/qt-NN-slug.zip: Overleaf-ready, A4 main.tex + main-screen.tex, PDFs in pdf/
```

Unzip into an empty folder and run `make` there once to confirm it builds cleanly.

## 9. Approval gate: update status everywhere

Deliver the zip, both PDFs, `substack/article.md` with its figures, the notebook and the posts, with the open points listed. Then update these places so they agree:

| Place | Draft delivered | Accepted | Published |
|---|---|---|---|
| `docs/posts/NN-slug/meta.json` `status` | `draft` | `accepted` | `published` |
| `docs/posts/NN-slug/README.md` status row | Draft, awaiting approval | Package accepted DATE | Published DATE |
| `docs/DEVELOPING.md` Posts table | add row | update status | update status |
| `README.md` Posts list (reader-facing) | (none) | (none) | add the entry: title, date, one-sentence claim, Substack, web, PDFs, notebook, Colab; add a BibTeX example only if the format changes |
| `BACKLOG.md` status column | Drafted (No. NN) | Accepted (No. NN) | Published (No. NN) |
| Backlog doc: Status dropdown | Drafted | Drafted | Posted |
| Backlog doc: Draw log row | add row | update Post/PDF cells | add post links |
| `meta.json` `substack` block | (empty) | (empty) | all fields, `frozen: true` |

Commit after each change of status (`git add -A && git commit`), authored as `osolari <solari@berkeley.edu>` with no `Co-Authored-By` or session trailers. Pushing is done by the author from the Mac (`git push origin main`); see the skill's "Sessions and the repo" for how a Claude session works on the Mac folder.

## 10. Publish

1. Publish on Substack (step 7b) and record the Substack details in `meta.json`.
2. Put the Substack URL in place of `[link]` in `post.txt` and `tweet.txt`, rerun `make tweets`, then post on X (thread or single post). Record `links.x_thread` / `links.x_tweet`.
3. Push `main`; the Pages workflow rebuilds the site and deploys it to `gh-pages` (or run `make pages PUSH=1 PAGES_REPO=owner/name` locally). Only `accepted` and `published` posts appear. Record `links.pages` (`https://<owner>.github.io/<repo>/posts/NN-slug/`).
4. Set status `published`, mirror the links in the post README's "Published links" table, update the places in step 9, commit and push.

## 11. Final checks (all must hold)

- `make all` passes (QA and verify for every post).
- `dist/qt-NN-slug.zip` builds from a clean unzip.
- Links agree across `meta.json`, the post README, `docs/DEVELOPING.md`, `README.md`, the backlog doc, the Substack post and the site.
