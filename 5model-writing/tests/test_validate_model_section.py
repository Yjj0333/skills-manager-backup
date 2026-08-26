import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate_model_section.py"
SPEC = importlib.util.spec_from_file_location("validate_model_section", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["validate_model_section"] = MODULE
SPEC.loader.exec_module(MODULE)


COMPLETE_DRAFT = r"""
# 建模章节草稿

## 输入与范围
本稿依据 reports/ANALYSIS_MODELING_REPORT.md、reports/RESULTS_REPORT.md 和 figures/ 生成。

## 题面任务—模型映射
| 子问题 | 任务角色 | 直接目标 | 输出形态 |
| --- | --- | --- | --- |
| 问题一 | 优化 | 成本最小 | 决策方案 |

## 问题一：模型建立与求解
### 任务与接口
输入为容量参数，输出为决策方案，供问题二继承。
### 变量与假设
决策变量 x_i，已知参数 c_i；假设容量边界来自题面并保持单位一致。
### 基线与缺陷诊断
线性规划作为基线，诊断结果显示需要增加整数约束。
### 数学表达与求解规格
目标函数：min Z = sum(c_i x_i)。
约束：sum(a_i x_i) <= b，x_i in {0,1}。
使用 MIP 求解并报告 E1 最优间隙。
### 验证与结果解释
检查可行性、约束残差、目标界和小规模精确基准。
### 结果证据
| 结论 | 数值/方向 | 来源 | 图表/表格 |
| --- | --- | --- | --- |
| 最优成本 | 12.4 | reports/RESULTS_REPORT.md | 表 1 |
### 下游交接
将 x_i 和不确定性界传给问题二。

## 限制与回退
若整数求解超时，保留可行解并报告最优间隙，不宣称全局最优。
"""


class ValidateModelSectionTests(unittest.TestCase):
    def write_draft(self, content: str) -> Path:
        handle = tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False)
        handle.write(content)
        handle.close()
        self.addCleanup(lambda: Path(handle.name).unlink(missing_ok=True))
        return Path(handle.name)

    def test_accepts_complete_draft(self):
        result = MODULE.validate_file(self.write_draft(COMPLETE_DRAFT))
        self.assertTrue(result.ok, result.errors)

    def test_rejects_missing_closed_loop_sections(self):
        content = COMPLETE_DRAFT.replace("### 验证与结果解释", "### 结果")
        result = MODULE.validate_file(self.write_draft(content))
        self.assertFalse(result.ok)
        self.assertTrue(any("验证与结果解释" in error for error in result.errors))

    def test_rejects_numeric_claim_without_evidence_table(self):
        content = COMPLETE_DRAFT.replace(
            "### 结果证据\n| 结论 | 数值/方向 | 来源 | 图表/表格 |\n| --- | --- | --- | --- |\n| 最优成本 | 12.4 | reports/RESULTS_REPORT.md | 表 1 |",
            "### 结果证据\n最优成本为 12.4。",
        )
        result = MODULE.validate_file(self.write_draft(content))
        self.assertFalse(result.ok)
        self.assertTrue(any("结果证据" in error for error in result.errors))

    def test_rejects_unresolved_placeholders(self):
        result = MODULE.validate_file(self.write_draft(COMPLETE_DRAFT + "\nTODO: 补充图表\n"))
        self.assertFalse(result.ok)
        self.assertTrue(any("占位符" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
