---
name: 3coding-visual
description: "数学建模编程实现、求解器组织、模型验证、运行快照、权威结果冻结、独立绘图脚本、最终论文图和支撑材料导出阶段。用于承接 ANALYSIS_MODELING_REPORT.md，将各问题落实为可复现工程；求解冻结后必须调用 $model-figure-selector，再按一张论文图一个脚本生成 figures/final/。"
---

# 编程实现、求解验证与数据图表

承接 `2analysis-modeling`，建立“数据 → 模型 → 求解 → 验证 → run 冻结 → 选图 → 独立绘图 → 写作交接 → 支撑材料导出”的可追溯链路。

## 不可混合的职责

```text
数据 ≠ 模型定义 ≠ 求解 ≠ 验证 ≠ 结果序列化 ≠ 绘图 ≠ 论文写作 ≠ 支撑材料导出
```

- 求解器不得导入绘图库、写入 `figures/final/`、修改 `figure_manifest.json` 或调用绘图脚本。
- 绘图脚本不得重新训练、拟合、优化、聚类、仿真、计算模型权重或修改权威结果。
- 验证逻辑与 solver 分离；简单问题可合并少量文件，但验证结果仍须独立序列化。
- 论文核心结果和最终图片必须来自同一个 promoted run，不得人工拼接多个 run。
- 技术路线、通用流程、概念结构等非数据型图交给 `4drawio`；获选后同样进入 `figures/final/`。

## 必读合同

开始编码前完整读取：

- [工程目录与运行合同](references/project-layout-contract.md)：目录、模块职责、run、promote、图表、导出和旧项目兼容；
- `../_references/math_modeling_norms.md` 中的题型防错、代码实现与图表小节；
- `reports/ANALYSIS_MODELING_REPORT.md`、`plan.md`、题面和真实附件。

求解冻结后、创建最终绘图脚本前完整读取：

- [图表选择交接合同](references/model-figure-selector-handoff.md)；
- CUMCM B 题国赛论文使用的 [5writing 结果交接合同](references/5writing-result-handoff.md)。

## 项目识别与旧项目保护

1. 审计实际存在的 `data/`、`code/`、`results/`、`figures/`、`delivery/` 和 `reports/`。
2. 新项目使用 `project-layout-contract.md` 的标准骨架，并按题面动态创建真实问题目录。
3. 已有扁平 `problem1.py`、`problem2.py`、`utils.py` 等旧项目时，只做职责盘点；本阶段不得自动移动、删除或覆盖。
4. 用户另行授权迁移时，逐问迁移并比较新旧结果；旧入口必须保留到新入口验证通过，删除仍需再次明确确认。
5. 不为形式统一创建没有实际职责的空模块。

## Step 0：输入、数据和环境门禁

- 原始附件进入 `data/raw/`，实际使用的外部数据进入 `data/external/`，可复用处理数据进入 `data/processed/`。
- 更新 `data/data_manifest.json`，记录来源、用途、附件/外部属性、支撑材料需要和必要访问日期。
- 所有程序使用项目相对路径；禁止本机用户名、盘符或主目录绝对路径，路径逻辑集中到公共路径模块。
- 核对数据编码、字段、主键、形状、单位、缺失、重复、异常和时序。
- 记录语言、依赖、硬件、求解器、入口命令和随机种子。
- 缺少关键输入时列出阻塞，不生成虚假数据继续。

## Step 1：按问题实现独立求解器

每个真实问题使用 `code/solvers/problemX/`：

- `main`：参数解析、输入加载、调用 model/solver/validate、序列化和状态返回；
- `model`：数学模型、参数结构、目标、约束、状态方程和必要数学转换；
- `solver`：训练、求解、优化、预测、仿真或参数估计，并输出 `core_results`、diagnostics 和结构化 `figure_data`；
- `validate`：约束、可行性、误差、残差、守恒、边界、稳定性、鲁棒性或灵敏度，并输出 `validation.json`。

公共路径、数据读取、验证助手和序列化逻辑放入 `code/common/`。不要为了复用改变数学含义。

## Step 2：创建正式 run snapshot

- 每次正式求解使用唯一 `run_id`，默认格式 `YYYYMMDD_HHMMSS`。
- 结果写入 `results/runs/<run_id>/`，历史 run 默认不可覆盖。
- `run_manifest.json` 至少记录 run ID、时间、状态、随机种子、问题列表、验证摘要和环境。
- 每问保存 `core_results.json`、`validation.json`、diagnostics、`figure_data` 和真实运行日志。
- 随机模型必须显式设置并记录 seed；需要稳定性结论时保存每个独立运行结果。
- `run_all_solvers` 只按问题依赖调度、汇总状态和判断 promote，不实现具体数学模型或绘图。

## Step 3：数学验证与 promote

内部文件、类型和维度检查不是论文模型检验。论文检验必须直接验证数学逻辑、约束可行性、拟合或预测性能、排序稳定性、基准改进、守恒或边界行为。

按模型选择合适验证：

- 优化/路径：约束值、松弛量、违反量、整数和路径可行性；
- 随机/智能优化：种子、重复运行、目标分布、可行率和耗时；
- 预测/机器学习：正确数据划分、逐样本预测、误差、概率及数据泄漏检查；
- 评价/决策：指标方向、标准化、权重和、排名及合理扰动；
- 微分方程/仿真：初边值、守恒、漂移、步长或网格收敛。

状态按 `running → solved → validated → promoted` 变化。只有全部预定问题完成规定验证后才能更新 `results/current_run.json`。

**FAILED RUN MUST NOT UPDATE `current_run.json`.**

失败 run 保留真实状态、日志和原因，不删除、不覆盖、不自动提升。

## Step 4：冻结结果后智能选图

正式结果 promoted 后，才调用 `$model-figure-selector`：

1. 提供建模报告、结果报告、current run、机器结果、验证结论和可用 `figure_data`；
2. 完成模型识别、论文 claim、数据充分性、候选评分、核心图链、绘图库和论文位置规划；
3. 没有 selector 或没有明确入选图时，不创建大量最终绘图脚本；
4. selector 指出缺数时，只能合法重跑 solver 补录并重新验证，不能在绘图层伪造。

通常每问保留 2～4 张有证据价值的图；删图不削弱结论时不画。

## Step 5：一张论文图一个脚本

- 每个入选 `figure_id` 对应 `code/plots/problemX/fig_qX_YY.py` 一个入口。
- 一个脚本只能生成一个独立论文 figure；共享图号、caption 和 label 的多面板图属于一个 figure，可由一个脚本生成。
- 内部 `figure_id` 和脚本路径使用稳定 ASCII；最终图片可使用中文描述性名称。
- 候选、调试和探索图进入 `figures/preview/`；真正用于论文的图片统一进入 `figures/final/`，不再按问题分最终图片目录。
- 每张最终图输出 300 DPI 以上 PNG，并输出 PDF 或 SVG。
- 绘图脚本优先读取 current run 的 `figure_data`，只允许展示性排序、单位换算、百分比、标注和排版。
- `render_selected.py` 只读取 manifest、定位脚本、分发执行和汇总状态，不含具体图形逻辑或大量图表 `if/elif`。
- `$nature-figure` 是学术风格和 QA 层，不是绘图库。

## Step 6：结果、图表和写作交接

`results/figure_manifest.json` 必须把论文 claim、冻结结果、绘图脚本和最终图片连成一条链。每图至少包含：

- `figure_id`、`problem`、`display_name`、`caption`、`claim`；
- `script_path`、`input_result_files`、`input_fields`；
- `output_png`、`output_pdf_or_svg`；
- current run、论文位置、label 和 QA 状态。

更新 `reports/RESULTS_REPORT.md`，记录运行环境、逐问实现与结果、论文级检验、图表 manifest、代码与支撑材料、AI 使用事实和建模差异。所有数值保持与机器结果相同精度。

`5writing` 只消费 `figures/final/` 的入选图片和 manifest，不到各问题目录猜测文件。

## Step 7：导出支撑材料

实现 `code/export_support_material.py`，以 `current_run.json` 为唯一结果入口：

- 导出必要 README、真实依赖、必要外部/处理数据、代码、current run 权威结果、figure manifest 和 `figures/final/`；
- 不默认复制完整 `results/runs/`、失败 run、预览图、日志、缓存或废弃代码；
- 纯绘图脚本保留在电子支撑材料，默认不进入论文附录；
- 生成 `delivery/delivery_manifest.json`，映射问题、求解器、冻结结果、验证、图表脚本和交付文件；
- 扫描姓名、学号、学校、赛区、本机用户名、绝对路径、Git/IDE 信息及 Office/PDF 元数据风险；
- 默认排除 `.git/`、`.idea/`、`.vscode/`、`__pycache__/`、虚拟环境、缓存、临时文件、debug 和旧实验输出。

## 阶段完成门禁

- 标准目录、相对路径、数据 manifest 和运行入口真实可用；
- 各问题 solver、validation 与建模报告一致；
- current run 来自同一完整 run，失败 run 未 promote；
- 关键结果、验证和图表都能追溯到机器文件与代码；
- selector 已决定最终图，一图一脚本且 final/preview 分离；
- `figures/final/`、figure manifest、结果报告和论文数值一致；
- 支撑材料只导出 current run 的必要权威内容，身份与无关文件检查已完成；
- 附录代码选择突出主要建模/求解方法，不机械收录全工程或纯绘图脚本；
- 未编造数据、实验、图表、验证或结论。

