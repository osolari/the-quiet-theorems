# De Bruijn's identity

*Under Gaussian smoothing, differential entropy grows at exactly half the rate of Fisher information*

**Probability Notes No. 01** · Omid Shams Solari, Ph.D. · 9 November 2026

[PDF (A4)](pdf/pn-01-debruijn.pdf) · [PDF (screen)](pdf/pn-01-debruijn-screen.pdf) · [Notebook](notebook.ipynb) · [LaTeX source](main.tex)

> **TL;DR.** Adding independent Gaussian noise to a random variable makes it more spread out, so its differential entropy grows with the noise variance. De Bruijn’s identity, published by Stam (1959), gives the rate exactly: the derivative of the entropy with respect to the noise variance is half the Fisher information of the noisy variable. Fisher information is therefore the speed at which Gaussian smoothing creates entropy.

## Setup and notation

Let $X$ and $Z$ be independent random variables on a probability space $(\Omega,\mathcal{F},\mathbb{P})$, with $Z\sim\mathcal{N}(0,1)$ and $X$ arbitrary (it may be discrete). For $t>0$ set

$$
Y_t\mathrel{:=}X+\sqrt t\,Z .
$$

| Symbol                                                                      | Meaning                               |
|:----------------------------------------------------------------------------|:--------------------------------------|
| $\varphi_t(z)=(2\pi t)^{-1/2}e^{-z^2/(2t)}$                                 | density of $\mathcal{N}(0,t)$         |
| $p_t(y)=\mathbb{E}\,\varphi_t(y-X)$                                         | density of $Y_t$ (Lemma 4)            |
| $p_t'$, $p_t''$; $\partial_t p_t$                                           | derivatives in $y$; derivative in $t$ |
| $h(Y_t)=-\int_{\mathbb{R}}p_t\log p_t\mathrm{d}y$                           | differential entropy (nats)           |
| $\rho_t=p_t'/p_t$                                                           | score of $Y_t$                        |
| $J(Y_t)=\int_{\mathbb{R}}(p_t')^2/p_t\mathrm{d}y=\mathbb{E}\,\rho_t(Y_t)^2$ | Fisher information of $Y_t$           |
| $\mu=\mathbb{E}X$, $\sigma^2=\operatorname{Var}X$                           | mean and variance of $X$              |

$J(Y_t)$ is the Fisher information of the location family $\{p_t(\cdot-\theta):\theta\in\mathbb{R}\}$, since $\partial_\theta\log p_t(y-\theta)=-\rho_t(y-\theta)$.

**Assumption A1.** $\mathbb{E}X^2<\infty$.

Statements of the identity often assume that $X$ has a smooth density; none is needed here, because the Gaussian noise supplies the regularity. Assumption A1 is used only to make $h(Y_t)$ finite and to control the tails of $\log p_t$.

## Result

> **Theorem 1 (de Bruijn; Stam, 1959).** Under Assumption A1, for every $t>0$ the entropy $h(Y_t)$ and the Fisher information $J(Y_t)$ are finite, $J(Y_t)\le 1/t$, and $t\mapsto h(Y_t)$ is differentiable on $(0,\infty)$ with
>
> $$
> \frac{\mathrm{d}}{\mathrm{d}t}\,h\big(X+\sqrt t\,Z\big)=\frac12\,J\big(X+\sqrt t\,Z\big). \tag{1}
> $$

**Remark 2.** For $X\sim\mathcal{N}(\mu,\sigma^2)$, $Y_t\sim\mathcal{N}(\mu,\sigma^2+t)$, so $h(Y_t)=\tfrac12\log\big(2\pi e(\sigma^2+t)\big)$ and $\rho_t(y)=-(y-\mu)/(\sigma^2+t)$, giving $J(Y_t)=1/(\sigma^2+t)$. Both sides of (1) equal $1/\big(2(\sigma^2+t)\big)$.

## Proof

Throughout, $0<a<b$ and $t\in[a,b]$; constants may depend on $a$, $b$ and $\mathbb{E}X^2$ but not on $t$ or $y$.

**Lemma 3.** The kernel satisfies $\partial_t\varphi_t=\tfrac12\varphi_t''$, with $\varphi_t'(z)=-(z/t)\varphi_t(z)$ and $\varphi_t''(z)=(z^2/t^2-1/t)\varphi_t(z)$. With $\Gamma(z)\mathrel{:=}(2\pi a)^{-1/2}e^{-z^2/(2b)}$,

$$
\varphi_t\le\Gamma,\qquad
|\varphi_t'(z)|\le\tfrac{|z|}{a}\Gamma(z),\qquad
|\varphi_t''(z)|\le\big(\tfrac{z^2}{a^2}+\tfrac1a\big)\Gamma(z). \tag{2}
$$

*Proof.* Differentiate $\varphi_t$ directly: $\partial_t\varphi_t=\big(\tfrac{z^2}{2t^2}-\tfrac1{2t}\big)\varphi_t=\tfrac12\varphi_t''$. The bounds follow from $t^{-1/2}\le a^{-1/2}$, $t^{-1}\le a^{-1}$ and $e^{-z^2/(2t)}\le e^{-z^2/(2b)}$. ∎

**Lemma 4.** $Y_t$ has the density $p_t(y)=\mathbb{E}\,\varphi_t(y-X)>0$. The map $(t,y)\mapsto p_t(y)$ is continuously differentiable in $t$ and twice in $y$ on $(0,\infty)\times\mathbb{R}$, with

$$
p_t^{(k)}(y)=\mathbb{E}\,\varphi_t^{(k)}(y-X)\ (k=1,2),\qquad
\partial_t p_t=\tfrac12\,p_t'' . \tag{3}
$$

Moreover $p_t'(y)\to0$ as $|y|\to\infty$, and for $t\in[a,b]$ and all $y$,

$$
|\log p_t(y)|\le A+y^2/a,\qquad A\mathrel{:=}\tfrac12|\log(2\pi a)|+\tfrac12|\log(2\pi b)|+\mathbb{E}X^2/a . \tag{4}
$$

*Proof.* **Step: Density.** For a Borel set $B$, conditioning on $X$ (Fubini, using $X\mathrel{\perp\!\!\!\perp}Z$) gives $\mathbb{P}(Y_t\in B)=\mathbb{E}\int_B\varphi_t(y-X)\mathrm{d}y=\int_B\mathbb{E}\,\varphi_t(y-X)\mathrm{d}y$. Positivity holds because $\varphi_t>0$.

*Justification (differentiation under $\mathbb{E}$).* By (2), $\varphi_t$, $\varphi_t'$, $\varphi_t''$ and $\partial_t\varphi_t$ are bounded on $[a,b]\times\mathbb{R}$ by constants, since $\sup_z(1+z^2)\Gamma(z)<\infty$. A constant is integrable under $\mathbb{P}$, so dominated convergence lets each derivative pass under $\mathbb{E}$ and gives continuity of the results in $(t,y)$. Since $[a,b]$ is arbitrary this holds on $(0,\infty)$, and $\partial_t p_t=\mathbb{E}\,\partial_t\varphi_t(y-X)=\tfrac12\mathbb{E}\,\varphi_t''(y-X)=\tfrac12p_t''$.

**Step: Decay.** $\varphi_t'(y-X)\to0$ pointwise as $|y|\to\infty$ and is bounded, so $p_t'(y)\to0$ by dominated convergence.

**Step: Log bound.** Upper: $p_t\le(2\pi a)^{-1/2}$, so $\log p_t\le\tfrac12|\log(2\pi a)|$. Lower: $\log$ is concave and $\mathbb{E}\log\varphi_t(y-X)=-\tfrac12\log(2\pi t)-\mathbb{E}(y-X)^2/(2t)$ is finite by Assumption A1, so Jensen’s inequality and $(y-X)^2\le2y^2+2X^2$ give

$$
\log p_t(y)\ge\mathbb{E}\log\varphi_t(y-X)\ge-\tfrac12\log(2\pi b)-\frac{y^2+\mathbb{E}X^2}{a}.
$$

∎

**Lemma 5.** For $t>0$, $\mathbb{E}[Z\mid Y_t]=-\sqrt t\,\rho_t(Y_t)$ almost surely. Consequently

$$
J(Y_t)=\frac{\mathbb{E}\big[(\mathbb{E}[Z\mid Y_t])^2\big]}{t}\le\frac1t . \tag{5}
$$

*Proof.* Let $g$ be bounded and Borel. Substituting $y=x+\sqrt t\,z$ in the inner integral,

$$
\begin{aligned}
\mathbb{E}[Z\,g(Y_t)]&=\mathbb{E}\int_{\mathbb{R}}z\,g(X+\sqrt t z)\varphi_1(z)\mathrm{d}z\\
&=\int_{\mathbb{R}}g(y)\,\mathbb{E}\Big[\tfrac{y-X}{\sqrt t}\,\varphi_t(y-X)\Big]\mathrm{d}y
=-\sqrt t\int_{\mathbb{R}}g\,p_t'\mathrm{d}y,
\end{aligned}
$$

using $\mathbb{E}[(y-X)\varphi_t(y-X)]=-t\,p_t'(y)$ from (3) and Lemma 3. The exchange of $\mathbb{E}$ and $\mathrm{d}y$ is Fubini: $\mathbb{E}\iint|z\,g|\varphi_1\mathrm{d}z\le\sup|g|$. The right side equals $\mathbb{E}[g(Y_t)\,(-\sqrt t\,\rho_t(Y_t))]$, and $\mathbb{E}|\rho_t(Y_t)|=\int|p_t'|\mathrm{d}y\le\mathbb{E}|Z|/\sqrt t$ by the same computation with $g=\operatorname{sign}p_t'$. As $-\sqrt t\rho_t(Y_t)$ is $\sigma(Y_t)$-measurable and integrable, it is $\mathbb{E}[Z\mid Y_t]$. Then $J(Y_t)=\mathbb{E}\rho_t(Y_t)^2=\mathbb{E}[(\mathbb{E}[Z\mid Y_t])^2]/t$, and conditional Jensen gives $\mathbb{E}[(\mathbb{E}[Z\mid Y_t])^2]\le\mathbb{E}Z^2=1$. ∎

**Lemma 6.** If $f\ge0$ is integrable on $\mathbb{R}$, there are $R_n\to\infty$ and $R_n'\to\infty$ with $f(R_n)\to0$ and $f(-R_n')\to0$.

*Proof.* Otherwise $f\ge\varepsilon>0$ on some half-line, contradicting integrability. ∎

*Proof of Theorem 1.* **Step: Finiteness.** By (4), $|p_t\log p_t|\le p_t(A+y^2/a)$, whose integral is $A+\mathbb{E}Y_t^2/a=A+(\mathbb{E}X^2+t)/a<\infty$. So $h(Y_t)$ is finite. $J(Y_t)\le1/t$ is Lemma 5.

**Step: Differentiating the entropy.** Fix $y$. Since $p_t(y)>0$ is $C^1$ in $t$, so is $\eta_t(y)\mathrel{:=}-p_t(y)\log p_t(y)$, with $\partial_t\eta_t=-\partial_tp_t\,(1+\log p_t)$.

*Justification (dominated convergence in $t$).* By (3), (2) and (4), for $t\in[a,b]$,

$$
|\partial_t\eta_t(y)|\le G(y)\mathrel{:=}\tfrac12\,\mathbb{E}\Big[\Big(\tfrac{(y-X)^2}{a^2}+\tfrac1a\Big)\Gamma(y-X)\Big]\,\big(1+A+y^2/a\big).
$$

$G$ is integrable: by Tonelli, the substitution $z=y-X$ and $y^2\le2z^2+2X^2$,

$$
\int_{\mathbb{R}}G\mathrm{d}y\le\tfrac12\,\mathbb{E}\int_{\mathbb{R}}\Big(\tfrac{z^2}{a^2}+\tfrac1a\Big)\Gamma(z)\Big(1+A+\tfrac{2z^2+2X^2}{a}\Big)\mathrm{d}z<\infty,
$$

since $\Gamma$ has finite moments of all orders and $\mathbb{E}X^2<\infty$. By the mean value theorem the difference quotients of $\eta_t(y)$ in $t$ are bounded by $G(y)$, so dominated convergence gives, for $t\in(a,b)$ and hence for all $t>0$,

$$
\frac{\mathrm{d}}{\mathrm{d}t}h(Y_t)=-\int_{\mathbb{R}}\partial_tp_t\,(1+\log p_t)\mathrm{d}y=-\frac12\int_{\mathbb{R}}p_t''\mathrm{d}y-\frac12\int_{\mathbb{R}}p_t''\log p_t\mathrm{d}y,
$$

both integrals converging absolutely by the same bound.

**Step: The constant term vanishes.** $\int_{-R'}^{R}p_t''\mathrm{d}y=p_t'(R)-p_t'(-R')\to0$ by Lemma 4.

**Step: Integration by parts.** On $[-R',R]$, since $(\log p_t)'=\rho_t$,

$$
\int_{-R'}^{R}p_t''\log p_t\mathrm{d}y=\big[p_t'\log p_t\big]_{-R'}^{R}-\int_{-R'}^{R}\frac{(p_t')^2}{p_t}\mathrm{d}y .
$$

*Justification (limits along sequences).* $|p_t'\log p_t|\le|p_t'|(A+y^2/a)$, which is integrable by the Tonelli argument above with $|\varphi_t'|\le(|z|/a)\Gamma$. By Lemma 6 choose $R_n,R_n'\to\infty$ along which the boundary term vanishes. Along these sequences the left side tends to $\int p_t''\log p_t$ (dominated convergence) and the last integral increases to $J(Y_t)$ (monotone convergence).

**Step: Conclusion.** Hence $-\tfrac12\int p_t''\log p_t\mathrm{d}y=\tfrac12J(Y_t)$, which is (1). ∎

## Insights

1.  **Fisher information as a rate.** Entropy measures spread; Fisher information measures how sharply the density varies, through the size of its score. Under Gaussian smoothing the two are tied: the more structure $p_t$ still has, the faster smoothing destroys it. For a Gaussian input there is least structure for its variance, and entropy grows at the slowest possible rate (Corollary 7).

2.  **The heat equation underneath.** The density $p_t$ solves $\partial_tp_t=\tfrac12p_t''$, and (1) says that the entropy production of this flow is $\tfrac12J$. Since $J(Y_t)>0$ (a density cannot have $p_t'\equiv0$ on $\mathbb{R}$), entropy increases strictly along the flow.

3.  **No regularity is needed from $X$.** $X$ can be discrete: one instant of noise already makes $p_t$ positive and smooth (Lemma 4). This makes Gaussian smoothing a convenient device for transferring statements about smooth densities to arbitrary laws.

4.  **The score is a denoiser.** By Lemma 5, $\rho_t(Y_t)=-\mathbb{E}[Z\mid Y_t]/\sqrt t$: the score of the noisy density is the best estimate of the injected noise, rescaled. Equivalently $\mathbb{E}[X\mid Y_t]=Y_t+t\,\rho_t(Y_t)$, the Gaussian case of an empirical Bayes formula for posterior means (Efron, 2011 \[2\]). Fisher information is the mean square of this denoiser.

> *Gaussian noise creates entropy at exactly half the rate of Fisher information.*

## Uses and consequences

The results below combine Theorem 1 with a lower bound on $J$ and with the posterior form of the score in Lemma 5.

### A lower bound on Fisher information

**Corollary 7.** Under Assumption A1, $J(Y_t)\ge1/\operatorname{Var}(Y_t)=1/(\sigma^2+t)$ for every $t>0$, with equality if and only if $X$ is Gaussian (possibly constant).

*Proof.* Let $m=\mathbb{E}Y_t$ and $v=\operatorname{Var}Y_t=\sigma^2+t$. On $[-R',R]$, $\int(y-m)p_t'\mathrm{d}y=[(y-m)p_t]_{-R'}^{R}-\int p_t\mathrm{d}y$. Both $|y-m|\,p_t$ and $|y-m|\,|p_t'|$ are integrable (the latter by the Tonelli argument in the proof of Theorem 1), so along sequences from Lemma 6 the boundary term vanishes and $\mathbb{E}[(Y_t-m)\rho_t(Y_t)]=\int(y-m)p_t'\mathrm{d}y=-1$. Cauchy–Schwarz gives $1\le v\,J(Y_t)$.

Equality forces $\rho_t(Y_t)=c\,(Y_t-m)$ almost surely, and then $c=-1/v$ from the identity just shown. As $p_t>0$ and $\rho_t$ is continuous, $\rho_t(y)=-(y-m)/v$ for all $y$, so $p_t$ is the $\mathcal{N}(m,v)$ density. The characteristic function of $X$ is then $e^{ims-vs^2/2}/e^{-ts^2/2}=e^{ims-\sigma^2s^2/2}$, so $X\sim\mathcal{N}(m,\sigma^2)$. Conversely Remark 2 gives equality for Gaussian $X$. ∎

### An entropy sandwich

**Corollary 8.** Under Assumption A1, for $0<a<b$,

$$
\frac12\log\frac{\sigma^2+b}{\sigma^2+a}\;\le\;h(Y_b)-h(Y_a)\;\le\;\frac12\log\frac ba ,
$$

with equality on the left if and only if $X$ is Gaussian.

*Proof.* By Theorem 1, Lemma 5 and Corollary 7, $t\mapsto h(Y_t)$ is differentiable with derivative between $1/(2(\sigma^2+t))$ and $1/(2t)$ on $[a,b]$. A differentiable function with bounded derivative is Lipschitz, hence absolutely continuous, so $h(Y_b)-h(Y_a)=\tfrac12\int_a^bJ(Y_t)\mathrm{d}t$; integrate the bounds. Equality on the left forces $J(Y_t)=1/(\sigma^2+t)$ for almost every $t$, and so Gaussian $X$ by Corollary 7. ∎

The upper bound is the entropy increment of pure noise, $h(\sqrt bZ)-h(\sqrt aZ)$: smoothing an arbitrary input never adds entropy faster than smoothing a point mass.

### Fisher information and estimation error

Let $\mathrm{mmse}(t)\mathrel{:=}\mathbb{E}\big(X-\mathbb{E}[X\mid Y_t]\big)^2$, the minimum mean-square error in estimating $X$ from $Y_t$.

**Corollary 9.** Under Assumption A1, for every $t>0$,

$$
J(Y_t)=\frac1t-\frac{\mathrm{mmse}(t)}{t^2},
\qquad\text{hence}\qquad
\frac{\mathrm{d}}{\mathrm{d}t}h(Y_t)=\frac1{2t}-\frac{\mathrm{mmse}(t)}{2t^2}.
$$

*Proof.* Since $X=Y_t-\sqrt tZ$, $X-\mathbb{E}[X\mid Y_t]=-\sqrt t\,(Z-\mathbb{E}[Z\mid Y_t])$, so $\mathrm{mmse}(t)=t\,\mathbb{E}(Z-\mathbb{E}[Z\mid Y_t])^2=t\big(1-\mathbb{E}[(\mathbb{E}[Z\mid Y_t])^2]\big)$ by orthogonality of $Z-\mathbb{E}[Z\mid Y_t]$ to $\sigma(Y_t)$. Substitute into (5), then use (1). ∎

Write $I(t)\mathrel{:=}h(Y_t)-h(\sqrt tZ)=h(Y_t)-\tfrac12\log(2\pi et)$, which is the mutual information between $X$ and $Y_t$ (not proved here; see Guo et al., 2005 \[3\]). Corollary 9 gives $I'(t)=-\mathrm{mmse}(t)/(2t^2)$, and with the signal-to-noise ratio $s=1/t$,

$$
\frac{\mathrm{d}I}{\mathrm{d}s}=\frac12\,\mathrm{mmse}(1/s),
$$

the information–estimation relation of Guo et al. (2005) \[3\]. De Bruijn’s identity and that relation are the same statement in different coordinates.

## Worked example

Let $X$ take the values $\pm1$ with probability $\tfrac12$ each, so $\mu=0$, $\sigma^2=1$. Then $Y_t$ is a two-component Gaussian mixture and everything is explicit:

$$
\begin{aligned}
p_t(y)&=\tfrac12\big[\varphi_t(y-1)+\varphi_t(y+1)\big]=\varphi_t(y)\,e^{-1/(2t)}\cosh(y/t),\\
\mathbb{E}[X\mid Y_t=y]&=\tanh(y/t),
\end{aligned}
$$

so $\rho_t(y)=\big(\tanh(y/t)-y\big)/t$ and, using $\mathbb{E}Y_t^2=1+t$,

$$
h(Y_t)=\tfrac12\log(2\pi et)+\tfrac1t-\mathbb{E}\log\cosh(Y_t/t),
\qquad
\mathrm{mmse}(t)=1-\mathbb{E}\tanh^2(Y_t/t).
$$

The last formula uses $\mathbb{E}[X\tanh(Y_t/t)]=\mathbb{E}\tanh^2(Y_t/t)$, by the tower property.

**Two regimes.** For small $t$ the components barely overlap: $\mathbb{E}\log\cosh(Y_t/t)\approx1/t-\log2$, so $h(Y_t)\approx\tfrac12\log(2\pi et)+\log2$, the entropy of noise plus one bit, and $t\,J(Y_t)\approx1$. For large $t$ the mixture is close to $\mathcal{N}(0,1+t)$ and $t\,J(Y_t)\approx t/(1+t)$. Figure 1 shows $t\,J(Y_t)$ between the two bounds of Corollary 7 and Lemma 5, $t/(1+t)\le tJ(Y_t)\le1$.

![Figure 1](img/figure-1.png)

*Figure 1.* Scaled Fisher information $t\,J(Y_t)$ for $X=\pm1$ (computed by `code/check.py`) and for Gaussian $X$ with the same variance. The Gaussian input has the least Fisher information, so its entropy grows most slowly; the two-point input starts at the noise-only rate and merges with the Gaussian curve as the noise dominates.

## Numerical check

All quantities use adaptive quadrature of the closed forms above; $\mathrm{d}h/\mathrm{d}t$ uses a four-point central difference with step $10^{-3}$.

| Case                                                                           |        Exact         |      Numerical       |
|:-------------------------------------------------------------------------------|:--------------------:|:--------------------:|
| $X\sim\mathcal{N}(0,1)$, $t=1$: $\mathrm{d}h/\mathrm{d}t$                      |        $1/4$         |      $0.250000$      |
| $X\sim\mathcal{N}(0,1)$, $t=1$: $J(Y_t)$                                       |        $1/2$         |      $0.500000$      |
| $X=\pm1$, $t=\tfrac12$: $\mathrm{d}h/\mathrm{d}t-\tfrac12J(Y_t)$               |         $0$          | $-1.9\times10^{-11}$ |
| $X=\pm1$, $t=\tfrac12$: $J(Y_t)-\big(\tfrac1t-\tfrac{\mathrm{mmse}}{t^2}\big)$ |         $0$          | $2.2\times10^{-16}$  |
| $X=\pm1$: $h(Y_1)-h(Y_{1/2})$                                                  | in $[0.1438,0.3466]$ |       $0.1833$       |

Rows 1–2 check Remark 2; rows 3–5 check (1), Corollary 9 and Corollary 8 for a discrete input. Rows 3–4 are at rounding level, so their last digits may vary across library versions.

**Code.** Every number in the table and the curve in Figure 1 are printed by `code/check.py` (the code at the end; run `python3 code/check.py`), whose docstring gives the requirements.

## Notes

The identity is due to N. G. de Bruijn, who communicated it to A. J. Stam. Stam published it as equation (2.12) of *Some inequalities satisfied by the quantities of information of Fisher and Shannon* (Stam, 1959 \[5\]), where, together with an inequality for the Fisher information of sums, it yields a proof of the entropy power inequality stated by Shannon (1948) \[4\]. Stam gave the identity in differential form; a proof in integral form appears in Barron (1986) \[1\], where it underpins a central limit theorem in relative entropy.

## References

1. Andrew R. Barron. Entropy and the central limit theorem. *Annals of Probability* 14(1):336–342, 1986.
2. Bradley Efron. Tweedie's formula and selection bias. *Journal of the American Statistical Association* 106(496):1602–1614, 2011.
3. Dongning Guo, Shlomo Shamai, Sergio Verdú. Mutual information and minimum mean-square error in Gaussian channels. *IEEE Transactions on Information Theory* 51(4):1261–1282, 2005.
4. C. E. Shannon. A mathematical theory of communication. *Bell System Technical Journal* 27:379–423, 623–656, 1948.
5. A. J. Stam. Some inequalities satisfied by the quantities of information of Fisher and Shannon. *Information and Control* 2(2):101–112, 1959.

## Code

Numerical check (`code/check.py`); run `python3 code/check.py`, or open [the notebook](notebook.ipynb).

```python
"""Probability Notes No. 01: numerical check.

Prints every number in the PDF's check table.
Requires Python >= 3.8, NumPy >= 1.20 and
SciPy >= 1.6.
Tested with Python 3.13, NumPy 2.5, SciPy 1.18.
Run: python3 check.py
"""
import numpy as np
from scipy.integrate import quad

def logphi(z, t):
    return -z * z / (2 * t) - 0.5 * np.log(2 * np.pi * t)

# Y_t = X + sqrt(t) Z for two inputs X.
# Each returns (log p_t(y), score p_t'(y)/p_t(y)).
def gauss(y, t):   # X ~ N(0, 1)
    v = 1 + t
    return logphi(y, v), -y / v

def lcosh(u):      # log cosh, overflow-safe
    u = abs(u)
    return u + np.log1p(np.exp(-2 * u)) - np.log(2)

def rade(y, t):    # X = +1 or -1, prob 1/2 each
    lp = logphi(y, t) + lcosh(y / t) - 1 / (2 * t)
    return lp, (np.tanh(y / t) - y) / t

def E(f, model, t):
    """E[f(y)] under Y_t, adaptive quadrature."""
    L = 2 + 14 * np.sqrt(1 + t)
    def g(y):
        return np.exp(model(y, t)[0]) * f(y)
    return quad(g, -L, L, limit=400, points=[0],
                epsabs=1e-14, epsrel=1e-13)[0]

def h(model, t):        # differential entropy
    return E(lambda y: -model(y, t)[0], model, t)

def J(model, t):        # Fisher information
    return E(lambda y: model(y, t)[1] ** 2, model, t)

def dh(model, t, d=1e-3):   # 4-point difference
    f = [h(model, t + k * d) for k in (-2, -1, 1, 2)]
    return (f[0] - 8 * f[1] + 8 * f[2] - f[3]) / (12 * d)

# 1-2. Gaussian X, t = 1: dh/dt = J/2 = 1/4.
print(f"Gauss dh/dt:   {dh(gauss, 1.0):.6f}")
print(f"Gauss J:       {J(gauss, 1.0):.6f}")

# 3. Rademacher X, t = 1/2: de Bruijn residual.
t = 0.5
a, b = dh(rade, t), J(rade, t) / 2
print(f"Rade dh/dt:    {a:.6f}")
print(f"Rade J/2:      {b:.6f}")
print(f"Difference:    {a - b:.1e}")

# 4. Fisher information versus MMSE:
#    J = 1/t - mmse/t^2, mmse = 1 - E tanh^2(Y/t).
th2 = E(lambda y: np.tanh(y / t) ** 2, rade, t)
mmse = 1 - th2
print(f"Rade mmse:     {mmse:.6f}")
a, b = J(rade, t), 1 / t - mmse / t ** 2
print(f"Rade J:        {a:.6f}")
print(f"1/t-mmse/t^2:  {b:.6f}")
print(f"Difference:    {a - b:.1e}")

# 5. Entropy sandwich on [1/2, 1], Var X = 1.
inc = h(rade, 1.0) - h(rade, 0.5)
lo, hi = 0.5 * np.log(2 / 1.5), 0.5 * np.log(2)
print(f"Increment:     {inc:.4f}")
print(f"Bounds:        [{lo:.4f}, {hi:.4f}]")

# 6. Figure data: t J(Y_t) for Rademacher X
#    and the Gaussian lower bound t/(1+t).
for e in np.linspace(-1.5, 1.5, 25):
    s = 10 ** e
    print(f"fig {e:+.2f} {s * J(rade, s):.4f}"
          f" {s / (1 + s):.4f}")
```
