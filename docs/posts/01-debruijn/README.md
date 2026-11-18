# The Quiet Theorems No. 01: De Bruijn's identity

d/dt h(X + √t Z) = ½ J(X + √t Z) (de Bruijn; Stam, 1959).

| Field | Value |
|---|---|
| Status | Published 18 Nov 2026 |
| Backlog rank | 1 |
| Package | [`qt-01-debruijn.zip`](qt-01-debruijn.zip) (archived as published; `make zip` copies it) |
| PDF | [A4](pdf/qt-01-debruijn.pdf) (12 pp.), [screen](pdf/qt-01-debruijn-screen.pdf) (15 pp.) |
| X post | [`post.txt`](post.txt) (one long post: lead 237 / 280, total 764; attach `substack/debruijn-figure.png`) |
| Substack article | [`substack/article.md`](substack/article.md) (hand-finished; frozen as published 18 Nov 2026), figure [`debruijn-figure.png`](substack/debruijn-figure.png) |
| Notebook | [`notebook.ipynb`](notebook.ipynb) (executed) |
| Metadata | [`meta.json`](meta.json) (status, links, Substack details) |

## Published links

Keep in sync with `meta.json` `links`.

| Where | Link |
|---|---|
| Substack post | https://omidsolari.substack.com/p/the-quiet-theorems-no-01-de-bruijns |
| X post | (not yet posted; `post.txt` carries the Substack URL) |
| Pages article | https://osolari.github.io/the-quiet-theorems/posts/01-debruijn/ |

## Open points and decisions

1. ~~Stam and Barron checked only via secondary sources~~ resolved 13 Nov 2026 against the originals. Stam (1959), *Information and Control* 2(2), 101–112: eq. (2.12) is dH(p_v)/dv = ½ I₀(p_v), v > 0, in differential form; Stam says (2.3) and (2.12) were communicated by de Bruijn to J. L. van Soest (Director of Physical Research, Netherlands Defence Research Council, who suggested the investigation), not to Stam. The Notes are corrected accordingly, without naming van Soest (credit rule). Barron (1986), *Annals of Probability* 14(1), 336–342: Lemma 1 (p. 338), "Entropy is an integral of Fisher informations", for any X with finite variance, proved on p. 339 from de Bruijn's identity (citing Stam and Blachman, 1965); the Notes now cite Lemma 1. Stam was read via the ScienceDirect open-archive text (OCR), Barron via the author's scan of the JSTOR copy; the Project Euclid page sits behind a CAPTCHA.
2. Stam cites the entropy power inequality as Shannon (1949), Theorem 15 (the book with Weaver); the post cites the 1948 paper, which contains the same theorem. Kept.
3. ~~Substack figure "(??)" label~~ resolved 13 Nov 2026: the label is now "≤ 1 (any X)" in PDF and PNG, and `scripts/figures.py` now resolves references from the A4 build and fails on "??" (commit 28f8696).
4. The optional "Alternative route" paragraph was dropped to keep the author card off an orphan page.
5. Proofread 18 Nov 2026 (PDF, article, posts): the TL;DR, insights and posts no longer call Fisher information itself the rate (the rate is half of it); the Gaussian-is-slowest claim is now restricted to inputs of a given variance; the Fubini bound in the score lemma is written out; the I–MMSE equivalence is stated as passing through Corollary 3 (PDF Corollary 9); Barron's Lemma 1 is described by its own content (entropy as an integral of Fisher informations); reading time 13 → 11 min (the article has the same length as No. 00's, 10 min); thread 2/2 now names all three of Guo, Shamai and Verdú and defines σ².
6. ~~File naming~~ resolved 13 Nov 2026: hyphens throughout (`qt-01-debruijn.zip`).
7. ~~Backlog doc status~~ resolved 13 Nov 2026: dropdown set to Drafted, draw log row updated (planned date 16 Nov 2026).
8. ~~Substack draft needs hand-finishing~~ resolved 13 Nov 2026: curly apostrophes, "Proof of the theorem" lead-in, Unicode figure caption, Barron Lemma 1 citation; notebook rebuilt from it.
9. ~~Date~~ resolved 18 Nov 2026: publication date 18 November 2026 in `project.tex`, `meta.json`, the PDFs and the backlog doc.
10. Substack draft created 18 Nov 2026, unpublished: https://omidsolari.substack.com/publish/post/225529600 (draft 225529600). Built from `substack/article.md` at 1f5d38e (254 inline and 17 display maths, all render in the editor without MathJax errors), A4 PDF attached after the TL;DR, figure uploaded with its caption, subscribe widgets placed as in No. 00, audience everyone. Publishing awaits the author's go-ahead.
11. Proofs expanded 18 Nov 2026 at the author's request: every lemma, the main proof and the three corollaries now give each computation and limit step explicitly (kernel derivatives and Γ moments; the density via Tonelli and the substitution; dominating constants for each derivative; both Jensen steps in the log bound; both Fubini swaps and Doob–Dynkin in the score lemma; the tails lemma by construction; the chain rule and the moment expansion for the integrable bound G; the Cauchy–Schwarz equality case via an open null set; absolute continuity in the sandwich; the tower property in the MMSE corollary; the I–MMSE change of variables; Bayes and the tower step in the worked example). The Proof section is now about 3.5 A4 pages against the standard's guide of 1 to 2; A4 9 → 12 pp., screen 11 → 15 pp. Reading time 11 → 18 min (PDF prose 1.76 times No. 00's, which is marked 10 min). Substack draft updated 18 Nov 2026 from GitHub at ba675a3: expanded text (436 inline and 25 display maths, all rendering without MathJax errors) and the new A4 PDF (406 466 bytes) after the TL;DR; still unpublished.
12. Substack: the second subscribe box (after the setup) removed from the live post 18 Nov 2026; one box remains, at the end. Edited in place, no email resent. The repository procedure now requires exactly one, at the end.

## References

Stam (1959); Shannon (1948); Barron (1986); Guo, Shamai and Verdú (2005); Efron (2011). Full entries in [`references.bib`](references.bib).
