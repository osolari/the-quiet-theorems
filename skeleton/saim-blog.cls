% saim-blog.cls - SAIM short-form blog-post class (pdfLaTeX).
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{saim-blog}[2026/11/08 Computer Modern Sans blog-post system, v1.2]

% Options:
%   a4paper (default) | letterpaper   print-friendly page with a reading measure
%   screen                            160 x 240 mm page for phones, tablets, and
%                                     PDF attachments to social posts
%   numbered                          number section headings (default: unnumbered)
\newif\ifSAIMblog@screen \SAIMblog@screenfalse
\newif\ifSAIMblog@letter \SAIMblog@letterfalse
\newif\ifSAIMblog@numbered \SAIMblog@numberedfalse
\DeclareOption{a4paper}{\SAIMblog@screenfalse\SAIMblog@letterfalse}
\DeclareOption{letterpaper}{\SAIMblog@screenfalse\SAIMblog@lettertrue}
\DeclareOption{screen}{\SAIMblog@screentrue}
\DeclareOption{numbered}{\SAIMblog@numberedtrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[11pt]{article}

% ---------------------------------------------------------------------------
% Page geometry. A blog post is read, not filed: keep the measure near
% 65-75 characters on paper and fill the width on the screen page.
% ---------------------------------------------------------------------------
\ifSAIMblog@screen
  \RequirePackage[paperwidth=160mm,paperheight=240mm,
    top=19mm,bottom=19mm,left=15mm,right=15mm,headheight=21pt,headsep=7mm,footskip=10mm]{geometry}
\else
  \ifSAIMblog@letter
    \RequirePackage[letterpaper,top=20mm,bottom=22mm,hmargin=40mm,
      headheight=21pt,headsep=8mm,footskip=11mm]{geometry}
  \else
    \RequirePackage[a4paper,top=20mm,bottom=22mm,hmargin=38mm,
      headheight=21pt,headsep=8mm,footskip=11mm]{geometry}
  \fi
\fi

\input{shared/brand/typography.tex}
\RequirePackage[english]{babel}
\RequirePackage{ragged2e}
\RequirePackage{etoolbox}
\RequirePackage{enumitem}
\RequirePackage{graphicx}
\RequirePackage{booktabs,array,tabularx}
\RequirePackage{amsmath,amssymb,mathtools}
\RequirePackage{xcolor}
\input{shared/brand/colors.tex}
\RequirePackage[most]{tcolorbox}
\usetikzlibrary{arrows.meta,positioning,calc}
\RequirePackage{listings}
\RequirePackage{eso-pic}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{titlesec}
\RequirePackage{caption}
\RequirePackage[numbers,sort&compress]{natbib}
\RequirePackage{hyperref}
\RequirePackage[noabbrev,nameinlink]{cleveref}
\input{shared/components/boxes.tex}
\input{shared/components/evidence.tex}
\input{shared/components/listings.tex}
\input{shared/components/table-columns.tex}
\color{Ink}

\hypersetup{colorlinks=true,linkcolor=PrimaryDark,citecolor=PrimaryDark,
  urlcolor=Secondary,pdfborder={0 0 0}}

% Body rhythm: slightly airier than the paper; first-line indents are
% replaced by paragraph space, as on the web.
\setstretch{1.12}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.72em plus 0.12em minus 0.08em}
\setlength{\emergencystretch}{2em}
\raggedbottom
\setlist[itemize]{leftmargin=1.4em,itemsep=2pt,topsep=2pt,parsep=0pt}
\setlist[enumerate]{leftmargin=1.6em,itemsep=2pt,topsep=2pt,parsep=0pt}
\renewcommand{\labelitemi}{\textcolor{Primary}{\raisebox{0.18ex}{\scriptsize$\bullet$}}}
\def\bibfont{\small}
\setlength{\bibsep}{3pt}

% ---------------------------------------------------------------------------
% Headings
% ---------------------------------------------------------------------------
\ifSAIMblog@numbered\setcounter{secnumdepth}{2}\else\setcounter{secnumdepth}{0}\fi
\titleformat{\section}[hang]{\Large\rmfamily\bfseries\color{Ink}}
  {\color{Primary}\thesection}{0.55em}{}
\titleformat{\subsection}[hang]{\large\rmfamily\bfseries\color{Ink}}
  {\color{Primary}\thesubsection}{0.5em}{}
\titleformat{\paragraph}[runin]{\normalsize\rmfamily\bfseries\color{Ink}}{}{0pt}{}
\titlespacing*{\section}{0pt}{17pt plus 3pt minus 2pt}{4pt}
\titlespacing*{\subsection}{0pt}{12pt plus 2pt minus 1pt}{3pt}
\titlespacing*{\paragraph}{0pt}{6pt}{0.5em}

\captionsetup{singlelinecheck=false,justification=raggedright,font={small},
  labelfont={bf,color=PrimaryDark},textfont={color=Muted},labelsep=period,skip=5pt}

% ---------------------------------------------------------------------------
% Post metadata. Defaults read project.tex when the macros exist there.
% ---------------------------------------------------------------------------
\newcommand{\SAIMblog@series}{\ifdefined\ProjectSeriesLabel\ProjectSeriesLabel\else SAIM NOTES\fi}
\newcommand{\SAIMblog@logo}{shared/brand/logos/saim-logo-color.png}
\newcommand{\SAIMblog@mark}{shared/brand/logos/saim-mark-color.png}
\newcommand{\postlogo}[1]{\renewcommand{\SAIMblog@logo}{#1}}
\newcommand{\postmark}[1]{\renewcommand{\SAIMblog@mark}{#1}}

% Small typographic primitives
\newcommand{\saimblogeyebrow}[1]{{\SAIMNavigationFont\fontsize{7.6}{9}\selectfont\color{Primary}\textls[150]{\MakeUppercase{#1}}}}
\newcommand{\saimblogsep}{\enspace\textcolor{RuleDark}{\textbullet}\enspace}

% Tag chips: \posttags{probability, statistics, derivations}
\newcommand{\saimblogchip}[1]{%
  \begingroup\setlength{\fboxsep}{2.2pt}\setlength{\fboxrule}{0.45pt}%
  \fcolorbox{Rule}{LightPanel}{\textcolor{Muted}{\fontsize{7.4}{8.6}\selectfont\strut #1}}%
  \endgroup}
\ExplSyntaxOn
\NewDocumentCommand{\SAIMblogTagRow}{m}
  {
    \clist_map_inline:nn {#1} { \saimblogchip{##1}\hspace{3pt}\allowbreak }
  }
\ExplSyntaxOff

% ---------------------------------------------------------------------------
% Opening: accent rule, eyebrow, title, dek, byline, tags. No cover page:
% the argument starts on page 1.
% ---------------------------------------------------------------------------
\newcommand{\SAIMblog@accent}{%
  \AddToShipoutPictureBG*{%
    \AtPageUpperLeft{\color{Primary}\rule[-3.2pt]{\paperwidth}{3.2pt}}}}

\renewcommand{\maketitle}{%
  \SAIMblog@accent
  \thispagestyle{plain}%
  \begingroup
  \setlength{\parskip}{0pt}\setstretch{1}%
  \noindent
  \begin{minipage}[b]{0.74\textwidth}
    \saimblogeyebrow{\SAIMblog@series}%
    \ifdefined\ProjectIssue\ifx\ProjectIssue\@empty\else
      \enspace\textcolor{RuleDark}{\fontsize{7.6}{9}\selectfont/}\enspace\saimblogeyebrow{\ProjectIssue}\fi\fi
  \end{minipage}%
  \begin{minipage}[b]{0.26\textwidth}
    \raggedleft\includegraphics[height=6.5mm]{\SAIMblog@logo}
  \end{minipage}\par
  \vspace{10pt}
  {\SAIMFrontRagged\SAIMCoverTitleFont
   \ifSAIMblog@screen\fontsize{23}{27}\else\fontsize{26}{30.5}\fi\selectfont
   \color{Ink}\ProjectTitle\par}
  \ifdefined\ProjectSubtitle\ifx\ProjectSubtitle\@empty\else
    \vspace{7pt}
    {\SAIMFrontRagged\SAIMCoverSubtitleFont\fontsize{13}{17}\selectfont\color{Muted}\ProjectSubtitle\par}
  \fi\fi
  \vspace{12pt}
  {\small\SAIMMetaFont
   \textbf{\color{Ink}\ProjectAuthorsPlainDisplay}%
   \saimblogsep{\color{Muted}\ProjectDate}%
   \ifdefined\ProjectReadingTime\ifx\ProjectReadingTime\@empty\else
     \saimblogsep{\color{Muted}\ProjectReadingTime}\fi\fi\par}
  \ifdefined\ProjectTags\ifx\ProjectTags\@empty\else
    \vspace{7pt}{\RaggedRight\SAIMblogTagRow{\ProjectTags}\par}
  \fi\fi
  \vspace{10pt}
  {\color{Rule}\rule{\textwidth}{0.6pt}}\par
  \vspace{4pt}
  \endgroup
}

% ---------------------------------------------------------------------------
% Running furniture: page 1 carries only the folio; later pages add the
% short title so a printed or forwarded page still identifies the post.
% ---------------------------------------------------------------------------
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\rmfamily\scriptsize\color{Muted}\ProjectShortTitle}
\fancyhead[R]{\rmfamily\scriptsize\color{Muted}\SAIMblog@series}
\fancyfoot[L]{\rmfamily\scriptsize\color{Muted}\ProjectAuthorsPlainDisplay}
\fancyfoot[R]{\rmfamily\scriptsize\color{Muted}\thepage\,/\,\pageref*{LastPage}}
\renewcommand{\headrulewidth}{0.35pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{Rule}\leaders\hrule height \headrulewidth\hfill}}
\renewcommand{\footrulewidth}{0pt}
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyfoot[L]{\rmfamily\scriptsize\color{Muted}\ProjectAuthorsPlainDisplay}%
  \fancyfoot[R]{\rmfamily\scriptsize\color{Muted}\thepage\,/\,\pageref*{LastPage}}%
  \renewcommand{\headrulewidth}{0pt}}

% ---------------------------------------------------------------------------
% Blog components
% ---------------------------------------------------------------------------
% TL;DR: the post in two or three sentences, directly under the opening.
\newtcolorbox{tldr}[1][TL;DR]{saim/primary,breakable=false,
  title={\saimblogeyebrow{#1}},attach title to upper={\par\vspace{3pt}},
  before skip=6pt,after skip=10pt}

% Pull quote: one sentence worth lifting out of the prose.
\newenvironment{pullquote}{%
  \par\vspace{6pt}%
  \begin{tcolorbox}[blanker,breakable=false,left=12pt,right=6pt,top=2pt,bottom=2pt,
    borderline west={2.4pt}{0pt}{Primary}]
  \RaggedRight\hyphenpenalty=10000\exhyphenpenalty=10000\SAIMHeadingFont\fontsize{14.5}{19}\selectfont\color{PrimaryDark}}
  {\end{tcolorbox}\par\vspace{4pt}}

% Takeaway, context, result, and caution callouts.
\newtcolorbox{takeaway}[1][Takeaway]{saim/primary,title={#1}}
\newtcolorbox{context}[1][Context]{saim/blue,title={#1}}
\newtcolorbox{result}[1][Result]{saim/green,title={#1}}
\newtcolorbox{caution}[1][Caution]{saim/amber,title={#1}}
\newtcolorbox{aside}[1][Aside]{saim/neutral,title={#1}}

% Full-width figure helper that keeps captions on the reading measure.
\newcommand{\postfigure}[3][\textwidth]{%
  \begin{figure}[htbp]\centering\includegraphics[width=#1]{#2}\caption{#3}\end{figure}}

% End-of-post author card. Reads \ProjectAuthorBio and \ProjectLinks.
\newcommand{\postauthorcard}{%
  \par\vspace{6pt}%
  \begin{tcolorbox}[saim/outline,breakable=false,left=10pt,right=10pt,top=7pt,bottom=7pt,before skip=2pt]
    \begin{minipage}[t]{11mm}\vspace{0pt}\includegraphics[width=9mm]{\SAIMblog@mark}\end{minipage}%
    \hfill
    \begin{minipage}[t]{\dimexpr\linewidth-14mm\relax}\vspace{0pt}\RaggedRight
      {\bfseries\color{Ink}\ProjectAuthorsPlainDisplay}\par
      {\footnotesize\color{Muted}\ProjectAffiliationsPlainDisplay\par}
      \ifdefined\ProjectAuthorBio\ifx\ProjectAuthorBio\@empty\else
        \vspace{4pt}{\small\ProjectAuthorBio\par}\fi\fi
      \ifdefined\ProjectLinks\ifx\ProjectLinks\@empty\else
        \vspace{4pt}{\footnotesize\ProjectLinks\par}\fi\fi
    \end{minipage}
  \end{tcolorbox}}

% Short reference list headed "Further reading" rather than a numbered section.
\renewcommand{\bibsection}{%
  \section*{Further reading}%
  \vspace{-4pt}}

\endinput
