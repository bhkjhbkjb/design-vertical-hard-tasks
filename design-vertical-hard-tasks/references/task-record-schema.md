# Task record schema

## Contents

- [Standard six-field output](#standard-six-field-output)
- [Legacy 16-field export](#legacy-16-field-export)
- [Task type](#task-type)
- [Internal record](#internal-record)
- [Status semantics](#status-semantics)
- [Structured validation](#structured-validation)

## Standard six-field output

For every new design and every repair, output these exact fields in this order:

1. `题目`
2. `题目领域一级目录`
3. `题目领域二级目录`
4. `相关附件`
5. `附件来源`
6. `后续交互思路`

Use exactly one controlled primary category from `references/taxonomy.md`. Create the secondary category to fit the real professional workflow.

### Field requirements

- `题目`: the complete user-facing task prompt.
- `题目领域一级目录`: one exact controlled value; no aliases or multiple values.
- `题目领域二级目录`: a concise custom professional capability or workstream.
- `相关附件`: exact material name, format, purpose, and `VERIFIED`/`UNVERIFIED`/`FAILED` status for each item.
- `附件来源`: one-to-one provenance for each attachment, including publisher or owner, source type, direct URL or authorized local path, publication date when available, access date, and verification status.
- `后续交互思路`: planned follow-up turns with objective, evidence trigger, follow-up direction, and stop or redirect condition. Keep it outside the user-facing prompt and do not reveal the expected answer.

### Writing effective follow-up turns

Each follow-up turn must advance the work toward a real decision, not merely request another round of analysis. A weak turn reads like a review checklist ("政策条款逐条筛查 — 从二十条中逐条提取核心要点，标注类型…") — dry, mechanical, field-by-field. A strong turn reads like a reviewer thinking aloud — confirming, cross-checking, questioning, and pushing toward what actually matters.

**Core principle: write like one person reviewing output, not like a project manager assigning tasks.**

**Voice and format.** Each turn is a continuous natural paragraph. Use 确认/核对/追问/检查/验证 as conversational verbs, chaining them together: "确认X是否来自附件Y，核对具体出处页码。追问如果Z不是这种情况，结论会不会反过来。检查是否考虑了A和B的差异——A的数据支撑是什么、B的假设是否成立。"

The internal JSON structure (阶段/目标/证据触发/追问方向/停止或转向条件 fields) must still be present for validation, but the visible output should read as unlabelled paragraphs. In the `目标` field, embed the full natural-language substance.

**Required elements within each turn** — all of these should appear organically, not as labelled sections:

1. **A specific attachment anchor.** Every turn must reference at least one concrete attachment by number and/or data point: "附件3中PE低于30%分位开启定投的结论" / "附件1指南和附件4队列随访数据" / "附件2调查中的收入分层数据（139.3/122.5/112.5）"

2. **A concrete number or parameter from the task.** Not generic thresholds — use real data: "600元/月的金额占月薪5000的比例（12%）" / "沪深300股息率2.48%、中证500股息率1.31%" / "BP价30元/条 vs 实际成交价6-8元/条"

3. **A conditional "如果…则…" or "是否…还是…".** Push beyond the obvious: "如果中途断供半年会怎样" / "如果三条路单独或组合均无法达成8%，诚实告知" / "是否仅基于收益率和波动率做了二选一，还是考虑了搭配定投的可能性"

4. **A stop or redirect condition tied to the current turn's output.** Make it concrete: "如果该数据无法从公开来源获取→标注行业估算并用区间范围替代" / "如果创始人不能接受估值→转向对赌、反稀释、董事会席位可行性排序" / "如果四条杠杆贡献加总低于6%→诚实告知8%一个季度内不可达，转向给老板的Plan B"

5. **In the final turn: push to real action.** Don't end with "撰写完整报告." End with a negotiation script, a roll-out decision with trigger signals, a meeting agenda with specific questions to ask, or a risk matrix with escalation thresholds.

**Minimum 6 rounds, maximum variety.** Do not use the same structure or rhythm for all rounds. A strong set draws from these patterns — and no round should feel like it's from the same template as the previous one:

| Pattern | What it does | Example snippet |
|---------|-------------|-----------------|
| **Data provenance check** | Verify exact source location and completeness | "确认中证500近一年30.04%的收益和21.46%波动率的具体出处页码，检查2022-2025单年度收益数据是否被遗漏" |
| **Assumption stress test** | Break the model's hidden assumptions | "如果均价和销量不是独立假设——加入价格弹性后生态型和性价比型的排序会不会逆转" |
| **Missing element discovery** | Find what the analysis didn't cover but should have | "追问互补型副手配置中'治住他又不翻脸'是否有具体人选画像，副手需要具备哪些能力特质和权力边界" |
| **Edge case exploration** | Push to the boundary | "追问若严格生活方式干预6个月后复查肝酶和B超均无改善但转氨酶仍正常，该情形下的下一步处理建议" |
| **Comparison deepening** | Move from "A vs B" to "under what conditions A beats B" | "是否仅基于收益率做了二选一，还是考虑了70%沪深300+30%中证500的搭配方案" |
| **Action-ready closing** | Turn analysis into executable next steps | "三个先行指标，每个标注'涨到多少算信号、跌到多少算证伪'" |

**Weak vs. strong — tested against real accepted examples:**

| Weak (会被打回的检查清单体) | Strong (通过的拟人化追问体) |
|---|---|
| "政策条款逐条筛查 — 从二十条中逐条提取核心要点，标注类型和受益行业，对照省数据标注关联度，输出关联矩阵" | "确认两个指数的PE/PB和波动率数据是否直接从附件月度概览中提取——追问中证500近一年30.04%的收益的具体出处页码，检查单年度数据是否被遗漏" |
| "将各项费用逐层拆解到可操作的最小单元" | "按产品形态、渠道、客单价、毛利率、体量五个维度逐一打分，确定留下哪一家、踢走哪一家，并给出调整系数" |
| "对三个团队的说法分别做数据验证" | "把销量弹性算出来——BP价30元/条 vs 实际成交价6-8元/条，给出调整后的营收预测" |
| "给出三条可达路径的数值方案" | "创始人80%+ vs 行业22%，给出一个合理的中性增速，测算2028年对应市占率，对标ffit8看是否合理" |
| "1. 确认达人合规管控框架是否适配…2. 针对brief内嵌合规条款…" (带编号的短句链) | 改成自然段落："确认合规框架是否适配联名业务。追问brief内嵌条款中是否补充了功效禁用话术案例——如果没有，审核标准与合规红线清单之间会存在什么缺口。补充达人签约环节的前置约束和违规整改方案。" |

Start from `assets/task-design-card.template.json`. Validate structured cards with `scripts/validate_task_output.py`.

## Legacy 16-field export

Produce this only when the user explicitly requests compatibility with the older submission template:

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

Run `scripts/validate_task_output.py` on the standard six-field JSON card. Add `--require-verified` before marking it `READY`.

Run `scripts/validate_task_record.py` only on a legacy 16-field export. Both validators check deterministic structure and hard flags; neither can decide whether professional reasoning is genuinely deep.
