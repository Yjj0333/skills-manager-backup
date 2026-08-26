# Network, dynamics, simulation, spatial, and robustness figure map

Use this reference for graph/network models, queueing, probability and Monte Carlo models, differential equations, dynamical systems, discrete-event or agent simulation, spatial models, and cross-model sensitivity or robustness analysis.

## Contents

- [Graph theory and network analysis](#graph-theory-and-network-analysis)
- [Queueing models](#queueing-models)
- [Probability and Monte Carlo](#probability-and-monte-carlo)
- [Differential equations and dynamical systems](#differential-equations-and-dynamical-systems)
- [Simulation](#simulation)
- [Spatial analysis](#spatial-analysis)
- [Sensitivity analysis](#sensitivity-analysis)
- [Robustness and stability](#robustness-and-stability)
- [Evidence requirements](#evidence-requirements)

## Graph theory and network analysis

Applies to shortest path, maximum flow, minimum spanning tree, complex networks, and centrality analysis.

| Model claim | Preferred figure | Notes |
|---|---|---|
| Network structure | node–edge network | encode only meaningful node/edge attributes |
| Shortest path | network with selected path highlighted | show source, target, direction, and total cost |
| Maximum flow | directed network with flow/capacity labels | distinguish used flow from capacity |
| Minimum spanning tree | full graph in light context plus MST highlight | report total tree weight |
| Centrality | network with size/color encoding plus ordered centrality plot | avoid unreadable hairballs |
| Degree pattern | degree distribution or CCDF | log scales only when justified and labeled |
| Matrix structure | adjacency/weight heatmap | reorder only with a documented rule |
| Group relation | chord or Sankey | use only for aggregated flows that remain legible |

Use NetworkX for standard Python graph algorithms and moderate graphs; consider igraph for larger graphs or community analysis. A force-directed layout is not geographic or metric evidence. For dense graphs, prefer matrix, community summaries, edge bundling, or sampled/aggregated views with an explicit rule.

## Queueing models

Recommended chain:

1. ★★★★★ queue length or system occupancy over time;
2. ★★★★ waiting-time distribution using ECDF, violin, or histogram + KDE;
3. ★★★★ server utilization with capacity/reference lines;
4. ★★★★ empirical vs theoretical state probabilities when validating a queueing formula;
5. ★★★★ performance sensitivity to arrival/service parameters;
6. ★★★ Monte Carlo distribution of wait, loss, or throughput.

Show transient and steady-state regions when the distinction matters. Report warm-up removal only if it was part of the actual analysis and document before/after counts. Do not hide unstable growth by truncating the time axis.

## Probability and Monte Carlo

Recommended figures:

- ★★★★★ output distribution using histogram + KDE, ECDF, or both;
- ★★★★★ estimate or error convergence against simulation count;
- ★★★★ confidence interval or bootstrap distribution;
- ★★★★ probability evolution for sequential simulation;
- ★★★★ two-dimensional simulation cloud or density view;
- ★★★★ sensitivity tornado or rank-correlation plot;
- ★★★ rare-event tail or exceedance plot when tail probability is the claim.

Use a simulation cloud only when individual draws or joint structure matter. For dense samples, prefer hexbin or contours. Show Monte Carlo uncertainty, seed strategy, and number of replications. A smooth KDE must not conceal discrete or bounded support.

For statistical inference, use confidence-interval dot/forest plots, bootstrap distributions, or posterior distributions when they match the actual method. Never add an interval that was not computed.

## Differential equations and dynamical systems

Applies to SIR/SEIR, population/ecology systems, physical processes, and other ODE/PDE state models.

| Evidence task | Preferred figure | Required interpretation |
|---|---|---|
| State evolution | state variables vs time | initial conditions, units, conservation if applicable |
| State interaction | phase portrait | direction, equilibria, trajectories |
| Local dynamics | vector field or streamplot | domain and parameter values |
| Regime change | bifurcation diagram | varied parameter and stability convention |
| Parameter effect | sensitivity trajectories/heatmap | actual re-solves over parameter values |
| Multi-state evolution | 3D state space | use only when the third state is essential |
| Spatial field | contour/heatmap/quiver | coordinates, time slice, units |

For epidemic models, mark observed data separately from simulated states and state whether parameters were fitted or assumed. Do not claim stability from a visually flat trajectory alone; use the mathematical or numerical criterion actually evaluated.

## Simulation

For discrete-event, system-dynamics, agent-based, and scenario simulation, match the plot to the verification question:

- state trajectories for system evolution;
- event timelines or occupancy plots for discrete-event behavior;
- spatial snapshots at a few predeclared times for agent movement;
- distribution/ECDF across replications for stochastic outcomes;
- scenario small multiples for policy comparison;
- conservation, balance, or invariant diagnostics for model verification;
- convergence with step size or simulation horizon for numerical verification;
- calibration plots against observed data when a calibration set exists.

Do not select visually attractive simulation snapshots without a rule. A single realization does not establish expected behavior or robustness.

## Spatial analysis

Use:

- choropleth for normalized area-level rates or scores;
- point/hexbin/density maps for events;
- raster heatmap for gridded fields;
- contour map for continuous surfaces;
- flow map for origin–destination movement;
- route map for spatial optimization;
- small-multiple maps for time or scenario comparison.

Choose an appropriate coordinate reference system. Do not map raw counts as if they were rates when population/exposure differs. Report spatial joins, aggregation resolution, classification bins, and missing regions. Use Folium for interactive exploration and GeoPandas + Matplotlib for reproducible static paper output. Avoid geographic area distortion when encoded area is irrelevant to the claim.

## Sensitivity analysis

Sensitivity figures require actual recomputation under changed inputs. Choose by design:

| Design | Preferred figure | Purpose |
|---|---|---|
| one parameter at a time | response curve with baseline | local/global effect over a range |
| two parameters | response heatmap or contour | interaction and feasible/decision regions |
| many independent inputs | tornado plot | ordered marginal influence |
| variance-based analysis | Sobol index bar/dot plot with intervals | first-order and total effects |
| model-explanation sensitivity | dependence plot | conditional response, not automatic causality |
| weights and rankings | rank trajectory, rank-correlation heatmap, or stability region | decision robustness |
| optimizer hyperparameters | performance heatmap plus feasibility | tuning effect |

State baseline, perturbation range, sampling scheme, response metric, and whether other parameters were held fixed or jointly sampled. Do not create a tornado chart from subjective guesses.

## Robustness and stability

Match the threat to the evidence:

- random initialization or stochastic algorithm: box/violin/ECDF across seeds;
- train/test sampling: cross-validation or repeated-split distributions;
- measurement noise: outcome vs perturbation magnitude and failure rate;
- scenario uncertainty: aligned small multiples or interval/ribbon comparison;
- ranking stability: rank trajectories, Kendall/Spearman stability, or top-k retention;
- optimization feasibility: feasibility rate and violation magnitude across runs;
- structural assumptions: scenario comparison using recomputed model outputs.

Show all valid runs and report failed or infeasible runs rather than silently dropping them. Separate robustness of the conclusion from repeatability of the algorithm. A narrow objective distribution does not prove decision stability if selected solutions differ materially.

## Evidence requirements

| Figure | Minimum required evidence |
|---|---|
| network/path/MST/flow | node and edge data, weights/capacities, and selected result |
| centrality/degree plot | computed node metrics or graph sufficient to compute them |
| queue trajectory | time-stamped arrivals/services or simulated state history |
| waiting-time ECDF | sample-level waiting times |
| simulation distribution | independent replications and seed/scenario metadata |
| convergence by simulation count | sequential estimates or saved checkpoints |
| phase portrait | solved state trajectories for the stated initial conditions |
| vector field/streamplot | explicit derivative function and parameter values |
| bifurcation diagram | equilibria/long-run states across a parameter grid |
| choropleth | spatial boundaries, join key, normalized metric, and CRS |
| flow map | origin/destination coordinates and flow magnitude |
| sensitivity heatmap/tornado | defined perturbation design and recomputed responses |
| robustness violin/boxplot | repeated runs with outcomes, feasibility, and run identifiers |

When the experiment was not run, describe the required experiment and leave the figure ungenerated.
