"""The Quiet Theorems No. 01: numerical check.

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
