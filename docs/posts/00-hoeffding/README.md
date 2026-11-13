# No. 00: Hoeffding's covariance identity

Cov(X,Y) = ∬ [F_{X,Y}(x,y) − F_X(x)F_Y(y)] dx dy (Hoeffding, 1940).

| Field | Value |
|---|---|
| Status | Published on Substack 9 Nov 2026, 09:49 PST; package accepted. Reference post for the series |
| Backlog rank | 0 |
| Package | `make zip P=00-hoeffding` → `dist/pn_00_hoeffding.zip` (identical to the published package) |
| PDF | [A4](pdf/pn-00-hoeffding.pdf) (8 pp., Result box on p. 1), [screen](pdf/pn-00-hoeffding-screen.pdf) (12 pp.) |
| Substack article | [`substack/article.md`](substack/article.md), as published (frozen), with [`hoeffding-figure.png`](substack/hoeffding-figure.png) |
| Notebook | [`notebook.ipynb`](notebook.ipynb) (executed) |
| Metadata | [`meta.json`](meta.json) (status, links, Substack details) |
| Thread | [`post.txt`](post.txt) (257 / 275 weighted) |
| Single tweet | [`tweet.txt`](tweet.txt) (274 weighted) |

## Published links

Keep in sync with `meta.json`.

| Where | Link |
|---|---|
| Substack post (audience: everyone) | https://omidsolari.substack.com/p/probability-notes-no-00-hoeffdings |
| Substack editor (draft id 224169408) | https://omidsolari.substack.com/publish/post/224169408 |
| PDF attached on Substack (A4 build) | https://omidsolari.substack.com/api/v1/file/4c024c81-13d7-418b-b924-661aac38df84.pdf |
| Figure on Substack | https://substack-post-media.s3.amazonaws.com/public/images/83fa447e-ebaa-4cee-8574-1d6e232d1e4c_583x309.png |
| X thread | (not yet posted; replace `[link]` with the Substack URL) |
| X single tweet | (not yet posted) |
| Pages article | (not yet published; will be `https://<owner>.github.io/<repo>/posts/00-hoeffding/`) |

## Content

- **Result:** under E|X|, E|Y|, E|XY| < ∞, Cov(X,Y) = ∬ [F_XY − F_X F_Y] dx dy.
- **Proof:** symmetrisation with independent copies on Ω×Ω (following Lehmann); four-term expansion with cross terms factorising by Fubini on the product space; indicator lemma; Tonelli/Fubini for the interchange, joint measurability stated.
- **Uses:** variance and mean absolute difference; PQD corollary (zero covariance + PQD ⇒ independence); association inequality; copulas and Spearman's rho; copula bounds and extremal covariance (second moments assumed); functions version (Cuadras).
- **Worked example:** X uniform on {−1, 0, 1}, Y = X²; D = ±1/9 on two unit squares.
- **Numerical check:** Gaussian ∬D = 0.5; same D against dF_X dF_Y = 0.4826; Exp(1) variance 0.999992; exact rational example 0 (sup|D| = 1/9).

## Decisions (9 Nov 2026)

1. **Credit.** Prose names only the originator (Hoeffding). Everyone whose work is used is cited where it is used: Lehmann 1966, Fréchet 1951, Sklar 1959, Spearman 1904, Kruskal 1958, Gini 1912, Slepian 1962, Esary–Proschan–Walkup 1967, Cuadras 2002, Embrechts–McNeil–Straumann 2002, Nelsen 2006, Hoeffding 1940 and 1948. Details checked against primary records; Hoeffding 1940 given as 5(3):181–233 from the catalogue record (some sources say 179–233).
2. **TL;DR wording.** "factorises into the product of its marginals"; no "over the plane"; "requires". Pull quote, Assumption A1 sentence and tweets aligned with it.
3. **Voice.** A rewrite aimed at an AI-text detector score was tried and reverted at the author's request; the earlier wording stands.
4. **Code.** A "Code." paragraph replaces the old "Reproduced" tag; the listing sits in the appendix in footnotesize, fitting one A4 page.
5. **Tags.** covariance, stochastic dependence, copulas, quadrant dependence, rank correlation.
6. **Author card.** "Omid Shams Solari, Ph.D.", sAIm Labs, "Founder, Principal Statistician and Principal AI Research Scientist" with three research lines; ", Ph.D." on the card only.
7. **Substack vs PDF.** Author–year citations and alphabetical references on Substack, numeric in the PDF; Substack equations as LaTeX blocks with typed numbers (1), (2); PDF attached right after the TL;DR; code and its output inline under "Numerical check".

## Open items

- Post the X thread or the single tweet with the Substack URL.
- Optional: change the Substack profile display name ("Omid Solari") to match the PDF byline.

## References

Hoeffding (1940, 1948); Lehmann (1966); Fréchet (1951); Sklar (1959); Spearman (1904); Kruskal (1958); Gini (1912); Slepian (1962); Esary, Proschan and Walkup (1967); Cuadras (2002); Embrechts, McNeil and Straumann (2002); Nelsen (2006). Full entries in [`references.bib`](references.bib).
