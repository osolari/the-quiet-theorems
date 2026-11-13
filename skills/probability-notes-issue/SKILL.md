---
name: "probability-notes-issue"
description: "Build a Probability Notes issue (weekly probability/statistics post + derivation PDF + Overleaf zip) to the accepted No. 00 standard on the SAIM blog template."
---

# Probability Notes: building an issue

Reference: the accepted package `pn_00_hoeffding.zip` (Hoeffding's covariance identity, accepted 9 Nov 2026). Every issue must match it in structure, tone, rigour and packaging. Topics come from the ranked backlog doc "Probability Notes: topic backlog" (claude.ai artifact 4i9oRaXXahj9CRiEAvSVUH). British English, no em-dashes, terse.

## 0. Base tree

Start from the most recent accepted issue zip (ask the user to attach it if it is not in the session). Copy the whole tree and replace ONLY:
`project.tex`, `main.tex` body, `code/check.py`, `shared/bibliography/references.bib`, `post.txt`, `tweet.txt`, `pdf/`.
Never edit `saim-blog.cls`, `shared/brand/*`, other `shared/components/*`, `Makefile`, `latexmkrc`, `main-screen.tex`, `people.tex`. Series layer files `shared/components/math.tex` (notation, appended block) and `shared/components/theorems.tex` may only gain new macros, never change existing ones; record any addition in STANDARD.md.

## 1. project.tex

Title = name of the result; subtitle = the claim in words; `\ProjectSeriesLabel{Probability Notes}`; `\ProjectIssue{No. NN}` (two digits); reading time from word count (~230 wpm, round); tags = 4 to 6 substantive subject terms (no "derivations"); keywords include the result's name. Keep the accepted author bio block, `\ProjectAuthorPostnominal{, Ph.D.}` and empty `\ProjectLinks`.

## 2. main.tex skeleton (fixed order, none dropped or renamed)

Preamble exactly as No. 00 (class, metadata, math.tex, theorems.tex, hypersetup). Then:

1. `\maketitle`, then `tldr`: three plain sentences (familiar fact; the result, attributed to originator with year; what it means).
2. `\SecSetup`: probability space, symbol table (`\SAIMTableHead`, booktabs, `\small`), numbered `assumption`s, one sentence noting when a commonly quoted condition is stronger than needed, and definitions of any words used later (e.g. "uncorrelated").
3. `\SecResult`: one `mainresult` box holding the theorem `[Originator, Year]`; equivalent/variant forms as remarks with one-line proofs.
4. `\SecProof`: lemmas first (with proofs), then `\begin{proof}[Proof of \cref{thm:main}]` in `\step{...}` paragraphs. Every interchange of limit/integral/expectation/derivative gets an `\interchange{...}` paragraph that states the dominating function or Tonelli bound and joint measurability. Spell out product-space constructions (independent copies on Omega x Omega) and why cross terms factorise. Optional "Alternative route (sketch)." paragraph.
5. `\SecInsight`: `enumerate` of 2 to 4 bold-led items (what it says; comparison; role of the measure/structure; sign or equality cases), then one `pullquote`.
6. `\SecUses`: one opening sentence saying how the consequences follow; each consequence a `\subsection` with a precise statement and a proof (state any extra moment condition it needs).
7. `\SecExample`: one fully explicit computation (prefer a counterexample or extreme case), a table, and a TikZ figure in `figure[tbp]` using palette colours (Primary, Secondary, Rule, RuleDark, Ink, Muted) with an informative caption, referenced via `\cref`.
8. `\SecCheck`: one sentence on the methods per row, booktabs table Case / Exact / Numerical; exact values not proved in the PDF carry a dagger with a footnote-style line citing the source and "not proved here". Prefer exact (rational/symbolic) computation over Monte Carlo. End with a `\paragraph{Code.}` sentence pointing to `\cref{lst:check}` and `python3 code/check.py`.
9. `\SecNotes`: originator history only: who, when, original title (with translation if not English), what the original contains, how it reached a wide audience. Then `\bibliographystyle{plainnat}` and `\bibliography{shared/bibliography/references}` (no `\nocite` padding).
10. Author card wrapped exactly as No. 00:
```
{\let\SAIMplainauthors\ProjectAuthorsPlainDisplay
 \renewcommand{\ProjectAuthorsPlainDisplay}{\SAIMplainauthors\ProjectAuthorPostnominal}%
 \postauthorcard}
```
11. `\clearpage\appendix\section{Code}` and
`\lstinputlisting[style=python,basicstyle=\ttfamily\footnotesize\color{Ink},caption={Numerical check (\texttt{code/check.py}).},label={lst:check}]{code/check.py}`.

Conventions: sections unnumbered; refer to results with `\cref` only, never to sections by number. Label lemmas/corollaries/remarks with their type: `\label[lemma]{...}`. Notation: capitals for random variables, F_X, F_{X,Y}, \bar F_X, f_X, Z/\varphi/\Phi, copies X_1,X_2, `\E \Prob \Var \Cov \Corr \ind{} \dd \eqd \indep \iid \Normal \Unif \Expo`, `\dd x` at the end of integrals. Display long formulas with `aligned`.

## 3. Names, credit, references

- Prose names only the originators of the issue's result. Everyone else is credited by citation where their work is used (`\citet`/`\citep`), and side results are named descriptively ("rank correlation", "copula bounds", "association inequality", "a Gaussian comparison inequality"). Standard tool names (Cauchy-Schwarz, Fubini-Tonelli, Lebesgue measure, Jensen) are fine.
- Unproved facts: `\citep[not proved here; see][]{key}`.
- References: peer-reviewed papers, books, monographs, theses, arXiv only. Never X posts, blogs, newspapers. Every work whose definitions, proofs or results are used is listed; check each entry (authors, title in original language, journal, volume, number, pages, year) against a primary record via web search before use; flag any detail you could not verify.

## 4. code/check.py

Docstring: "Probability Notes No. NN: numerical check.", what it prints, requirements (Python/NumPy/SciPy minimum versions and the tested versions), run command. Lines at most 60 characters. Prints every number in the check table, one labelled line each. Use exact arithmetic (fractions) where the object allows; quadrature otherwise.

## 5. Posts (no X Premium)

Weighted length per X rules: code points 0-4351, 8192-8205, 8208-8223, 8242-8247 count 1; everything else (e.g. minus U+2212, double integral, subscript digits, less-or-equal) counts 2; any URL counts 23. Check with:
```python
import re
def wlen(s):
    s = re.sub(r'https?://\S+', 'x'*23, s)
    return sum(1 if (c<=4351 or 8192<=c<=8205 or 8208<=c<=8223 or 8242<=c<=8247) else 2 for c in map(ord, s))
```
- `post.txt`: two-tweet thread headed `1/2` and `2/2`, each body at most 280. Tweet 1: familiar fact, then "Originator (Year) showed ..." and the formula on its own line. Tweet 2: meaning in words, one consequence with citation-style attribution, then "Proofs, examples and code: [link]".
- `tweet.txt`: single tweet at most 280: fact, formula with originator and year, one-line meaning, "Probability Notes No. NN (proofs and code): [link]".
- Plain text, Unicode maths, no hashtags, no emoji, no @-mentions.

## 6. Build and QA gate (all must pass before delivery)

- `make` from a clean unzip builds `build/saim-post.pdf` (A4) and `build/saim-post-screen.pdf` (160 x 240 mm).
- Overleaf-style build of `main-screen.tex` from the root also succeeds.
- Logs: zero errors, LaTeX/package warnings, undefined references, overfull or underfull boxes (`grep -E "Warning|Overfull|Underfull|^!|undefined" build/*.log`, ignoring infwarerr).
- `pdffonts`: Type 1 only.
- Render pages to PNG and inspect: mainresult box not split, figure placement, code listing not wrapping, cross-reference names correct (Lemma, Corollary, not Theorem).
- `python3 code/check.py` output matches the table digit for digit.
- Proofread for overclaims: every claim proved or flagged; conditions minimal and stated; equality cases correct.
- Tweet weights verified with `wlen`.

## 7. Packaging

Copy `build/saim-post.pdf` to `pdf/pn-NN-slug.pdf` and the screen build to `pdf/pn-NN-slug-screen.pdf`, remove `build/`, zip the tree root-flat as `pn_NN_slug.zip` (matching the accepted file name style), test a clean unzip build, then send the zip plus both PDFs. Update the backlog doc: set the topic's Status and add a Draw log row.

## 8. Workflow

Phased, with one consolidated approval gate: deliver the full draft package, list open points and anything flagged (unverified reference details, unproved facts), and wait for approval before marking the issue Posted.