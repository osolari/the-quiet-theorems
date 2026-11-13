"""Probability Notes No. 00: figures (matplotlib).

Runs in the notebook after check.py, in the same namespace.
Figure 1: the dependence function D(x, y) for
X ~ Unif{-1, 0, 1}, Y = X^2.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

INK, MUTED = "#17131F", "#6F6879"
NEG, POS = "#2E5C8A", "#32127A"

fig, ax = plt.subplots(figsize=(5.2, 2.8))
for x0, val, col in [(-1, "−1/9", NEG), (0, "+1/9", POS)]:
    ax.add_patch(Rectangle((x0, 0), 1, 1, color=col,
                           alpha=0.25, lw=0))
    ax.text(x0 + 0.5, 0.5, val, ha="center",
            va="center", color=INK, fontsize=13)
ax.add_patch(Rectangle((-1, 0), 2, 1, fill=False,
                       ec="#978EA7"))
ax.axhline(0, color="#D8D3E1", lw=1)
ax.axvline(0, color="#D8D3E1", lw=1)
ax.set_xlim(-2, 2)
ax.set_ylim(-0.4, 1.5)
ax.set_xlabel("x", color=INK)
ax.set_ylabel("y", color=INK)
ax.text(1.1, 1.3, "D = 0 elsewhere", color=MUTED)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_title("Dependence function D(x, y)", color=INK)
plt.tight_layout()
plt.show()
