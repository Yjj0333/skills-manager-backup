# Statistical and predictive model–figure map

Use this reference after identifying the actual estimator, data structure, target variable, and paper claim. Select figures by evidence role; do not emit every chart listed here.

## Contents

- [Data preprocessing and EDA](#data-preprocessing-and-eda)
- [Correlation analysis](#correlation-analysis)
- [Regression](#regression)
- [Time series and forecasting](#time-series-and-forecasting)
- [Clustering](#clustering)
- [Classification](#classification)
- [PCA and dimensionality reduction](#pca-and-dimensionality-reduction)
- [Machine learning and deep learning](#machine-learning-and-deep-learning)
- [Evidence requirements](#evidence-requirements)

## Data preprocessing and EDA

Use EDA figures to establish data quality, distribution, scale, dependence, or grouping that affects later modeling.

| Evidence need | Preferred figures | Typical library | Notes |
|---|---|---|---|
| Missingness or cleaning impact | missingness matrix, before/after count flow, compact quality heatmap | Matplotlib, Seaborn | Report rules and counts; do not imply imputation quality without validation. |
| One-variable distribution | histogram + KDE, ECDF, boxplot, violin, raincloud | Seaborn + Matplotlib | Use ECDF for skewed/heavy-tailed data; use violin only with enough observations. |
| Distribution plus observations | raincloud, violin + swarm, box + swarm | Seaborn, PtitPrince or custom Matplotlib | Avoid overplotting; sample only for display with an explicit rule while retaining full analysis. |
| Two-variable relationship | scatter + fitted trend, jointplot, hexbin, 2D KDE contours | Seaborn + Matplotlib | Prefer hexbin/KDE for large dense samples. |
| Many-variable relationship | pairplot, correlation heatmap, clustermap | Seaborn | Pairplot only for a manageable number of variables. |
| Group comparison | violin/box/raincloud with direct group labels | Seaborn + Matplotlib | Show uncertainty or raw points when sample size permits. |

Do not turn every variable into a bar chart. Reserve bars for discrete categories or estimates whose baseline and uncertainty are meaningful. Avoid pie charts when precise comparison matters or categories are numerous.

## Correlation analysis

Choose the correlation definition before plotting:

- use Pearson for linear association under suitable scale/assumption conditions;
- use Spearman or Kendall for monotonic/rank relationships or strong non-normality;
- distinguish correlation from causation in the caption and analysis.

Recommended evidence chain:

1. ★★★★★ correlation heatmap or clustermap for many variables;
2. ★★★★ scatter + regression/smoother for a small number of claimed relationships;
3. ★★★★ hexbin or 2D KDE contours for large, dense samples;
4. ★★★ pairplot for a small exploratory variable set.

Annotate coefficients only when legible. Add significance or uncertainty only if it was actually computed with an appropriate method. Do not fill a heatmap with meaningless decimals or hide missing-pair sample sizes when they vary materially.

## Regression

Applies to linear, multiple, ridge, LASSO, generalized, and nonlinear regression. A single fitted line is rarely sufficient.

| Paper task | Preferred figure | Encodings | Evidence supplied |
|---|---|---|---|
| Fit/result | observed vs predicted | x = observed, y = predicted, identity line, optional uncertainty | calibration of magnitude and visible bias |
| Functional relationship | fitted curve with confidence/prediction band | x = predictor, y = response | estimated relation and uncertainty |
| Residual validation | residuals vs fitted | x = fitted, y = residual, zero line | heteroscedasticity, nonlinearity, outliers |
| Distributional validation | Q–Q plot and/or residual distribution | theoretical vs sample quantiles | deviation from assumed residual distribution |
| Coefficient interpretation | coefficient forest plot | estimate with interval | direction, magnitude, uncertainty |
| Regularization path | coefficient path | x = penalty, y = coefficient | feature shrinkage and selection behavior |
| Nonlinear interpretation | PDP/ICE or response surface | feature value(s) vs partial prediction | model response while holding other effects controlled |
| Feature contribution | importance or SHAP | feature vs contribution | predictive contribution, not automatic causality |

Use train/test or cross-validated predictions for generalization claims. Do not plot in-sample fit and describe it as out-of-sample performance. For multiple outputs or groups, keep scales comparable or state why they differ.

## Time series and forecasting

Applies to ARIMA/SARIMA, Holt–Winters, exponential smoothing, grey prediction, Prophet, LSTM, and other forecasting models.

For a forecasting paper, prioritize this minimum chain:

1. ★★★★★ original time series with events, units, and train/test boundary;
2. ★★★★ actual vs forecast with forecast interval where the model supports one;
3. ★★★★ error or residual validation, such as rolling error, residual distribution, or residual ACF.

Additional candidates:

| Need | Figure | Conditions |
|---|---|---|
| Explain structure | trend–seasonal–residual decomposition | decomposition is valid for the frequency and method |
| Identify lag structure | ACF and PACF | use before/after differencing as relevant; show confidence bounds |
| Show periodic concentration | calendar heatmap | dates and calendar cycles are meaningful |
| Compare changing components | streamgraph | components sum to a meaningful total; otherwise prefer lines or stacked areas |
| Compare models | aligned error distribution or forecast panels | same horizon, split, and metric definition |
| Diagnose drift | rolling error or rolling calibration | enough evaluation points exist |

Mark forecasts and observations unambiguously. Never draw a confidence band by applying an arbitrary percentage around the point forecast. Grey-model posterior checks or relative error plots require the actual computed diagnostics.

## Clustering

Applies to K-means, hierarchical clustering, DBSCAN, and Gaussian mixture models.

Recommended chain:

1. ★★★★★ cluster-quality evidence: silhouette plot, stability analysis, or method-appropriate validity metric;
2. ★★★★ structure/result evidence: PCA, t-SNE, or UMAP projection colored by cluster;
3. ★★★★ cluster interpretation: per-cluster violin plots, clustermap, centroid parallel coordinates, or a carefully limited radar chart;
4. ★★★ dendrogram for hierarchical clustering.

Projection is a view, not proof of separation. State the projection method, parameters, and explained variance when applicable. Do not use t-SNE/UMAP geometry to claim original-space distances. For DBSCAN, distinguish noise points explicitly. For GMM, show membership uncertainty when it matters.

Avoid returning only one colored two-dimensional scatter plot. A useful cluster story normally needs both cluster validity and cluster meaning.

## Classification

Applies to logistic regression, SVM, decision trees, random forests, XGBoost, LightGBM, and neural classifiers.

| Evidence task | Preferred figure | Critical condition |
|---|---|---|
| Error structure | confusion-matrix heatmap | state counts or normalization basis |
| Ranking discrimination | ROC curve | include operating context and AUC only when computed |
| Imbalanced performance | precision–recall curve | prefer over ROC as the primary curve when positives are rare |
| Probability quality | calibration curve | requires predicted probabilities and enough samples per bin |
| Threshold decision | metric/utility vs threshold | define costs or target metric |
| Generalization | learning curve | use real train/validation sizes or epochs |
| Interpretation | feature importance, SHAP summary/dependence, PDP | explain method limitations; do not equate association with causation |
| Low-dimensional mechanism | decision boundary | only for genuinely two-dimensional or explicitly projected inputs |

Use held-out or cross-validated predictions for performance figures. For multi-class tasks, state micro/macro/weighted averaging. Never hide minority-class failure behind overall accuracy.

## PCA and dimensionality reduction

Prioritize:

1. ★★★★★ scree plot plus cumulative explained variance for component selection;
2. ★★★★ loading heatmap or contribution plot for interpretation;
3. ★★★★ PCA scores plot for sample structure;
4. ★★★ PCA biplot when the number of variables and labels remains readable.

Label the variance explained by each displayed component. Standardize features only if the modeling pipeline actually did so. For t-SNE/UMAP, report key parameters and avoid reading axis values as interpretable latent factors.

## Machine learning and deep learning

Combine performance with interpretation and generalization evidence.

Recommended candidates:

- observed vs predicted and residual plots for regression models;
- confusion matrix, ROC, PR, and calibration for classifiers;
- feature importance, SHAP summary/dependence, and PDP/ICE for tabular models;
- learning curves for sample sufficiency;
- training/validation loss and task metric by epoch for deep learning;
- ablation or component comparison only when those experiments were actually run;
- repeated split/seed distributions for stability;
- representative error cases only when selection rules are disclosed.

Do not report only Accuracy, RMSE, or another scalar. Do not describe attention weights or one explanation method as definitive causal explanation. Do not create an ablation, learning curve, or seed distribution from a single final checkpoint.

## Evidence requirements

| Figure | Minimum required evidence |
|---|---|
| histogram/KDE/ECDF/violin | raw observations plus units and group labels |
| correlation heatmap | aligned variables and stated correlation method |
| observed vs predicted | paired observations and predictions from the stated evaluation split |
| residual/Q–Q | paired observations and predictions; residual definition |
| confidence/prediction band | fitted uncertainty from the model or a justified resampling method |
| ROC/PR/calibration | true labels and continuous scores/probabilities |
| learning curve | performance recorded over training sizes or epochs |
| silhouette plot | sample-level cluster labels and distances/features |
| coefficient forest plot | estimates and valid uncertainty intervals |
| SHAP/PDP | fitted model, exact feature matrix, and recorded preprocessing |
| forecast interval | model- or resampling-derived interval values |
| repeated-run distribution | multiple independent seeds, folds, splits, or scenarios |

When any minimum evidence is missing, plan the figure only as a future requirement and name the exact artifact that must be generated.
