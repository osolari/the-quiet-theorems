# Probability Notes No. 00: Hoeffding’s covariance identity

*Independence is a pointwise equality of distribution functions; uncorrelatedness is the same equality, integrated*

Published 9 November 2026: https://omidsolari.substack.com/p/probability-notes-no-00-hoeffdings

> **TL;DR.** Two random variables are independent exactly when their joint distribution function factorises into the product of its marginals. Hoeffding (1940) showed that their covariance is the integral of the difference between the two. Independence requires that difference to vanish everywhere; zero covariance requires only that its integral vanish.

[PDF attachment: *Probability Notes No. 00: Hoeffding’s covariance identity (PDF)*. Full proofs, references and the numerical-check code.]

## Setup and notation

Let $(X,Y)$ be a random vector on a probability space $(\Omega ,\mathcal{F},\mathbb{P})$, taking values in $\mathbb{R}^2$. Write

1. $F_{X,Y}(x,y)=\mathbb{P}(X\le x,Y\le y)$ for the joint distribution function, and $F_X$, $F_Y$ for the marginals;
2. $\bar F_X=1-F_X$, $\bar F_Y=1-F_Y$ for the survival functions;
3. $D(x,y)=F_{X,Y}(x,y)-F_X(x)F_Y(y)$ for the *dependence function*;
4. $(X_1,Y_1)$, $(X_2,Y_2)$ for independent copies of $(X,Y)$ (see the proof).

By definition, $X$ and $Y$ are independent if and only if $D(x,y)=0$ for every $(x,y)$.

**Assumption A1.** $\mathbb{E}|X|<\infty$, $\mathbb{E}|Y|<\infty$ and $\mathbb{E}|XY|<\infty$.

A1 follows from $\mathbb{E} X^2,\mathbb{E} Y^2<\infty$ (Cauchy–Schwarz), the form usually quoted; the proof requires only A1. *Uncorrelated* means $\mathrm{Cov}(X,Y)=0$.

## Result

**Theorem (Hoeffding, 1940).** Under A1, $D$ is Lebesgue integrable on $\mathbb{R}^2$ and

$$
\operatorname{Cov}(X,Y)=\iint_{\mathbb{R}^2}\big[F_{X,Y}(x,y)-F_X(x)F_Y(y)\big]\,\mathrm{d}x\,\mathrm{d}y. \qquad (1)
$$

**Remark.** Equivalently, since by inclusion–exclusion $\mathbb{P}(X>x,Y>y)-\bar F_X(x)\bar F_Y(y)=D(x,y)$ pointwise,

$$
\operatorname{Cov}(X,Y)=\iint_{\mathbb{R}^2}\big[\mathbb{P}(X>x,Y>y)-\bar F_X(x)\bar F_Y(y)\big]\,\mathrm{d}x\,\mathrm{d}y.
$$

## Proof

**Lemma.** For real $a,b$,

$$
a-b=\int_{\mathbb{R}}\big[\mathbf{1}\{b\le u\}-\mathbf{1}\{a\le u\}\big]\,\mathrm{d}u,\qquad |a-b|=\int_{\mathbb{R}}\big|\mathbf{1}\{b\le u\}-\mathbf{1}\{a\le u\}\big|\,\mathrm{d}u.
$$

*Proof.* If $a=b$ the integrand vanishes. If $a>b$ it equals $1$ on $[b,a)$ and $0$ elsewhere; if $a<b$ it equals $-1$ on $[a,b)$ and $0$ elsewhere. ∎

**Step 1: symmetrisation.** Let $(X_1,Y_1)$ and $(X_2,Y_2)$ be independent copies of $(X,Y)$: two independent draws from the joint law of $(X,Y)$, realised on $\Omega \times \Omega $ if necessary. The argument follows Lehmann (1966). Expanding,

$$
\begin{aligned}\mathbb{E}\big[(X_1-X_2)(Y_1-Y_2)\big]&=\mathbb{E}[X_1Y_1]+\mathbb{E}[X_2Y_2]-\mathbb{E}[X_1Y_2]-\mathbb{E}[X_2Y_1]\\&=2\,\mathbb{E}[XY]-2\,\mathbb{E}X\,\mathbb{E}Y.\end{aligned}
$$

Each same-copy term equals $\mathbb{E}[XY]$, since $(X_i,Y_i)$ has the law of $(X,Y)$. Each cross term has its factors in different copies: on $\Omega \times \Omega $, with points $(\omega_1,\omega_2)$, $X_1$ depends only on $\omega_1$ and $Y_2$ only on $\omega_2$, so $\mathbb{E}|X_1Y_2|=\mathbb{E}|X|\,\mathbb{E}|Y|$ by Tonelli and $\mathbb{E}[X_1Y_2]=\mathbb{E} X\,\mathbb{E} Y$ by Fubini; likewise for $X_2Y_1$. A1 makes all four terms finite, which justifies the expansion. Hence $\mathrm{Cov}(X,Y)=\tfrac12\mathbb{E}[(X_1-X_2)(Y_1-Y_2)]$. The means have dropped out: $X-\mathbb{E} X$ and $Y-\mathbb{E} Y$ are replaced by the differences $X_1-X_2$ and $Y_1-Y_2$, to which the lemma applies directly.

**Step 2: integral representation.** Apply the lemma in $u$ to $X_1-X_2$ and in $v$ to $Y_1-Y_2$, and multiply:

$$
(X_1-X_2)(Y_1-Y_2)=\iint_{\mathbb{R}^2}\Phi(u,v)\,\mathrm{d}u\,\mathrm{d}v,\quad \Phi(u,v)=\big[\mathbf{1}\{X_2\le u\}-\mathbf{1}\{X_1\le u\}\big]\big[\mathbf{1}\{Y_2\le v\}-\mathbf{1}\{Y_1\le v\}\big].
$$

*Justification (Fubini–Tonelli).* By the second identity in the lemma, $\iint|\Phi|=|X_1-X_2|\,|Y_1-Y_2|$, and

$$
\mathbb{E}\big[|X_1-X_2|\,|Y_1-Y_2|\big]\le\mathbb{E}\big[(|X_1|+|X_2|)(|Y_1|+|Y_2|)\big]=2\,\mathbb{E}|XY|+2\,\mathbb{E}|X|\,\mathbb{E}|Y|<\infty.
$$

Here $\Phi$ depends on $(u,v)$ and on the outcome $\omega$, and is jointly measurable, being built from indicators of sets such as $\{(u,\omega):X_2(\omega)\le u\}$. By Tonelli the two displays give $\mathbb{E}\iint|\Phi|\,du\,dv<\infty$, so $\Phi$ is integrable for the product of Lebesgue measure on $\mathbb{R}^2$ and $\mathbb{P}$, and Fubini gives

$$
\mathbb{E}\iint_{\mathbb{R}^2}\Phi\,\mathrm{d}u\,\mathrm{d}v=\iint_{\mathbb{R}^2}\mathbb{E}\,\Phi(u,v)\,\mathrm{d}u\,\mathrm{d}v.
$$

**Step 3: expectation of the integrand.** Expanding $\Phi$ into four products of indicators,

$$
\mathbb{E}\,\Phi(u,v)=2F_{X,Y}(u,v)-2F_X(u)F_Y(v)=2D(u,v),
$$

because terms with both coordinates from the same copy give $F_{X,Y}$, and terms mixing the copies factorise.

**Step 4: conclusion.** $\mathrm{Cov}(X,Y)=\tfrac12\iint\mathbb{E}\Phi=\iint D$. Integrability of $D$ follows from $|D|=\tfrac12|\mathbb{E}\Phi|\le\tfrac12\mathbb{E}|\Phi|$ and the bound above. ∎

**Alternative route (sketch).** Write $X=\int_0^\infty\mathbf{1}\{X>t\}\,dt-\int_{-\infty}^0\mathbf{1}\{X\le t\}\,dt$, do the same for $Y$, multiply, take expectations quadrant by quadrant, and subtract $\mathbb{E} X\,\mathbb{E} Y$ written the same way. In every quadrant the integrand is ±[joint − product], and identities such as $\mathbb{P}(X\le u,Y>v)-F_X(u)\bar F_Y(v)=-D(u,v)$ make the four signs agree. The symmetrisation proof avoids this bookkeeping.

## Insights

1. **Independence and zero covariance compared.** Independence says $D\equiv0$, a condition on a whole function on the plane. Zero covariance says $\iint D=0$, a single linear functional of the same function. The first implies the second at once. The converse fails exactly when $D$ takes both signs and its positive and negative parts cancel, as in the worked example below.
2. **The role of Lebesgue measure.** Covariance integrates $D$ against $dx\,dy$, which depends on the scale of each axis. For continuous marginals, $D$ written in the coordinates $(F_X(x),F_Y(y))$ does not. This is why covariance changes under strictly increasing transformations of the variables while rank correlation does not. Invariance under such rescalings was the subject of Hoeffding’s dissertation.
3. **Sign information.** When $D$ has constant sign, $|\mathrm{Cov}(X,Y)|=\iint|D|$ is the $L^1$ norm of $D$, so zero covariance forces $D\equiv0$ (Corollary 1 below).

> **Independence requires D to vanish everywhere; zero covariance requires only that its integral vanish.** (pull quote)

## Uses and consequences

The results below follow from the theorem by choosing a particular pair, integrand or integrating measure.

### Variance and mean absolute difference

Take $Y=X$ with $\mathbb{E} X^2<\infty$. Then $F_{X,X}(x,y)=F_X(x\wedge y)$ and, for $x\le y$, $D(x,y)=F_X(x)\bar F_X(y)$. By symmetry,

$$
\operatorname{Var}(X)=2\iint_{x<y}F_X(x)\,\bar F_X(y)\,\mathrm{d}x\,\mathrm{d}y,
$$

while taking expectations in the second identity of the lemma gives the mean absolute difference (Gini, 1912),

$$
\mathbb{E}|X_1-X_2|=2\int_{\mathbb{R}}F_X(x)\,\bar F_X(x)\,\mathrm{d}x.
$$

Both are built from the kernel $F_X(x)\bar F_X(y)$, variance by integrating it over the plane and the mean absolute difference by integrating it along the diagonal.

### Positive quadrant dependence

$(X,Y)$ is *positively quadrant dependent* (PQD) if $D\ge0$ on the plane (Lehmann, 1966).

**Corollary 1** (Lehmann, 1966)**.** Under A1: (i) if $(X,Y)$ is PQD then $\mathrm{Cov}(X,Y)\ge0$; (ii) if $(X,Y)$ is PQD and $\mathrm{Cov}(X,Y)=0$, then $X$ and $Y$ are independent.

*Proof.* (i) is immediate from (1). For (ii), $D\ge0$ and $\iint D=0$ give $D=0$ Lebesgue-almost everywhere. Fix $(x,y)$. A null set contains no open square, so each square $(x,x+\tfrac1n)\times(y,y+\tfrac1n)$ contains a point $(x_n,y_n)$ with $D(x_n,y_n)=0$. Monotonicity gives $F_{X,Y}(x,y)\le F_{X,Y}(x_n,y_n)\le F_{X,Y}(x+\tfrac1n,y+\tfrac1n)$, and the right side tends to $F_{X,Y}(x,y)$ by continuity of probability along decreasing events; likewise for $F_X$ and $F_Y$. Hence $D(x,y)=\lim_n D(x_n,y_n)=0$. ∎

So zero covariance does imply independence when the dependence has a fixed sign. The bivariate normal with $\rho\ge0$ is PQD, by a Gaussian comparison inequality (Slepian, 1962; not proved here).

### An association inequality

**Corollary 2** (association; see Esary, Proschan and Walkup, 1967)**.** If $f,g$ are non-decreasing and $f(X),g(X)$ have finite second moments, then $\mathrm{Cov}(f(X),g(X))\ge0$.

*Proof.* Let $U=f(X)$, $V=g(X)$. Each of the events $\{U\le u\}$ and $\{V\le v\}$ has the form $\{X\in I\}$ with $I$ a down-set of the real line, so one contains the other and

$$
\mathbb{P}(U\le u,V\le v)=\min\{\mathbb{P}(U\le u),\mathbb{P}(V\le v)\}\ge\mathbb{P}(U\le u)\,\mathbb{P}(V\le v).
$$

Thus $(U,V)$ is PQD; apply Corollary 1(i). ∎

### Copulas and rank correlation

Let $F_X,F_Y$ be continuous. Then $(U,V)=(F_X(X),F_Y(Y))$ has uniform marginals, and its distribution function $C$, the copula, satisfies $F_{X,Y}(x,y)=C(F_X(x),F_Y(y))$ (Sklar, 1959; Nelsen, 2006; not proved here). Applying the theorem to $(U,V)$, with $\mathrm{Var}\,U=\mathrm{Var}\,V=\tfrac1{12}$, gives the population form of the rank correlation of Spearman (1904),

$$
\rho_S(X,Y):=\operatorname{Corr}(U,V)=12\iint_{[0,1]^2}\big[C(s,t)-st\big]\,\mathrm{d}s\,\mathrm{d}t, \qquad (2)
$$

whereas for the original variables

$$
\operatorname{Cov}(X,Y)=\iint_{\mathbb{R}^2}\big[C(F_X(x),F_Y(y))-F_X(x)F_Y(y)\big]\,\mathrm{d}x\,\mathrm{d}y.
$$

Rank correlation therefore depends on $C$ alone, while covariance also depends on the marginals through the measure of integration.

### Extremal covariance for fixed marginals

Fix marginals with $\mathbb{E} X^2,\mathbb{E} Y^2<\infty$, so that A1 holds for every coupling (with only first moments the comonotone covariance can be $+\infty$). Every joint distribution function with these marginals satisfies the copula bounds (Hoeffding, 1940; Fréchet, 1951)

$$
\max\{F_X(x)+F_Y(y)-1,\,0\}\le F_{X,Y}(x,y)\le\min\{F_X(x),F_Y(y)\},
$$

which follow from $\mathbb{P}(A\cap B)\ge\mathbb{P}(A)+\mathbb{P}(B)-1$ and $\mathbb{P}(A\cap B)\le\min\{\mathbb{P}(A),\mathbb{P}(B)\}$. The upper bound is attained by the comonotone coupling $(F_X^{-1}(W),F_Y^{-1}(W))$ and the lower by the countermonotone coupling $(F_X^{-1}(W),F_Y^{-1}(1-W))$, with $W$ uniform on $(0,1)$ (attainment not proved here; see Nelsen, 2006). Inserting the bounds in (1), these two couplings maximise and minimise the covariance among all couplings with the given marginals. Correlation ±1 needs an exact affine relation (the equality case of Cauchy–Schwarz), which the marginals may forbid: if $X,Y$ are lognormal, $Y=a-bX$ with $b>0$ is negative for large $X$, so correlation $-1$ is unattainable (Embrechts, McNeil and Straumann, 2002).

### Functions of the variables

Let $f,g$ be monotone and absolutely continuous, and let A1 hold for $(f(X),g(Y))$. Replacing the lemma by $f(a)-f(b)=\int[\mathbf{1}\{b\le u\}-\mathbf{1}\{a\le u\}]f'(u)\,du$, and noting that monotonicity gives the matching identity for $|f(a)-f(b)|$ with $|f'|$, the proof goes through verbatim (Cuadras, 2002):

$$
\operatorname{Cov}\big(f(X),g(Y)\big)=\iint_{\mathbb{R}^2}D(x,y)\,f'(x)\,g'(y)\,\mathrm{d}x\,\mathrm{d}y.
$$

## Worked example

Let $X$ be uniform on $\{-1,0,1\}$ and $Y=X^2$. Since $\mathbb{E} X=\mathbb{E} X^3=0$, $\mathrm{Cov}(X,Y)=\mathbb{E} X^3-\mathbb{E} X\,\mathbb{E} X^2=0$, yet $Y$ is a function of $X$.

**Marginals.** $F_X$ equals $0,\tfrac13,\tfrac23,1$ on $(-\infty,-1)$, $[-1,0)$, $[0,1)$, $[1,\infty)$, and $F_Y$ equals $0,\tfrac13,1$ on $(-\infty,0)$, $[0,1)$, $[1,\infty)$.

**Dependence function.** For $y<0$, $F_{X,Y}=F_Y=0$, so $D=0$. For $y\ge1$, $F_{X,Y}=F_X$ and $F_Y=1$, so $D=0$. For $0\le y<1$, $\{Y\le y\}=\{X=0\}$, so $F_{X,Y}(x,y)=\tfrac13\mathbf{1}\{x\ge0\}$ and

$$
D(x,y)=\tfrac13\big[\mathbf{1}\{x\ge0\}-F_X(x)\big]=\begin{cases}-\tfrac19, & -1\le x<0,\\ +\tfrac19, & 0\le x<1,\\ 0, & \text{otherwise.}\end{cases}
$$

![Dependence function D for X ~ Unif{−1, 0, 1}, Y = X². The two squares cancel, so Cov(X, Y) = 0 although Y is a function of X.](hoeffding-figure.png)

*Dependence function D for X ~ Unif{−1, 0, 1}, Y = X². The two squares cancel, so Cov(X, Y) = 0 although Y is a function of X.*

The function $D$ is supported on two unit squares of opposite sign, so $\iint D=-\tfrac19+\tfrac19=0$, as (1) requires. For $x$ just below $0$, the events $\{X\le x\}$ and $\{Y=0\}$ are disjoint, a negative dependence; just above $0$ the dependence is positive. Covariance does not register this, but a functional of $|D|$ does, for instance $\sup|D|=\tfrac19$. Hoeffding’s 1948 test of independence is built on $\iint D^2\,dF_{X,Y}$, which characterises independence for continuous joint distributions.

## Numerical check

Rows 1 to 3 integrate $D$ by trapezoidal quadrature on a grid; row 4 integrates the step function $D$ exactly in rational arithmetic.

1. Normal, unit variances, $\rho=\tfrac12$: $\iint D\,dx\,dy$. Exact $0.5$; numerical $0.500000$.
2. Same $D$: $12\iint D\,dF_X\,dF_Y$, i.e. (2). Exact $0.4826$ (from the closed form $\tfrac6\pi\arcsin(\rho/2)$; Kruskal, 1958; not proved here); numerical $0.4826$.
3. $X=Y\sim\mathrm{Exp}(1)$: $\iint D$. Exact $1$; numerical $0.999992$.
4. Worked example: $\iint D$. Exact $0$; computed $0$ exactly.

Rows 1 and 2 integrate the same $D$, against $dx\,dy$ and against $dF_X\,dF_Y$ respectively; only the measure differs.

**Code.** Every number above is printed by the script below (Python 3, NumPy, SciPy); its docstring gives the requirements.

```python
"""Probability Notes No. 00: numerical check.

Prints every number in the PDF's check table.
Requires Python >= 3.8, NumPy >= 1.20 and
SciPy >= 1.6 (for scipy.integrate.trapezoid).
Tested with Python 3.13, NumPy 2.5, SciPy 1.18.
Run: python3 check.py
"""
from fractions import Fraction as Q
import numpy as np
from scipy.integrate import trapezoid
from scipy.stats import norm, multivariate_normal

def trapz2(d, x, y):
    return trapezoid(trapezoid(d, x, axis=1), y)

# 1. Bivariate normal, rho = 0.5: integral of D = rho.
rho = 0.5
g = np.linspace(-7.0, 7.0, 281)
x, y = np.meshgrid(g, g)
pts = np.column_stack([x.ravel(), y.ravel()])
cov = [[1, rho], [rho, 1]]
mvn = multivariate_normal([0, 0], cov)
d = mvn.cdf(pts).reshape(x.shape)
d -= norm.cdf(x) * norm.cdf(y)
print(f"Gaussian cov:  {trapz2(d, g, g):.6f}")

# 2. Same D, measure dF_X dF_Y: rank correlation.
w = norm.pdf(x) * norm.pdf(y)
rs = 12 * trapz2(d * w, g, g)
print(f"Rank corr:     {rs:.4f}")
print(f"Closed form:   {6/np.pi*np.arcsin(rho/2):.4f}")

# 3. X = Y ~ Exp(1): integral of D = Var(X) = 1.
t = np.linspace(0.0, 40.0, 4001)
fx, fy = np.meshgrid(1 - np.exp(-t), 1 - np.exp(-t))
d = np.minimum(fx, fy) - fx * fy
print(f"Exp(1) var:    {trapz2(d, t, t):.6f}")

# 4. X ~ Unif{-1,0,1}, Y = X^2: D is a step
# function; integrate it exactly on unit cells.
px = {-1: Q(1, 3), 0: Q(1, 3), 1: Q(1, 3)}
def D(u, v):
    fxy = sum(p for k, p in px.items()
              if k <= u and k * k <= v)
    fx = sum(p for k, p in px.items() if k <= u)
    fy = sum(p for k, p in px.items() if k * k <= v)
    return fxy - fx * fy
cells = [(u + Q(1, 2), v + Q(1, 2))
         for u in range(-2, 2) for v in range(-1, 2)]
tot = sum(D(u, v) for u, v in cells)
mx = max(abs(D(u, v)) for u, v in cells)
print(f"Example: int D = {tot}, sup|D| = {mx}")
```

**Output:**

```
Gaussian cov:  0.500000
Rank corr:     0.4826
Closed form:   0.4826
Exp(1) var:    0.999992
Example: int D = 0, sup|D| = 1/9
```


## Notes

Wassily Hoeffding proved (1) in his Berlin doctoral dissertation, *Maßstabinvariante Korrelationstheorie* (‘Scale-invariant correlation theory’), published in 1940. The dissertation develops a theory of dependence invariant under monotone rescaling of the axes, the rank-based view of the copula section above, and already contains the copula bounds. In 1948 he based a test of independence on the whole of $D$. The identity reached a wide audience through Lehmann (1966).

### References

Cuadras, C. M. (2002). On the covariance between functions. *Journal of Multivariate Analysis*, 81(1), 19–27.

Embrechts, P., McNeil, A. J. and Straumann, D. (2002). Correlation and dependence in risk management: properties and pitfalls. In M. A. H. Dempster (ed.), *Risk Management: Value at Risk and Beyond*, 176–223. Cambridge University Press.

Esary, J. D., Proschan, F. and Walkup, D. W. (1967). Association of random variables, with applications. *Annals of Mathematical Statistics*, 38(5), 1466–1474.

Fréchet, M. (1951). Sur les tableaux de corrélation dont les marges sont données. *Annales de l’Université de Lyon, Section A, Série 3*, 14, 53–77.

Gini, C. (1912). *Variabilità e Mutabilità: Contributo allo Studio delle Distribuzioni e delle Relazioni Statistiche*. Tipografia di Paolo Cuppini, Bologna.

Hoeffding, W. (1940). Maßstabinvariante Korrelationstheorie. *Schriften des Mathematischen Instituts und des Instituts für Angewandte Mathematik der Universität Berlin*, 5(3), 181–233. English translation in N. I. Fisher and P. K. Sen (eds.), *The Collected Works of Wassily Hoeffding*, Springer, 1994.

Hoeffding, W. (1948). A non-parametric test of independence. *Annals of Mathematical Statistics*, 19(4), 546–557.

Kruskal, W. H. (1958). Ordinal measures of association. *Journal of the American Statistical Association*, 53(284), 814–861.

Lehmann, E. L. (1966). Some concepts of dependence. *Annals of Mathematical Statistics*, 37(5), 1137–1153.

Nelsen, R. B. (2006). *An Introduction to Copulas*, 2nd edn. Springer, New York.

Sklar, A. (1959). Fonctions de répartition à n dimensions et leurs marges. *Publications de l’Institut de Statistique de l’Université de Paris*, 8, 229–231.

Slepian, D. (1962). The one-sided barrier problem for Gaussian noise. *Bell System Technical Journal*, 41(2), 463–501.

Spearman, C. (1904). The proof and measurement of association between two things. *American Journal of Psychology*, 15(1), 72–101.
