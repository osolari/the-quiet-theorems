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
