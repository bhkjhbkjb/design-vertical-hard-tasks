#!/usr/bin/env python3
"""Validate deterministic structure and hard gates for a task-record JSON file."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
from typing import Any


SUBMISSION_FIELDS = [
    "uid",
    "题目",
    "任务类型",
    "题目领域一级目录",
    "题目领域二级目录",
    "题目领域三级目录",
    "任务概括",
    "标注专家工作年限（未工作的可以写最高学历）",
    "人类所需完成时间",
    "相关附件",
    "附件格式标签",
    "附件内容（总结概括）",
    "产物格式标签",
    "产物内容（总结概括）",
    "做题关键步骤（必选）",
    "打分checklist（必填）",
]

READY_REQUIRED_FIELDS = [
    field for field in SUBMISSION_FIELDS if field != "uid"
]

REALITY_FIELDS = [
    "专家实际职责",
    "真实问题",
    "业务目标",
    "交付对象",
    "决策后果",
    "现实工作流程",
    "脱敏说明",
]

QUALITY_GATES = [
    "真实工作",
    "专业壁垒",
    "推理深度",
    "可解性",
    "产物可用性",
    "工时可信",
    "证据完整",
    "非模板化",
]

INTERNAL_PACK_FIELDS = [
    "证据映射",
    "关键事实",
    "计算与口径",
    "专业判断点",
    "不确定性",
    "预期产物",
    "严重漏答项",
    "禁止编造项",
]

ATTACHMENT_FIELDS = [
    "id",
    "name",
    "language",
    "publisher",
    "status",
    "supports",
]

LEGACY_TIER_RE = re.compile(r"(?<![A-Za-z0-9])L[123](?![A-Za-z0-9])", re.I)
SHA256_RE = re.compile(r"^[0-9a-f]{64}$", re.I)


def is_empty(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, dict, tuple, set)):
        return len(value) == 0
    return False


def is_english(language: Any) -> bool:
    text = str(language or "").strip().lower()
    return text in {"en", "en-us", "en-gb", "english", "英文"} or "英文" in text


def count_items(text: Any) -> int:
    if not isinstance(text, str):
        return 0
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) > 1:
        return len(lines)
    return len([part for part in re.split(r"[；;]", text) if part.strip()])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path, help="UTF-8 JSON task record")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    try:
        data = json.loads(args.record.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(json.dumps({"valid": False, "errors": ["文件不存在"]}, ensure_ascii=False, indent=2))
        return 1
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [f"无法读取 UTF-8 JSON：{exc}"]}, ensure_ascii=False, indent=2))
        return 1

    if not isinstance(data, dict):
        errors.append("根节点必须是 JSON 对象")
        data = {}

    status = data.get("status")
    if status not in {"DRAFT", "READY", "BLOCKED"}:
        errors.append("status 必须是 DRAFT、READY 或 BLOCKED")
    ready = status == "READY"

    submission = data.get("submission")
    if not isinstance(submission, dict):
        errors.append("submission 必须是对象")
        submission = {}

    missing_fields = [field for field in SUBMISSION_FIELDS if field not in submission]
    if missing_fields:
        errors.append("submission 缺少字段：" + "、".join(missing_fields))

    internal = data.get("internal")
    if not isinstance(internal, dict):
        errors.append("internal 必须是对象")
        internal = {}

    attachment_strategy = internal.get("附件策略")
    if attachment_strategy not in {"required", "not_required"}:
        errors.append("internal.附件策略 必须是 required 或 not_required")

    for field in READY_REQUIRED_FIELDS:
        if field in {"相关附件", "附件格式标签", "附件内容（总结概括）"} and attachment_strategy == "not_required":
            continue
        if is_empty(submission.get(field)):
            message = f"submission.{field} 为空"
            (errors if ready else warnings).append(message)

    task_type = str(submission.get("任务类型") or "")
    if LEGACY_TIER_RE.search(task_type) or any(label in task_type for label in ("探索型", "流程型", "系统型")):
        errors.append("任务类型不得使用已废止的 L1/L2/L3 或旧层级名称")

    prompt = str(submission.get("题目") or "")
    leakage_terms = [term for term in ("标准答案", "打分checklist", "做题关键步骤", "INTERNAL—禁止写入题面") if term in prompt]
    if leakage_terms:
        message = "题面泄漏内部层内容：" + "、".join(leakage_terms)
        (errors if ready else warnings).append(message)

    if count_items(submission.get("做题关键步骤（必选）")) < 3:
        warnings.append("做题关键步骤少于 3 项，请确认真实工作流是否被充分刻画")
    if count_items(submission.get("打分checklist（必填）")) < 4:
        warnings.append("打分 checklist 少于 4 项，请确认是否足以验收专业交付")

    reality = internal.get("真实场景确认")
    if not isinstance(reality, dict):
        errors.append("internal.真实场景确认 必须是对象")
        reality = {}
    expert_confirmed = reality.get("专家确认") is True
    if ready and not expert_confirmed:
        errors.append("READY 必须有专家真实性确认")
    elif not expert_confirmed:
        warnings.append("专家尚未确认真实场景，状态必须保持 DRAFT 或 BLOCKED")

    for field in REALITY_FIELDS:
        if is_empty(reality.get(field)):
            message = f"真实场景确认.{field} 为空"
            (errors if ready else warnings).append(message)

    work_time = internal.get("预计人类工时")
    if not isinstance(work_time, dict):
        errors.append("internal.预计人类工时 必须是对象")
        work_time = {}
    total = work_time.get("总计")
    try:
        total_hours = float(total)
    except (TypeError, ValueError):
        total_hours = math.nan
        (errors if ready else warnings).append("预计人类工时.总计 必须是数字")
    if not math.isnan(total_hours) and total_hours < 4:
        (errors if ready else warnings).append("预计人类工时低于 4 小时")

    breakdown = work_time.get("拆解")
    if not isinstance(breakdown, list) or not breakdown:
        (errors if ready else warnings).append("预计人类工时缺少非空拆解")
    else:
        breakdown_total = 0.0
        breakdown_valid = True
        for index, item in enumerate(breakdown, 1):
            if not isinstance(item, dict) or is_empty(item.get("环节")):
                warnings.append(f"工时拆解第 {index} 项缺少环节")
            try:
                breakdown_total += float(item.get("小时"))
            except (TypeError, ValueError):
                breakdown_valid = False
                warnings.append(f"工时拆解第 {index} 项小时数无效")
        if breakdown_valid and not math.isnan(total_hours) and abs(breakdown_total - total_hours) > 0.25:
            (errors if ready else warnings).append(
                f"工时拆解合计 {breakdown_total:g} 与总计 {total_hours:g} 不一致"
            )

    attachments = internal.get("附件核验")
    if not isinstance(attachments, list):
        errors.append("internal.附件核验 必须是数组")
        attachments = []

    if attachment_strategy == "required" and not attachments:
        (errors if ready else warnings).append("附件策略为 required，但附件核验为空")
    if attachment_strategy == "not_required" and attachments:
        warnings.append("附件策略为 not_required，但仍存在附件核验记录")

    global_english_whitelist = internal.get("英文材料白名单确认") is True
    for index, item in enumerate(attachments, 1):
        if not isinstance(item, dict):
            errors.append(f"附件核验第 {index} 项必须是对象")
            continue
        for field in ATTACHMENT_FIELDS:
            if is_empty(item.get(field)):
                message = f"附件 {index} 缺少 {field}"
                (errors if ready else warnings).append(message)
        if is_empty(item.get("source_url")) and is_empty(item.get("local_path")):
            (errors if ready else warnings).append(f"附件 {index} 缺少 source_url 或 local_path")
        item_status = item.get("status")
        if item_status not in {"VERIFIED", "UNVERIFIED", "FAILED"}:
            errors.append(f"附件 {index} status 必须是 VERIFIED、UNVERIFIED 或 FAILED")
        if ready and item_status != "VERIFIED":
            errors.append(f"READY 的附件 {index} 未通过 VERIFIED")
        local_path = item.get("local_path")
        if local_path and not SHA256_RE.match(str(item.get("sha256") or "")):
            (errors if ready else warnings).append(f"附件 {index} 有本地文件但缺少有效 SHA-256")
        if is_english(item.get("language")):
            item_whitelist = item.get("english_whitelist_confirmed") is True
            if ready and not (global_english_whitelist and item_whitelist):
                errors.append(f"英文附件 {index} 未获得项目白名单确认")
        if item.get("anonymized") is True and item.get("anonymization_confirmed") is not True:
            (errors if ready else warnings).append(f"附件 {index} 已脱敏但尚未确认核心事实和逻辑未改变")

    gates = internal.get("质量门禁")
    if not isinstance(gates, dict):
        errors.append("internal.质量门禁 必须是对象")
        gates = {}
    for gate in QUALITY_GATES:
        if gates.get(gate) is not True:
            message = f"质量门禁.{gate} 未通过"
            (errors if ready else warnings).append(message)

    pack = internal.get("内部验收底稿")
    if not isinstance(pack, dict):
        errors.append("internal.内部验收底稿 必须是对象")
        pack = {}
    for field in INTERNAL_PACK_FIELDS:
        if is_empty(pack.get(field)):
            message = f"内部验收底稿.{field} 为空"
            (errors if ready else warnings).append(message)

    blockers = internal.get("阻断原因")
    if status == "BLOCKED" and is_empty(blockers):
        errors.append("BLOCKED 必须填写 internal.阻断原因")
    if ready and not is_empty(blockers):
        errors.append("READY 不得保留阻断原因")

    report = {
        "file": str(args.record),
        "status": status,
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "ready_disclaimer": "READY 仅表示可提交人工审核，不代表项目审核通过。" if ready else None,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
