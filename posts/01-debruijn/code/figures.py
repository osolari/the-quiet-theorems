"""The Quiet Theorems No. 01: figures (matplotlib).

Runs in the notebook after check.py, in the same namespace
(uses J and rade from check.py).
Figure 1: t J(Y_t) for X = +-1, between the bounds
t/(1+t) (Gaussian input) and 1.
"""
import matplotlib.pyplot as plt
import numpy as np

INK, MUTED = "#17131F", "#6F6879"
PRI, WARN = "#32127A", "#9B6418"

ts = np.logspace(-1.5, 1.5, 61)
tj = [s * J(rade, s) for s in ts]

fig, ax = plt.subplots(figsize=(5.6, 3.2))
ax.semilogx(ts, tj, color=PRI, lw=2, label="X = ±1")
ax.semilogx(ts, ts / (1 + ts), color=WARN, lw=2,
            ls="--", label="Gaussian X: t/(1+t)")
ax.axhline(1, color="#978EA7", ls=":", lw=1)
ax.text(ts[-1], 1.02, "≤ 1", ha="right", color=MUTED)
ax.set_xlabel("noise variance t (log scale)", color=INK)
ax.set_ylabel("t J(Y_t)", color=INK)
ax.set_ylim(0, 1.1)
ax.legend(frameon=False, loc="lower right")
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
plt.tight_layout()
plt.show()
