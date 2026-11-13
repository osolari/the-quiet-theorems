# The Quiet Theorems No. 01: De Bruijn's identity

d/dt h(X + √t Z) = ½ J(X + √t Z) (de Bruijn; Stam, 1959).

| Field | Value |
|---|---|
| Status | Draft, awaiting approval (revised 13 Nov 2026); publication planned for 16 Nov 2026 |
| Backlog rank | 1 |
| Package | `make zip P=01-debruijn` → `dist/qt-01-debruijn.zip` |
| PDF | [A4](pdf/qt-01-debruijn.pdf) (9 pp.), [screen](pdf/qt-01-debruijn-screen.pdf) (11 pp.) |
| Thread | [`post.txt`](post.txt) (226 / 280 weighted) |
| Substack article | [`substack/article.md`](substack/article.md) (hand-finished to the house style 13 Nov 2026), figure [`debruijn-figure.png`](substack/debruijn-figure.png) |
| Notebook | [`notebook.ipynb`](notebook.ipynb) (executed) |
| Metadata | [`meta.json`](meta.json) (status, links, Substack details) |
| Single tweet | [`tweet.txt`](tweet.txt) (274 weighted) |

## Published links

Keep in sync with `meta.json` `links`.

| Where | Link |
|---|---|
| Substack post | (not yet published) |
| X thread | (not yet posted) |
| X single tweet | (not yet posted) |
| Pages article | (not yet published; will be `https://<owner>.github.io/<repo>/posts/01-debruijn/`) |

## Open points before approval

1. ~~Stam and Barron checked only via secondary sources~~ resolved 13 Nov 2026 against the originals. Stam (1959), *Information and Control* 2(2), 101–112: eq. (2.12) is dH(p_v)/dv = ½ I₀(p_v), v > 0, in differential form; Stam says (2.3) and (2.12) were communicated by de Bruijn to J. L. van Soest (Director of Physical Research, Netherlands Defence Research Council, who suggested the investigation), not to Stam. The Notes are corrected accordingly, without naming van Soest (credit rule). Barron (1986), *Annals of Probability* 14(1), 336–342: Lemma 1 (p. 338), "Entropy is an integral of Fisher informations", for any X with finite variance, proved on p. 339 from de Bruijn's identity (citing Stam and Blachman, 1965); the Notes now cite Lemma 1. Stam was read via the ScienceDirect open-archive text (OCR), Barron via the author's scan of the JSTOR copy; the Project Euclid page sits behind a CAPTCHA.
2. Stam cites the entropy power inequality as Shannon (1949), Theorem 15 (the book with Weaver); the post cites the 1948 paper, which contains the same theorem. Kept.
3. Substack figure fixed 13 Nov 2026: its "≤ 1" label read "(??)" because `scripts/figures.py` does not resolve `\cref` inside TikZ; the label is now "(any X)" in both PDF and PNG. Development session: make `figures.py` fail on "??" (No. 00's figure should be checked too).
4. The optional "Alternative route" paragraph was dropped to keep the author card off an orphan page.
5. Thread tweet 2 is exactly 280 weighted characters.
6. ~~File naming~~ resolved 13 Nov 2026: hyphens throughout (`qt-01-debruijn.zip`).
7. ~~Backlog doc status~~ resolved 13 Nov 2026: dropdown set to Drafted, draw log row updated (planned date 16 Nov 2026).
8. ~~Substack draft needs hand-finishing~~ resolved 13 Nov 2026: curly apostrophes, "Proof of the theorem" lead-in, Unicode figure caption, Barron Lemma 1 citation; notebook rebuilt from it.
9. Date: `project.tex` and `meta.json` give 16 November 2026, the planned publication date, so the PDF carries it before publication.

## References

Stam (1959); Shannon (1948); Barron (1986); Guo, Shamai and Verdú (2005); Efron (2011). Full entries in [`references.bib`](references.bib).
