#!/usr/bin/env python3
"""Validate the mandatory six-field vertical-hard-task design card."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


PRIMARY_CATEGORIES = [
    "个人金融与理财投资",
    "商业与市场分析",
    "职业发展与教育规划",
    "企业经营与战略决策",
    "房地产与大宗资产",
    "科技与产品研发",
    "个人生活与重大决策",
    "互联网与平台业务",
    "科技软件与 AI 工作流",
    "游戏与互动内容",
    "品牌市场与电商零售",
    "投资战略、专业服务与企业经营",
    "金融服务与财富投研",
    "教育科研与生命科学",
    "法律、政务与公共服务",
]

REQUIRED_FIELDS = [
    "题目",
    "题目领域一级目录",
    "题目领域二级目录",
    "相关附件",
    "附件来源",
    "后续交互思路",
]

ATTACHMENT_FIELDS = ["附件名称", "格式", "用途", "语言", "核验状态"]
SOURCE_REQUIRED = ["附件名称", "直接链接或本地路径", "核验状态"]
SOURCE_OPTIONAL = ["发布机构", "来源类型", "查询日期"]
FOLLOWUP_FIELDS = ["阶段", "目标", "证据触发", "追问方向", "停止或转向条件"]
SOURCE_STATUSES = {"VERIFIED", "UNVERIFIED", "FAILED"}
SOURCE_TYPES = {"官方", "第一方", "标准组织", "权威机构", "行业机构", "用户提供内部材料", "其他可靠来源"}
WINDOWS_ABS_RE = re.compile(r"^[A-Za-z]:[\\/]")
SEARCH_HOSTS = {
    "www.baidu.com",
    "baidu.com",
    "www.google.com",
    "google.com",
    "www.bing.com",
    "bing.com",
}


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


def valid_date(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        date.fromisoformat(value.strip())
    except ValueError:
        return False
    return True


def location_kind(value: Any) -> tuple[str, str | None]:
    text = str(value or "").strip()
    if text in {"待检索", "待补充", "未获取", "无法联网"}:
        return "pending", "来源位置尚未取得"
    parsed = urlparse(text)
    if parsed.scheme in {"http", "https"} and parsed.netloc:
        host = parsed.netloc.lower().split(":", 1)[0]
        if host in SEARCH_HOSTS and (
            parsed.path.startswith("/search")
            or parsed.path.startswith("/s")
            or "q=" in parsed.query
            or "wd=" in parsed.query
        ):
            return "invalid", "搜索结果页不能作为附件来源"
        if parsed.path in {"", "/"}:
            return "homepage", "来源链接看起来是站点首页，不是直接内容页"
        return "url", None
    if WINDOWS_ABS_RE.match(text) or text.startswith("/"):
        return "path", None
    return "invalid", "必须填写直接 http(s) 链接或绝对本地路径"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("card", type=Path, help="UTF-8 JSON six-field task card")
    parser.add_argument(
        "--require-verified",
        action="store_true",
        help="Fail unless every attachment and source is VERIFIED",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    try:
        data = json.loads(args.card.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(json.dumps({"valid": False, "errors": ["文件不存在"]}, ensure_ascii=False, indent=2))
        return 1
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [f"无法读取 UTF-8 JSON：{exc}"]}, ensure_ascii=False, indent=2))
        return 1

    if not isinstance(data, dict):
        errors.append("根节点必须是 JSON 对象")
        data = {}

    missing = [field for field in REQUIRED_FIELDS if field not in data]
    unexpected = [field for field in data if field not in REQUIRED_FIELDS]
    if missing:
        errors.append("缺少必填维度：" + "、".join(missing))
    if unexpected:
        errors.append("存在非标准顶层维度：" + "、".join(unexpected))

    for field in REQUIRED_FIELDS[:3]:
        if is_empty(data.get(field)):
            errors.append(f"{field} 为空")

    primary = data.get("题目领域一级目录")
    if not is_empty(primary) and primary not in PRIMARY_CATEGORIES:
        errors.append("题目领域一级目录不在九个受控值中")

    attachments = data.get("相关附件")
    if not isinstance(attachments, list) or not attachments:
        errors.append("相关附件必须是非空数组")
        attachments = []

    attachment_names: list[str] = []
    attachment_statuses: dict[str, str] = {}
    for index, item in enumerate(attachments, 1):
        if not isinstance(item, dict):
            errors.append(f"相关附件第 {index} 项必须是对象")
            continue
        for field in ATTACHMENT_FIELDS:
            if is_empty(item.get(field)):
                errors.append(f"相关附件第 {index} 项缺少 {field}")
        name = str(item.get("附件名称") or "").strip()
        if name:
            attachment_names.append(name)
        status = item.get("核验状态")
        if status not in SOURCE_STATUSES:
            errors.append(f"相关附件第 {index} 项核验状态无效")
        elif name:
            attachment_statuses[name] = status
        if args.require_verified and status != "VERIFIED":
            errors.append(f"相关附件 {name or index} 未通过 VERIFIED")
        if is_english(item.get("语言")) and item.get("英文白名单确认") is not True:
            message = f"英文附件 {name or index} 未确认项目白名单"
            (errors if args.require_verified else warnings).append(message)

    if len(attachment_names) != len(set(attachment_names)):
        errors.append("相关附件存在重复附件名称")

    sources = data.get("附件来源")
    if not isinstance(sources, list) or not sources:
        errors.append("附件来源必须是非空数组")
        sources = []

    source_names: list[str] = []
    source_statuses: dict[str, str] = {}
    for index, item in enumerate(sources, 1):
        if not isinstance(item, dict):
            errors.append(f"附件来源第 {index} 项必须是对象")
            continue
        for field in SOURCE_REQUIRED:
            if is_empty(item.get(field)):
                errors.append(f"附件来源第 {index} 项缺少 {field}")
        name = str(item.get("附件名称") or "").strip()
        if name:
            source_names.append(name)
        status = item.get("核验状态")
        if status not in SOURCE_STATUSES:
            errors.append(f"附件来源第 {index} 项核验状态无效")
        elif name:
            source_statuses[name] = status
        if args.require_verified and status != "VERIFIED":
            errors.append(f"附件来源 {name or index} 未通过 VERIFIED")
        query_date = item.get("查询日期")
        if not is_empty(query_date) and not valid_date(query_date):
            errors.append(f"附件来源第 {index} 项查询日期必须是 YYYY-MM-DD")
        src_type = item.get("来源类型")
        if not is_empty(src_type) and src_type not in SOURCE_TYPES:
            errors.append(f"附件来源第 {index} 项来源类型无效")
        kind, issue = location_kind(item.get("直接链接或本地路径"))
        if kind == "invalid":
            errors.append(f"附件来源第 {index} 项：{issue}")
        elif kind == "homepage":
            (errors if args.require_verified or status == "VERIFIED" else warnings).append(
                f"附件来源第 {index} 项：{issue}"
            )
        elif kind == "pending":
            (errors if args.require_verified or status == "VERIFIED" else warnings).append(
                f"附件来源第 {index} 项：{issue}"
            )
        elif kind == "path":
            local_path = Path(str(item.get("直接链接或本地路径") or "").strip())
            if not local_path.is_file():
                (errors if status == "VERIFIED" or args.require_verified else warnings).append(
                    f"附件来源第 {index} 项本地文件不存在"
                )

    if len(source_names) != len(set(source_names)):
        errors.append("附件来源存在重复附件名称")

    attachment_set = set(attachment_names)
    source_set = set(source_names)
    missing_sources = sorted(attachment_set - source_set)
    orphan_sources = sorted(source_set - attachment_set)
    if missing_sources:
        errors.append("以下附件缺少一一对应的来源：" + "、".join(missing_sources))
    if orphan_sources:
        errors.append("以下来源没有对应附件：" + "、".join(orphan_sources))
    for name in sorted(attachment_set & source_set):
        if attachment_statuses.get(name) != source_statuses.get(name):
            errors.append(f"附件 {name} 在相关附件与附件来源中的核验状态不一致")

    followups = data.get("后续交互思路")
    if not isinstance(followups, list) or not followups:
        errors.append("后续交互思路必须是非空数组")
        followups = []
    for index, item in enumerate(followups, 1):
        if not isinstance(item, dict):
            errors.append(f"后续交互思路第 {index} 项必须是对象")
            continue
        for field in FOLLOWUP_FIELDS:
            if is_empty(item.get(field)):
                errors.append(f"后续交互思路第 {index} 项缺少 {field}")

    all_verified = bool(attachments and sources) and all(
        status == "VERIFIED" for status in [*attachment_statuses.values(), *source_statuses.values()]
    )
    report = {
        "file": str(args.card),
        "valid": not errors,
        "ready_eligible": not errors and not warnings and all_verified,
        "primary_category": primary,
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
