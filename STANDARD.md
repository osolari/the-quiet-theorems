# The Quiet Theorems: series standard (v1.1, 8 Nov 2026)

Built on the SAIM blog template v1.2 (`saim-blog.cls`). Series additions live in `shared/components/math.tex` (notation, appended) and `shared/components/theorems.tex` (theorem system, section skeleton, `mainresult` box). Template files are otherwise untouched.

Every issue = one post + one PDF + one Overleaf-ready zip. British English. No em-dashes.

## 1. The post (X)

Plain text, Unicode maths only. No X Premium: every tweet must be at most 280 by X's count (links count 23; maths symbols such as − and ∬ count 2). `post.txt` is a two-tweet thread; `tweet.txt` is the single-tweet version.

1. **Anchor**: the familiar fact the reader already knows (one or two lines).
2. **Question**: the natural question it raises.
3. **Result**: the identity or theorem, displayed on its own line, attributed to its originator(s) with year.
4. **Meaning**: one or two sentences on what it says, in words.
5. **Pointer**: "Derivations, conditions and examples: [PDF link]".

No hashtags, no emoji.

## 2. The PDF: fixed skeleton

Input `shared/components/math.tex` then `shared/components/theorems.tex` in `main.tex`. Set identity in `project.tex` (series label `The Quiet Theorems`, issue `No. NN`, reading time, tags). Open with a `tldr` box. Use the section macros in this order; none may be dropped or renamed.

| § | Macro | Contents | Length guide |
|---|---|---|---|
| title | `\maketitle` from `project.tex`; subtitle = the claim in words; then `tldr` | 2 to 3 sentences | 1 box |
| 1 | `\SecSetup` | Probability space, objects, every symbol used later, numbered assumptions `\begin{assumption}` | ½ page |
| 2 | `\SecResult` | The headline result in one `mainresult` box (unbreakable), with the exact hypotheses (cite assumptions by label); weaker/stronger variants as remarks | ¼ page |
| 3 | `\SecProof` | Lemmas first, then main proof in labelled `\step{}`s; every interchange of limits/integrals/expectations gets an `\interchange{}` paragraph; one alternative route sketched if instructive | 1 to 2 pages |
| 4 | `\SecInsight` | What the result *means*: interpretation, what it rules in/out, why it is surprising; ends with one `pullquote` | ½ page |
| 5 | `\SecUses` | Corollaries and applications, each a numbered subsection with statement + short proof | 1 to 2 pages |
| 6 | `\SecExample` | One fully explicit computation, ideally a counterexample or extreme case, with a TikZ figure | ½ to 1 page |
| 7 | `\SecCheck` | Table: case, exact, numerical; every unproved exact value flagged; a "Code." paragraph pointing to the listing and run command | ½ page |
| 8 | `\SecNotes` | Originator's history (who, when, original title), then originator references only | ¼ page |
| App. | `\appendix` | `\lstinputlisting[style=python]{code/check.py}` (lines ≤ 60 chars), after the author card | as needed |

## 3. Notation (series-wide, defined in `shared/components/math.tex`)

- Random variables capital (X, Y, Z); integration variables lower case.
- F_X marginal CDF, F_{X,Y} joint CDF, \bar F_X = 1 − F_X; densities f_X, f_{X,Y}.
- Z standard normal, φ and Φ its density and CDF.
- Independent copies X_1, X_2 (or X′); independence `\indep`; iid `\iid`.
- Macros: `\E \Prob \Var \Cov \Corr \ind{} \dd \eqd \R \Normal \Unif \Expo` (`\Exp` avoided).
- Sections are unnumbered (blog default): refer to results with `\cref`, never to sections by number. Label lemmas, corollaries and remarks with their type, e.g. `\label[lemma]{lem:x}` (cleveref precedes amsthm in the class).
- Integrals written with `\dd x` at the end.

## 4. Rigour rules

- **Names and credit**: prose names only the originators of the issue's result (e.g. Hoeffding in No. 0); everyone else is credited by citation (author and number) where their work is used, and side results are named descriptively ("rank correlation", "copula bounds", "association inequality"). Standard tool names (Cauchy–Schwarz, Fubini–Tonelli, Lebesgue measure) are allowed. References list every work whose definitions, proofs or results are used, with details checked against a primary record.

- State minimal sufficient moment/regularity conditions; say when a commonly quoted condition is stronger than needed.
- No claim without proof. Anything not proved in the PDF is flagged "(not proved here)".
- Every numerical claim in §7 is printed by `code/check.py`, whose docstring states its requirements.
- `make` builds A4 and screen variants with zero errors, warnings, overfull or underfull boxes, and Type 1 fonts only.

## 5. Files

```
qt-NN-slug/          % SAIM blog template tree, main.tex at the root
  main.tex  main-screen.tex  project.tex  people.tex  saim-blog.cls  shared/ ...
  code/check.py      % numerical check, listed in the PDF
  post.txt           % the X thread (two tweets, each at most 280)
  tweet.txt          % the X short post (at most 280, link counted as 23)
  STANDARD.md        % this file
```
Zip: `qt-NN-slug.zip`, containing `main.tex` (A4 entry), `main-screen.tex` (screen entry) and both built PDFs in `pdf/`. PDFs: `qt-NN-slug.pdf` (A4) and `qt-NN-slug-screen.pdf` (160 x 240 mm, for attaching to posts).
