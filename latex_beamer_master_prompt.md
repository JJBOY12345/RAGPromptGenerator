# Master Prompt — LaTeX Beamer Presentation Generation

> Beamer is LaTeX's presentation framework. It produces a pixel-sharp, mathematically precise PDF slide deck that is the gold standard in academic and technical presentations. This prompt tells Claude exactly how to produce one.
>
> Paste everything below the second `---` into a new conversation. Fill in the `[BRACKETED]` placeholders and send.

---

## HOW TO USE THIS PROMPT

1. Copy everything below the second `---`.
2. Paste it as your **first message** in a new conversation.
3. Fill in every bracketed section.
4. Attach any images or data files you want on the slides.

---

You are a professional LaTeX Beamer slide designer. I want you to produce a complete, compilable `.tex` source file for a polished presentation. Follow every instruction here exactly.

---

## 1. PRESENTATION IDENTITY

**Title:** [Full presentation title]

**Subtitle:** [Optional — a one-line descriptor or tagline]

**Author(s):** [Name(s), roll number or designation]

**Institution:** [e.g., SSN College of Engineering]

**Event / Course:** [e.g., ICS1402 — Database Systems, Semester IV Review]

**Date:** `\today` unless otherwise specified.

**Estimated slides:** [e.g., 12–15 slides]

---

## 2. THEME & VISUAL DESIGN

### 2a. Base Beamer Theme

Use a **custom theme** built from scratch using Beamer's inner/outer/colour/font theme layers — do NOT use the default themes (Warsaw, Madrid, Berlin etc.) which look dated.

Start from:
```latex
\usetheme{default}
\useinnertheme{circles}        % bullet point style
\useoutertheme{infolines}      % or {miniframes} for progress dots
```

Then override everything with `\setbeamercolor`, `\setbeamerfont`, and `\setbeamertemplate` commands as detailed below.

### 2b. Colour Palette

**My palette preference:** [Choose one from the list below, or describe your own]

| Name | Background | Primary | Accent | Text |
|---|---|---|---|---|
| **Midnight Navy** | `#0D1B2A` | `#1F4E79` | `#4FC3F7` | `#F0F4F8` |
| **Forest Academic** | `#FAFAFA` | `#2C5F2D` | `#97BC62` | `#1A1A1A` |
| **Warm Slate** | `#F7F6F3` | `#36454F` | `#B85042` | `#1A1A1A` |
| **Deep Teal** | `#FEFEFE` | `#028090` | `#02C39A` | `#1C1C1C` |
| **Cherry Bold** | `#FCFCFC` | `#990011` | `#2F3C7E` | `#1A1A1A` |
| **Charcoal Minimal** | `#1E1E1E` | `#3A3A3A` | `#E0E0E0` | `#F5F5F5` |

Define in LaTeX:
```latex
\definecolor{bgmain}{HTML}{...}
\definecolor{primary}{HTML}{...}
\definecolor{accent}{HTML}{...}
\definecolor{textmain}{HTML}{...}
\definecolor{textlight}{HTML}{...}   % muted, for captions/subtitles
```

### 2c. Colour Application Rules

```latex
% Background
\setbeamercolor{background canvas}{bg=bgmain}

% Title slide
\setbeamercolor{title}{fg=accent}
\setbeamercolor{subtitle}{fg=textlight}
\setbeamercolor{author}{fg=textmain}
\setbeamercolor{institute}{fg=textlight}
\setbeamercolor{date}{fg=textlight}

% Frame titles
\setbeamercolor{frametitle}{fg=primary, bg=bgmain}
\setbeamercolor{framesubtitle}{fg=textlight}

% Body text
\setbeamercolor{normal text}{fg=textmain, bg=bgmain}

% Blocks
\setbeamercolor{block title}{fg=bgmain, bg=primary}
\setbeamercolor{block body}{fg=textmain, bg=primary!10}

% Alert blocks (for key facts, warnings)
\setbeamercolor{block title alerted}{fg=bgmain, bg=accent}
\setbeamercolor{block body alerted}{fg=textmain, bg=accent!15}

% Example blocks (for code, examples)
\setbeamercolor{block title example}{fg=bgmain, bg=primary!70}
\setbeamercolor{block body example}{fg=textmain, bg=primary!10}

% Items / bullets
\setbeamercolor{item}{fg=accent}
\setbeamercolor{subitem}{fg=primary}

% Footer / headline
\setbeamercolor{footline}{fg=textlight, bg=bgmain}
\setbeamercolor{headline}{fg=textlight, bg=bgmain}
```

---

## 3. TYPOGRAPHY

```latex
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{microtype}

% Font sizes — Beamer uses 11pt base; scale up for readability
\setbeamerfont{title}{size=\LARGE, series=\bfseries}
\setbeamerfont{subtitle}{size=\large, series=\normalfont, shape=\itshape}
\setbeamerfont{frametitle}{size=\large, series=\bfseries}
\setbeamerfont{framesubtitle}{size=\normalsize}
\setbeamerfont{author}{size=\normalsize}
\setbeamerfont{institute}{size=\small}
\setbeamerfont{date}{size=\small}
\setbeamerfont{block title}{size=\normalsize, series=\bfseries}
\setbeamerfont{footline}{size=\tiny}
```

---

## 4. REQUIRED PACKAGES

```latex
\usepackage{booktabs}           % professional table rules
\usepackage{tabularx}           % auto-width table columns
\usepackage{array}              % column type customisation
\usepackage{multirow}           % spanning cells
\usepackage{colortbl}           % coloured rows
\usepackage{graphicx}           % images
\usepackage{caption}            % caption formatting
\usepackage{subcaption}         % side-by-side figures
\usepackage{listings}           % code blocks
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{tikz}               % for decorative shapes, progress bars
\usetikzlibrary{shapes,positioning,arrows.meta}
\usepackage{fontawesome5}       % icons (if needed)
\usepackage{tcolorbox}          % styled boxes
\tcbuselibrary{skins}
```

---

## 5. SLIDE DIMENSIONS

Use the 16:9 widescreen aspect ratio (standard for modern projectors):

```latex
\documentclass[aspectratio=169, 11pt]{beamer}
```

For traditional 4:3 (older projectors):
```latex
\documentclass[aspectratio=43, 11pt]{beamer}
```

**My preference:** [16:9 / 4:3]

---

## 6. FRAME TITLE TEMPLATE

Remove the default Beamer title line decoration and build a clean one:

```latex
\setbeamertemplate{frametitle}{
  \vskip0.4em
  \usebeamerfont{frametitle}\usebeamercolor[fg]{frametitle}\insertframetitle\\
  \ifx\insertframesubtitle\@empty\else
    \usebeamerfont{framesubtitle}\usebeamercolor[fg]{framesubtitle}%
    \insertframesubtitle
  \fi
  \vskip0.2em
  \textcolor{accent}{\rule{\linewidth}{1.2pt}}  % accent underline rule
  \vskip-0.4em
}
```

---

## 7. FOOTLINE

Build a three-part footer:

```latex
\setbeamertemplate{footline}{
  \leavevmode
  \hbox{%
    \begin{beamercolorbox}[wd=.33\paperwidth,ht=2.4ex,dp=1ex,left,leftskip=1em]{footline}
      \usebeamerfont{footline}\insertshortauthor
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.34\paperwidth,ht=2.4ex,dp=1ex,center]{footline}
      \usebeamerfont{footline}\insertshorttitle
    \end{beamercolorbox}%
    \begin{beamercolorbox}[wd=.33\paperwidth,ht=2.4ex,dp=1ex,right,rightskip=1em]{footline}
      \usebeamerfont{footline}\insertframenumber{} / \inserttotalframenumber
    \end{beamercolorbox}%
  }%
  \vskip0pt%
}
\setbeamertemplate{navigation symbols}{}  % removes the default nav icons
```

---

## 8. SLIDE TYPES — Use These Templates

### 8a. Title Slide (always first)

```latex
\begin{frame}[plain]
  \titlepage
\end{frame}
```

Beamer auto-fills title, subtitle, author, institute, date from `\title{}`, `\subtitle{}`, etc.

### 8b. Table of Contents (second slide)

```latex
\begin{frame}{Outline}
  \tableofcontents[hideallsubsections]
\end{frame}
```

### 8c. Section Divider Slide (between major sections)

```latex
\begin{frame}[plain]
  \begin{center}
    \vfill
    {\Large\bfseries\color{accent} Section Title}\\[0.5em]
    {\normalsize\color{textlight} Brief description of what's coming}
    \vfill
  \end{center}
\end{frame}
```

### 8d. Standard Content Slide (bullets)

```latex
\begin{frame}{Frame Title}
  \framesubtitle{Optional subtitle}
  \begin{itemize}
    \item First key point
    \begin{itemize}
      \item Detail or sub-point
    \end{itemize}
    \item Second key point
    \item Third key point
  \end{itemize}
\end{frame}
```

### 8e. Two-Column Slide (text + image, or text + table)

```latex
\begin{frame}{Frame Title}
  \begin{columns}[T]
    \begin{column}{0.52\textwidth}
      \begin{itemize}
        \item Key point one
        \item Key point two
      \end{itemize}
    \end{column}
    \begin{column}{0.44\textwidth}
      \includegraphics[width=\linewidth]{image.pdf}
      % or a table
    \end{column}
  \end{columns}
\end{frame}
```

### 8f. Highlighted Key-Fact Slide (big number / stat callout)

```latex
\begin{frame}{Frame Title}
  \begin{columns}[c]
    \begin{column}{0.45\textwidth}
      \centering
      {\fontsize{60}{66}\selectfont\bfseries\color{accent} 42}\\[0.3em]
      {\large\color{textlight} Entities in schema}
    \end{column}
    \begin{column}{0.5\textwidth}
      \begin{itemize}
        \item Supporting point
        \item Context or source
      \end{itemize}
    \end{column}
  \end{columns}
\end{frame}
```

### 8g. Block Slide (definition / theorem / key concept)

```latex
\begin{frame}{Frame Title}
  \begin{block}{Definition: Normal Form}
    A relation is in BCNF if every determinant is a superkey.
  \end{block}
  \begin{alertblock}{Key Insight}
    One transitive dependency is retained for practical simplicity.
  \end{alertblock}
  \begin{exampleblock}{Example}
    \texttt{zip\_code $\to$ state} in \texttt{policyholder}.
  \end{exampleblock}
\end{frame}
```

### 8h. Code Listing Slide

```latex
\begin{frame}[fragile]{Frame Title}
  \begin{lstlisting}[language=SQL, basicstyle=\ttfamily\scriptsize]
SELECT c.claim_id, c.claim_status, s.settlement_amount
FROM   claim c
JOIN   settlement s ON s.claim_id = c.claim_id
WHERE  c.claim_status = 'Approved';
  \end{lstlisting}
\end{frame}
```

Note: frames with `lstlisting` or `verbatim` **must** have `[fragile]`.

### 8i. Table Slide

```latex
\begin{frame}{Frame Title}
  \begin{table}
    \centering
    \scriptsize
    \begin{tabularx}{\linewidth}{l X l}
      \toprule
      \textbf{Column} & \textbf{Description} & \textbf{Type} \\
      \midrule
      claim\_id & Unique identifier & INT \\
      policy\_id & FK to policy & INT \\
      \bottomrule
    \end{tabularx}
  \end{table}
\end{frame}
```

Use `\scriptsize` or `\footnotesize` for tables on slides — default body text is too large.

### 8j. Image Full-Width Slide

```latex
\begin{frame}{Frame Title}
  \begin{center}
    \includegraphics[width=0.9\linewidth, height=0.78\textheight, keepaspectratio]{image.pdf}
  \end{center}
\end{frame}
```

Use `height=0.78\textheight, keepaspectratio` so large images don't overflow the frame.

### 8k. Thank You / Closing Slide (always last)

```latex
\begin{frame}[plain]
  \begin{center}
    \vfill
    {\LARGE\bfseries\color{accent} Thank You}\\[1em]
    {\large Questions \& Discussion}\\[1.5em]
    {\small\color{textlight} \insertauthor{} · \insertinstitute}
    \vfill
  \end{center}
\end{frame}
```

---

## 9. TABLE RULES ON SLIDES

Same as PDF rules, plus slide-specific ones:
- Always `\scriptsize` or `\footnotesize` inside table — never default size
- Max 4–5 columns on a single slide — if more, use two slides or split columns
- Use `tabularx` with `X` columns so the table fills the full slide width
- Alternating rows: `\rowcolors{2}{primary!10}{bgmain}`
- Never use vertical lines (`|`) — booktabs horizontal rules only
- `\caption` on slides should be short (≤8 words), placed below the table

---

## 10. OVERLAY / PROGRESSIVE REVEAL (optional)

If you want bullet points to appear one at a time:

```latex
\begin{frame}{Frame Title}
  \begin{itemize}
    \item<1-> Always visible from slide 1 onwards
    \item<2-> Appears from overlay 2 onwards
    \item<3-> Appears from overlay 3 onwards
  \end{itemize}
\end{frame}
```

**Use sparingly** — overlays inflate the PDF page count. Only use them for pedagogical reveals (building up a diagram or argument step by step). Never use them just for decoration.

---

## 11. SECTION NUMBERING IN TOC

```latex
% Automatically insert section divider slides
\AtBeginSection[]{
  \begin{frame}[plain]
    \centering
    \vfill
    {\Large\bfseries\color{accent} \insertsectionhead}
    \vfill
  \end{frame}
}
```

---

## 12. CODE LISTINGS IN BEAMER

Configure `listings` for slide use:

```latex
\lstset{
  backgroundcolor=\color{primary!8},
  basicstyle=\ttfamily\scriptsize,
  breaklines=true,
  frame=none,                 % no box frame — cleaner on slides
  tabsize=2,
  numbers=none,               % no line numbers on slides (too small)
  keywordstyle=\color{accent}\bfseries,
  commentstyle=\color{textlight}\itshape,
  stringstyle=\color{primary},
  showstringspaces=false,
}
```

---

## 13. COMMON BEAMER PITFALLS

| Problem | Fix |
|---|---|
| Text overflows frame bottom | Use `\scriptsize`, cut content, or split into two frames |
| `verbatim` / `lstlisting` error | Add `[fragile]` to the frame: `\begin{frame}[fragile]` |
| Navigation dots clutter slides | `\setbeamertemplate{navigation symbols}{}` |
| Table too wide for slide | Use `tabularx` with `X` columns; reduce to `\scriptsize` |
| Image overflows | Use `height=0.78\textheight, keepaspectratio` |
| Bullets too close to edge | `\setlength{\leftmargini}{1.2em}` |
| TOC shows too many levels | Use `\tableofcontents[hideallsubsections]` |
| Frame title too long | Keep frame titles ≤5 words; put detail in `\framesubtitle` |
| Overlays bloat PDF | Use only when pedagogically necessary |
| Dark theme, white text invisible on print | Add `\mode<handout>` overrides for print |

---

## 14. SLIDE-COUNT GUIDANCE

| Total slides | Structure |
|---|---|
| 5–8 | Title + TOC + 3–5 content + Closing |
| 10–15 | Title + TOC + 2 section dividers + 8–10 content + Closing |
| 20–30 | Title + TOC + 4 section dividers + 15–20 content + Closing |

Keep each content slide to **one main idea** with 3–5 bullet points maximum. If you have more, split the slide.

---

## 15. CONTENT TO INCLUDE IN THE PRESENTATION

[Describe your slides here. For each slide, specify: the title, what kind of slide (bullets / table / image / code / callout), and the content. Claude will turn this into properly structured Beamer frames.]

**Example:**
```
Slide 1: Title slide — "Insurance Claim Processing System", subtitle "Database Design Report", author "Your Name, Roll 123"

Slide 2: TOC

Slide 3 (section divider): "System Overview"

Slide 4 (bullets): "What is ICPS?" — 4 bullet points about health/vehicle/life insurance, claim processing, adjuster assignment, settlement

Slide 5 (table): "Entity Summary" — table with Entity | Type | Primary Key columns, 6 rows

Slide 6 (image): "ER Diagram" — insert er_diagram.pdf full width

Slide 7 (two-column): Left: "Normalisation Levels" (4 bullets 1NF–BCNF), Right: show the FD zip_code → state

Slide 8 (code): SQL query joining claim and settlement tables

Slide 9 (block): Definition of BCNF + alertblock for the exception

Slide 10: Closing / Thank You
```

---

## 16. OUTPUT REQUIREMENTS

- Output a single, complete `.tex` file compilable with `pdflatex` (run **twice** to resolve TOC and references).
- The aspect ratio must match what I specified (16:9 or 4:3).
- Do not use any built-in Beamer theme as-is — build the visual design from scratch using `\setbeamercolor` and `\setbeamerfont`.
- Do not use default nav icons — remove them with `\setbeamertemplate{navigation symbols}{}`.
- Annotate the top of the file with which image files need to be in the same directory.
- If content for a slide wasn't provided, write a placeholder comment `% TODO: slide N content` rather than inventing filler.

---

*End of master prompt — paste your slide content into Section 15 and send.*
