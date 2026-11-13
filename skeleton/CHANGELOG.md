# Changelog

## v1.2 - 2026-11-08

Split into four independent packages (paper, slides, book, blog), each an
Overleaf-ready project with `main.tex` at the root.

### Fixed
- **Bitmap fonts.** `\textbullet` resolved to the TS1 encoding via `textcomp`,
  pulling METAFONT bitmap glyphs (`tcss0800`, Type 3) into slides, book, and
  gallery PDFs whenever cm-super was absent. Bullets now come from the OMS
  symbol font; every PDF contains Type 1 outlines only.
- **Email angle brackets.** `\ProjectAuthorEmailsPlainDisplay` typeset
  `<address>` in OT1 Computer Modern Sans, which prints as `¡address¿`. Now uses
  `\textless`/`\textgreater`.
- **Undefined `\addtolist`.** The paper class redefined `\addtolist` with
  `\renewcommand`, but `article` does not define it; the class now uses a
  private `\SAIM@addtolist`.
- **Architecture diagram.** Output-to-QA connectors ran through the
  "Slides + notes" and "Technical book" boxes, the shared-layer label
  overflowed its box, and the "revise once" label sat on its dashed line.
  Rebuilt with explicit coordinates and distribution/collector buses.
- **Calibration cards.** The three cards were vertically centred on differing
  content heights, so they did not share a top edge. Bodies are now top-aligned.
- **Book unnumbered chapters.** Every unnumbered chapter, including the
  back-matter References, carried a "Front matter" eyebrow. The label now
  follows `\frontmatter`/`\mainmatter`/`\backmatter`.
- **Book appendix badge.** Appendix chapters were badged "CHAPTER A"; they now
  read "APPENDIX A".
- **Book chapter spacing.** A second `\titlespacing*{\chapter}` silently
  overrode the numbered-chapter spacing; it now targets numberless chapters only.
- **Exercise numbering.** Front-matter exercises were numbered "0.1" and the
  solutions referred to them by hard-coded text. Exercises carry labels and
  solutions use `\ref`.
- **Cover and title-page overprinting.** The book subtitle and the slide
  subtitle sat at fixed offsets, so a three-line title overprinted them. All
  rows are now chained to the row above.
- **Slide title overflow.** Titles longer than three lines pushed the author
  block off the slide; the title now steps down from 25pt to 20pt or 17pt.
- **Single-affiliation superscripts.** A lone affiliation produced a stray
  "¹" after every name. Marks now appear only with two or more affiliations.
- **Slide footer.** Frames before the first section showed a dangling "/".
- **Continuation numbering.** A one-page `allowframebreaks` frame was titled
  "References I". Numbering now starts from the second page.
- **Catcode hygiene.** `\makeatletter`/`\makeatother` pairs inside `.cls`/`.sty`
  files flipped `@` mid-file; removed.
- **latexmkrc.** Removed `$force_mode = 1` (it lets builds continue past
  errors) and a host-specific BibTeX path.
- **Evidence tags.** Tighter padding keeps inline tags within body leading.

### Changed
- Identity moved to a root-level `project.tex`; people remain in a root-level
  `people.tex`. `shared/metadata.tex` is now registry code only.
- Eyebrow labels on the paper, slide title page, book cover, and lecture notes
  come from `\ProjectSeriesLabel` instead of hard-coded text.
- `\saimSectionDivider` takes an optional first argument for its footnote
  line; v1.1 printed the same boilerplate sentence on every divider.
- Paper class options `notoc` and `compact` (two-column body from page 1).

### Added
- `saim-blog` package: short-form post class with A4, US Letter, and
  160 x 240 mm screen layouts; series and issue eyebrow; dek; byline with
  reading time; tag chips; TL;DR, pull quote, takeaway, context, result,
  caution, and aside components; author card; "Further reading".

### Removed
- The component gallery target. Each package's sample document now
  exercises its own components.

## v1.1 - 2026-08-15

- Adopted the author/affiliation registry architecture from the supplied Cerebras v1.12 template.
- Added `shared/people.tex` as the single source of truth for authors, affiliations, and emails.
- Set the default SAIM author to Omid Shams Solari and the default affiliation to sAIm Labs.
- Added multi-affiliation superscripts and compile-time validation of affiliation keys.
- Added optional `\CorrespondingAuthor{Name}{email}` override while retaining first-author correspondence as the default.
- Propagated people metadata into paper, report, slides, speaker notes, lecture notes, book, gallery, and PDF properties.
- Separated typeset author strings from clean PDF/bibliography/plain-text representations.
- Reworked slide and book cover metadata into separate author, affiliation, date/version, and contact rows.
- Removed hard-coded author and affiliation strings from embedded paper mockups.
- Added `textcomp`, normalized the Beamer font theme, mapped italic requests to the native CM Sans slanted face, and changed code comments to slanted text.
- Refined evidence-tag tracking and metadata line handling.
- Changed release packaging to a flat Overleaf-ready ZIP root.

## v1.0 - 2026-08-04

- Rebuilt the supplied SAIM paper and slide identities as one unified source tree.
- Adopted the supplied Cerebras v1.8 architecture for paper, report, slides,
  notes, lecture notes, technical book, component gallery, and build tooling.
- Replaced all Cerebras branding with the supplied SAIM logos and an
  indigo/lavender semantic palette.
- Standardized Computer Modern Sans typography across body text, headings,
  tables, captions, diagrams, running furniture, and slides.
- Added shared metadata, components, figures, tables, code, bibliography, and
  evidence-status labels.
- Preserved compatibility aliases used by the prior SAIM manuscript and Beamer
  templates.
