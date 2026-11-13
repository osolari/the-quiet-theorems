# Probability Notes: session handoff (13 Nov 2026)

Paste this file (or point the new session at `claude/HANDOFF.md` in the "prob notes" Project), attach `pn_migration_bundle.zip`, and say: "Continue No. 01 from the handoff."

## 1. What the series is

Weekly post on a probability/statistics result, modelled on a 6 Nov 2026 X post about Hoeffding's covariance identity. Each issue ships:
- an X thread (`post.txt`, two tweets) and a single tweet (`tweet.txt`), each at most 280 weighted characters (URL = 23; code points outside the X weight-1 ranges count 2), no X Premium;
- a derivation PDF in A4 and screen (160 x 240 mm) layouts;
- an Overleaf-ready zip that builds with zero errors, warnings, undefined references, overfull or underfull boxes, Type 1 fonts only.

Base: SAIM blog template v1.2 (`saim-blog.cls`). Series additions: an appended notation block in `shared/components/math.tex` and `shared/components/theorems.tex` (theorem environments, `\step`, `\interchange`, eight section macros, unbreakable `mainresult` box). Template files are otherwise untouched.

## 2. Standard (authoritative copies)

- Accepted reference: `pn_00_hoeffding.zip` (accepted 9 Nov 2026). Its `STANDARD.md` and `main.tex` are also in the Project as `reference/pn-00-STANDARD.md` and `reference/pn-00-main.tex`.
- Skill: **probability-notes-issue** (saved to the account). It encodes the workflow, skeleton, credit rules, tweet-weight checker, QA gate and packaging. Load it first in the new session.
- Skeleton, in order: TL;DR; Setup and notation; Result (one `mainresult` box); Proof (lemmas, `\step`s, `\interchange` for every limit/integral swap); Insights (+ one pull quote); Uses and consequences; Worked example (+ TikZ figure); Numerical check (Case/Exact/Numerical table, "Code." paragraph); Notes (originator history only) + bibliography; author card with ", Ph.D."; `\clearpage` appendix with the code listing.
- Rules: British English, no em-dashes; prose names only the result's originators, everyone else by citation; side results named descriptively; references only peer-reviewed papers, books, theses, arXiv (no X posts, blogs, newspapers), each checked against a primary record; unproved facts marked "not proved here"; `\cref` only, lemma/corollary/remark labels typed (`\label[lemma]{...}`) because the class loads cleveref before amsthm; `\interchange` not `\justify` (ragged2e clash).
- Workflow: phased, one consolidated approval gate per issue.

## 3. Topic backlog

Doc "Probability Notes: topic backlog": https://claude.ai/artifact/4i9oRaXXahj9CRiEAvSVUH
46 ranked topics (Surprise/Elegance/Depth/Relevance, each 1 to 5), status dropdowns, draw log. Top of the queue after No. 01: SURE (2), James–Stein (3), Price's theorem (4), Tweedie's formula (5). Note: SURE rests on Stein's lemma (rank 16); a Stein's lemma, SURE, Tweedie arc was suggested.

## 4. Status

| Issue | Topic | State |
|---|---|---|
| No. 00 | Hoeffding's covariance identity | Published on Substack 9 Nov 2026 (https://omidsolari.substack.com/p/probability-notes-no-00-hoeffdings); X not yet posted |
| No. 01 | De Bruijn's identity | Draft delivered 9 Nov 2026, awaiting approval |

### No. 01 draft (in the bundle as `pn_01_debruijn.zip`)

Content: for X with E X² < ∞ (any law, discrete allowed) and independent Z ~ N(0,1), d/dt h(X+√tZ) = ½ J(X+√tZ), with J ≤ 1/t. Self-contained proof via heat-kernel bounds, Jensen lower bound on log p_t, score as posterior mean, dominated convergence and integration by parts along tail sequences. Uses: J ≥ 1/Var with Gaussian equality; entropy sandwich ½log((σ²+b)/(σ²+a)) ≤ h(Y_b) − h(Y_a) ≤ ½log(b/a); J = 1/t − mmse/t², i.e. the information–estimation relation. Example: X = ±1, closed forms, figure of t·J(Y_t). Check: Gaussian 0.250000 and 0.500000 exact; ±1 residuals −1.9e−11 and 2.2e−16; increment 0.1833 in [0.1438, 0.3466]. A4 9 pp., screen 11 pp., QA gate passed. Tweet weights 226 / 280 (thread), 274 (single).

References: Stam 1959 (Inf. Control 2(2):101–112); Shannon 1948 (BSTJ 27:379–423, 623–656); Barron 1986 (Ann. Probab. 14(1):336–342); Guo, Shamai, Verdú 2005 (IEEE Trans. IT 51(4):1261–1282); Efron 2011 (JASA 106(496):1602–1614).

Open points awaiting the user:
1. De Bruijn's communication to Stam, "equation (2.12)", and Barron's integral-form proof are confirmed via secondary sources only, not Stam's or Barron's text.
2. Optional "Alternative route" paragraph was dropped to keep the author card off an orphan page.
3. Tweet 2 of the thread is exactly at 280.
4. File naming: zip `pn_01_debruijn.zip` (underscores, matching the user's upload) vs STANDARD.md's `pn-NN-slug.zip`; PDFs are `pn-01-debruijn*.pdf`. Needs a decision, then align STANDARD.md and the skill.
5. Backlog: de Bruijn's Status dropdown still reads Queued; draw-log row added.

## 5. Next actions

1. Get the user's verdict on No. 01 and the five open points; revise, rebuild, rerun the QA gate, redeliver.
2. Mark No. 01 in the backlog (Status, draw log).
3. Optionally set up a weekly scheduled task to draft the next queued topic for review (offered, not yet agreed).

## 6. Repository

Git repo `probability-notes` at `~/workspace/projects/probability-notes` on the author's machine. Layout: `skeleton/` (shared template + series layer), `docs/posts/NN-slug/` (issue-specific files, PDFs, pinned links), `scripts/assemble.sh` (rebuilds an Overleaf-ready tree; reproduces the accepted No. 00 package file for file), `Makefile` (`new`, `check`, `qa`, `pdfs`, `zip`, `all`), `BACKLOG.md` snapshot, `skills/probability-notes-issue/SKILL.md`, pinned `requirements.txt`. New issues start with `make new P=NN-slug`.

## 7. Formats and site (added 13 Nov 2026)

Every post now also has `article.md` (Markdown, MathJax, embedded figures), `notebook.ipynb` (executed), `img/`, `meta.json` (status and published links) and `code/figures.py`. The site for GitHub Pages is built by `make site` and deployed to the `gh-pages` branch (workflow or `make pages PUSH=1`); only accepted and published posts appear. Full procedure and link checklist: `docs/POST_GUIDE.md`. No GitHub remote exists yet.

## 8. Substack (added 13 Nov 2026)

No. 00 was published on Substack on 9 Nov 2026; its published text, figure and Substack details are in `docs/posts/00-hoeffding/` (`substack/`, `meta.json`, `README.md`) and it is the reference post. Every post now carries `substack/article.md` (drafted by `make formats`, hand-finished, frozen on publication) instead of `article.md`/`img/`. X posts link to the Substack URL. House style and publishing procedure: `docs/POST_GUIDE.md` 7a and 7b.
