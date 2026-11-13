# SAIM Blog Post Template v1.2

Short-form post on the SAIM Computer Modern Sans system: no cover page, a
reading measure of roughly 70 characters, and an author card at the end.

| Target | Command | Output |
|---|---|---|
| A4 post | `make post` | `build/saim-post.pdf` |
| 160 x 240 mm screen post | `make post-screen` | `build/saim-post-screen.pdf` |

Class options: `a4paper` (default), `letterpaper`, `screen`, `numbered`
(number the headings; unnumbered by default). On Overleaf, use
`\documentclass[screen]{saim-blog}`.

## Edit once

1. `project.tex`: title, short title, subtitle, series label, date, version, keywords, issue number, reading time, tags, author bio, links.
2. `people.tex`: authors, affiliations, emails, optional corresponding author.

```tex
\Affiliation{saim}{sAIm Labs}
\Affiliation{exampleu}{Example University}
\Author{Omid Shams Solari}{}{saim}
\Author{Second Author}{second.author@example.edu}{saim,exampleu}
\CorrespondingAuthor{Second Author}{second.author@example.edu}   % optional
```

Affiliation superscripts appear automatically once two or more affiliations
are declared. `shared/metadata.tex` is registry code; do not edit it.

Any of `\ProjectIssue`, `\ProjectReadingTime`, `\ProjectTags`,
`\ProjectAuthorBio`, `\ProjectLinks` can be left empty to hide it.

## Components

- `tldr`: the post in two or three sentences, under the opening
- `pullquote`: one sentence lifted from the prose
- `takeaway`, `context`, `result`, `caution`, `aside`: semantic callouts
- `\postfigure[width]{file}{caption}`: image figure on the reading measure
- `\postauthorcard`: author, affiliation, bio, links
- Listings: `style=python` or `style=console`
- References print under "Further reading" (`plainnat`, numeric)
- Logo and mark: `\postlogo{file}`, `\postmark{file}`

The sample post (the birthday problem) checks its own numbers: p(22) = 0.476,
p(23) = 0.507, and the exponential approximation never exceeds the exact value,
with a maximum error of 1.03 percentage points (at n = 33).

## Shared layer

- `shared/brand/`: palette, Computer Modern Sans typography, logos
- `shared/components/`: callouts, evidence tags, table columns, listings, TikZ, notation
- `shared/bibliography/`: `references.bib`

Evidence tags: `\MeasuredTag`, `\ReproducedTag`, `\SyntheticTag`,
`\PlannedTag`, `\IllustrativeTag`, `\ExternalTag`.

## Overleaf

Upload the ZIP as a new project. `main.tex` is at the root; set the compiler
to **pdfLaTeX**. No font files are bundled or required.

## Local build

`make` builds every target into `build/` with `latexmk`; `make clean` removes it.
The release was compiled from a clean extraction with no errors, warnings,
overfull or underfull boxes, or undefined references, and with Type 1 fonts only.

See `CHANGELOG.md` for the v1.2 fixes.
