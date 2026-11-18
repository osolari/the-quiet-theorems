# The Quiet Theorems: topic backlog (snapshot)

Snapshot of the live backlog doc, taken 13 Nov 2026 (No. 00 status updated after its Substack publication). The doc is the source of truth: <https://claude.ai/artifact/4i9oRaXXahj9CRiEAvSVUH>

Scores 1 to 5 (author's judgement): **S**urprise (how little-known to a statistically literate ML audience), **E**legance (one-line statement), **D**epth (what a careful derivation adds), **R**elevance (to modern ML). Ties broken by Surprise, then Relevance.

Scope now includes machine-learning and AI theorems; the list will be extended accordingly.

Note: SURE (2) rests on Stein's lemma (16); a Stein's lemma, SURE, Tweedie arc is an option.

| Rank | Topic | One-line statement | S | E | D | R | Total | Status |
|---|---|---|---|---|---|---|---|---|
| 0 | Hoeffding's covariance identity | Cov(X,Y) = ∬ [H(x,y) − F(x)G(y)] dx dy | 4 | 5 | 5 | 4 | 18 | Published (No. 00) |
| 1 | de Bruijn's identity | d/dt h(X + √t Z) = ½ J(X + √t Z): entropy grows at half the Fisher information | 5 | 5 | 5 | 4 | 19 | Published (No. 01) |
| 2 | Stein's unbiased risk estimate (SURE) | E‖f(y) − θ‖² is estimable without θ: ‖f(y) − y‖² − nσ² + 2σ² div f(y) | 5 | 4 | 4 | 5 | 18 | Queued |
| 3 | James–Stein estimator | In d ≥ 3 the sample mean is inadmissible under squared loss | 5 | 4 | 5 | 4 | 18 | Queued |
| 4 | Price's theorem | For jointly Gaussian X,Y: ∂E[g(X,Y)]/∂ρ = E[∂²g/∂x∂y] | 5 | 5 | 4 | 4 | 18 | Queued |
| 5 | Tweedie's formula | E[θ \| y] = y + σ² ∇ log p(y): denoising is the score | 4 | 5 | 4 | 5 | 18 | Queued |
| 6 | Donsker–Varadhan formula | KL(P‖Q) = sup_f E_P f − log E_Q e^f | 4 | 5 | 4 | 5 | 18 | Queued |
| 7 | Ville's inequality and e-values | P(sup_t M_t ≥ 1/α) ≤ α for a non-negative martingale with M_0 = 1 | 4 | 5 | 4 | 5 | 18 | Queued |
| 8 | Gumbel-max trick | argmax_i (log p_i + G_i) ~ Categorical(p) for iid Gumbel G_i | 4 | 5 | 4 | 5 | 18 | Queued |
| 9 | Robbins' empirical Bayes | Poisson: E[θ \| x] = (x + 1) p(x + 1) / p(x), no prior needed | 5 | 5 | 3 | 4 | 17 | Queued |
| 10 | Wendel's theorem | P(n random symmetric points in R^d lie in a half-space) = 2^{−n+1} Σ_{k<d} C(n−1,k) | 5 | 5 | 4 | 3 | 17 | Queued |
| 11 | Prequential marginal likelihood | log p(x_1..n) = Σ log p(x_i \| x_<i): Bayesian Occam is sequential prediction | 4 | 5 | 3 | 5 | 17 | Queued |
| 12 | Pólya's urn | Draw fractions converge to a Beta; exchangeability without independence | 4 | 5 | 4 | 4 | 17 | Queued |
| 13 | Lindeberg's swapping proof of the CLT | Replace summands by Gaussians one at a time; Taylor to third order | 4 | 4 | 5 | 4 | 17 | Queued |
| 14 | Johnson–Lindenstrauss via concentration | k = O(ε⁻² log n) random projections preserve all pairwise distances | 3 | 4 | 5 | 5 | 17 | Queued |
| 15 | Fisher information is curvature of KL | KL(p_θ ‖ p_{θ+δ}) = ½ δᵀ I(θ) δ + o(‖δ‖²) | 3 | 5 | 4 | 5 | 17 | Queued |
| 16 | Stein's lemma | E[Z g(Z)] = E[g'(Z)], and this characterises the Gaussian | 3 | 5 | 4 | 5 | 17 | Queued |
| 17 | Inspection paradox | The interval covering a random time has mean E[L²]/E[L] ≥ E[L] | 5 | 5 | 3 | 3 | 16 | Queued |
| 18 | Attainable correlations (Fréchet–Hoeffding) | Two lognormals can never have correlation −1 (touched on in No. 00) | 5 | 4 | 4 | 3 | 16 | Queued |
| 19 | Efron–Stein inequality | Var f(X) ≤ ½ Σ E[(f(X) − f(X^(i)))²] | 4 | 4 | 4 | 4 | 16 | Queued |
| 20 | Rényi representation | Exponential order-statistic spacings are independent exponentials | 4 | 5 | 4 | 3 | 16 | Queued |
| 21 | Basu's theorem | Complete sufficient ⟂ ancillary; why X̄ ⟂ S² for Gaussians | 4 | 5 | 4 | 3 | 16 | Queued |
| 22 | Reflection principle | P(max_{s≤t} B_s ≥ a) = 2 P(B_t ≥ a) | 4 | 5 | 4 | 3 | 16 | Queued |
| 23 | Kac's lemma | Mean return time to a state = 1/π(state) | 4 | 5 | 4 | 3 | 16 | Queued |
| 24 | Gaussian Poincaré inequality | Var f(Z) ≤ E‖∇f(Z)‖² | 3 | 5 | 4 | 4 | 16 | Queued |
| 25 | Cramér–Rao from Cauchy–Schwarz | One line: Cov(T, score)² ≤ Var T · I(θ) | 2 | 5 | 4 | 5 | 16 | Queued |
| 26 | Pinsker's inequality | TV(P,Q) ≤ √(KL(P‖Q)/2) | 2 | 5 | 4 | 5 | 16 | Queued |
| 27 | Exponential families | Derivatives of log Z are cumulants; MLE is moment matching | 2 | 5 | 4 | 5 | 16 | Queued |
| 28 | Benford's law | Scale invariance forces P(first digit = d) = log₁₀(1 + 1/d) | 5 | 4 | 4 | 2 | 15 | Queued |
| 29 | Isserlis–Wick theorem | Gaussian moments are sums over pairings | 3 | 4 | 4 | 4 | 15 | Queued |
| 30 | Variance stabilisation (Anscombe) | 2√(X + 3/8) makes Poisson noise near-unit variance | 3 | 4 | 4 | 4 | 15 | Queued |
| 31 | Bernstein–von Mises | Posteriors become Gaussian, centred at the MLE, covariance I⁻¹/n | 3 | 3 | 5 | 4 | 15 | Queued |
| 32 | Exponential race | P(X_i is the minimum) = λ_i / Σ λ_j, and the minimum is independent of the winner | 3 | 5 | 3 | 4 | 15 | Queued |
| 33 | Conditional expectation as projection | Law of total variance is Pythagoras in L² | 2 | 5 | 3 | 5 | 15 | Queued |
| 34 | ELBO decomposition | log p(x) = ELBO(q) + KL(q ‖ p(· \| x)) | 2 | 5 | 3 | 5 | 15 | Queued |
| 35 | Score-function identity | ∇ E_θ[f] = E_θ[f ∇ log p_θ] (REINFORCE) | 2 | 5 | 3 | 5 | 15 | Queued |
| 36 | Hoeffding's lemma | E e^{λ(X−EX)} ≤ e^{λ²(b−a)²/8} for X in [a,b] | 2 | 4 | 4 | 5 | 15 | Queued |
| 37 | Neyman–Pearson lemma | The likelihood-ratio test is most powerful; three-line proof | 2 | 5 | 4 | 4 | 15 | Queued |
| 38 | Berkson's paradox | Conditioning on a collider manufactures correlation | 4 | 4 | 2 | 4 | 14 | Queued |
| 39 | Mean of Cauchys is Cauchy | The sample mean of n iid Cauchy has the same law as one draw | 3 | 5 | 3 | 3 | 14 | Queued |
| 40 | Box–Muller | χ²₂ is exponential, so the Gaussian radius is √(−2 log U) | 3 | 5 | 3 | 3 | 14 | Queued |
| 41 | Simpson's paradox | Reversal under aggregation as geometry of mixtures | 3 | 4 | 2 | 4 | 13 | Queued |
| 42 | Buffon's needle | P(cross) = 2ℓ/(πd), and Crofton's formula behind it | 3 | 5 | 3 | 2 | 13 | Queued |
| 43 | Gambler's ruin by optional stopping | P(hit b before −a) = a/(a + b) | 2 | 4 | 4 | 3 | 13 | Queued |
| 44 | Mills ratio bounds | φ(x) x/(1 + x²) ≤ 1 − Φ(x) ≤ φ(x)/x | 2 | 4 | 4 | 3 | 13 | Queued |
| 45 | Bertrand's paradox | "Random chord" has three different answers | 4 | 4 | 2 | 2 | 12 | Queued |
