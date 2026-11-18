# The Quiet Theorems No. 00: Hoeffding's covariance identity

First published on 9 Nov 2026 as *Probability Notes* No. 00, the series' earlier name. A revised edition, aligned with No. 01, was approved and published on 18 Nov 2026: the series name is The Quiet Theorems, the prefix is `qt`, and every proof and corollary is written out step by step. The live Substack post was edited in place (same URL and date, PDF and figure swapped, title changed, no new email).

Cov(X,Y) = ∬ [F_{X,Y}(x,y) − F_X(x)F_Y(y)] dx dy (Hoeffding, 1940).

| Field | Value |
|---|---|
| Status | Published 9 Nov 2026, 09:49 PST; revised 18 Nov 2026 (live post edited in place) |
| Backlog rank | 0 |
| Package | [`qt-00-hoeffding.zip`](qt-00-hoeffding.zip), the revised package as published on 18 Nov (`package_frozen`; `make zip` copies it). The 9 Nov package `pn-00-hoeffding.zip` is in the git history |
| PDF | [A4](pdf/qt-00-hoeffding.pdf) (11 pp., Result box on p. 1), [screen](pdf/qt-00-hoeffding-screen.pdf) (15 pp.) |
| Substack article | [`substack/article.md`](substack/article.md), revised edition as published, frozen, with [`hoeffding-figure.png`](substack/hoeffding-figure.png) |
| Notebook | [`notebook.ipynb`](notebook.ipynb) (executed) |
| Metadata | [`meta.json`](meta.json) (status, links, Substack details) |
| X post | [`post.txt`](post.txt) (one long post: lead 225 / 280, total 677; attach `substack/hoeffding-figure.png`) |

## Published links

Keep in sync with `meta.json`.

| Where | Link |
|---|---|
| Substack post (audience: everyone) | https://omidsolari.substack.com/p/probability-notes-no-00-hoeffdings |
| Substack editor (draft id 224169408) | https://omidsolari.substack.com/publish/post/224169408 |
| PDF attached on Substack | https://omidsolari.substack.com/api/v1/file/40023d45-8a0a-40f8-bc0e-8e3e4ac4fe7a.pdf (`qt-00-hoeffding.pdf`, revised edition) |
| Figure on Substack | https://substack-post-media.s3.amazonaws.com/public/images/71c2bd65-3520-4b18-97ae-d462cada9ae8_659x344.png (revised figure) |
| X post | (not yet posted; `post.txt` carries the Substack URL) |
| Pages article | https://osolari.github.io/the-quiet-theorems/posts/00-hoeffding/ (live; redirects to `solari.stat.berkeley.edu/the-quiet-theorems/posts/00-hoeffding/`) |

## Content

- **Result:** under E|X|, E|Y|, E|XY| < ∞, Cov(X,Y) = ∬ [F_XY − F_X F_Y] dx dy.
- **Proof:** a roadmap paragraph, then two lemmas. Lemma 3 is the indicator identity, case by case. Lemma 4 builds the independent copies on Ω×Ω with product measure and proves the factorisation of cross terms by Tonelli and Fubini. The main proof follows Lehmann's symmetrisation: integrability of all four terms, joint measurability of Φ, the Tonelli bound (6), Fubini, and E Φ = 2D term by term.
- **Uses** (each a corollary with a step-by-step proof):
  - variance and mean absolute difference (Corollary 5);
  - PQD (Corollary 6, Lehmann);
  - the association inequality (Corollary 7);
  - copulas and rank correlation (Corollary 8). Uniform marginals and the copula representation are now proved for continuous marginals; Sklar and Nelsen are cited for the general theory;
  - copula bounds and extremal covariance (Corollary 9). The generalised-inverse property and attainment are now proved;
  - functions of the variables (Corollary 10, Cuadras).
- **Worked example:** X uniform on {−1, 0, 1}, Y = X²; D = ±1/9 on two unit squares.
- **Numerical check:** Gaussian ∬D = 0.5; the same D against dF_X dF_Y = 0.4826; Exp(1) variance 0.999992; the exact rational example 0 (sup|D| = 1/9).
- **Still cited and not proved here:** Gaussian PQD for ρ ≥ 0 (Slepian, 1962); the arcsin closed form for Spearman's rho (Kruskal, 1958).

## Decisions

1. **Credit (9 Nov).** Prose names only the originator (Hoeffding). Everyone whose work is used is cited where it is used: Lehmann 1966, Fréchet 1951, Sklar 1959, Spearman 1904, Kruskal 1958, Gini 1912, Slepian 1962, Esary–Proschan–Walkup 1967, Cuadras 2002, Embrechts–McNeil–Straumann 2002, Nelsen 2006, Hoeffding 1940 and 1948. Details were checked against primary records. Hoeffding 1940 is given as 5(3):181–233, from the catalogue record; some sources give 179–233.
2. **TL;DR wording (9 Nov).** "factorises into the product of its marginals"; no "over the plane"; "requires".
3. **Voice (9 Nov).** A rewrite aimed at an AI-text detector score was tried and reverted at the author's request.
4. **Author card (9 Nov).** "Omid Shams Solari, Ph.D.", sAIm Labs, "Founder, Principal Statistician and Principal AI Research Scientist", with three research lines.
5. **Re-issue (18 Nov).** The author chose a full re-issue aligned with No. 01:
   - series name and `qt` prefix;
   - proofs expanded step by step;
   - date "9 November 2026, revised 18 November 2026";
   - reading time 10 → 13 min;
   - figure tick relabelled "y = 1", so it no longer sits on the square's edge;
   - live post edited in place on 18 Nov, with no revision note and no new email.
6. **Subscribe box (18 Nov).** The second subscribe box (after the setup) was removed from the live post; one remains, at the end. Edited in place, no email resent. The repository procedure now requires exactly one, at the end.

## Open points (development session)

1. **Shared files still describe No. 00 as `pn` / Probability Notes:** `skills/quiet-theorems-post/SKILL.md`, `docs/POST_GUIDE.md`, `STANDARD.md` and `docs/DEVELOPING.md` ("No. 00 keeps its published prefix `pn`"). These are for the development session.
2. **Site: `polyfill.io` script.** Pandoc 3.1.3's default HTML template adds `<script src="https://polyfill.io/v3/polyfill.min.js?features=es6">` when run with `--mathjax`. The domain was taken over in 2024 and served malicious code. `scripts/build_site.py` should use its own template, or strip the tag, and the site be redeployed. This is for the development session and is urgent.
3. **Site: maths written with a space before the closing `$`** (as in the 9 Nov article) is rejected by pandoc's dollar-maths reader. The revised article has none, but `build_site.py` could normalise this for robustness.
4. **Screen PDF:** 15 pp.; the author card shares p. 13 with the references.
5. **Article fixes at publication (18 Nov).** Conversion slips corrected in `substack/article.md` and on Substack: the worked-example table as a four-item list, "2nd edn" for Nelsen, plain primes in the Corollary 6 display, "(Slepian, 1962; not proved here)", and the check-list dagger replaced by an inline Kruskal citation. `tex2md.py` could handle these for later posts.

## QA, 18 Nov 2026 (revised edition)

- `make qa`: log issues 0, non-Type-1 fonts 0; X post lead 225 / 280, total 677 (one long post, plot attached).
- `make check` matches the table digit for digit; `make verify` and `make all` pass.
- Pages rendered and inspected: Result box on p. 1, author card on the references page, listing on one page, cross-reference names right (Lemma 3–4, Corollary 5–10).
- `dist/qt-00-hoeffding.zip` builds from a clean unzip.

## References

Hoeffding (1940, 1948); Lehmann (1966); Fréchet (1951); Sklar (1959); Spearman (1904); Kruskal (1958); Gini (1912); Slepian (1962); Esary, Proschan and Walkup (1967); Cuadras (2002); Embrechts, McNeil and Straumann (2002); Nelsen (2006). Full entries in [`references.bib`](references.bib).
