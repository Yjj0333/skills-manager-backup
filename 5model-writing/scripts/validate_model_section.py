"""Validate the contract of an evidence-grounded modeling-section draft.

The validator intentionally checks structure and provenance markers, not prose quality.
It is suitable for a pre-handoff gate before the full-paper writing skill assembles
the competition template.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


TOP_LEVEL_HEADINGS = ("## 输入与范围", "## 题面任务—模型映射")
PROBLEM_HEADINGS = (
    "### 任务与接口",
    "### 变量与假设",
    "### 基线与缺陷诊断",
    "### 数学表达与求解规格",
    "### 验证与结果解释",
    "### 结果证据",
    "### 下游交接",
)
PLACEHOLDER_RE = re.compile(r"(?:TODO|TBD|FIXME|\[待(?:填|补)|\?{3,})", re.IGNORECASE)
PROBLEM_RE = re.compile(r"^##\s+(?:问题|Problem)\s*([一二三四五六七八九十0-9]+)", re.IGNORECASE | re.MULTILINE)


@dataclass
class ValidationResult:
    ok: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def _has_data_row(table: str) -> bool:
    rows = [line.strip() for line in table.splitlines() if line.strip().startswith("|")]
    if len(rows) < 3:
        return False
    return any("---" not in row for row in rows[2:])


def _validate_evidence(problem_text: str, problem_label: str, errors: list[str]) -> None:
    evidence_match = re.search(
        r"###\s*结果证据(?P<body>.*?)(?=^###\s+|^##\s+|\Z)",
        problem_text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    if not evidence_match:
        errors.append(f"{problem_label}缺少结果证据段落。")
        return

    body = evidence_match.group("body")
    header = next((line for line in body.splitlines() if line.strip().startswith("|")), "")
    required_columns = ("结论", "来源")
    if not all(column in header for column in required_columns):
        errors.append(f"{problem_label}的结果证据表必须包含“结论”和“来源”列。")
    if not _has_data_row(body):
        errors.append(f"{problem_label}的结果证据表必须至少有一行数据。")
    if "RESULTS_REPORT.md" not in body and "figures/" not in body:
        errors.append(f"{problem_label}的结果证据必须指向 RESULTS_REPORT.md 或 figures/。")


def validate_text(text: str) -> ValidationResult:
    errors: list[str] = []
    warnings: list[str] = []

    for heading in TOP_LEVEL_HEADINGS:
        if heading not in text:
            errors.append(f"缺少顶层段落：{heading}。")

    if "ANALYSIS_MODELING_REPORT.md" not in text:
        errors.append("必须声明建模输入来源 ANALYSIS_MODELING_REPORT.md。")
    if "RESULTS_REPORT.md" not in text:
        errors.append("必须声明结果输入来源 RESULTS_REPORT.md。")
    if PLACEHOLDER_RE.search(text):
        errors.append("存在未解决的占位符（TODO/TBD/[待填]/???）。")

    problem_matches = list(PROBLEM_RE.finditer(text))
    if not problem_matches:
        errors.append("至少需要一个以“## 问题...”或“## Problem...”开头的子问题章节。")
    for index, match in enumerate(problem_matches):
        end = problem_matches[index + 1].start() if index + 1 < len(problem_matches) else len(text)
        problem_text = text[match.start() : end]
        problem_label = f"问题 {match.group(1)}"
        for heading in PROBLEM_HEADINGS:
            if heading not in problem_text:
                errors.append(f"{problem_label}缺少“{heading[3:]}”段落。")
        _validate_evidence(problem_text, problem_label, errors)

    mapping_match = re.search(r"^##\s+题面任务—模型映射(?P<body>.*?)(?=^##\s+|\Z)", text, re.MULTILINE | re.DOTALL)
    if mapping_match and not _has_data_row(mapping_match.group("body")):
        errors.append("题面任务—模型映射必须包含至少一行数据。")

    return ValidationResult(ok=not errors, errors=errors, warnings=warnings)


def validate_file(path: Path) -> ValidationResult:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return ValidationResult(False, [f"无法读取报告：{exc}"])
    return validate_text(text)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a modeling-section draft.")
    parser.add_argument("report", type=Path, help="Markdown draft to validate")
    args = parser.parse_args(argv)
    result = validate_file(args.report)
    if result.ok:
        print(f"OK: {args.report}")
        return 0
    for error in result.errors:
        print(f"ERROR: {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
