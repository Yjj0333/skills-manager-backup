# Chart families and plotting-library selection

Use this reference when multiple chart forms could support the same claim, when an advanced chart is proposed, or when choosing between static, interactive, network, spatial, and diagram tooling.

## Contents

- [Select by data and evidence](#select-by-data-and-evidence)
- [Chart-family map](#chart-family-map)
- [Library decision matrix](#library-decision-matrix)
- [Static versus interactive output](#static-versus-interactive-output)
- [Charts requiring special restraint](#charts-requiring-special-restraint)
- [Selection checklist](#selection-checklist)

## Select by data and evidence

Choose in this order:

1. define the conclusion the figure must support;
2. identify the data type, dimensionality, sampling structure, and uncertainty;
3. decide whether the viewer must compare magnitude, distribution, relation, topology, space, time, or optimization trade-offs;
4. select the lowest-complexity chart that preserves the required information;
5. select the library based on geometry, customization, scale, and final output;
6. verify that the chart remains interpretable at the paper's physical size.

Use bars for discrete magnitude comparison, lines for ordered or continuous progression, and pies only for a very small part-to-whole comparison where precise ranking is not the main task. Their ordinary nature is not a reason to reject them; weak evidence fit is.

## Chart-family map

### Relationships

- heatmap: many pairwise values on a common matrix;
- clustermap: matrix plus meaningful hierarchical ordering;
- pairplot: a small exploratory variable set;
- scatter + fitted line: individual relation and trend;
- hexbin: dense two-variable observations;
- 2D KDE contour: continuous joint-density structure.

### Distributions

- histogram + KDE: frequency and smooth density;
- ECDF: exact cumulative distribution and tails;
- violin: group density comparison with adequate sample size;
- raincloud: density, summary, and observations;
- swarm: small-to-medium sample observations without overlap;
- ridgeline: many ordered group distributions;
- jointplot: marginal plus joint distributions.

### Multidimensional data

- parallel coordinates: many dimensions across a manageable number of highlighted cases;
- radar: few normalized dimensions and few alternatives;
- bubble plot: two axes plus meaningful size and color variables;
- Sankey: conserved or interpretable flow between stages;
- 3D scatter/surface: genuine third spatial/state/objective dimension;
- small multiples: repeated comparable views with shared scales.

### Optimization

- Pareto front/surface: non-dominated trade-offs;
- convergence curve: objective, fitness, or gap over iteration/time;
- feasible region: low-dimensional constraint geometry;
- contour: objective or response surface;
- quiver/trajectory: direction field or search motion;
- sensitivity heatmap: recomputed response over two parameters.

### Model diagnostics

- residual plot and Q–Q plot;
- ROC and precision–recall curves;
- calibration curve;
- learning curve;
- confusion-matrix heatmap;
- SHAP summary/dependence;
- partial-dependence and ICE plots.

### Statistical inference

- confidence-interval dot/forest plot;
- bootstrap distribution;
- posterior/credible-interval display when the model is Bayesian;
- paired-difference plot when observations are matched.

### Dynamical systems

- state trajectory;
- phase portrait;
- streamplot/vector field;
- bifurcation diagram.

### Networks

- node–edge network;
- adjacency matrix;
- chord;
- dendrogram;
- Sankey.

### Spatial data

- choropleth;
- raster heatmap;
- density/hexbin map;
- contour map;
- flow map;
- geographic route map.

## Library decision matrix

| Library/stack | Prefer for | Avoid or supplement when |
|---|---|---|
| Seaborn + Matplotlib | EDA, distributions, correlations, regression diagnostics, statistical heatmaps, violin/KDE/pairplot/boxplot | geometry, graph algorithms, or GIS dominates |
| Matplotlib | convergence, mathematical functions, feasible regions, Pareto sets, paths, layouts, dynamics, high-customization static figures | interactive exploration is the primary deliverable |
| Plotly | Sankey, sunburst, treemap, hover-rich 3D, interactive exploration | final paper output is not tested as a high-quality static export |
| NetworkX | graph construction, shortest path, MST, flow, centrality for small/medium networks | very large graph performance or specialized community analytics are required |
| igraph | larger networks and efficient community/topology analysis | only a simple Python-native graph is needed |
| GeoPandas + Matplotlib | reproducible static GIS maps for papers | tile-based interaction or browser exploration is central |
| Folium | interactive geographic exploration and route inspection | a self-contained vector/static paper figure is required |
| Graphviz | model frameworks, decision trees, state transitions, algorithm flow | quantitative axes or continuous data geometry are needed |
| Plotnine | layered grammar-of-graphics statistical plots in Python | specialized network, GIS, or highly custom low-level geometry dominates |

Supporting analysis libraries such as statsmodels, scikit-learn, SciPy, SHAP, or SALib may compute diagnostics or sensitivity indices, but they are not substitutes for the plotting backend.

## Static versus interactive output

For a contest or manuscript, treat the static figure as authoritative:

- export PDF or SVG for vector geometry and text;
- export PNG at 300 DPI or higher for compatibility and preview;
- use TIFF only when the target rules require it;
- test Plotly static export, fonts, colors, and dimensions rather than relying on the browser view;
- avoid Folium screenshots as the only final map when a reproducible static map can be produced;
- retain plotting code and exact data lineage.

An interactive companion can aid exploration, but it does not replace a legible paper figure.

## Charts requiring special restraint

### Radar

Use only for a few alternatives and normalized indicators with a meaningful common direction. Do not compare areas as if they were linear quantities. Prefer heatmaps or parallel coordinates when dimensions or alternatives are numerous.

### Sankey

Use only for meaningful flow, allocation, transition, or hierarchical weight propagation. Check conservation semantics. Do not convert an arbitrary table into ribbons.

### 3D

Use only when depth encodes a genuine spatial, state, surface, or objective dimension. Avoid perspective distortion, occlusion, and static views that prevent comparison. Prefer contours, facets, or projections when they communicate more clearly.

### Streamgraph

Use only when components form a meaningful changing composition. It is poor for reading exact values and can distort baselines; lines or stacked areas are often clearer.

### Chord and dense networks

Use only when the number of groups and edges remains interpretable. Aggregate with a declared rule or choose an adjacency matrix when edge crossings dominate.

### Dual axes

Avoid unless the shared x-domain and scale choices are essential and non-misleading. Prefer aligned panels with a shared x-axis.

### Truncated axes

Use only when it improves resolution without distorting magnitude. Mark the scale and do not truncate bars in a way that exaggerates differences.

## Selection checklist

Before finalizing a chart/library pair, answer:

- What exact comparison or pattern must the reader perceive?
- Is the data continuous, categorical, ordered, temporal, spatial, networked, or multi-objective?
- Are observations paired, repeated, weighted, censored, or uncertain?
- Does the chart preserve units, sample size, uncertainty, and missingness?
- Will overplotting require hexbin, density, rasterization, aggregation, or small multiples?
- Does the library support the required geometry and reliable PDF/SVG/PNG export?
- Can the figure be read at final paper size without interaction?
- Would a simpler chart convey the same evidence more accurately?

If the last answer is yes, choose the simpler chart.
