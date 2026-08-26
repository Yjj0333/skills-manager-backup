# Evaluation and optimization model–figure map

Use this reference for comprehensive evaluation, multi-criteria decision, mathematical programming, intelligent optimization, and routing problems. Preserve the distinction between model structure, solver behavior, final decisions, feasibility, and robustness.

## Contents

- [AHP](#ahp)
- [Entropy weighting](#entropy-weighting)
- [TOPSIS and combined weighting](#topsis-and-combined-weighting)
- [Fuzzy comprehensive evaluation](#fuzzy-comprehensive-evaluation)
- [Grey relational analysis](#grey-relational-analysis)
- [Linear and integer programming](#linear-and-integer-programming)
- [Multi-objective optimization](#multi-objective-optimization)
- [Genetic algorithms](#genetic-algorithms)
- [Simulated annealing](#simulated-annealing)
- [Particle swarm optimization](#particle-swarm-optimization)
- [Ant colony optimization](#ant-colony-optimization)
- [TSP, VRP, and path planning](#tsp-vrp-and-path-planning)
- [Evidence requirements](#evidence-requirements)

## AHP

Match figures to the hierarchy and decision claim:

| Priority | Figure | Paper role |
|---|---|---|
| ★★★★★ | hierarchy structure diagram | show goal–criterion–subcriterion–alternative logic |
| ★★★★★ | ordered weight dot/bar plot | communicate relative criterion importance |
| ★★★★ | weight sensitivity plot | test whether plausible judgment changes alter decisions |
| ★★★ | radar chart | compare a small number of normalized weight profiles |
| ★★★ | Sankey diagram | show weight flow through a deep hierarchy when flow is clearer than a tree |

Do not turn the consistency ratio into a decorative chart. Report the consistency test in text or a compact table unless a multi-matrix comparison itself is a claim. Do not create sensitivity results without recomputing weights and rankings under stated perturbations.

## Entropy weighting

Useful figures:

- ★★★★ ordered entropy-weight plot for criterion contribution;
- ★★★★ information-entropy or divergence plot when explaining why weights differ;
- ★★★★ criterion-by-group heatmap when weights vary across regions, times, or scenarios;
- ★★★ normalized radar plot only for a small criterion set;
- ★★★ contribution decomposition when the method's derivation supplies a meaningful additive contribution.

State normalization and benefit/cost orientation. Do not imply that an entropy weight is expert importance; it represents information differentiation in the observed data.

## TOPSIS and combined weighting

Prioritize:

1. ★★★★★ final closeness-score ranking with labels and uncertainty/sensitivity if available;
2. ★★★★ distance to positive ideal vs distance to negative ideal, with selected alternatives highlighted;
3. ★★★★ criterion–alternative normalized-value heatmap;
4. ★★★ parallel coordinates for a manageable number of alternatives and criteria;
5. ★★★ radar chart for a small set of finalists;
6. ★★★★ rank-stability or weight-sensitivity view when robustness is claimed.

For entropy-weight TOPSIS, make the visual chain explicit:

> criterion weights → closeness scores → ranking stability

Keep benefit/cost transformations traceable. A ranking bar plot proves ordering, not robustness. Do not attach error bars unless uncertainty was actually estimated.

## Fuzzy comprehensive evaluation

Recommended figures:

- ★★★★★ membership heatmap: criteria or alternatives by evaluation grade;
- ★★★★ evaluation-grade distribution: stacked bars, dot distribution, or alluvial/Sankey when transitions or weight flow are meaningful;
- ★★★★ compact comprehensive-evaluation matrix heatmap;
- ★★★ radar comparison for few normalized dimensions;
- ★★★ Sankey for a genuine hierarchy-to-grade flow.

State the membership function, grade order, and normalization. Do not use a Sankey merely to make a static matrix look advanced.

## Grey relational analysis

Recommended figures:

- ★★★★★ ordered grey relational grade plot;
- ★★★★ relation-coefficient or relation-grade heatmap;
- ★★★ radar comparison for a small indicator set;
- ★★★ indicator association network when a threshold has a justified interpretation.

State reference sequence, distinguishing coefficient, normalization, and benefit/cost handling. Do not choose a network threshold only for visual neatness.

## Linear and integer programming

Separate geometric explanation, resource decision, schedule, and feasibility:

| Problem structure | Preferred figure | Evidence role |
|---|---|---|
| Two continuous decision variables | feasible region + constraint boundaries + optimal point | directly show feasibility and optimum |
| Resource allocation | grouped/stacked allocation plot or Sankey | show where resources go |
| Scheduling | Gantt chart | show timing, overlap, and precedence |
| Assignment | assignment matrix heatmap or bipartite graph | show selected matches |
| Facility/layout | geometry or layout view | show spatial decision and constraints |
| Capacity utilization | utilization profile with limits | show binding or slack resources |
| General high-dimensional model | compact solution-structure chart plus constraint diagnostics | explain decision without fake projection |

For a two-dimensional problem, prefer the feasible region and optimal point. For higher dimensions, do not create a misleading two-dimensional feasible polygon unless it is a clearly labeled slice or projection. Visualize constraint slacks or violations only from solved values.

## Multi-objective optimization

Principally consider a Pareto view:

- ★★★★★ Pareto front for two objectives;
- ★★★★★ Pareto surface or carefully designed projections for three objectives;
- ★★★★ parallel coordinates for many objectives;
- ★★★★ compromise solution highlighted with its selection rule;
- ★★★ bubble plot for a meaningful third/fourth variable;
- ★★★ radar comparison for a few selected solutions;
- ★★★★ objective/weight/parameter sensitivity when recomputed solutions exist.

Display dominated and non-dominated points distinctly when both are available. Show objective direction and units. Do not connect unordered Pareto points into a false trajectory. A single weighted-sum solution is not a Pareto front.

## Genetic algorithms

Recommended chain:

1. ★★★★★ best and mean fitness by generation;
2. ★★★★ population diversity or feasibility rate by generation;
3. ★★★★ final solution structure;
4. ★★★★ box/violin distribution across independent runs;
5. ★★★ parameter-sensitivity heatmap from an actual experimental grid.

Define whether larger or smaller fitness is better. Distinguish raw objective, penalized fitness, and feasibility; do not label one as another. A convergence curve from one seed supports solver behavior for that run, not stochastic robustness.

## Simulated annealing

Recommended figures:

- ★★★★★ objective vs iteration, separating current and best-so-far values when both exist;
- ★★★★ temperature vs iteration or a combined aligned panel;
- ★★★★ accepted/rejected move state, acceptance ratio, or uphill acceptance by temperature;
- ★★★★ final layout or path;
- ★★★★ box/violin distribution across independent runs;
- ★★★ parameter-sensitivity heatmap from actual schedules/runs.

Mark first feasible solution only if the solver recorded its exact event. Do not infer it from coarse history checkpoints. Distinguish constraint penalties from strict feasibility and avoid presenting best-found as proven global optimum.

## Particle swarm optimization

Recommended figures:

- ★★★★★ global-best objective convergence;
- ★★★★ particle trajectory or position evolution when the decision space is truly two-dimensional;
- ★★★★ contour + particle trajectory for a two-dimensional objective surface;
- ★★★★ final solution structure;
- ★★★★ repeated-run stability;
- ★★★ parameter sensitivity for inertia and acceleration settings.

For higher-dimensional search, prefer diversity, distance-to-best, or projected trajectories with a clear projection warning. Do not imply a 2D projection is the full optimization landscape.

## Ant colony optimization

Recommended figures:

- ★★★★★ best route or solution graph;
- ★★★★★ objective convergence;
- ★★★★ pheromone matrix heatmap when pheromone values are recorded and interpretable;
- ★★★ route evolution at a few justified checkpoints;
- ★★★★ repeated-run stability.

Do not animate or show every iteration in a static paper. Select checkpoints by algorithm events or a fixed documented rule.

## TSP, VRP, and path planning

Never rely only on a table of node order.

| Evidence need | Preferred figure | Encodings |
|---|---|---|
| Input geometry | node spatial distribution | coordinates, depot/customer type, demand if relevant |
| Final route | route map/graph | directed sequence, node labels, distance scale |
| Multiple vehicles | one consistent color per vehicle | depot, route, capacity or demand |
| Geographic context | static map route | projected coordinates, scale, north arrow when appropriate |
| Pairwise structure | distance/cost matrix heatmap | ordered nodes and units |
| Timing | Gantt or time-window chart | service/travel intervals and windows |
| Capacity | load along route | stop index/distance vs remaining or used load |
| Flow/allocation | Sankey | only for aggregated source–destination flow |
| Multiple objectives | Pareto front | distance, cost, vehicles, emissions, or other computed objectives |

Use equal aspect ratio for planar geometry when distances are Euclidean. For maps, use an appropriate coordinate reference system. Highlight violations only from actual checks, and distinguish route visualization from proof of feasibility.

## Evidence requirements

| Figure | Minimum required evidence |
|---|---|
| hierarchy/Sankey | complete hierarchy, local/global weights, and valid parent–child links |
| score/rank plot | alternative IDs, computed score, rank, and direction |
| sensitivity plot | parameter or weight grid plus recomputed scores/ranks/solutions |
| feasible region | explicit inequalities, bounds, objective, and solved optimum |
| Gantt chart | task/resource start and finish times |
| Pareto front | objective vectors and dominance status or enough data to compute it |
| convergence curve | iteration-level current/best/mean values with metric definition |
| diversity/acceptance plot | recorded population or acceptance diagnostics |
| repeated-run distribution | independent seed/run outcomes and feasibility status |
| route/layout | coordinates and the actual selected sequence/placement |
| load profile | route order, demand/capacity, and load update convention |
| pheromone heatmap | recorded pheromone matrix for a stated iteration |

If only final objective values exist, do not manufacture a convergence history. If only one optimization run exists, do not claim algorithmic stability.
