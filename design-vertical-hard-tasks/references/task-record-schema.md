# Task record schema

## Submission record

Populate these 16 fields using the current project template's exact column names:

1. `uid`
2. `题目`
3. `任务类型`
4. `题目领域一级目录`
5. `题目领域二级目录`
6. `题目领域三级目录`
7. `任务概括`
8. `标注专家工作年限（未工作的可以写最高学历）`
9. `人类所需完成时间`
10. `相关附件`
11. `附件格式标签`
12. `附件内容（总结概括）`
13. `产物格式标签`
14. `产物内容（总结概括）`
15. `做题关键步骤（必选）`
16. `打分checklist（必填）`

`uid` may remain empty while designing if assignment happens later. Keep every other applicable field explicit. For a legitimate no-attachment task, write `无` or `不适用` consistently and set the internal attachment strategy to `not_required`.

## Task type

Use the actual work archetype rather than a difficulty level. Prefer a concise label such as:

- 经营诊断
- 投研决策
- 尽职调查
- 合规审查
- 证据综合
- 数据建模
- 方案设计
- 产品研究
- 质量诊断
- 工作流设计

Use a more precise professional label when these do not fit. Never put L1/L2/L3 in this field.

## Internal record

Keep the following data outside the submission prompt:

```json
{
  "status": "DRAFT",
  "submission": {},
  "internal": {
    "规则版本": "expert-real-scenario-2026-07-23",
    "真实场景确认": {
      "专家确认": false,
      "专家实际职责": "",
      "真实问题": "",
      "业务目标": "",
      "交付对象": "",
      "决策后果": "",
      "现实工作流程": [],
      "脱敏说明": ""
    },
    "预计人类工时": {
      "总计": 0,
      "拆解": []
    },
    "附件策略": "required",
    "附件核验": [],
    "英文材料白名单确认": false,
    "质量门禁": {},
    "内部验收底稿": {},
    "假设与待确认项": [],
    "阻断原因": []
  }
}
```

## Status semantics

- `DRAFT`: useful but not ready for submission review.
- `READY`: all hard gates passed; ready for human review only.
- `BLOCKED`: a core issue prevents a valid task without material scope change.

Do not add `APPROVED`; only project reviewers can assign approval.

## Structured validation

Run `scripts/validate_task_record.py` on JSON records. The validator checks deterministic structure and hard flags; it cannot decide whether professional reasoning is genuinely deep. Perform the qualitative gate separately.
