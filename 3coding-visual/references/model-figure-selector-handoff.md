# 求解结果到图表决策的跨 Skill 合同

在每个子问题完成正式求解、验证并形成 promoted run 后使用本合同。它规定 `3coding-visual` 如何调用项目内的 `$model-figure-selector`，以及如何把论文 claim、冻结结果、独立绘图脚本和最终图片连接起来。

## 目录

- [调用时机](#调用时机)
- [依赖门禁](#依赖门禁)
- [输入包](#输入包)
- [调用要求](#调用要求)
- [返回合同](#返回合同)
- [缺数修复循环](#缺数修复循环)
- [图表归属边界](#图表归属边界)
- [执行与回填](#执行与回填)
- [验收场景](#验收场景)

## 调用时机

必须满足以下条件后再调用：

1. 模型代码已经执行；
2. 正式结果已经产生；
3. 约束、误差、守恒或一致性已经检查；
4. 绘图需要的迭代、预测、概率、坐标、权重、排名、轨迹或重复运行数据已经保存到 current run 的 `figure_data` 或其他权威结果；
5. `reports/RESULTS_REPORT.md` 至少已有结果草稿。

不得在求解前让图表方案反向诱导修改模型或制造数据。

## 依赖门禁

按以下顺序解析：

1. 若当前上下文可直接调用 `$model-figure-selector`，使用它。
2. 若当前项目包含 `.agents/skills/model-figure-selector/SKILL.md`，读取并按该项目 Skill 执行。
3. 若两者都不存在，停止图表生成，报告“缺少 model-figure-selector，代码与结果已完成，图表决策阶段未完成”。

不要退回“预测画折线图、评价画雷达图、优化画收敛曲线”的固定模板。依赖缺失不影响继续验证求解结果，但阻止完整阶段验收。

## 输入包

向 `$model-figure-selector` 提供：

- 题目与子问题编号；
- `reports/ANALYSIS_MODELING_REPORT.md`；
- `reports/RESULTS_REPORT.md` 当前草稿；
- 模型/算法名称及其公式、目标、约束和验证任务；
- 权威机器结果文件清单；
- 可用字段、形状、单位、时间索引、组别、种子、场景和运行次数；
- 已有核心结论及其数值来源；
- current run ID、论文语言、输出格式、`figures/preview/` 和 `figures/final/` 位置；
- “本阶段只生成数据驱动图，非数据图交给 4drawio”的边界。

不传递没有运行过的实验作为候选证据。

## 调用要求

使用“完整图表设计”模式，而不是直接索要图名。要求完成：

> 模型识别 → A–F 论文任务 → 每图 claim → 数据充分性 → 候选评分与去重 → 2～4 张核心图表链 → 绘图库 → 论文位置 → caption/label → 正文分析要点

明确要求：

- 只基于真实结果；
- 对数据不足的图返回缺失字段/日志/实验；
- 把 ★★★★★ 和 ★★★★ 作为正文优先图；
- ★★★ 仅在篇幅允许、附录有价值或用户明确要求时生成；
- 列出不推荐图及原因；
- 保持同一对象的颜色、线型和标记一致。

## 返回合同

每张入选图至少包含：

| 字段 | 内容 |
|---|---|
| figure_id | 稳定 ASCII ID，例如 `fig_q1_01` |
| problem | 所属顶层问题，例如 `problem1` |
| display_name | 最终图片的中文描述性名称，不承担内部 ID 职责 |
| priority | ★★★★★、★★★★ 或 ★★★ |
| task | A 数据、B 建模、C 求解、D 结果、E 验证、F 稳健性 |
| claim | 删除该图会失去哪层证据 |
| chart | 图形类型和多面板结构 |
| encoding | x/y/color/size/facet/annotation/单位 |
| source | 权威结果文件与字段 |
| transform | 展示变换及公式 |
| library | 实际绘图库，不得写 nature-figure |
| style_route | 是否需要 `$nature-figure` |
| placement | 论文小节及相对段落位置 |
| caption | 简短正式图题 |
| label | 稳定论文交叉引用标签 |
| script_path | 一图一脚本的稳定 ASCII 路径，例如 `code/plots/problem1/fig_q1_01.py` |
| input_result_files | current run 内的权威输入文件 |
| input_fields | 绘图实际读取字段 |
| output_png | `figures/final/` 中的中文描述性 PNG 路径 |
| output_pdf_or_svg | `figures/final/` 中的 PDF 或 SVG 路径 |
| analysis | 展示什么、规律、原因、模型含义 |
| qa_risk | 不确定性、重叠、尺度、乱码或误读风险 |

把该合同记录到 `reports/RESULTS_REPORT.md`，并保存为 `results/figure_manifest.json`。manifest 必须建立“论文结论 → current run 冻结结果 → 绘图脚本 → 最终图片”的可追溯关系。

`figure_id`、`display_name`、`caption` 和 `script_path` 是独立字段。修改中文图片名不得改变内部 ID。

## 缺数修复循环

若推荐图缺少证据：

1. 判断所缺数据能否由当前已批准模型在不改变数学含义的前提下重新运行并记录；
2. 能补录时，修改结果序列化而不是伪造数组，重新运行、重新验证并更新结果快照；
3. 再次调用 `$model-figure-selector` 检查图是否已获支持；
4. 不能补录时，将该图列为“当前数据不足以生成”，不生成占位图。

常见合法补录包括迭代级目标、逐样本预测、分类概率、约束松弛量、每个随机种子结果和真实参数扰动结果。不得从最终值插值伪造收敛曲线，也不得把单次运行复制成稳定性样本。

## 图表归属边界

| 图表 | 归属 |
|---|---|
| 真实数据分布、预测诊断、收敛、Pareto、敏感性、约束检查 | `3coding-visual` |
| 由节点/边/坐标/权重/求解方案生成的网络、路径、布局 | `3coding-visual` |
| 技术路线、通用算法流程、数据处理流程、指标层次、纯概念结构 | `4drawio` |
| 需要精确数据但被包装成“示意图”的图 | 仍归 `3coding-visual`，不得改成交给生成式图片 |

如果 `$model-figure-selector` 推荐了非数据型模型结构图，将它写入后续 `4drawio` 交接项，不在本阶段绘制。

## 执行与回填

1. 没有 selector 的最终入选清单时，不创建大量最终绘图脚本。
2. 每个入选 `figure_id` 创建一个独立 `script_path`；一个脚本不能生成多个独立论文 figure。
3. 共享同一图号、caption 和 label 的多面板图属于一个 figure，可以由一个脚本生成。
4. 使用选择结果指定的绘图库；`$nature-figure` 只负责学术风格、后端和 QA。
5. 绘图脚本只读取 current run 的权威结果或 `figure_data`，不得调用 solver、重新训练/拟合/优化或修改结果。
6. 候选和调试图进入 `figures/preview/`；最终 PDF/SVG 与 300 DPI 以上 PNG 统一进入 `figures/final/`，不按问题建立最终图片子目录。
7. `code/plots/render_selected.py` 只读取 manifest、定位并调用脚本、汇总状态，不包含具体图表逻辑或大量特定图分支。
8. 检查最终尺寸、文字、单位、图例、遮挡、颜色一致性和数值一致性。
9. 在结果报告中记录 claim、current run、数据源、脚本、输出、caption/label、正文分析和 QA 状态。
10. 把未生成图及原因单列，不要用空白占位图冒充完成。

## 验收场景

- 熵权–TOPSIS：应形成“权重 → 综合得分 → 排名稳定性”证据链，而不是默认雷达图合集。
- 类别不平衡分类：应优先 PR 曲线并保留混淆矩阵/校准等真实诊断，不能只报 Accuracy 或 ROC。
- 模拟退火：只有迭代级历史才能画收敛；只有精确事件记录才能标注首次可行；只有多次独立运行才能画稳定性分布。
- 多目标优化：只有真实目标向量/非支配解集才能画 Pareto；单个加权解不能伪装成前沿。
- 路径规划：必须画真实节点与求解路径并验证容量/时间窗等约束，不能只用表格列路径。
