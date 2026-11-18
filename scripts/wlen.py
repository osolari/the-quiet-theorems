"""Check a post's X post (X Premium long post) in docs/posts/<post>/post.txt.

Weights: code points 0-4351, 8192-8205, 8208-8223 and 8242-8247
weigh 1; all others weigh 2; a URL or the placeholder [link]
weighs 23.
Rules (failures exit non-zero):
- the first line carries the link ([link] or the Substack URL);
- the lead (everything before the first blank line: heading line
  and hook) is at most 280, so the whole lead and the attached plot
  show before X's "Show more";
- the whole post is at most 25,000 (X Premium limit);
- the plot to attach exists: substack/<slug>-figure.png
  (or <slug>-figure-1.png when there are several).
The total above 1,500 is reported as a note (aim: 600 to 1,500).
Usage: python3 scripts/wlen.py docs/posts/<post>/post.txt
"""
import re
import sys
from pathlib import Path

ONE = [(0, 4351), (8192, 8205), (8208, 8223),
       (8242, 8247)]
LEAD, TOTAL, AIM = 280, 25000, 1500


def wlen(s):
    s = s.replace("[link]", "x" * 23)
    s = re.sub(r"https?://\S+", "x" * 23, s)
    return sum(1 if any(a <= c <= b for a, b in ONE)
               else 2 for c in map(ord, s))


def check(path):
    p = Path(path)
    text = p.read_text().strip()
    bad = []
    first = text.splitlines()[0] if text else ""
    if "[link]" not in first and not re.search(r"https?://", first):
        bad.append("link not in the first line")
    lead = text.split("\n\n", 1)[0]
    nl, nt = wlen(lead), wlen(text)
    if nl > LEAD:
        bad.append(f"lead {nl} > {LEAD}")
    if nt > TOTAL:
        bad.append(f"total {nt} > {TOTAL}")
    slug = p.parent.name.split("-", 1)[-1]
    sub = p.parent / "substack"
    figs = [sub / f"{slug}-figure.png", sub / f"{slug}-figure-1.png"]
    fig = next((f for f in figs if f.exists()), None)
    if fig is None:
        bad.append(f"no plot to attach ({figs[0].name})")
    print(f"{path}: lead {nl}/{LEAD}, total {nt}"
          + (f" (aim <= {AIM})" if nt > AIM else "")
          + (f"; attach {fig.relative_to(p.parent)}" if fig else ""))
    for b in bad:
        print(f"{path}: {b}")
    return bool(bad)


if __name__ == "__main__":
    sys.exit(any([check(a) for a in sys.argv[1:]]))
