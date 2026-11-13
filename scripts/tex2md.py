"""Draft the Substack article for a post: main.tex -> substack/article.md.

Usage: python3 scripts/tex2md.py <post> [--force]

Writes docs/posts/<post>/substack/article.md in the Substack house style
fixed by the published No. 00 (see docs/POST_GUIDE.md, "Substack"):
  * title "Probability Notes No. NN: <Title>", italic subtitle,
    "Published <date>: <url>" once meta.json has the Substack link;
  * TL;DR blockquote, then the PDF-attachment placeholder line;
  * no tables (Substack has none): tables become numbered lists;
  * each result kind numbered on its own counter, and only if there is
    more than one of it ("Theorem (Hoeffding, 1940)", "Corollary 1");
  * proof steps numbered "Step k: name."; only referenced equations
    numbered, typed as "\\qquad (k)";
  * author-year citations, alphabetical reference list;
  * figures as <slug>-figure.png (or -N.png) next to the article;
  * numerical check as a numbered list, then the code and its output.
The draft is then finished by hand. A published article is frozen
(meta.json substack.frozen = true) and is never overwritten without
--force.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KINDS = ["theorem", "lemma", "corollary", "remark", "proposition",
         "definition", "example"]
NAME = {k: k.capitalize() for k in KINDS}


# ---------------------------------------------------------------- helpers
def braced(s, i):
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


def detex(s):
    rep = {"{\\'u}": "ú", "\\'u": "ú", '{\\"u}': "ü", '\\"u': "ü",
           '{\\"a}': "ä", '\\"a': "ä", '{\\"o}': "ö", '\\"o': "ö",
           "{\\ss}": "ß", "\\ss": "ß", "{\\'e}": "é", "\\'e": "é",
           "{\\`e}": "è", "\\`e": "è", "{\\`a}": "à", "\\`a": "à",
           "---": "–", "--": "–", "~": " ", "\\&": "&"}
    for a, b in rep.items():
        s = s.replace(a, b)
    return re.sub(r"[{}]", "", s).strip()


def field(tex, name):
    m = re.search(r"\\newcommand\{\\%s\}\{(.*?)\}\s*(%%|\n)" % name, tex)
    return m.group(1).strip() if m else ""


# ---------------------------------------------------------------- bibliography
def parse_bib(text):
    out = {}
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", text, re.S):
        body = m.group(3) + "\n"
        f = {}
        for fm in re.finditer(r"(\w+)\s*=\s*\{", body):
            val, _ = braced(body, fm.end() - 1)
            f[fm.group(1).lower()] = val
        out[m.group(2)] = (m.group(1).lower(), f)
    return out


def authors(f):
    raw = detex(f.get("author", f.get("editor", "")))
    people = [p.strip() for p in re.split(r"\s+and\s+", raw) if p.strip()]
    res = []
    for p in people:
        if "," in p:
            last, first = [x.strip() for x in p.split(",", 1)]
        else:
            parts = p.split()
            last, first = parts[-1], " ".join(parts[:-1])
        initials = " ".join(x[0] + "." for x in re.split(r"[\s.]+", first) if x)
        res.append((last, initials))
    return res


def surnames(f):
    a = [last for last, _ in authors(f)]
    if len(a) == 1:
        return a[0]
    if len(a) <= 3:
        return ", ".join(a[:-1]) + " and " + a[-1]
    return a[0] + " et al."


def ref_entry(kind, f):
    a = authors(f)
    names = [f"{l}, {i}".strip().rstrip(",") for l, i in a]
    who = names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]
    year = f.get("year", "n.d.")
    title = detex(f.get("title", ""))
    if kind == "book":
        ed = f.get("edition", "")
        ed = {"2": ", 2nd edn", "3": ", 3rd edn"}.get(ed, f", {ed}th edn" if ed else "")
        pub = detex(f.get("publisher", ""))
        addr = detex(f.get("address", ""))
        return f"{who} ({year}). *{title}*{ed}. {pub}{', ' + addr if addr else ''}."
    if kind == "incollection":
        eds = detex(f.get("editor", ""))
        bt = detex(f.get("booktitle", ""))
        pages = detex(f.get("pages", ""))
        pub = detex(f.get("publisher", ""))
        return (f"{who} ({year}). {title}. In {eds} (ed.), *{bt}*, {pages}. {pub}.")
    venue = detex(f.get("journal", f.get("booktitle", f.get("school", ""))))
    vol, num = f.get("volume", ""), f.get("number", "")
    pages = detex(f.get("pages", ""))
    loc = vol + (f"({num})" if num else "")
    s = f"{who} ({year}). {title}. *{venue}*"
    s += f", {loc}" if loc else ""
    s += f", {pages}" if pages else ""
    s += "."
    if f.get("note"):
        s += " " + detex(f["note"]) + "."
    return s


# ---------------------------------------------------------------- main
def main(post, force=False):
    pdir = ROOT / "docs" / "posts" / post
    meta = json.loads((pdir / "meta.json").read_text())
    sub = meta.get("substack", {})
    out_dir = pdir / "substack"
    target = out_dir / "article.md"
    if sub.get("frozen") and not force:
        print(f"skip: {target} is frozen (published); --force overwrites")
        return
    proj = (pdir / "project.tex").read_text()
    tex = (pdir / "main.tex").read_text()
    bib = parse_bib((pdir / "references.bib").read_text())
    nn, slug = meta["issue"], meta["slug"]

    body = tex.split("\\begin{document}", 1)[1].split("\\end{document}", 1)[0]
    body = re.sub(r"(?m)(?<!\\)%.*$", "", body)
    body = body.split("\\bibliographystyle", 1)[0]
    body = body.split("{\\let\\SAIMplainauthors", 1)[0]

    # --- numbering: result kinds on own counters, only if >1 of a kind
    envs = re.findall(r"\\begin\{(%s)\}" % "|".join(KINDS), body)
    count = {k: envs.count(k) for k in KINDS}
    seen = {k: 0 for k in KINDS}
    labels = {}
    for m in re.finditer(r"\\begin\{(%s|assumption)\}(\[[^\]]*\])?\s*\\label(?:\[\w+\])?\{(.+?)\}" % "|".join(KINDS), body):
        kind, lab = m.group(1), m.group(3)
        if kind == "assumption":
            n = len([v for v in labels.values() if v[0] == "assumption"]) + 1
            labels[lab] = ("assumption", f"A{n}")
            continue
        seen[kind] += 1
        labels[lab] = (kind, str(seen[kind]) if count[kind] > 1 else "")
    # equations: number only those referenced, in order of appearance
    refd = set(re.findall(r"\\(?:eqref|cref|Cref)\{([^}]*)\}", body))
    refd = {k.strip() for r in refd for k in r.split(",")}
    eqn = 0
    for m in re.finditer(r"\\begin\{equation\}(.*?)\\end\{equation\}", body, re.S):
        lm = re.search(r"\\label\{(.+?)\}", m.group(1))
        if lm and lm.group(1) in refd:
            eqn += 1
            labels[lm.group(1)] = ("equation", str(eqn))
    fig_labels = re.findall(r"\\label\{(fig:[^}]+)\}", body)
    nfig = len(fig_labels)
    for i, lab in enumerate(fig_labels, 1):
        labels[lab] = ("figure", str(i) if nfig > 1 else "")

    def ref(o, keys):
        parts = []
        for k in keys.split(","):
            k = k.strip()
            if k.startswith("lst:"):
                parts.append("the code below")
                continue
            kind, num = labels.get(k, ("?", "??"))
            if kind == "equation":
                parts.append(f"({num})")
            elif kind == "assumption":
                parts.append(num)
            elif kind == "figure":
                parts.append(f"Figure {num}" if num else "the figure")
            elif num:
                parts.append(f"{NAME.get(kind, kind)} {num}")
            else:
                parts.append(f"the {kind}")
        return " and ".join(parts)

    def cite_items(keys):
        items = []
        for k in keys.split(","):
            kind, f = bib.get(k.strip(), ("misc", {"author": k}))
            items.append((surnames(f), f.get("year", "n.d.")))
        return items

    def citet(o, keys):
        return "; ".join(f"{a} ({y})" for a, y in cite_items(keys))

    def citealp(o, keys):
        return "; ".join(f"{a}, {y}" for a, y in cite_items(keys))

    def citep(o, keys):
        pre = o[0].strip() + " " if len(o) >= 2 and o[0].strip() else ""
        post = o[-1].strip() if o and o[-1].strip() and len(o) in (1, 2) else ""
        if len(o) == 2 and not o[1].strip():
            post = ""
        core = "; ".join(f"{a}, {y}" for a, y in cite_items(keys))
        return "(" + pre + core + (f"; {post}" if post else "") + ")"

    # result environments (before citations, so notes keep their form)
    def env(m):
        kind, opt, rest = m.group(1), (m.group(2) or "")[1:-1], m.group(3)
        lm = re.match(r"\s*\\label(?:\[\w+\])?\{(.+?)\}", rest)
        if lm:
            lab, rest = lm.group(1), rest[lm.end():]
            num = labels.get(lab, (kind, ""))[1]
        else:
            num = ""
        if kind == "assumption":
            head = f"\\textbf{{Assumption {num}.}}"
        else:
            opt = sub_macro(opt, "citet", lambda o, k: citealp(o, k), opt=True)
            head = f"\\textbf{{{NAME[kind]}{' ' + num if num else ''}}}"
            head += f" ({opt})\\textbf{{.}}" if opt else "\\textbf{.}"
            if opt and kind == "theorem":
                head = f"\\textbf{{{NAME[kind]}{' ' + num if num else ''} ({opt}).}}"
        return "\n\n" + head + " " + rest.strip() + "\n\n"
    body = re.sub(r"\\begin\{(%s|assumption)\}(\[[^\]]*\])?(.*?)\\end\{\1\}" % "|".join(KINDS),
                  env, body, flags=re.S)

    body = sub_macro(body, "cref", ref, opt=True)
    body = sub_macro(body, "Cref", lambda o, k: ref(o, k)[:1].upper() + ref(o, k)[1:], opt=True)
    body = sub_macro(body, "eqref", ref)
    body = sub_macro(body, "citet", citet, opt=True)
    body = sub_macro(body, "Citet", citet, opt=True)
    body = sub_macro(body, "citealp", citealp, opt=True)
    body = sub_macro(body, "citep", citep, opt=True)

    def proof(m):
        o = m.group(1)
        inner = m.group(2)
        k = [0]

        def step(o2, a):
            k[0] += 1
            return f"\\textbf{{Step {k[0]}: {a[:1].lower() + a[1:]}.}}"
        inner = sub_macro(inner, "step", step)
        head = "\\emph{Proof.}" if not o or "Proof of" in o else f"\\emph{{{o[1:-1]}.}}"
        if o and "Proof of" in o:
            head = ""
        return "\n\n" + head + " " + inner.strip() + " ∎\n\n"
    body = re.sub(r"\\begin\{proof\}(\[[^\]]*\])?(.*?)\\end\{proof\}", proof, body, flags=re.S)

    def equation(m):
        inner = m.group(1)
        lm = re.search(r"\\label\{(.+?)\}", inner)
        tag = ""
        if lm:
            if lm.group(1) in labels:
                tag = r" \qquad (%s)" % labels[lm.group(1)][1]
            inner = inner.replace(lm.group(0), "")
        return "\n\\[" + inner.strip() + tag + "\\]\n"
    body = re.sub(r"\\begin\{equation\}(.*?)\\end\{equation\}", equation, body, flags=re.S)

    figs = []

    def figure(m):
        cap = re.search(r"\\caption\{", m.group(0))
        caption = braced(m.group(0), cap.end() - 1)[0] if cap else ""
        figs.append(caption)
        n = len(figs)
        return f"\n\n@@FIG{n}@@\n\n"
    body = re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", figure, body, flags=re.S)

    # tables -> numbered lists (Substack has no tables)
    def table(m):
        rows = re.split(r"\\\\", m.group(1))
        items = []
        header = True
        for r in rows:
            r = re.sub(r"\\(toprule|midrule|bottomrule|hline)", "", r).strip()
            if not r:
                continue
            cells = [c.strip() for c in r.split("&")]
            if header and "SAIMTableHead" in r:
                header = False
                continue
            if len(cells) == 3:
                items.append(f"{cells[0]}. Exact {cells[1]}; numerical {cells[2]}.")
            elif len(cells) == 2:
                items.append(f"{cells[0]}: {cells[1]};")
            else:
                items.append("; ".join(cells) + ".")
        if items and items[-1].endswith(";"):
            items[-1] = items[-1][:-1] + "."
        return "\n\\begin{enumerate}\n" + "\n".join("\\item " + i for i in items) + "\n\\end{enumerate}\n"
    body = re.sub(r"\\begin\{tabular\}\{[^}]*\}(.*?)\\end\{tabular\}", table, body, flags=re.S)

    boxes = {"tldr": "\\textbf{TL;DR.} ", "mainresult": "", "pullquote": ""}
    for envn, lead in boxes.items():
        def bq(m, lead=lead, envn=envn):
            inner = m.group(1).strip()
            if envn == "pullquote":
                return "\n\n@@BQ@@\\textbf{" + inner + "} (pull quote)@@EQ@@\n\n"
            if envn == "mainresult":
                return "\n\n" + inner + "\n\n"
            return "\n\n@@BQ@@" + lead + inner + "@@EQ@@\n\n"
        body = re.sub(r"\\begin\{%s\}(?:\[[^\]]*\])?(.*?)\\end\{%s\}" % (envn, envn), bq, body, flags=re.S)

    secs = {"SecSetup": "Setup and notation", "SecResult": "Result", "SecProof": "Proof",
            "SecInsight": "Insights", "SecUses": "Uses and consequences",
            "SecExample": "Worked example", "SecCheck": "Numerical check", "SecNotes": "Notes"}
    for k, v in secs.items():
        body = body.replace("\\" + k, "\n\\section{" + v + "}\n")
    body = sub_macro(body, "interchange", lambda o, a: f"\\emph{{Justification ({a}).}}")
    body = sub_macro(body, "SAIMTableHead", lambda o, a: a)
    body = sub_macro(body, "texorpdfstring", lambda o, a, b: a, nargs=2)
    # the PDF's Code paragraph is replaced by the Substack one
    body = re.sub(r"\\paragraph\{Code\.\}.*?(?=\\section|\Z)", "@@CODE@@\n", body, flags=re.S)
    body = sub_macro(body, "paragraph", lambda o, a: f"\n\n\\textbf{{{a}}} ")
    for drop in ["\\begin{center}", "\\end{center}", "\\maketitle", "\\qedhere",
                 "\\small", "\\centering", "\\clearpage", "\\appendix"]:
        body = body.replace(drop, "")
    body = re.split(r"\\section\{Code\}", body)[0]

    macros = (ROOT / "skeleton/shared/components/math.tex").read_text()
    macros = re.sub(r"(?m)^\s*%.*$", "", macros).replace("\\providecommand", "\\newcommand")
    macros = re.sub(r"\\newcommand\{\\(dd|eqd)\}.*\n", "", macros)
    macros += "\n\\newcommand{\\dd}{\\mathrm{d}}\n\\newcommand{\\coloneqq}{\\mathrel{:=}}\n\\newcommand{\\eqd}{\\overset{d}{=}}\n"
    src = macros + "\\begin{document}\n" + body + "\n\\end{document}\n"
    r = subprocess.run(["pandoc", "-f", "latex", "-t", "gfm+tex_math_dollars",
                        "--wrap=none", "--shift-heading-level-by=1"],
                       input=src, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr)
    md = r.stdout

    def block_math(m):
        return "\n\n$$\n" + m.group(1).strip() + "\n$$\n\n"
    md = re.sub(r"[ \t]*\$\$(.+?)\$\$[ \t]*", block_math, md, flags=re.S)
    md = re.sub(r"\n\n\$\$\n(.*?)\n\$\$\n\n([.,;:])", lambda m: "\n\n$$\n" + m.group(1) + m.group(2) + "\n$$\n\n", md, flags=re.S)
    md = re.sub(r"@@BQ@@(.*?)@@EQ@@", lambda m: "\n".join(("> " + l).rstrip() for l in re.sub(r"\n[ \t]*\n(?:[ \t]*\n)+", "\n\n", m.group(1).strip()).split("\n")), md, flags=re.S)

    def fig_md(m):
        n = int(m.group(1))
        name = f"{slug}-figure.png" if len(figs) == 1 else f"{slug}-figure-{n}.png"
        cap = subprocess.run(["pandoc", "-f", "latex", "-t", "plain", "--wrap=none"],
                             input=macros + "\\begin{document}\n" + figs[n - 1] + "\n\\end{document}",
                             capture_output=True, text=True).stdout.strip()
        cap = re.sub(r"\s+", " ", cap)
        return f"![{cap}]({name})\n\n*{cap}*"
    md = re.sub(r"@@FIG(\d+)@@", fig_md, md)

    code = (pdir / "code" / "check.py").read_text()
    out = subprocess.run([sys.executable, "check.py"], cwd=pdir / "code",
                         capture_output=True, text=True).stdout
    code_md = ("**Code.** Every number above is printed by the script below (Python 3, NumPy, SciPy); "
               f"its docstring gives the requirements.\n\n```python\n{code.rstrip()}\n```\n\n"
               f"**Output:**\n\n```\n{out.rstrip()}\n```\n")
    md = md.replace("@@CODE@@", code_md)

    title, subt = field(proj, "ProjectTitle"), field(proj, "ProjectSubtitle")
    issue = field(proj, "ProjectIssue")
    date = field(proj, "ProjectDate")
    head = f"# Probability Notes {issue}: {title}\n\n*{subt}*\n\n"
    if sub.get("url"):
        head += f"Published {date}: {sub['url']}\n\n"
    md = md.strip()
    pdf_line = (f"[PDF attachment: *Probability Notes {issue}: {title} (PDF)*. "
                "Full proofs, references and the numerical-check code.]")
    md = re.sub(r"^(> \*\*TL;DR\.\*\*.*?)(\n\n|$)", lambda m: m.group(1) + "\n\n" + pdf_line + "\n\n", md, count=1, flags=re.S)
    refs = sorted((ref_entry(*bib[k]) for k in bib), key=lambda s: s.lower())
    md = head + md + "\n\n### References\n\n" + "\n\n".join(refs) + "\n"
    md = re.sub(r"(?<=[\w)\]}'|])\\mathrm\{d\}(?=[a-zA-Z])", r"\\,\\mathrm{d}", md)
    md = re.sub(r"(?m)^(\d+)\.  ", r"\1. ", md)
    md = re.sub(r"(?m)^(\d+\. .*)\n\n(?=\d+\. )", r"\1\n", md)
    md = re.sub(r"(?m)^(\d+\. .*)\n\n(?=\d+\. )", r"\1\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    out_dir.mkdir(exist_ok=True)
    target.write_text(md)
    print(target)


if __name__ == "__main__":
    main(sys.argv[1], force="--force" in sys.argv)
