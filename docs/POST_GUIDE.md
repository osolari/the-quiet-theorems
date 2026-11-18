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
| `post.txt` | hand | the X post: one long post, lead ≤ 280 weighted, posted with the plot attached |
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
2. `make new P=NN-slug`. This copies `skeleton/new-post/` (main.tex, project.tex, references.bib, code/check.py, code/figures.py, post.txt, meta.json with issue and slug filled in).

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

- `post.txt` is one X Premium long post, with the post's plot attached (`substack/<slug>-figure.png`; the first figure if there are several). Line 1: `<Title> (The Quiet Theorems No. NN): [link]`. Line 2: a one-sentence hook on what the plot shows. These two lines are the lead: at most 280 weighted, so the lead and the plot appear before X's "Show more". After a blank line: "Originator (Year) showed that", the formula on its own line, the weakest condition and what the symbols are; then the meaning in words and the familiar fact it sharpens; then one consequence with its attribution. The link appears only on line 1. Aim for 600 to 1,500 weighted in total (hard limit 25,000). `make tweets` fails if line 1 lacks the link, the lead exceeds 280, the total exceeds 25,000 or the plot is missing; it prints the file to attach.
- Plain text, Unicode maths, no hashtags, emoji or @-mentions. Weights: a URL or `[link]` counts 23; characters outside X's weight-1 ranges count 2.
- `[link]` is replaced by the post's Substack URL only at publication (step 10).

## 6. Build and QA the PDF

```sh
make qa P=NN-slug      # A4 + screen; zero warnings/overfull/underfull/undefined; Type 1 fonts; X post checks
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

Then preview the post's web page, drafts included:

```sh
make site SITE_ALL=1     # site/ with drafts; open site/posts/NN-slug/index.html
```

Check that the article's maths renders, the figure shows, the PDF and notebook links resolve, and the Substack and X links are absent or blank but never broken. The delivery says the page was checked (step 9).

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

## 7b. Substack: draft before approval, publish after

Two stages. The draft is created before approval and is part of the package; publishing happens after approval, only on the author's explicit word.

### Create the draft (before approval, after QA and step 8 pass)

1. Load the `built-in-browser` skill, then use the built-in browser, where the author is already signed in to https://omidsolari.substack.com.
2. New post. Title `The Quiet Theorems No. NN: <Title>`, then the subtitle.
3. Paste the finished `substack/article.md` section by section (LaTeX blocks for display maths, inline LaTeX for inline maths).
4. Drag `pdf/qt-NN-slug.pdf` (A4) into the editor right after the TL;DR, in place of the `[PDF attachment: ...]` line. There is no file button; dragging creates a file block, and "Replace" on the block swaps the file.
5. Upload each `substack/<slug>-figure*.png` at its place, with its caption.
6. Exactly one subscribe box ("Thanks for reading! Subscribe for free to receive new posts and support my work."), at the very end of the post, after the references. None in the middle: remove any other that the editor or a template inserts (Nos. 00 and 01 had a second one after the setup, removed 18 Nov 2026).
7. Audience: everyone. **Never press Publish.**
8. Record `substack.editor` (editor URL) and `substack.draft_id` in `meta.json`. Leave `links.substack` and `substack.url` empty: the editor link is private and must not reach the site.
9. If the browser is unavailable or Substack refuses an action, do the rest, say exactly what failed and list it as an open point; do not stop the delivery.

### Publish (after approval, on the author's word)

1. Reload the draft. Never edit one draft in two browsers or tabs at once: the stale one gets HTTP 409 and Publish fails silently.
2. Check the preview (including exactly one subscribe box, at the end), then publish. The banner "may be truncated in some email clients" is a warning only; it does not block publishing.
3. Archive the Overleaf package that matches what was published: `make zip P=NN-slug` and copy `dist/qt-NN-slug.zip` to `docs/posts/NN-slug/qt-NN-slug.zip`; set `package_frozen: true`.
4. Record in `meta.json` `substack`: `url`, `published` (ISO time), `audience`, `pdf_attachment` (the file URL Substack assigns), `pdf_attached` (which build), `images` (file name to Substack image URL), `byline`; set `frozen: true` and `links.substack`. Add the published-on line to the article head (it is the record of what was published).

## 8. Package

```sh
make zip P=NN-slug       # dist/qt-NN-slug.zip: Overleaf-ready, A4 main.tex + main-screen.tex, PDFs in pdf/
```

Unzip into an empty folder and run `make` there once to confirm it builds cleanly. Then create the Substack draft (step 7b, first stage).

## 9. Approval gate: update status everywhere

Deliver, in one message, the zip, both PDFs, `substack/article.md` with its figures, the notebook and the posts, with the open points listed. The delivery must state, for each of these two, either "done" with the link or why not:

- **Substack draft**: "done" with the editor link, or what failed;
- **Pages page**: "done: checked locally with `make site SITE_ALL=1`" (it goes live only after approval and the push), or what failed.

Keep these places in agreement:

| Place | Draft delivered | Accepted | Published |
|---|---|---|---|
| `docs/posts/NN-slug/meta.json` `status` | `draft` | `accepted` | `published` |
| `docs/posts/NN-slug/README.md` status row | Draft, awaiting approval | Package accepted DATE | Published DATE |
| `docs/DEVELOPING.md` Posts table | add row | update status | update status |
| `README.md` Posts list (reader-facing) | (none) | (none) | add the entry: title, date, one-sentence claim, Substack, web, PDFs, notebook, Colab; add a BibTeX example only if the format changes |
| `BACKLOG.md` status column | Drafted (No. NN) | Accepted (No. NN) | Published (No. NN) |
| Backlog doc: Status dropdown | Drafted | Accepted (Drafted if the dropdown has no Accepted) | Posted |
| Backlog doc: Draw log row | add row | update Post/PDF cells | add post links |
| `meta.json` `substack` block | `editor`, `draft_id` | unchanged | all fields, `frozen: true` |
| Substack post | draft created (editor link) | draft, unchanged | published with the PDF attached |
| Pages page | checked locally (`make site SITE_ALL=1`) | `make site` checked; live once `main` is pushed | live; `links.pages` recorded |

Commit after each change of status (`git add -A && git commit`), with the repo's configured git identity; never add the AI agent as a co-author (no `Co-Authored-By` or session trailers). Pushing is done by the author from the Mac (`git push origin main`); see the skill's "Sessions and the repo" for how a Claude session works on the Mac folder.

### On approval

Without further prompting:

1. Set `accepted` in `meta.json`, the post `README.md`, the `docs/DEVELOPING.md` Posts table, `BACKLOG.md` and the backlog doc.
2. `make site` (accepted and published posts only) and check the post's page again.
3. Commit; never add the AI agent as a co-author.
4. Give the author the push command (`cd ~/workspace/projects/the-quiet-theorems && git push origin main`) and say that pushing `main` deploys the Pages site through the workflow.
5. Only on the author's explicit word to publish: step 10.

## 10. Publish

Only on the author's explicit word, without further prompting once it is given:

1. Publish the Substack draft and record it (step 7b, second stage): archive the zip, freeze the article, fill `meta.json` `links.substack` and the `substack` block.
2. Put the Substack URL in place of `[link]` in `post.txt` and rerun `make tweets`.
3. Set status `published` everywhere in step 9, including the `README.md` Posts list; mirror the links in the post README's "Published links" table.
4. Commit and give the push command. Pushing `main` redeploys the site; record `links.pages` (`https://osolari.github.io/the-quiet-theorems/posts/NN-slug/`) once the page is live.
5. Posting on X is the author's, unless they ask the session to do it: paste `post.txt` as one post and attach `substack/<slug>-figure.png`. Record `links.x_post` and commit.

## 11. Final checks (all must hold)

- `make all` passes (QA and verify for every post).
- `dist/qt-NN-slug.zip` builds from a clean unzip.
- Links agree across `meta.json`, the post README, `docs/DEVELOPING.md`, `README.md`, the backlog doc, the Substack post and the site.
