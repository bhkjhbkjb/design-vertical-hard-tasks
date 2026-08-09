---
name: design-vertical-hard-tasks
description: Design or revise Chinese vertical-domain high-difficulty Agent annotation tasks from experts' real professional work problems, with mandatory active evidence research, a controlled nine-value primary taxonomy, and a six-field output covering 题目、题目领域一级目录、题目领域二级目录、相关附件、附件来源、后续交互思路. Use when Codex needs to create, repair, deepen, classify, source, or batch-plan these tasks, or decide whether a design is DRAFT, READY, or BLOCKED. Do not use to solve the task or score completed artifacts.
---

# Design Vertical Hard Tasks

Design expert-authored, professionally deep tasks. Treat the task as a real work assignment, not as a long prompt-writing exercise.

## Core contract

- Use the latest explicit project or leader update over older manuals and examples.
- Do not use the deprecated L1/L2/L3 scheme anywhere in a new record.
- Use exactly one of the fifteen controlled primary categories in `references/taxonomy.md`; define the secondary category to fit the real workflow.
- **When the user provides only the primary category, discuss the secondary category together — do not assign it unilaterally.**
- Require the expert to confirm that the scenario comes from their real work before marking a task `READY`.
- Actively search, open, and verify real supporting materials for every design or repair. Do not wait for the user to request research.
- **All data in attachments must come from real, verifiable sources. Never fabricate numbers, facts, or source materials. If a source cannot be verified, mark it UNVERIFIED and state the limitation.**
- Keep autonomously proposed scenarios `DRAFT` until the expert confirms the real scenario.
- Treat `READY` as "ready for human review," never as project approval.
- Keep the user-facing prompt, key steps, scoring checklist, and internal evidence pack separate.
- Never fabricate, rewrite, or "improve" source materials or source data.
- **Save all attachment files to `E:\瞬知\YYYY-MM-DD\<序号-任务名>\` with descriptive filenames (`附件1_简要内容描述.pdf`). Never put attachments on C drive. Attachment format MUST be PDF, Word (.docx), or Excel (.xlsx) only. Markdown (.md), TXT, JSON, HTML, and all other formats are forbidden for attachments. If source content is in a non-approved format, convert it to PDF before saving.**
- **When sampling from `passed-prompt-library.md`: study openings, rhythms, and closing styles for inspiration. Never copy domain, structure, or noun phrases. Reference ≠ replication.**
- **场景互斥检查（必检）：** 每个题目必须通过"白领工作场景"检验。核心判断标准：决策的主要受益方是谁？如果是提问者本人或家庭 → 个人生活场景，直接打回。如果是雇主、客户、专业组织 → 工作场景，继续。常见伪装：在个人决策中提及"HR""公司""同事"等职场元素，但核心问题仍是个人选择（如年终奖计税、个人投资、房贷选择、子女教育规划、个人保险配置）→ 同样属于个人生活场景，打回。拒绝一切形式的个人生活/投资/消费决策伪装成工作场景。

## Expert Agent Integration — 从真实从业者视角出题

设计题目时，孵化（spawn）一个领域专家 Agent 来生成题目场景。Agent 扮演该领域的真实从业者，从自己的工作经历中提取问题——而非让 skill 凭空"想象"一个专家会问什么。

### 何时孵化专家 Agent

| 场景 | 操作 |
|---|---|
| 用户指定一级目录，开始 design 模式 | 孵化领域专家 Agent 生成真实工作场景 |
| 用户提供了草稿场景 | 孵化领域专家 Agent 验证/修复真实性 |
| batch-plan 模式 | 孵化专家 Agent(s) 做多样性校验 |
| repair 模式 | 孵化领域专家 Agent 交叉检查领域准确性 |

### 领域 → Agent 角色映射

| 一级目录典型值 | Agent 角色 | 出题指令要点 |
|---|---|---|
| 投研与金融研判 | Senior Financial Analyst | 描述你上季度做过的一个真实分析——有什么数据、决策挂在这上头、什么可能出错 |
| 法律与合规 | Legal & Compliance Expert | 描述一个真实的案件/客户事项，其中模糊的法规创造了真正的专业判断压力 |
| 医疗与教育（医疗类） | Clinical Physician / Researcher | 描述一个真实的临床证据评估案例，指南不清晰、治疗决策悬而未决 |
| 科技软件与 AI 工作流 | Senior DevOps / SRE Engineer | 描述一个真实的系统事故或架构决策，多种故障模式相互竞争 |
| 互联网与增长运营 | Growth Analytics Lead | 描述一个真实的 campaign/feature 分析，指标与直觉相互矛盾 |
| 品牌与市场 | Brand Strategy Director | 描述一个真实的品牌决策，量化信号与质性信号指向相反方向 |
| 战略与经营 | Management Consultant | 描述一个真实的客户项目，利益相关方激励不一致、建议具有政治敏感性 |
| 数据与 AI | Data Science Lead | 描述一个真实的建模问题，数据泄露或评估指标选择威胁到生产有效性 |
| 工程/产品开发 | Senior Software Architect | 描述一个真实的架构决策，可扩展性、成本和时间的权衡真实痛苦 |
| 通用/其他 | Domain Practitioner (5+年经验) | 描述你职业生涯中遇到的最棘手的一个专业决策——不是教科书案例，是真实发生的 |

### Agent 孵化模板

使用 Agent 工具孵化领域专家时，使用以下模板：

```
You are acting as a [ROLE] with [X]+ years of experience in [INDUSTRY/DOMAIN].

Your task: Help design a professionally authentic question for an AI annotation task.
The question MUST come from YOUR real work experience — not a textbook, not a case study, not a hypothetical.

HARD REQUIREMENTS:
1. Describe a real professional problem YOU have actually faced at work.
2. The scenario MUST be a WHITE-COLLAR professional work scenario — the primary 
   beneficiary of the decision must be an employer, client, or professional 
   organization, NOT the question-asker personally or their family.
3. REJECT: personal tax optimization, personal investment, personal housing, 
   personal insurance, personal healthcare, consumer purchases, family financial planning.
4. The problem must require domain-specific professional judgment that a general 
   non-practitioner could NOT reliably perform.
5. Use natural, spoken Chinese — not consultant-style, not symmetrical paragraphs, 
   not AI-formatted. Write like a colleague describing a problem at lunch.

DOMAIN: [一级目录] / [二级目录]
TASK DIFFICULTY: [L1/L2]
CORE DECISION TYPE: [分析/判断/设计/审计/诊断/规划]

OUTPUT:
1. The question scenario in the asker's natural voice (200-500字)
2. Professional judgment points this task tests
3. Required domain knowledge a generalist would lack
4. Typical attachment types needed for this scenario
5. Expected reasoning chain (>=8 steps for L2)

AUTHENTICITY CHECK: Would a real [ROLE] actually ask this question in their 
work chat or email? If it reads like a polished case study, start over.
```

### 专家 Agent 输出处理

Agent 返回的场景不能直接作为最终题目。处理流程：
1. 将 Agent 输出的场景作为"专家确认过的真实工作锚点"
2. 在此基础上搜索真实附件材料（Workflow Step 2）
3. 按照题目写作规范重写（Workflow Step 3-4），保留 Agent 提供的专业判断点
4. 状态标记为 `DRAFT`，等待进一步验证

## Load the right references

Read these files before designing or revising a task:

- `references/rule-priority.md` for current overrides and conflicts.
- `references/task-record-schema.md` for the mandatory six-field output and optional legacy export.
- `references/depth-and-realism-gates.md` for the unified professional-depth gate.
- `references/prompt-and-internal-pack.md` for prompt disclosure and output structure.
- `references/positive-sample-patterns.md` before writing or diagnosing a prompt; it contains calibrated lessons from previously accepted tasks.
- `references/passed-prompt-library.md` immediately before writing or rewriting every prompt — randomly sample 2-3 entries for stylistic variety.
- `references/taxonomy.md` before assigning the primary or secondary category.
- `references/source-verification.md` before researching or listing attachments.
- `references/external-corpus.md` for the optional external **Moment Research** corpus — sample it before designing to enrich real-scenario realism (reference only, never copy; do not treat it as an authoritative source).

Also read:

- `references/anti-patterns-and-repairs.md` for repair mode, batch mode, final quality review, and during prompt writing (especially the AI-tone rejection pattern).
- `references/audit-compliance-guide.md` for the RAG审核系统合规指南 — mandatory reading before every submission. Contains audit pass/fail criteria reverse-engineered from the live audit system's 880-record knowledge base. This guide takes precedence over other references when they conflict.

## Select a mode

- `design`: Turn an expert-confirmed real problem into one complete task.
- `repair`: Diagnose and rewrite an existing draft while preserving its valid facts and intent.
- `ideate`: Propose candidate directions or search for possible materials. Always output `DRAFT`.
- `batch-plan`: Build a diversity plan first. Do not mass-produce long prompts before the plan is accepted.

Default to one deeply designed task. For more than three requested tasks, produce a batch plan first and then work task by task.

## Workflow

### 1. Establish the real-work anchor

Capture the expert's actual role, real problem, business goal, deliverable recipient, decision consequence, time anchor, normal human workflow, professional judgment points, and anonymization boundary.

Ask no more than three blocking questions at a time. Ask only when the answer changes realism, source selection, task shape, or core deliverable. If the user cannot answer, continue as `DRAFT` and list the gaps; do not invent reality.

**If the user specifies only the primary category,** discuss the secondary category together. Do not assign it unilaterally. Ask: what specific sub-domain, industry, or decision type does this scenario belong to? Confirm before locking the value.

#### 1a. Spawn domain expert Agent (design mode default)

When the user initiates `design` mode with a known primary category, spawn a domain expert Agent BEFORE drafting the scenario. This replaces the skill "imagining" a professional scenario — the Agent IS the professional.

**Procedure:**
1. Match the primary category to an Agent role using the mapping table in the "Expert Agent Integration" section above.
2. Spawn an Agent using the Agent tool with `subagent_type="general-purpose"`, passing the Agent 孵化模板 from the Expert Agent Integration section.
3. The Agent returns: question scenario + professional judgment points + domain knowledge requirements + attachment types + reasoning chain.
4. Use the Agent's output as the "expert-confirmed work anchor" — it replaces the skill's own scenario brainstorming.
5. Run the 场景互斥检查 against the Agent's scenario: is this a white-collar work scenario? If the Agent generated a personal-life scenario, reject it and re-spawn with reinforced instructions.

**Skip the expert Agent only when:**
- The user explicitly provides a fully formed, expert-confirmed scenario.
- The mode is `repair` and the existing scenario is already expert-confirmed.
- The user requests a quick draft without expert validation (then keep it `DRAFT`).

**For batch-plan mode:** Spawn one expert Agent per distinct domain category to validate scenario diversity.

### 2. Actively search and verify sources

Use the available web search or browser tool before drafting the final six fields. This applies to `design`, `ideate`, and `repair`; for repair, re-open existing links and search for missing, stale, or stronger evidence.

Do not satisfy this step by saying what should be searched. Execute the search:

1. Search the authoritative rule, mechanism, specification, or first-party material.
2. Search scenario-specific facts, data, cases, or comparable practice needed by the task.
3. Open candidate results; never cite search snippets or result pages.
4. Inspect the relevant section, table, sheet, or page and map it to a task requirement.
5. Prefer direct files or direct content pages; preserve or hash files when lawful and practical.
6. Keep only sources that materially affect solvability, judgment, or verification.

Normally open at least two candidate sources and retain the smallest sufficient evidence set. Include at least one official, first-party, standard-setting, or otherwise primary source whenever the task relies on public facts. Do not add filler solely to meet a count.

If the user explicitly forbids web research, browsing is unavailable, or confidentiality makes public search unsafe, do not invent sources. Keep the task `DRAFT` and state the limitation in `附件来源`. User-provided internal materials still require item-by-item inspection; public materials must not substitute for missing internal facts.

Preserve provenance. Keep English materials unapproved by default; require an explicit project whitelist before allowing them in `READY`. Keep anonymized material `DRAFT` until the user confirms that anonymization did not alter core facts or logic. Use `scripts/build_source_manifest.py` to hash local files when useful.

### 3. Build the task blueprint before the prompt

Define:

- the trigger event, observed facts, current disagreement, and decision pressure;
- the real decision or professional outcome;
- necessary evidence and source precedence;
- calculations, units, assumptions, and missing-data rules;
- professional tradeoffs, conflicts, and uncertainty;
- editable and verifiable deliverables;
- the downstream user and the action the deliverable will support;
- expected human workflow and time breakdown;
- critical omissions and prohibited fabrications.

Reject shallow complexity. Prompt length, attachment count, and decorative output requirements do not prove difficulty.

### 4. Write the prompt with minimum sufficient disclosure

**MANDATORY PRE-STEP: Before writing any prompt, open `references/passed-prompt-library.md` and sample 3-5 accepted prompts from diverse domains.** This is the single highest-priority rule in the entire workflow. Study openings, rhythms, connector patterns, and closings as stylistic reference — never copy domains, structures, or noun phrases. The library teaches *how* to write, not *what* to write. Vary the sampled combination each time; never reuse the same set of opening/closing techniques two consecutive tasks.

**Opening styles.** Choose freely among three:

| Style | Cue | When to use |
|-------|-----|-------------|
| 直接任务 | "最近接了个PE客户的项目，他们想投国内企业级低代码赛道…" | Default. Direct task description, no greeting. |
| 场景叙事 | "今天来了一位新客户王先生，今年28岁…" | Client service, consultation |
| 角色自述 | "我是制造业民企的生产副总，之前…" | Business decision, org management |

**CRITICAL — No fake-human address.** Do NOT use "兄弟""帮我看看""你们一般怎么处理""你之前碰没碰过""麻烦你了" or any greeting that pretends the AI is a human colleague. The assessor and the model both know this is an AI interaction. Direct statement of the work problem is always correct. "最近接了个项目，客户要做X，需要Y" is good. "兄弟，有个活儿想请你帮看看" is rejected.

**Minimal paragraph breaks.** Keep the prompt body compact — maximum 2-3 paragraphs. Real work requests are dense, not airy. Multiple short paragraphs read like a structured document, not a real ask.

**Number discipline.** Anchoring numbers that frame the problem are allowed in the prompt (direction, not precision): "营收下滑""渠道占比从八成掉到七成""现金流明显收缩". Never copy exact attachment figures into the prompt. The precise data lives in the attachments. The prompt provides the question; the attachments provide the evidence.

**Source quality over source domain.** Search broadly for high-quality materials from anywhere on the web. The standard is not ".gov.cn vs .com" — it is: is the data first-hand, is the source traceable, can it be independently verified. This includes government documents (国务院, 财政部, 药监局), exchange filings (巨潮资讯网, 上交所, 深交所, SEC), industry association reports, academic papers, official company disclosures, and authoritative first-hand journalism. Media reprints may supplement but prefer original sources when available.

**Workflow before writing:**
1. Search broadly for real attachments from any high-quality source on the web
2. Read the data — stop when you find a concrete contradiction, anomaly, or decision point
3. Write the prompt around that tension
4. Self-audit: read aloud. Does it sound like a real work request (not a friendly chat)? Are there any fake-human greetings ("兄弟""帮我看看""你们一般怎么处理")? Is attachment data leaking through? Are paragraphs compact (2-3 max) rather than fragmented? Are the follow-up turns written as natural paragraphs (not checklist summaries)? Do they vary in pattern?

Write in the register that fits the real workflow: an internal chat, technical brief, formal assignment, or professional request. First person is useful when authentic but is not mandatory.

Build an evidence-to-decision chain:

- state what happened and why the work is needed now;
- provide decision-critical observations, inputs, and constraints;
- expose the real competing explanations, options, or risks;
- ask for a judgment, decision, diagnostic order, or next action at the level the evidence supports;
- name the downstream user and work product when they are operationally real;
- define uncertainty, missing-data, source, and fabrication boundaries;
- exclude adjacent work that would dilute the core decision.

It is legitimate to specify Word, Excel, Markdown, PDF, a comparison table, or required sections when the actual recipient or workflow needs them. It is also legitimate to use exact operational figures and numbered requirements. Reject them only when they are decorative, artificially exhaustive, or disclose the solution.

Keep task-defining facts in the prompt: current state, anomalies, thresholds, dates, constraints, and known alternatives. Leave source extraction, detailed evidence, and professional interpretation to the attachments and the Agent. The prompt should frame the decision without reproducing the attachments.

**CRITICAL — Attachment firewall.** The #1 audit rejection reason is exposing attachment content or prescribing attachment use in the prompt. Follow these rules absolutely:

- **Forbidden:** Any phrase that tells the model which attachment to use for which purpose. This includes "参照附件X""用附件Y的数据计算""按照附件Z的格式""附件A里有…""Sheet1是…" and any variant.
- **Allowed:** Describe what the OUTPUT should contain (modules, analyses, sections). Say "我需要一份包含市场规模、竞品格局和财务测算三个模块的进入可行性报告" — do NOT say "用附件1做市场规模分析，用附件2做竞品分析，用附件3做财务测算".
- **Allowed:** Mention that materials/data exist without specifying their content. Say "我整理了去年的销售数据和今年的预算" — do NOT say "附件A是去年的销售数据包含各区域的营收和毛利".
- **Allowed:** Reference attachments by number in `后续交互思路` — the follow-up turns operate after the model has already seen the attachments.
- **Test:** Read the prompt aloud. Would a colleague who hasn't seen the attachments understand what needs to be produced? If yes → good. Does the prompt read like it's narrating what's inside the attachments? If yes → rewrite.

Do not treat one punctuation mark, transition, exact number, role introduction, or numbered list as proof of AI writing. Rewrite when several signals combine with generic facts, symmetrical consultant-style structure, ornamental requirements, or a pre-solved answer. See `references/positive-sample-patterns.md` and `references/anti-patterns-and-repairs.md`.

Do not expose the standard solution path, expected conclusion, complete scoring checklist, or internal evidence map. If the available evidence cannot support a final business conclusion, require the strongest defensible interim judgment and the next evidence or experiment—not false certainty.

Verify that every key step has the information or attachment needed for a human to perform it. Remove inaccessible dependencies or keep the task `DRAFT`/`BLOCKED`.

### 5. Produce the six-field task card and internal pack

For every new task and every repair, output these six fields in this exact order:

1. `题目`
2. `题目领域一级目录`
3. `题目领域二级目录`
4. `相关附件`
5. `附件来源`
6. `后续交互思路`

Start structured work from `assets/task-design-card.template.json`. In `相关附件`, list exact material names, formats, and purposes. In `附件来源`, keep it minimal: **attachment number + URL only** (e.g., `附件1 — https://...`). Publication dates, access dates, and verification details are for internal tracking only — do not include them in the user-facing output.

**Output directly in conversation.** Present the six-field task card directly in the chat — do not save it to a file and only reference it. The user should see the full task card inline.

**Voice for 后续交互思路.** Never write checklist-style short-hand summaries ("政策条款逐条筛查 — 从二十条中逐条提取…"). Write each turn as a continuous natural paragraph — confirm, cross-check, question, push to edge cases. Use 确认/核对/追问/检查/验证 as conversational verbs. Embed specific attachment numbers, concrete task data points, and conditional "如果…则…" branches directly into the flow. A good turn reads like a reviewer thinking aloud, not a project manager assigning sub-tasks. Minimum 6 rounds with maximum variety across patterns. Every turn must carry a concrete quantitative anchor, force a choice or decision, and push toward a real action. See `references/task-record-schema.md` → "Writing effective follow-up turns" for the full pattern with worked examples and weak-vs-strong contrast.

Create an `INTERNAL—禁止写入题面` evidence pack for reasoning control, but do not emit it by default. Produce the legacy 16-field submission record only when the user explicitly requests submission/export compatibility.

### 6. Run the gates and assign status

Assign exactly one status:

- `DRAFT`: A useful design exists, but expert confirmation, source verification, anonymization confirmation, or another required gate is incomplete.
- `READY`: The expert confirmed the real scenario, all required materials passed verification, the unified quality gates passed, and human work is credibly at least four hours. This means ready for human review only.
- `BLOCKED`: A core source is fabricated or unusable, essential information is unavailable, the scenario is unsafe or non-authentic, or the task cannot be made solvable without changing its purpose.

Never mark a task `READY` merely because it looks polished.

### 7. Pass the audit compliance gate

**This is a mandatory pre-submission step. Do not skip it for any task that will be submitted to the RAG审核系统.**

Before marking any task `READY`, run the audit compliance checklist from `references/audit-compliance-guide.md`. The audit system uses BM25 retrieval of similar cases + LLM structured judgment. It will reject tasks for:

1. **附件暴露**（最高频打回原因）：题目中明确指定"参照附件X""用附件Y""按照附件Z"。修复：题目描述产物要求，不描述附件用途；说"我整理了一些材料你看看"而不说"附件A里有XX数据用XX方法分析"。
2. **AI表述/模板化**（次高频）：对称段落、背景堆砌、叠问句式、顾问腔、过度标注意图。修复：读出声来检查；结构可以略乱；事实自己说话不标注角色。
3. **内部数据缺失**（L2三审打回）：题目需要某实体的内部数据但未提供。修复：要么把缺失数据做成附件，要么缩小任务范围，要么标注为"基于公开信息的初步分析"。
4. **步骤不足**（L2硬门槛）：L2 推理步骤必须 ≥ 8 步，L1 无硬性要求但推理链须完整。
5. **模板重复**：题目结构与已有题目雷同。修复：变化决策类型、叙事角度、产物类型。

The full checklist is in `references/audit-compliance-guide.md`. Every item must pass before `READY`. If any item fails, fix the task or keep it `DRAFT` with the failure noted.

### 8. Validate structured output

When a six-field JSON task card exists, run:

```bash
python scripts/validate_task_output.py path/to/task-design-card.json
```

Before using `READY`, run with `--require-verified`. Fix all errors:

```bash
python scripts/validate_task_output.py path/to/task-design-card.json --require-verified
```

Use `scripts/validate_task_record.py` only for an explicitly requested legacy 16-field export.

## Output contract

State the status and concise reason, then always return the six required fields in the exact order defined above. Do this for both new designs and repairs. Do not replace them with a critique, a 16-field table, or an internal evidence pack.

For `READY`, always state: “READY 仅表示可提交人工审核，不代表项目审核通过。”

## Batch discipline

Vary business role, decision type, primary and secondary category, attachment type, deliverable, reasoning burden, and time anchor. Evaluate, research, and output all six fields for each task independently. Treat project percentages as batch-planning signals rather than single-task requirements.

Block rename-only variants. Changing the company, industry, or numbers while preserving the same reasoning and deliverable skeleton is template duplication.
