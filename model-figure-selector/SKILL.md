---
name: model-figure-selector
description: Select, prioritize, plan, audit, and when requested generate evidence-driven academic figures for CUMCM and general mathematical-modeling papers. Use when identifying models from a problem, report, data, formulas, or code; answering “这个模型应该画什么图”; designing a complete figure chain; choosing plotting libraries, visual styles, or color palettes; applying the bundled publication-figure template library (SHAP, raincloud, ROC, Taylor, chord, circular heatmap, and more) to real project data; planning figure placement, captions, labels, and analysis text; reviewing whether existing figures support conclusions; or preparing paper-ready plotting code and static exports for statistics, prediction, evaluation, optimization, networks, dynamics, simulation, machine learning, sensitivity, and robustness tasks.
---

# Model–Figure Selector

Act as the visualization decision layer for mathematical-modeling papers. Decide what the paper needs to prove, which figure supplies that evidence, which data and library it requires, and where it belongs. Do not reduce this task to chart styling.

## Preserve the responsibility boundary

- Use this skill to decide **what to draw, why it is needed, how figures form an evidence chain, and how they enter the paper**.
- Use plotting libraries such as Matplotlib, Seaborn, Plotly, NetworkX, igraph, GeoPandas, Folium, Graphviz, or Plotnine to produce the graphic.
- When the installed academic-figure skill is available, use its actual name, `$nature-figure`, for publication styling, backend-specific rendering, export, and rendered QA. Treat “nature-figures” as an informal alias, not as a plotting library.
- Do not invoke `$nature-figure` for interactive-only Plotly/Folium exploration if its own routing excludes that task.
- When a bundled template matches the chosen chart and the available data, prefer adapting it over hand-writing style code: keep the template visual genes and export contract, replace only its synthetic-data function with real project data (see references/visual-templates.md). Apply this skill's minimum static-output standards instead.

## Enforce non-negotiable rules

1. Preserve original data, model definitions, constraints, outputs, and conclusions.
2. Never remove inconvenient observations, manufacture a trend, invent a run, fabricate a sensitivity study, or infer unavailable diagnostics merely to obtain a figure.
3. Use actual source artifacts when drawing. Do not generate mock values unless the user explicitly requests a clearly labeled demonstration.
4. If required evidence is absent, say `当前数据不足以生成该图`, list the exact missing fields or runs, and continue planning only the figures supported by available data.
5. Prefer two to four high-value figures per problem over a gallery of redundant charts.
6. Retain a figure only when removing it would weaken at least one stated conclusion, validation claim, or robustness claim.
7. Favor information density, explanatory power, and model fit over novelty or visual complexity.

## Route references

Read only the references needed for the recognized model family or requested operation:

| Situation | Required reference |
|---|---|
| EDA, correlation, regression, time series, prediction, clustering, classification, PCA, machine learning, deep learning | [references/statistical-predictive-models.md](references/statistical-predictive-models.md) |
| AHP, entropy weighting, TOPSIS, fuzzy evaluation, grey relation, linear/integer programming, multi-objective or intelligent optimization, TSP/VRP | [references/evaluation-optimization-models.md](references/evaluation-optimization-models.md) |
| Graph/network, queueing, Monte Carlo, probability, differential equations, dynamics, simulation, spatial analysis, sensitivity or robustness | [references/network-dynamics-simulation-spatial.md](references/network-dynamics-simulation-spatial.md) |
| Library choice is ambiguous, interactive and static outputs differ, or an advanced chart family is proposed | [references/chart-families-and-libraries.md](references/chart-families-and-libraries.md) |
| A matched visual template, color palette, or figure styling baseline is needed | [references/visual-templates.md](references/visual-templates.md) |
| Full-paper planning, direct drawing, LaTeX integration, visual-system design, caption writing, or QA | [references/paper-integration-and-qa.md](references/paper-integration-and-qa.md) |

For a mixed problem, read every applicable model-family reference and analyze each model separately before combining the figure chain.

## Follow the mandatory workflow

### 1. Inspect the task and authoritative artifacts

Read the supplied problem statement, analysis/modeling report, result report, data dictionary, tables, code, and generated outputs that determine the model and numerical claims. Prefer authoritative machine-readable results over prose copies when they disagree. Record:

- subproblem and modeling stage;
- model or algorithm name;
- inputs, outputs, decision variables, constraints, and uncertainty;
- available raw, intermediate, result, validation, and repeated-run data;
- claims already made or intended in the paper;
- target section, output format, language, and plotting environment.

Do not assume a model solely from a filename or one keyword. Infer it from formulas, objectives, constraints, fitted estimators, algorithm steps, or actual outputs, and mark uncertain identifications as provisional.

### 2. Classify every modeling component

Classify the work into one or more of:

- data preprocessing, descriptive statistics, correlation, regression, classification, clustering;
- time series, forecasting, probability/statistics, comprehensive evaluation, multi-criteria decision;
- operations research, intelligent optimization, multi-objective optimization, path planning;
- graph theory, network analysis, spatial analysis;
- differential equations, dynamical systems, simulation;
- machine learning, deep learning;
- sensitivity analysis, robustness analysis, or another explicitly named modeling task.

For compound workflows, preserve the order. Example: entropy weighting → TOPSIS → ranking sensitivity is three linked components, not one “evaluation model.”

### 3. Define why each figure exists

Assign each candidate exactly one primary paper task and optionally one secondary task:

| Task | Question the figure must answer |
|---|---|
| A. Data understanding | What are the distributions, outliers, relationships, density patterns, or natural groups? |
| B. Model construction | What variables, mechanisms, hierarchy, states, objectives, and constraints form the model? |
| C. Algorithm solving | Does the search converge, remain diverse, stabilize, or outperform a comparator? |
| D. Result presentation | What is the predicted, ranked, optimized, routed, allocated, or simulated outcome? |
| E. Model validation | Is fit, error, calibration, classification, constraint satisfaction, or generalization acceptable? |
| F. Sensitivity/robustness | Do conclusions persist under parameter, weight, data, seed, or scenario changes? |

Write a one-sentence evidence claim before choosing a chart. Reject candidates whose claim is merely “show the data” or “make the paper richer.”

### 4. Build a candidate figure chain

Consider these layers in paper order:

1. data features;
2. model structure;
3. solution process;
4. core result;
5. validation;
6. sensitivity or robustness.

Do not require all six layers. Select the smallest set that closes the paper's evidence chain. Merge panels when they support one Results-level claim; split figures when claims are independent.

### 5. Check evidence availability before ranking

For every candidate, identify:

- exact source file, table, array, log, or model output;
- required columns, dimensions, units, groups, time index, seeds, or scenarios;
- transformations used only for display, with formulas and provenance;
- whether the data support uncertainty, comparison, diagnostic, or sensitivity claims.

Reject or defer unsupported figures. In particular:

- require observed values and predictions for residual or actual-vs-predicted plots;
- require labels and continuous scores/probabilities for ROC, PR, and calibration curves;
- require iteration-level history for convergence plots;
- require repeated independent runs for stochastic-stability distributions;
- require varied parameters, weights, or perturbations for sensitivity plots;
- require feasible solutions/objective vectors for Pareto plots;
- require coordinates/edges or a spatial layer for network and map figures.

### 6. Score, prune, and prioritize

Score each supported candidate:

- claim support: 0–3;
- unique information beyond tables/other figures: 0–2;
- data readiness and traceability: 0–2;
- validation or decision value: 0–2;
- readability at paper size: 0–1;
- redundancy or interpretation risk: subtract 0–2.

Immediately reject any candidate that requires invented evidence or misleading transformations.

Map the final score to:

- 8–10: ★★★★★ strong recommendation;
- 6–7: ★★★★ recommendation;
- 4–5: ★★★ optional;
- 0–3: do not recommend.

Treat these bands as decision aids, not arithmetic substitutes for judgment. Keep a lower-scoring figure if it is the only evidence for a critical claim, and explain why.

### 7. Match chart and library

Use the relevant model-family reference, then select the simplest chart that expresses the evidence correctly. Apply these defaults:

- Seaborn + Matplotlib for statistical distributions, relationships, regression diagnostics, and heatmaps;
- Matplotlib for convergence, functions, feasible regions, Pareto sets, geometry, routes, and dynamical systems;
- Plotly for interactive Sankey, sunburst, treemap, and complex 3D exploration, with a verified static export for the paper;
- NetworkX or igraph for graph structures and network metrics;
- GeoPandas or Folium for GIS and route context; prefer GeoPandas/Matplotlib for final static paper maps;
- Graphviz for model frameworks, algorithms, decision structures, and state transitions;
- Plotnine when a ggplot-style layered statistical grammar materially improves the implementation.

Never prescribe one library for every figure. Do not use 3D when depth adds no encoded variable or spatial meaning.

### 7b. Prefer the bundled visual template when one matches

Read `references/visual-templates.md` and check the 11 bundled scripts under `assets/scibox-templates/`. If a template matches both the chosen chart and the available evidence:

1. copy the template script into the project plotting directory; keep `configure_matplotlib()`, the layout code, and the PNG/PDF/SVG export untouched;
2. replace only its synthetic-data function (`synthetic_*` / `simulate_*`) with loaders for the real verified data; update labels, group names, significance marks, and annotation numbers to the terms of the paper;
3. never let the template simulated values reach the paper: if required fields are missing, declare a data gap (rule 4) instead of forcing the template;
4. when no template fits, start new matplotlib code from the style contract in `references/visual-templates.md` (palette table plus a copied `configure_matplotlib()` base) so all paper figures stay visually consistent, and hand journal-grade polish and rendered QA to `$nature-figure` as before.

### 8. Plan paper integration

For every retained figure, specify:

- figure name and priority;
- primary paper task and claim supported;
- chart type and panel structure;
- x-axis, y-axis, color, size, facets, annotations, and units;
- data source and required fields;
- plotting library and static export path;
- paper section and exact placement relative to the model/result paragraph;
- concise caption and stable label;
- two to four sentences the body should discuss: what is shown, what pattern appears, why it appears, and what it proves.

When planning a full paper, define a global visual identity before drawing: semantic colors, fonts, sizes, line widths, markers, grids, aspect ratios, annotation style, and export formats. Keep the same object or algorithm visually identical across figures.

### 9. Execute only when requested

If the user asks only what to draw, return the plan without creating files.

If the user asks for code, provide or create code that consumes the real data and exposes input/output paths and required columns. Do not silently hardcode result values.

If the user asks to draw:

1. complete Steps 1–8 first;
2. confirm that required data exist without blocking on preferences that can be inferred safely;
3. select the plotting stack and the matching bundled visual template when one exists (step 7b);
4. invoke and follow `$nature-figure` when it applies, including its backend rule, export contract, and rendered QA;
5. render paper-ready PDF or SVG plus PNG at 300 DPI or higher;
6. inspect the final-size output for clipping, overlaps, illegible text, misleading scales, bad legends, missing units, and Chinese font failures;
7. verify plotted values against the authoritative source;
8. report what was generated and which requested figures remain unsupported.

## Use the required response contracts

### “这个模型应该画什么图？”

Use these sections:

1. `模型识别`: identify each model and confidence/evidence.
2. `图表任务`: state the claims that need visual evidence.
3. `推荐图表`: order by ★★★★★, ★★★★, then ★★★. For each figure include name, purpose, axes/encodings, data source, library, bundled template id (when one applies, per references/visual-templates.md), rationale, and paper placement.
4. `不推荐`: name low-value or misleading charts and explain why.
5. `数据缺口`: include only when a recommended diagnostic or robustness claim lacks evidence.

### “给这个问题设计完整图表”

Organize the smallest coherent chain as:

- 图1: data layer;
- 图2: model or algorithm layer;
- 图3: core result;
- 图4: validation, sensitivity, or robustness.

Use fewer or more only when the evidence chain requires it. Explain the logical transition between figures.

### “直接帮我画”

Return the selected figure contract before or alongside implementation, then deliver code, static outputs, data lineage, paper placement, caption/label, and QA status. Separate completed local rendering from any unperformed journal, device, cloud, or external acceptance check.

## Final decision test

Before retaining a figure, ask:

> If this figure were removed, which conclusion would lose evidence?

If no conclusion, model assumption, validation result, or robustness claim loses evidence, drop the figure.
