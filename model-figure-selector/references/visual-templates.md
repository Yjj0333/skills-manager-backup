# 视觉模板库（scibox 复刻模板 × 真实数据改造）

来源：github.com/jihe520/sci-box 的 scibox-figure（11 个模板脚本已内置到 assets/scibox-templates/）。
模板用确定性模拟数据复刻出版级风格；本 skill 的用法是：**保留全部视觉基因（配色、布局、字体、导出），只把模拟数据函数替换为真实数据**。

## 使用流程

1. 按第 7 步选定的图表类型，在下表匹配模板；
2. 核对"真实数据需求"列与本项目已验证的数据；
3. 把模板脚本复制进项目绘图目录，只改数据构造与标签文案；
4. 不动样式、布局、导出代码；
5. 按 paper-integration-and-qa.md 做渲染 QA 与数值核对。

## 改造红线（对应 skill 规则 1–4）

- 只替换 synthetic_* / simulate_* 系列函数——各脚本的数据构造都集中在这类函数里，固定 np.random.default_rng(seed)，一眼可定位。
- 替换模拟数据时，同步删除只服务模拟的注释与数值表（如 cv_roc_ci 里"指定的 AUC 值"），**模拟数字不得流入论文**。
- 真实数据缺字段（无逐折 ROC、无重复 run、无逐类 SHAP）时，该图按数据缺口处理（说 当前数据不足以生成该图），不硬套模板。
- 保持脚本骨架：入口设 MPLCONFIGDIR → configure_matplotlib() → 数据函数 → make_figure(output_stem) → PNG/PDF/SVG 三格式导出。

## 模板索引（按图表任务组织）

### A. 数据理解

| 模板 id | 脚本 | 表达什么 | 真实数据需求 | 改造点 |
|---|---|---|---|---|
| paired-raincloud | make_paired_raincloud.py | 配对前后/两条件对比：半小提琴+散点+箱线+均值连线+显著性括号 | 两组等长配对测量值 | 替换 synthetic_sepal_width_data()；改组名、指标名、显著性标注 |
| correlation-pairgrid | make_correlation_pairgrid.py | 对角分布+下三角散点拟合线+上三角相关系数的 EDA 组合图 | 数值型 DataFrame | 替换数据加载与变量名 |
| grouped-corr-split-violin | make_grouped_corr_split_violin.py | 下三角相关矩阵半边小提琴+特征分组着色 | 相关矩阵 + 分组标签 + 特征原始值 | 替换相关值与分组定义 |

### C. 求解过程

| 模板 id | 脚本 | 表达什么 | 真实数据需求 | 改造点 |
|---|---|---|---|---|
| rf-tpe-surface | make_rf_tpe_surface.py | TPE/贝叶斯超参搜索 3D 曲面（coolwarm） | 网格化 (param1, param2, score) | 用 Optuna/网格搜索结果替换模拟曲面 |

### D. 结果展示

| 模板 id | 脚本 | 表达什么 | 真实数据需求 | 改造点 |
|---|---|---|---|---|
| prediction-marginal-grid | make_prediction_marginal_grid.py | 预测 vs 真实散点 + 边缘分布组合 | y_true、y_pred（可分集） | 替换 y 数组与误差指标注释 |
| grouped-circular-heatmap | make_grouped_circular_heatmap.py | 分组环形热图 + 显著性星号（大矩阵） | 数值矩阵 + 行/列分组 | 替换 simulate_heatmap_values() 与 TraitSpec 色系映射 |
| urban-park-cooling-combo | make_urban_park_cooling_combo.py | 堆叠序列 + 云雨图 + 箱线多 panel 组合 | 多组时间/空间序列与分布 | 脚本最长，先跑通原模板再逐 panel 换数据 |
| nature-chord-diagram | make_nature_chord_diagram.py | Nature 风格和弦图（流量/转移/评价流向） | 方阵 flow matrix + 扇区命名 | 替换矩阵与扇区标签 |

### E. 模型验证

| 模板 id | 脚本 | 表达什么 | 真实数据需求 | 改造点 |
|---|---|---|---|---|
| cv-roc-ci | make_cv_roc_ci.py | 多折 ROC + 均值曲线 ± CI + 折 AUC 表 | 每折 y_true/y_score 或折 AUC | 替换 simulate_cv_rocs() 为真实折曲线；无逐折数据则降级为单 ROC 并如实说明 |
| taylor-diagram | make_taylor_diagram.py | 泰勒图多模型 σ–R 对比 | 各模型标准差、相关系数（可含 RMS） | 替换统计量数组与模型名 |
| multiclass-shap-combo | make_multiclass_shap_combo.py | 多分类 SHAP 重要性柱 + 蜂群双 panel | per-class SHAP values + 特征名 | 替换 SHAP 数组；柱图与蜂群共用同一解释结果 |

### F. 敏感性/稳健性

无专用模板。多情景对比可复用 taylor-diagram（把"多模型"换成"多参数情景"）；其余按通用画法 + 下文风格契约执行。

## 全局视觉契约（新画的图也遵循，保证与模板图同族）

- **导出三件套**：PNG 300 dpi + PDF + SVG，bbox_inches="tight"；环形热图等紧凑图加 pad_inches=0.02。
- **环境**：入口 os.environ.setdefault("MPLCONFIGDIR", ...)（模板已带）；中文字体策略见 paper-integration-and-qa.md。
- **风格基座**：每个模板 24–53 行处的 configure_matplotlib()（字号、线宽、去脊、网格）可直接复制为自写图的起点。

### 配色速查（从模板提取，按场景取用）

| 场景 | 色值 |
|---|---|
| 双组对照（干预前后 / 两方案） | #c9253e #ee7f8d / #145f86 #6f9fba |
| 2–5 条折线或交叉验证折线 | #2d214c #8f3032 #c47b4b #3c8849 #242585 |
| 多模型对比（泰勒图 / 收敛曲线） | #d7191c #2222a0 #36a852 #0b6b20 #f2a51a |
| 柔和多类（≤6 类） | #6fb8d7 #e5bd50 #54c887 #df8984 #a86cba #e8c65d |
| 分组小提琴 / 分组散点 | #2f7e91 #c7474d #3f9d54 #2f7fa7 |
| 时空序列渐变（冷→暖语义） | #34485b #557280 #759b9d #95bdae #c8ded4 |
| 环形热图特质色对（深→浅） | 紫 #51448a→#e7e4f2 · 绿 #4e9568→#e2f0e4 · 红 #bd454c→#f5dddd · 蓝 #3d719b→#e3edf5 |
| 和弦图扇区 | #8176b0 #6b248b · #d3ba73 #9d5c08 · #7dd2c4 |
| SHAP 双向贡献（低→高） | #2166ac → #fdae61 → #d73027（RdYlBu 系） |
| 发散型 3D 曲面 | cmap="coolwarm" |

### 无模板图型的兜底

没有匹配模板时：复制任一模板的 configure_matplotlib() 作风格基座 + 按上表选同场景配色。期刊级打磨、后端选择与渲染 QA 仍按职责边界交给 nature-figure；非数据型示意图（技术路线、模型结构）走 4drawio。
