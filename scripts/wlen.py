"""Weighted X (Twitter) length of each tweet in a post file.

Rules: code points 0-4351, 8192-8205, 8208-8223 and
8242-8247 weigh 1; all others weigh 2; a URL or the
placeholder [link] weighs 23. Limit 280 (no Premium).
Usage: python3 scripts/wlen.py docs/posts/<post>/post.txt
"""
import re
import sys

ONE = [(0, 4351), (8192, 8205), (8208, 8223),
       (8242, 8247)]

def wlen(s):
    s = s.replace("[link]", "x" * 23)
    s = re.sub(r"https?://\S+", "x" * 23, s)
    return sum(1 if any(a <= c <= b for a, b in ONE)
               else 2 for c in map(ord, s))

def tweets(text):
    parts = re.split(r"^\d+/\d+\s*$", text, flags=re.M)
    parts = [p.strip() for p in parts if p.strip()]
    return parts or [text.strip()]

if __name__ == "__main__":
    bad = 0
    for path in sys.argv[1:]:
        for i, t in enumerate(tweets(open(path).read()), 1):
            n = wlen(t)
            bad |= n > 280
            flag = "OVER" if n > 280 else "ok"
            print(f"{path} tweet {i}: {n} {flag}")
    sys.exit(bad)
