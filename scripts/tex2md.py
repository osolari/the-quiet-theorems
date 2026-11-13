"""Convert a post's main.tex into article.md (GitHub-flavoured, MathJax).

Usage: python3 scripts/tex2md.py <post-dir-name>
Needs the post built first (make build P=<post>): uses the .aux for
theorem/equation numbers and citations, and figure PNGs in img/.

Output: docs/posts/<post>/article.md with $...$ / $$...$$ maths,
numbered results, resolved cross-references, figures as
img/figure-N.png, references from references.bib, and the
numerical-check code inline.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TYPE = {"theorem": "Theorem", "lemma": "Lemma", "corollary": "Corollary",
        "remark": "Remark", "proposition": "Proposition",
        "definition": "Definition", "example": "Example",
        "assumption": "Assumption", "figure": "Figure",
        "listing": "Listing", "equation": "", "table": "Table"}
ENVS = ["theorem", "lemma", "corollary", "remark", "proposition",
        "definition", "example", "assumption"]


def grab(src, macro):
    m = re.search(r"\\newcommand\{\\%s\}\{(.*?)\}\s*(%%|\n)" % macro, src)
    return m.group(1).strip() if m else ""


def braced(s, i):
    """Return (content, end) for the {...} group starting at s[i]."""
    assert s[i] == "{", s[i:i + 30]
    depth, j = 0, i
    while True:
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1


def sub_macro(s, name, fn, nargs=1, opt=False):
    """Replace \\name[opt]{a}{b}... using fn(opt, *args)."""
    out, i = [], 0
    pat = re.compile(r"\\%s(?![A-Za-z@])" % re.escape(name))
    while True:
        m = pat.search(s, i)
        if not m:
            out.append(s[i:])
            return "".join(out)
        out.append(s[i:m.start()])
        j = m.end()
        o = []
        while opt and j < len(s) and s[j] == "[":
            k = s.index("]", j)
            o.append(s[j + 1:k])
            j = k + 1
        args = []
        for _ in range(nargs):
            while s[j] in " \n":
                j += 1
            a, j = braced(s, j)
            args.append(a)
        out.append(fn(o, *args))
        i = j


def read_aux(aux):
    labels, cites = {}, {}
    for line in aux.read_text().splitlines():
        m = re.match(r"\\newlabel\{(.+?)@cref\}\{\{\[(\w+)\]\[\d+\]\[\]([^}]*)\}", line)
        if m:
            labels[m.group(1)] = (m.group(2), m.group(3))
        m = re.match(r"\\bibcite\{(.+?)\}\{\{(\d+)\}\{(\d+)\}\{\{(.+?)\}\}", line)
        if m:
            cites[m.group(1)] = (m.group(2), m.group(3),
                                 m.group(4).replace("~", " "))
    return labels, cites


def detex(s):
    s = s.replace("{\\'u}", "ú").replace("\\'u", "ú").replace('{\\"u}', "ü")
    s = s.replace('\\"u', "ü").replace('{\\"a}', "ä").replace('\\"a', "ä")
    s = s.replace("{\\ss}", "ß").replace("\\ss", "ß").replace("--", "–")
    s = s.replace("{\\'e}", "é").replace("\\'e", "é")
    return re.sub(r"[{}]", "", s).replace("~", " ")


def references(bib, cites):
    entries = {}
    for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", bib, re.S):
        f = dict(re.findall(r"(\w+)\s*=\s*\{(.*?)\},?\s*\n", m.group(3) + "\n", re.S))
        entries[m.group(2).strip()] = (m.group(1).lower(), f)
    out = []
    for key, (num, year, _) in sorted(cites.items(), key=lambda kv: int(kv[1][0])):
        kind, f = entries.get(key, ("misc", {}))
        a = detex(f.get("author", "")).replace(" and ", ", ")
        t = detex(f.get("title", ""))
        if kind == "book":
            ed = f" {f['edition']}nd ed." if f.get("edition") == "2" else ""
            src = f"*{t}*.{ed} {detex(f.get('publisher', ''))}"
            out.append(f"{num}. {a}. {src}, {year}.")
            continue
        venue = detex(f.get("journal", f.get("booktitle", "")))
        vol = f.get("volume", "")
        num_ = f"({f['number']})" if f.get("number") else ""
        pages = detex(f.get("pages", ""))
        loc = f" {vol}{num_}:{pages}" if vol else (f", {pages}" if pages else "")
        note = f" {detex(f['note'])}." if f.get("note") else ""
        out.append(f"{num}. {a}. {t}. *{venue}*{loc}, {year}.{note}")
    return "\n".join(out)


def main(post):
    pdir = ROOT / "docs" / "posts" / post
    bdir = ROOT / "build" / post
    proj = (pdir / "project.tex").read_text()
    tex = (pdir / "main.tex").read_text()
    labels, cites = read_aux(bdir / "build" / "saim-post.aux")
    body = tex.split("\\begin{document}", 1)[1].split("\\end{document}", 1)[0]
    body = re.sub(r"(?m)(?<!\\)%.*$", "", body)
    body = body.split("\\bibliographystyle", 1)[0]

    def ref(o, keys):
        parts = []
        for k in keys.split(","):
            k = k.strip()
            if k.startswith("lst:"):
                parts.append("the code at the end")
                continue
            typ, num = labels.get(k, ("?", "??"))
            parts.append(f"({num})" if typ == "equation" else f"{TYPE.get(typ, typ)} {num}".strip())
        return " and ".join(parts)

    def cite(kind):
        def f(o, keys):
            items = []
            for k in keys.split(","):
                n, y, a = cites.get(k.strip(), ("?", "?", k))
                items.append((a, y, n))
            if kind == "t":
                return "; ".join(f"{a} ({y}) [{n}]" for a, y, n in items)
            if kind == "alp":
                return "; ".join(f"{a}, {y} [{n}]" for a, y, n in items)
            pre = o[0] + " " if len(o) >= 2 and o[0] else ""
            post = ", " + o[-1] if (len(o) == 1 and o[0]) or (len(o) >= 2 and o[1]) else ""
            return "(" + pre + "; ".join(f"{a}, {y} [{n}]" for a, y, n in items) + post + ")"
        return f


    # numbered environments, by order of appearance (matches aux numbering)
    counters = {"theorem": 0, "assumption": 0, "equation": 0, "figure": 0}

    def env_head(name, o, label):
        if label and label in labels:
            num = labels[label][1]
        else:
            key = "assumption" if name == "assumption" else "theorem"
            counters[key] += 1
            num = ("A" if name == "assumption" else "") + str(counters[key])
        t = f"\\textbf{{{TYPE[name]} {num}"
        t += f" ({o})" if o else ""
        return t + ".}"

    for name in ENVS:
        def rep(m, name=name):
            o = m.group(1) or ""
            label = None
            rest = m.group(2)
            lm = re.match(r"\s*\\label(?:\[\w+\])?\{(.+?)\}", rest)
            if lm:
                label, rest = lm.group(1), rest[lm.end():]
            return "\n\n" + env_head(name, o.strip("[]"), label) + " " + rest.strip() + "\n\n"
        body = re.sub(r"\\begin\{%s\}(\[[^\]]*\])?(.*?)\\end\{%s\}" % (name, name), rep, body, flags=re.S)

    body = sub_macro(body, "cref", ref, opt=True)
    body = sub_macro(body, "Cref", ref, opt=True)
    body = sub_macro(body, "eqref", lambda o, k: ref(o, k))
    body = sub_macro(body, "citet", cite("t"), opt=True)
    body = sub_macro(body, "Citet", cite("t"), opt=True)
    body = sub_macro(body, "citealp", cite("alp"), opt=True)
    body = sub_macro(body, "citep", cite("p"), opt=True)

    def proof(m):
        o = m.group(1)
        head = f"\\emph{{{o[1:-1]}.}}" if o else "\\emph{Proof.}"
        return "\n\n" + head + " " + m.group(2).strip() + " ∎\n\n"
    body = re.sub(r"\\begin\{proof\}(\[[^\]]*\])?(.*?)\\end\{proof\}", proof, body, flags=re.S)

    def equation(m):
        inner = m.group(1)
        lm = re.search(r"\\label\{(.+?)\}", inner)
        tag = ""
        if lm:
            tag = r" \tag{%s}" % labels.get(lm.group(1), ("", "?"))[1]
            inner = inner.replace(lm.group(0), "")
        return "\n\\[" + inner.strip() + tag + "\\]\n"
    body = re.sub(r"\\begin\{equation\}(.*?)\\end\{equation\}", equation, body, flags=re.S)

    fig_n = [0]

    def figure(m):
        fig_n[0] += 1
        cap = re.search(r"\\caption\{", m.group(0))
        caption = braced(m.group(0), cap.end() - 1)[0] if cap else ""
        lm = re.search(r"\\label\{(.+?)\}", m.group(0))
        num = labels.get(lm.group(1), ("", fig_n[0]))[1] if lm else fig_n[0]
        return (f"\n\n@@FIG{num}@@\n\n\\emph{{Figure {num}.}} {caption}\n\n")
    body = re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", figure, body, flags=re.S)

    boxes = {"tldr": "\\textbf{TL;DR.} ", "mainresult": "", "pullquote": ""}
    for env, lead in boxes.items():
        def bq(m, lead=lead, env=env):
            inner = m.group(1).strip()
            if env == "pullquote":
                inner = "\\emph{" + inner + "}"
            return "\n\n@@BQ@@" + lead + inner + "@@EQ@@\n\n"
        body = re.sub(r"\\begin\{%s\}(?:\[[^\]]*\])?(.*?)\\end\{%s\}" % (env, env), bq, body, flags=re.S)

    secs = {"SecSetup": "Setup and notation", "SecResult": "Result", "SecProof": "Proof",
            "SecInsight": "Insights", "SecUses": "Uses and consequences",
            "SecExample": "Worked example", "SecCheck": "Numerical check", "SecNotes": "Notes"}
    for k, v in secs.items():
        body = body.replace("\\" + k, "\n\\section{" + v + "}\n")
    body = sub_macro(body, "step", lambda o, a: f"\\textbf{{Step: {a}.}}")
    body = sub_macro(body, "interchange", lambda o, a: f"\\emph{{Justification ({a}).}}")
    body = sub_macro(body, "paragraph", lambda o, a: f"\n\n\\textbf{{{a}}} ")
    body = sub_macro(body, "SAIMTableHead", lambda o, a: a)
    body = sub_macro(body, "texorpdfstring", lambda o, a, b: a, nargs=2)
    for drop in ["\\begin{center}", "\\end{center}", "\\maketitle", "\\qedhere", "\\small", "\\centering", "\\clearpage", "\\appendix"]:
        body = body.replace(drop, "")
    body = body.split("{\\let\\SAIMplainauthors", 1)[0]

    macros = (ROOT / "skeleton/shared/components/math.tex").read_text()
    macros = re.sub(r"(?m)^\s*%.*$", "", macros)
    macros = macros.replace("\\providecommand", "\\newcommand")
    extra = r"""
\newcommand{\dd}{\mathrm{d}}
\newcommand{\coloneqq}{\mathrel{:=}}
\newcommand{\eqd}{\overset{d}{=}}
"""
    macros = re.sub(r"\\newcommand\{\\(dd|eqd)\}.*\n", "", macros)
    src = macros + extra + "\n\\begin{document}\n" + body + "\n\\end{document}\n"
    md = subprocess.run(["pandoc", "-f", "latex", "-t", "gfm+tex_math_dollars", "--wrap=none", "--shift-heading-level-by=1"],
                        input=src, capture_output=True, text=True)
    if md.returncode:
        sys.exit(md.stderr)
    md = md.stdout

    def block_math(m):
        return "\n\n$$\n" + m.group(1).strip() + "\n$$\n\n"
    md = re.sub(r"[ \t]*\$\$(.+?)\$\$[ \t]*", block_math, md, flags=re.S)
    md = re.sub(r"\n\n\$\$\n(.*?)\n\$\$\n\n([.,;:])", lambda m: "\n\n$$\n" + m.group(1) + m.group(2) + "\n$$\n\n", md, flags=re.S)
    md = re.sub(r"@@BQ@@(.*?)@@EQ@@", lambda m: "\n".join(("> " + l).rstrip() for l in re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", m.group(1).strip()).split("\n")), md, flags=re.S)
    md = re.sub(r"@@FIG(\w+)@@", lambda m: f"![Figure {m.group(1)}](img/figure-{m.group(1)}.png)", md)
    md = md.replace("``` math", "$$").replace("```math", "$$")
    md = re.sub(r"\$\$\n(.*?)\n```", lambda m: "$$\n" + m.group(1) + "\n$$", md, flags=re.S)

    title, sub = grab(proj, "ProjectTitle"), grab(proj, "ProjectSubtitle")
    issue, date = grab(proj, "ProjectIssue"), grab(proj, "ProjectDate")
    nn = post.split("-")[0]
    slug = post.split("-", 1)[1]
    head = (f"# {title}\n\n*{sub}*\n\n**Probability Notes {issue}** · Omid Shams Solari, Ph.D. · {date}\n\n"
            f"[PDF (A4)](pdf/pn-{nn}-{slug}.pdf) · [PDF (screen)](pdf/pn-{nn}-{slug}-screen.pdf) · "
            f"[Notebook](notebook.ipynb) · [LaTeX source](main.tex)\n\n")
    refs = references((pdir / "references.bib").read_text(), cites)
    code = (pdir / "code" / "check.py").read_text()
    tail = (f"\n\n## References\n\n{refs}\n\n## Code\n\nNumerical check (`code/check.py`); "
            f"run `python3 code/check.py`, or open [the notebook](notebook.ipynb).\n\n```python\n{code}```\n")
    md = head + md.strip() + tail
    md = re.sub(r"\n{3,}", "\n\n", md)
    (pdir / "article.md").write_text(md)
    print(pdir / "article.md")


if __name__ == "__main__":
    main(sys.argv[1])
