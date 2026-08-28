---
name: 1start-mathmodel
description: "数学建模竞赛工作流入口。用于启动 CUMCM 及一般数学建模项目，确认比赛、排版、语言和问题数，生成 plan.md 与 todo.md，初始化可追溯的数据、求解、验证、绘图、写作和支撑材料骨架，并依次调用后续建模 Skills。"
---

# 数学建模工作流入口

负责启动项目、记录用户决策、建立未来项目骨架并调度各阶段 Skill。不要在本阶段代替后续 Skill 建模、求解、绘图或撰写论文。

## 必读合同

- 如需数学建模领域判断，读取 `../_references/math_modeling_norms.md`。
- 初始化编码与结果目录前，完整读取 `../3coding-visual/references/project-layout-contract.md`。该文件是项目工程骨架、运行快照、最终图片和支撑材料目录的唯一详细来源。
- 使用项目内 `2analysis-modeling`、`3coding-visual` 和 `5writing` 的当前合同，不用全局旧版覆盖本地约定。

## 必须产出

在当前建模项目创建或更新：

- `plan.md`：用户偏好、赛题信息、阶段顺序、目录合同、预期产物和风险；
- `todo.md`：五阶段任务及状态；
- 新项目的必要顶层工程骨架。

对已有项目先审计，不迁移、不删除、不覆盖旧代码。目录重构必须由用户另行明确授权。

## Step 1：确认关键偏好

只询问会改变工作流的事项：

1. 排版引擎：LaTeX 或 Typst；未明确时默认 LaTeX；
2. 竞赛类型和题号；
3. 论文语言；
4. 题面明确的顶层问题数；未知时交给 `2analysis-modeling` 识别。

CUMCM B 题可在题面缺失时按四问规划，但题面一旦明确必须以题面为准。

## Step 2：生成方案与待办

`plan.md` 至少记录：

```markdown
# 方案

用户偏好：
- 排版引擎：<LaTeX / Typst>
- 竞赛类型：<CUMCM / 其他>
- 题号：<A / B / C / ...>
- 论文语言：<中文 / 英文>
- 子问题数量：<N / 待分析>

workflow:
1. 赛题分析与建模设计 - 2analysis-modeling
2. 编程实现、验证、结果冻结与数据图表 - 3coding-visual
3. 非数据型图示 - 4drawio
4. 论文撰写 - 5writing
5. 最终验证与验收 - 6verity
```

`todo.md` 使用相同阶段顺序。每完成一个阶段只更新对应状态，不提前标记下游完成。

## Step 3：初始化未来项目骨架

新项目默认采用：

```text
project/
├── README.md
├── requirements.txt
├── plan.md
├── todo.md
├── data/
│   ├── raw/
│   ├── external/
│   ├── processed/
│   └── data_manifest.json
├── code/
│   ├── run_all_solvers.py
│   ├── export_support_material.py
│   ├── common/
│   ├── solvers/problemX/
│   └── plots/problemX/
├── results/
│   ├── runs/
│   ├── current_run.json
│   └── figure_manifest.json
├── figures/
│   ├── preview/
│   └── final/
├── delivery/
│   ├── support_material/
│   ├── appendix/
│   └── delivery_manifest.json
├── reports/
└── paper/
```

执行初始化时遵守：

- `README.md` 只记录已知项目说明和复现入口；`requirements.txt` 只记录实际依赖。
- `data_manifest.json` 可先建立空文件清单，但不得编造数据来源。
- 问题数未知时，不创建 `problem1` 至 `problem4` 空目录；由分析阶段确认后，只为真实问题创建目录。
- 对简单问题按实际职责合并文件，不为了树形整齐制造空 `model.py`、`solver.py` 或 `validate.py`。
- 在首个 run 完成全部预定验证前，不写入虚假的 current run 指针。
- 不再使用 `code/problem1.py`、`code/problem2.py`、`code/utils.py` 作为新项目默认骨架。
- Python 是默认示例语言；实际采用其他语言时保留同样的职责与目录边界。

## Step 4：按顺序调用阶段

| 阶段 | Skill | 主要产物 |
|---|---|---|
| 分析与建模 | `2analysis-modeling` | `reports/ANALYSIS_MODELING_REPORT.md` |
| 求解与数据图 | `3coding-visual` | `code/`、`results/`、`figures/final/`、`reports/RESULTS_REPORT.md` |
| 非数据图 | `4drawio` | 可编辑源文件、获选后进入 `figures/final/` 的论文图、`reports/DRAWIO_REPORT.md` |
| 论文写作 | `5writing` | `paper/`、论文 PDF、附录选择 |
| 验证验收 | `6verity` | `reports/VERIFY_REPORT.md`、提交就绪结论 |

不得跳过前序结果冻结直接写论文，也不得让后序 Skill 静默修改前序模型和权威结果。

## 阶段边界

- `3coding-visual` 负责数据读取、模型实现、正式求解、验证、run 冻结、数据图和支撑材料导出合同。
- `4drawio` 只负责非数据型图示；其获选论文图同样集中到 `figures/final/`。
- `5writing` 只从 `figures/final/` 和图表 manifest 消费最终论文图。
- 纯绘图脚本保留在电子支撑材料，默认不进入论文附录。
- 论文核心结果不得从多个 run 人工拼接。

## 完成门禁

- `plan.md`、`todo.md` 与实际比赛、问题数和引擎一致；
- 项目骨架与 `project-layout-contract.md` 一致；
- 不存在旧扁平骨架作为新项目默认；
- 没有创建虚假问题目录、依赖、数据、运行或结果；
- 下游 Skill、产物和阶段边界明确；
- 全局 Skill 未被修改。

