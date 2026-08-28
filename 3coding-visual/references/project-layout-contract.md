# 数学建模工程目录与运行合同

本合同是新数学建模项目的默认工程规范。它定义数据、模型、求解、验证、运行快照、绘图、写作交接和支撑材料导出的职责边界。旧项目只审计，不在未授权时迁移。

## 目录

- [标准链路](#标准链路)
- [标准项目目录](#标准项目目录)
- [数据合同](#数据合同)
- [求解器合同](#求解器合同)
- [运行快照与冻结](#运行快照与冻结)
- [绘图合同](#绘图合同)
- [图表清单](#图表清单)
- [支撑材料导出](#支撑材料导出)
- [论文附录代码选择](#论文附录代码选择)
- [旧项目迁移](#旧项目迁移)
- [非-Python 项目](#非-python-项目)
- [验收场景](#验收场景)

## 标准链路

```text
data
  ↓
code/solvers/problemX
  ↓
core_results + validation + diagnostics + figure_data
  ↓
results/runs/<run_id>
  ↓
全部预定问题通过规定验证
  ↓
results/current_run.json
  ↓
model-figure-selector
  ↓
code/plots/problemX/fig_qX_YY
  ↓
figures/final
  ↓
5writing
```

支撑材料链：

```text
current_run + code + 必要数据 + 权威结果 + figures/final
  ↓
export_support_material
  ↓
delivery/support_material + delivery_manifest.json
```

必须保持：

```text
数据 ≠ 模型定义 ≠ 求解 ≠ 验证 ≠ 结果序列化 ≠ 绘图 ≠ 写作 ≠ 导出
```

## 标准项目目录

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
│   │   ├── __init__.py
│   │   ├── paths.py
│   │   ├── data_io.py
│   │   ├── validation.py
│   │   └── serialization.py
│   ├── solvers/
│   │   ├── __init__.py
│   │   └── problemX/
│   │       ├── __init__.py
│   │       ├── main.py
│   │       ├── model.py
│   │       ├── solver.py
│   │       └── validate.py
│   └── plots/
│       ├── __init__.py
│       ├── style.py
│       ├── render_selected.py
│       └── problemX/
│           ├── __init__.py
│           └── fig_qX_YY.py
├── results/
│   ├── runs/
│   │   └── <run_id>/
│   │       ├── run_manifest.json
│   │       └── problemX/
│   │           ├── core_results.json
│   │           ├── validation.json
│   │           ├── diagnostics/
│   │           ├── figure_data/
│   │           └── run.log
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

CUMCM B 题可以四问为初始规划，但只按题面真实问数创建 `problemX`。不保留无意义空问题目录和空模块。

## 数据合同

### `data/raw/`

保存赛题提供的原始附件。不得为了清洗方便覆盖原件。

### `data/external/`

保存比赛过程中自行查找且实际进入模型的数据。没有进入模型的检索文件不混入最终支撑材料。

### `data/processed/`

保存经过清洗、转换、标准化或聚合后需要被多次复用的数据。一次性内存变换不必为了目录完整强制落盘。

### `data_manifest.json`

每个实际文件至少记录：

```json
{
  "path": "data/raw/example.csv",
  "data_type": "csv",
  "source": "题目附件或真实来源",
  "purpose": "进入哪个问题和模型",
  "is_official_attachment": true,
  "is_external": false,
  "include_in_support_material": true,
  "accessed_at": null
}
```

外部数据在必要时记录访问日期。未知字段使用 `null`，不得猜测。

### 路径

- 全部程序使用相对项目根目录的路径。
- 路径逻辑优先集中到 `code/common/paths`。
- 禁止把 `C:/Users/...`、`D:/Users/...`、`/Users/...`、`/home/...` 等开发者绝对路径写入代码、manifest、论文或支撑材料。
- 运行入口应能从项目根目录稳定执行。

## 求解器合同

### `main`

只负责：参数解析、加载输入、构造 model、调用 solver、调用 validate、序列化本问 snapshot 和返回状态。

禁止包含大量核心算法、最终论文绘图、`figures/final/` 写入或论文视觉排版。

默认示例：

```text
python code/solvers/problem1/main.py --run-id <run_id>
```

### `model`

负责数学模型定义、参数/数据结构、目标函数、约束、状态方程、特征定义和必要数学转换。不得承担最终论文绘图。

### `solver`

只负责模型训练、数值求解、优化、预测、聚类、仿真、Monte Carlo 或参数估计，并输出：

- `core_results`；
- 迭代、逐样本预测、轨迹等 diagnostics；
- 已完成复杂计算的结构化 `figure_data`。

强制禁止：

- 导入 Matplotlib、Seaborn、Plotly、Pyecharts 等绘图库；
- 写入 `figures/final/`；
- 保存论文最终图片；
- 修改 `figure_manifest.json`；
- 调用最终绘图脚本；
- 承担论文排版。

### `validate`

独立完成与本问相适配的约束、可行性、残差、误差、守恒、边界、稳定性、鲁棒性、灵敏度、预测性能或结果完整性检查，并将结构化结果写入 `validation.json`。

不要把全部验证逻辑塞入 solver。简单字段或类型门禁可以使用公共助手，但不能冒充论文模型检验。

### 简单问题

如果某问确实简单，可以把 `model` 和 `solver` 等少量职责合并到更少文件，但必须保持：

- 求解与论文绘图分离；
- 验证状态可独立判断和序列化；
- 主要代码能够被附录按价值选择；
- 不创建只有空函数或转发调用的模块。

### `run_all_solvers`

只负责接收 run ID、按问题依赖调用各问、汇总 solve/validation 状态和执行 promote 条件。不得实现任何具体问题的核心模型、算法或图表。

默认示例：

```text
python code/run_all_solvers.py --run-id <run_id>
```

## 运行快照与冻结

### `run_id`

每次正式求解使用唯一 run ID，默认 `YYYYMMDD_HHMMSS`。结果写入 `results/runs/<run_id>/`，历史 run 不默认覆盖。

### `run_manifest.json`

至少包含：

```json
{
  "run_id": "20260904_153012",
  "created_at": "ISO-8601 timestamp",
  "status": "running",
  "random_seed": 42,
  "problems": [],
  "validation": {},
  "environment": {}
}
```

根据实际模型补充入口命令、依赖、数据版本、终止原因和警告。不得把示例值当真实运行值。

### 随机种子

Monte Carlo、GA、PSO、SA、KMeans、随机森林、XGBoost、神经网络、随机初始化和随机采样等正式模型必须尽可能显式设置 seed，并写入 run manifest。稳定性结论还需保存每次独立运行的真实结果。

### 状态

```text
running → solved → validated → promoted
```

只有全部预定问题完成规定验证后才能 promote，并更新 `results/current_run.json`。当前权威指针不存在时不得伪造 run；可以明确记录尚无 promoted run。

### 失败 run

- 保留在 `results/runs/<run_id>/`；
- 记录 `failed`、失败问题、指标和原因；
- 不删除、不覆盖、不自动提升；
- 不更新 current pointer。

**FAILED RUN MUST NOT UPDATE `current_run.json`.**

### 单一冻结 run

论文不得使用 Q1 来自 run A、Q2 来自 run B、图表来自 run C 的人工拼接。若补算改变权威结果，必须形成一个包含完整问题链的新 run 并重新 promote。

## 绘图合同

### `figure_data`

标准链：

```text
solver → core_results → figure_data → plot script
```

绘图脚本允许单位换算、百分比、排序、坐标轴、label、annotation、subplot 和展示格式转换。

禁止在绘图脚本中重新训练、拟合、优化、聚类、Monte Carlo、计算权重、执行主要数学模型或修改 `core_results`、`validation`、`figure_data`。影响论文结论的计算必须回到 solver 并形成新 run。

### 一图一脚本

**ONE PAPER FIGURE = ONE SCRIPT ENTRY.**

- `fig_q1_01` → `code/plots/problem1/fig_q1_01.py`；
- 一个脚本只生成一个独立论文 `figure_id`；
- 同一图号、caption 和 label 下的 `(a)(b)(c)` 多面板视为一个 figure，可由一个脚本生成；
- 禁止一个大脚本生成整篇论文所有独立图；
- 禁止 solver 直接生成最终论文图。

没有 `$model-figure-selector` 的最终选择结果时，不得预建大量 `fig_qX_YY` 等待筛选。若某问最终入选三图，就只规划三个绘图入口。

### `render_selected`

只允许：读取 figure manifest、获得待生成 ID、找到 `script_path`、调用对应脚本并汇总状态。

禁止包含某张图的主要绘图代码、大量针对具体图的 `if/elif`、重新处理模型、调用 solver 或修改权威结果。

默认示例：

```text
python code/plots/render_selected.py --run-id <run_id>
```

### preview 与 final

- 调试、探索、候选图进入 `figures/preview/`；
- 真正用于论文的图进入 `figures/final/`；
- 最终图片集中存放，不建立 `figures/final/problem1/` 等问题子目录；
- 绘图代码仍按 `code/plots/problemX/` 分类。

### 命名

内部：

```text
figure_id  = fig_q1_01
script     = code/plots/problem1/fig_q1_01.py
```

最终输出可使用：

```text
figures/final/Q1_图01_原始数据变化趋势.png
figures/final/Q1_图01_原始数据变化趋势.pdf
```

`figure_id`、`display_name`、`caption`、`script_path` 是不同字段。修改中文文件名不得改变内部 ID。

## 图表清单

`results/figure_manifest.json` 每图至少记录：

```json
{
  "fig_q1_01": {
    "figure_id": "fig_q1_01",
    "problem": "problem1",
    "display_name": "Q1_图01_原始数据变化趋势",
    "caption": "原始数据变化趋势",
    "claim": "该图支持的论文结论",
    "script_path": "code/plots/problem1/fig_q1_01.py",
    "input_result_files": ["problem1/figure_data/trend.json"],
    "input_fields": ["time", "observed", "predicted"],
    "output_png": "figures/final/Q1_图01_原始数据变化趋势.png",
    "output_pdf_or_svg": "figures/final/Q1_图01_原始数据变化趋势.pdf"
  }
}
```

实际记录还应包含 current run ID、论文位置、label、生成状态和 QA 状态。manifest 必须建立：

```text
论文结论 → 冻结结果 → 绘图脚本 → 最终图片
```

## 支撑材料导出

### `export_support_material`

以 `results/current_run.json` 为唯一结果入口，生成 `delivery/support_material/`。默认保留：

- 真实 README 和依赖；
- 实际使用且允许提交的 external/processed 数据；
- `code/common/`、`code/solvers/`、`code/plots/`；
- current run 对应各问权威结果和 figure manifest；
- `figures/final/`。

不得默认整体复制内部 `results/runs/`。失败 run、旧实验、预览图和运行日志默认排除。

默认示例：

```text
python code/export_support_material.py
```

### `delivery_manifest.json`

至少记录：

- promoted `run_id`；
- 各问题入口、主要模型/求解程序；
- core results 和 validation；
- figure ID、script、输入字段和输出；
- 最终支撑材料文件列表。

它用于连接：

```text
问题 ↔ 求解程序 ↔ 冻结结果 ↔ 论文图 ↔ 绘图脚本 ↔ 最终交付
```

### 身份和无关文件扫描

导出前至少检查姓名、学号、学校、赛区、本机用户名、绝对路径、`/Users/...`、`/home/...`、`C:/Users/...`、Git author、IDE 信息、run log 以及 Office/PDF 元数据风险。

默认排除：

```text
.git/ .idea/ .vscode/ __pycache__/ venv/ .venv/ cache/
临时文件 debug 文件 失败图片 废弃代码 旧实验输出
```

扫描命中时报告具体文件和风险；不要静默删除来源不明的重要文件。

## 论文附录代码选择

附录 C 展示主要建模和算法实现，不是整个软件工程目录转储。

按实际问数组织：

```text
C.1 支撑材料文件列表
C.2 问题一主要源程序
C.3 问题二主要源程序
...
```

优先收录：

- 体现数学模型、核心算法和求解过程的完整必要代码；
- 各问实际主要 `model`、`solver`；
- 具有论文方法价值的灵敏度、稳健性、误差模型、约束验证或显著性检验；
- 被主要程序依赖且读者理解/运行所需的公共模块。

不默认收录：

- 只有参数解析和转发调用的 main；
- 简单 assert 或字段检查；
- 纯字体、坐标轴、annotation、legend、subplot 和保存图片的绘图脚本；
- 与论文核心方法无关的工程辅助代码。

纯绘图脚本仍必须保留在电子支撑材料 `code/plots/`，用于复现与追溯。若绘图文件包含拟合、优化、聚类、模型权重或主要数值生成，说明职责错误，应把计算迁回 model/solver。

## 旧项目迁移

本合同不自动迁移旧项目。未来获得明确授权后：

1. 审计旧 `problem1.py`、`problem2.py`、`utils.py` 等文件；
2. 标记其中的数据、模型、求解、验证、绘图和序列化职责；
3. 逐问迁移到 `code/solvers/problemX/` 和 `code/plots/problemX/`；
4. 使用同一输入和参数比较新旧核心结果与约束；
5. 新入口验证通过后才允许提升；
6. 原文件继续保留，删除必须再次获得用户明确确认。

## 非 Python 项目

Python 只作为默认示例语言。R、MATLAB、Julia、C++ 或其他环境使用等价扩展名、包结构和运行命令，但必须保持：

- 数据、model、solver、validate、plot 和 export 职责分离；
- run snapshot、current pointer 和 manifest；
- 一图一脚本入口；
- final/preview 分离；
- 相对路径、随机种子、失败 run 和单一 promoted run 规则。

## 验收场景

- 问题一选中三张论文图：只规划 `fig_q1_01`、`fig_q1_02`、`fig_q1_03` 三个脚本。
- 图 5 含 `(a)(b)(c)` 且共享 caption：允许一个 `fig_q2_03` 脚本生成整图。
- selector 尚未返回最终选择：不创建最终图脚本。
- 验证失败：失败 run 保留，current pointer 不变。
- 中文图片名变化：figure ID 与 script path 保持不变，manifest 更新输出路径。
- 导出支撑材料：只提取 current run 权威结果，不复制所有历史 runs。
- 论文附录：主要 model/solver 可进入，纯绘图脚本只进入电子支撑材料。

