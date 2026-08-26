# Paper integration, visual system, and QA

Use this reference for full-paper figure planning, direct drawing, LaTeX placement, captions, figure analysis, style unification, or final quality checks.

## Contents

- [Build the manuscript evidence sequence](#build-the-manuscript-evidence-sequence)
- [Define a global visual system](#define-a-global-visual-system)
- [Integrate nature-figure correctly](#integrate-nature-figure-correctly)
- [Plan each figure](#plan-each-figure)
- [Write captions, labels, and body analysis](#write-captions-labels-and-body-analysis)
- [Meet output quality standards](#meet-output-quality-standards)
- [Protect data integrity](#protect-data-integrity)
- [Direct-drawing workflow](#direct-drawing-workflow)
- [Delivery templates](#delivery-templates)

## Build the manuscript evidence sequence

Plan figures by subproblem and claim, not by input table. For each subproblem, consider:

1. data characteristics needed to justify preprocessing or assumptions;
2. model structure needed to make variables/mechanisms understandable;
3. solver behavior needed to establish a credible solution process;
4. core outcome needed to answer the question;
5. validation needed to support fit, feasibility, or predictive performance;
6. sensitivity or robustness needed to bound the conclusion.

Use only the layers that carry unique evidence. Usually two to four figures per subproblem are enough. A multi-panel figure should answer one Results-level question; assign panels complementary roles instead of repeating the same ranking or metric.

Arrange the manuscript sequence so that claims escalate:

> data basis → model/algorithm credibility → substantive result → validation/robustness

Move exploratory or redundant figures to an appendix only when they remain useful for reproducibility. Drop figures that do not support a claim even if they are attractive.

## Define a global visual system

Create one paper-wide registry before drawing:

| Element | Required decision |
|---|---|
| semantic colors | stable color for each algorithm, scenario, group, vehicle, or state |
| palette | restrained, colorblind-aware neutrals plus a limited signal/accent family |
| font | Chinese-capable body and math-compatible font; verify glyph rendering |
| title size | consistent hierarchy; omit axes titles when the caption/section already supplies the figure title |
| labels/ticks | legible at final physical size |
| lines/markers | stable width, dash, marker shape, and salience by object role |
| legend | consistent order and wording; prefer direct labels when clearer |
| grid/spines | light and purposeful; remove non-informative borders |
| dimensions | repeatable single-column, double-column, or page-width sizes |
| annotations | one style for optima, thresholds, events, confidence, and panel letters |
| export | PDF/SVG plus PNG at 300 DPI or higher |

Never let Algorithm A, a disease state, a scenario, or a vehicle change identity across figures. Do not blindly apply title case to model names such as XGBoost, LightGBM, LSTM, or DBSCAN.

For Chinese text:

- discover an installed CJK font instead of assuming one exists;
- set the font explicitly in the plotting source;
- preserve minus signs and mathematical symbols;
- inspect the exported PDF/PNG for missing-glyph boxes;
- embed or outline fonts only when the target workflow and license permit it.

## Integrate nature-figure correctly

Treat `$nature-figure` as a publication-figure skill, not as a plotting package.

For planning only:

- this skill owns model recognition, evidence roles, chart selection, data requirements, library recommendation, and paper placement;
- consult `$nature-figure` when detailed publication aesthetics, multi-panel architecture, export, or review risk matters.

For actual static scientific plotting:

1. finish the model-to-figure decision first;
2. invoke `$nature-figure` if it is installed and the route applies;
3. follow its current router, backend preference, exclusive-backend rule, export contract, and rendered QA;
4. use the selected plotting library within that backend to draw;
5. do not copy or freeze private internal paths from another skill into generated code or user-facing text.

When the requested output is interactive-only Plotly or Folium and `$nature-figure` excludes that route, do not force it. Apply the static fallback standards in this reference if a paper export is also required.

If `$nature-figure` is unavailable, continue with this reference's minimum standards and state that specialized publication-style QA was not run.

## Plan each figure

Use this figure contract:

| Field | Content |
|---|---|
| ID and title | stable figure number/name |
| priority | ★★★★★, ★★★★, or ★★★ |
| primary task | A data, B construction, C solution, D result, E validation, or F robustness |
| claim | one sentence the figure must support |
| chart/panels | chart type and complementary panel roles |
| encodings | x, y, color, size, facets, annotations, units, scale |
| source | exact authoritative artifact and required fields |
| transformation | display-only calculation with formula and provenance |
| library | plotting and supporting analysis libraries |
| placement | section and paragraph after which the figure appears |
| caption/label | concise title and stable cross-reference |
| body analysis | what, pattern, reason, implication |
| risk/QA | uncertainty, overplotting, feasibility, missing data, or interpretation risks |

Do not use a generic placement such as “results section” when a precise placement is possible. Prefer “after the paragraph that defines the Pareto compromise rule and before the selected-solution table.”

## Write captions, labels, and body analysis

For Chinese CUMCM papers, prefer a concise caption of no more than about 20 Chinese characters when clarity permits. Use the caption as the figure name, not as a paragraph of analysis.

Example:

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.82\linewidth]{figures/pareto_front.pdf}
  \caption{多目标优化的 Pareto 前沿}
  \label{fig:pareto-front}
\end{figure}
```

Reference it with `图~\ref{fig:pareto-front}` or the template's required style.

Use stable semantic labels such as:

- `fig:data-distribution`
- `fig:forecast-validation`
- `fig:ga-convergence`
- `fig:route-solution`
- `fig:ranking-sensitivity`

Write the surrounding body analysis to answer:

1. what the figure displays;
2. what pattern, contrast, optimum, error, or transition appears;
3. why it appears under the model or data mechanism;
4. what it proves, limits, or changes in the model conclusion.

Do not repeat every axis value. Do not claim causality, optimality, stability, or significance beyond the evidence.

## Meet output quality standards

Every final paper figure must satisfy:

- raster output at 300 DPI or higher;
- PDF or SVG for vector-compatible content;
- clear labels, complete axis names, and explicit units;
- accurate legends and consistent semantic colors;
- Chinese text without mojibake or missing glyphs;
- readable type at final physical size;
- no clipped or overlapping labels, legends, annotations, or panel letters;
- no unnecessary frame, grid, or whitespace;
- no high-saturation fluorescent palette;
- no meaningless 3D or perspective distortion;
- no deceptive axis, area, binning, smoothing, normalization, or color scale;
- no hidden observations or modified result values;
- uncertainty definition, sample size, and normalization disclosed when relevant.

Inspect both every panel and the whole figure. Automated source checks do not prove perceptual hierarchy, label clearance, or truthful interpretation.

## Protect data integrity

Keep source data immutable. Write derived plotting tables to a separate output only when useful, and record:

- source path and hash or version when practical;
- selected columns and row counts;
- filtering rule and scientific reason;
- normalization, aggregation, interpolation, or projection formula;
- before/after counts for any exclusion;
- units and category ordering;
- random seeds and run identifiers;
- exact model output from which annotations were taken.

Do not:

- delete outliers because they spoil the appearance;
- smooth away adverse behavior;
- choose a convenient time window without disclosure;
- turn penalties into feasibility or best-found into global optimum;
- add confidence bands, error bars, p-values, or sensitivity outcomes that were not computed;
- alter model parameters or solve a different model unless the user explicitly requests new analysis.

When data are insufficient, list the missing artifacts. Examples:

- convergence curve needs iteration-level objective history;
- stochastic stability needs multiple independent runs;
- rank robustness needs recomputed ranks under weight changes;
- calibration needs labels and predicted probabilities;
- a path map needs coordinates and selected route order.

## Direct-drawing workflow

1. inventory input files and identify the numerical source of truth;
2. validate schema, units, missingness, and row counts;
3. freeze the figure contract and global visual registry;
4. create plotting code that reads source files rather than embedding result arrays;
5. render PDF/SVG and PNG from the same code and data;
6. check plotted values against source tables or serialized results;
7. inspect final-size exports for fonts, collisions, scale, salience, and color;
8. rerun after every material change to data geometry, text, legends, axes, or layout;
9. retain source code and record the environment/packages needed to reproduce the figures;
10. report unsupported requested figures separately from completed outputs.

If `$nature-figure` is active, also complete every validation step it currently requires. Report a failed or unavailable QA check accurately; do not turn “source code ran” into “publication-ready.”

## Delivery templates

### Recommendation record

```markdown
### 图1：<图名> — ★★★★★
- 论文任务：<A–F 与具体任务>
- 证明内容：<一句话 claim>
- 图形与编码：<chart; x/y/color/facet/units>
- 数据来源：<artifact and fields>
- 绘图库：<library and rationale>
- 插入位置：<section and paragraph relation>
- Caption / Label：<caption>; <label>
- 正文分析：<what → pattern → reason → implication>
```

### Unsupported-figure record

```markdown
### 暂不能生成：<图名>
当前数据不足以生成该图。
- 缺少：<exact fields, logs, runs, or coordinates>
- 可支持的替代图：<only if backed by current evidence>
- 禁止替代：<fabricated or misleading workaround>
```

### Whole-problem chain

```markdown
图1 数据依据 → 图2 模型/算法可信度 → 图3 核心答案 → 图4 验证或稳健性
```

Explain which claim each arrow enables. Shorten the chain whenever one figure duplicates another.
