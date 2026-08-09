# Anti-patterns and repairs

## Contents

- [Authenticity and duplication](#invented-professionalism)
- [Attachment use and evidence sufficiency](#attachment-padding)
- [Depth and source fit](#macro-to-specific-leap)
- [Prompt voice and structure](#ai-tone-templated-prompt)
- [Role and solution disclosure](#case-study-role-overload)
- [Solvability and source integrity](#impossible-or-contradictory-task)
- [Domain and material restrictions](#non-professional-or-unsafe-scenario)
- [Batch planning](#batch-planning)

## Common rejection patterns

### Invented professionalism

**Symptom:** A long fictional role description with no expert-confirmed work problem. Overly detailed role titles ("某国货护肤品牌内容营销负责人") that read like a case-study setup rather than real workplace communication.

**Repair:** Ask for the expert's actual responsibility, recent case, decision consequence, and normal workflow. In the prompt, use minimal role context—a real colleague doesn't restate their full job title when asking for help. Keep `DRAFT` until confirmed.

### Template substitution

**Symptom:** Swap the company, industry, or numbers while retaining the same analysis and deliverable skeleton.

**Repair:** Change the underlying decision, evidence relationships, professional judgment, and artifact use—not merely the nouns.

### Attachment padding

**Symptom:** Add many reports that do not affect the task.

**Repair:** Map every attachment to a requirement and remove any source with no indispensable role.

### Oversummarized attachments

**Symptom:** The prompt excessively summarizes attachment content, effectively doing the AI's analysis work in advance. The task becomes a reading comprehension exercise on the prompt's own summary rather than requiring the AI to extract and interpret from source materials.

**Repair:** Put task-defining facts in the prompt: the current state, key anomaly, known constraint, decision stakes, and any fixed calculation input. Leave detailed evidence, record-level facts, and source interpretation in the attachments. The test is whether the prompt frames the decision without making attachment review unnecessary.

### Attachment firewall violation (RAG审核系统 #1 打回原因)

**Symptom:** The prompt explicitly tells the model which attachment to use for which purpose. Examples: "参照附件1《行业白皮书》""用附件2的财务数据""按照附件3的模板""附件A里有去年的销售数据，附件B里有今年的预算".

**Repair:** Describe OUTPUT requirements (what the deliverable should contain), not ATTACHMENT prescriptions (which file to use for what). The model must discover attachments on its own. Say "我需要一份包含市场规模、竞品分析和财务测算的进入可行性报告" — never "用附件1做市场规模，用附件2做竞品分析，用附件3做财务测算". In `后续交互思路`, referencing attachments by number is acceptable because those turns operate after the model has already seen the materials.

### Internal data starvation (RAG审核系统三审打回)

**Symptom:** The task requires entity-specific internal data (company budgets, proprietary datasets, operational benchmarks, internal portfolio holdings) to produce a non-generic answer, but that data is not provided in attachments. The audit system flags this as delivering only "通用模板" or "方案偏泛化".

**Repair:** Three options: (A) provide the internal data as an attachment; (B) narrow the task scope to only what public/available data can support; (C) position as "初步分析 based on public information" and explicitly state the gap. Never leave the model to fabricate internal data to fill the gap.

### Macro-to-specific leap

**Symptom:** Use generic policy or market reports to make a specific company or personal decision without entity-level facts.

**Repair:** Add verified specific information or narrow the requested conclusion.

### Simple calculation disguised as depth

**Symptom:** One formula, repeated rows, or administrative accumulation is presented as expert work.

**Repair:** Add authentic professional interpretation, conflicting constraints, scenario analysis, risk judgment, and a real downstream decision—or reject the topic.

### Checklist-style follow-up turns

**Symptom:** 后续交互思路 written as short summaries with "—" separators: "政策条款逐条筛查 — 从二十条中逐条提取核心要点，标注类型和受益行业，对照省数据标注关联度，输出关联矩阵。" Reads like a project manager's sub-task list, not like a reviewer thinking aloud.

**Repair:** Rewrite each turn as a continuous natural paragraph. Use 确认/核对/追问/检查 as conversational verbs. Embed specific attachment numbers, concrete data, and conditional "如果X则Y" branches. Read it aloud — if it sounds like a meeting agenda item, it's still checklist-style.

**Contrast:**
- Weak: "1. 确认达人合规管控框架是否适配抗老护肤与二类射频器械联名业务，核查环节完整性"
- Strong: "确认合规框架是否适配联名业务。追问brief内嵌条款中是否补充了功效禁用话术案例——如果没有，审核标准与合规红线清单之间会存在什么缺口。检查达人签约环节的前置约束和违规整改方案——这些环节在现有的达人合作协议里是空白。"

### AI-tone templated prompt

**Symptom:** The prompt has a consultant-style shell but lacks a believable evidence-to-decision chain. Common combinations include:

- a polished fictional role introduction with no actual responsibility or consequence;
- symmetrical sections that enumerate a whole domain rather than resolve one decision;
- precise figures, adjectives, or background facts that do not affect analysis;
- output requirements with no real recipient or operational use;
- numbered steps that disclose the expected reasoning or answer;
- identical sentence rhythm, repeated command verbs, and ornamental transitions across the whole prompt;
- **Stacked parallel questions:** a long sentence joined by semicolons (or Chinese enumeration commas) listing 3+ discrete questions the AI should answer — "我需要先判断几件事：窗口期还剩多少天、投诉书要写哪些内容、证据够不够..." This reads like a meeting agenda, not a real request for help;
- **Background dump:** a rapid-fire sequence of facts (budget, bid prices, procedural history, evidence inventory) stacked without narrative breathing room, like a case brief file-dump rather than a colleague describing their problem;
- **Over-annotated context:** labeling every fact with its role ("这是我需要判断的""这个是附件里的") rather than letting facts speak for themselves.
- **Fake-human address:** using "兄弟""帮我看看""你们一般怎么处理""你之前碰没碰过""麻烦你了" or any greeting that pretends the AI is a human colleague. The assessor and model both know this is an AI interaction. Direct, unaddressed statement of the work problem is always correct. "最近接了个PE客户的项目，需要做X" is good. "兄弟，有个活儿想请你帮看看" is rejected.
- **Paragraph fragmentation:** the prompt body broken into 5+ short paragraphs. Real work requests are dense — 2-3 paragraphs max. Fragmented formatting reads like a structured document, not a real ask.
- **附件来源 over-formatting:** the 附件来源 field presented as a full table with publication date, access date, verification status columns. Keep it minimal: `附件1 — https://...` format only. Internal tracking details stay in internal records.

Punctuation and surface markers can support a diagnosis, but no single em dash, quotation mark, negation structure, short sentence, exact number, first-person role, or numbered list proves AI generation.

**Repair:** Rebuild the prompt around:

1. the event that triggered the work;
2. observed facts that constrain the judgment;
3. competing explanations, options, or risks;
4. a real deadline, resource limit, source boundary, or information gap;
5. the decision or next action required;
6. the recipient and work product.

Choose the authentic register. An internal chat can be loose; a compliance, technical, scientific, legal, or executive assignment can be formal. First person is optional.

**Output-format calibration:** Explicit Word, Excel, Markdown, PDF, tables, filenames, or required sections are valid when the downstream workflow needs them. Remove requirements that are decorative, duplicated, or unrelated to acceptance. Do not expose the solution path merely to fill sections.

**Data calibration:** Exact operational metrics, dates, thresholds, system states, and calculation inputs are valuable. Generic market statistics copied into the setup are suspect unless their source and role in the decision are clear.

Verify: after removing the job title, formatting instructions, and adjectives, can a reviewer still identify the trigger, evidence, conflict, constraint, judgment, and consequence? If not, rewrite.

**RAG审核系统专项 — AI表述加强信号.** The live audit system flags these additional patterns as "AI表述" or "模板化":

- **"戏太多" (over-acting):** Adding dramatic emotional tone, manufactured conflict, or theatrical urgency that doesn't come from the real work. Real professionals under real pressure don't narrate their own drama.
- **背景过冗 (excessively long background):** Spending 3+ paragraphs on context before reaching the actual ask. The system flags: "背景过于冗长，精简表达."
- **对称工整 (symmetrical formatting):** Multiple paragraphs of near-identical length and structure. Real workplace communication is rarely symmetrical.
- **句句标注 (sentence-by-sentence annotation):** Every sentence explicitly states its purpose: "这是背景情况""这是需要解决的问题""这是现有的约束条件". Let facts flow naturally without meta-labels.
- **总结性收尾 (summary-like closing):** Ending with "帮我把这笔账算清楚""把数字摆出来""给我一个明确的结论" — these read as AI-generated wrap-ups, not genuine endings.

**Tone calibration for audit pass:**
- Read the prompt aloud at normal speaking pace. If you stumble on symmetry, it's too templated.
- Count the number of "需要""要求""必须""应该" per paragraph. If consistently 2+ per sentence, it's consultant-speak.
- Check: does any sentence describe what a sentence is about to do? If yes, cut the meta-description.
- The ideal register: a colleague describing their problem at lunch — structured enough to be understood, loose enough to be real.

### Data-starved prompt

**Symptom:** The prompt references attachments as the sole source of decision-critical facts, but the prompt text itself contains zero specific data points—no numbers, no named criteria, no quantified findings. The question becomes unanswerable without opening every attachment, and the prompt lacks the minimal self-sufficiency a real work request would have.

**Repair:** Include the task-defining current state, anomaly, threshold, or known finding in the prompt. Attachments should provide the evidence needed to verify, quantify, and interpret—not merely repeat the prompt, and not hide the existence of the problem.

### Case-study role overload

**Symptom:** The prompt enumerates demographic, biographical, organizational, or personality details like a case-study fact sheet, but those details do not alter the applicable rule, professional perspective, evidence, constraint, or recommendation.

**Repair:** Keep role and context that change accountability, source access, legal position, target audience, or decision criteria. Remove details that do not change the answer. A concise “我负责订单模块” can be more authentic and useful than either no role or a long title.

### Over-specified solution

**Repair:** Retain correctness-critical definitions and deliverables; move the solution path and detailed checklist to internal layers.

### Impossible or contradictory task

**Symptom:** Required facts are absent, units conflict, dates do not align, or the requested deliverable depends on inaccessible private data.

**Repair:** Correct the inputs, define missing-data behavior, narrow the claim, or mark `BLOCKED`.

### AI-generated or altered sources

**Symptom:** Inventing, modifying, or "improving" source materials instead of using real, verified data. Numbers or facts that cannot be traced back to an actual published source. "Cleaned" data fabricated to make the task look clean.

**Repair:** All attachment data must come from real, publicly searchable, verifiable sources. If a number cannot be confirmed, mark it UNVERIFIED and state the limitation. Never adjust data to make a task "cleaner" or "more balanced." Real data is messy — that's the point. Do not upgrade to `READY` until verified.

### Library copying

**Symptom:** Sampling from `passed-prompt-library.md` and replicating the sampled prompt's domain, structure, industry, role, key phrases, or clause patterns into the new task.

**Repair:** When sampling, study the *technique* — how the opening hooks, how the conflict surfaces, how the closing lands — and apply that technique to a completely different domain with completely different facts. If a library entry opens with "我在一家中型投行消费组做研究，入行第3年," use the role+tenure hooking technique for a different industry, not the same one. The test: can a reviewer identify which library entries were sampled? If yes, you copied. Vary the domains you sample from across tasks.

### Information insufficiency

**Symptom:** The 做题关键步骤 list mentions data or materials that are not provided in the attachments. The task requires the AI to reference specific documents, datasets, or information that do not exist in the prompt or attachments. If a normal human would be unable to complete the task with the provided information, the task is unsolvable.

**Repair:** For every item in 做题关键步骤 that references specific data (contracts, detailed records, raw datasets, app information, etc.), verify that the corresponding material is included in the attachments. Remove any step that requires inaccessible information, or add the missing attachment. If critical information is missing and cannot be provided, mark `BLOCKED`.

### Non-professional or unsafe scenario

**Symptom:** Primarily manual/blue-collar accumulation, academic puzzle difficulty, unlawful evasion, political provocation, or unsafe activity. Also includes **labor arbitration cases** (劳动仲裁), which are explicitly rejected per 质检 guidelines.

**Repair:** Re-anchor in legitimate professional knowledge work or reject it. Labor arbitration scenarios: directly discard.

### Personal life / Non-work scenario (RAG审核系统高频打回)

**Symptom:** The scenario is framed as a personal life decision rather than professional work. Core examples: personal tax optimization, personal investment choices, consumer purchasing decisions, family financial planning, personal health management, housing decisions, personal insurance selection, children's education planning, personal career decisions. The classic tell: a workplace element is mentioned as window dressing ("HR sent a notice""同事推荐了""公司有这个政策"), but the core decision benefits the individual question-asker, not an employer, client, or professional organization.

**Concrete rejection examples:**
- "HR让我在个税APP上选年终奖计税方式，单独还是合并" → 这是个人税务优化，不是HR工作
- "同事推荐了几支基金，帮我分析一下哪个好" → 除非提问者是专业理财顾问服务客户，否则是个人投资
- "公司有补充医疗保险方案让我选，帮我算算哪个划算" → 个人消费决策
- "孩子要上学了，帮我比较一下学区房和私立学校的成本" → 个人生活规划
- "年底了想换工作，帮我分析一下三个offer" → 个人职业决策

**Repair:** Directly reject — do not attempt to "fix" by adding more workplace window dressing. The test: is the primary beneficiary of the decision an employer, client, or professional organization? If the answer is the individual posing the question → reject. If the answer involves professional accountability to others → proceed.

**Reject outright checklist:**
- [ ] 个人税务优化（年终奖计税、个税筹划、专项附加扣除选择）
- [ ] 个人投资决策（基金/股票/理财产品选择）
- [ ] 个人住房决策（买房/租房/装修选择）
- [ ] 个人保险配置（重疾险/医疗险/车险选择）
- [ ] 个人医疗健康管理（体检方案/治疗方案/用药选择）
- [ ] 个人消费决策（购车/电子产品/大宗消费选择）
- [ ] 子女教育规划（学校选择/培训班选择/留学规划）
- [ ] 个人职业决策（offer选择/跳槽评估/职业转型）
- [ ] 家庭财务规划（储蓄/预算/债务管理）

Contrast with legitimate work scenarios:
- ✅ "客户让我帮他做年终奖税务筹划方案" → 税务顾问的工作
- ✅ "公司的补充医疗保险供应商竞标，帮我评估三家的方案" → HR/行政的工作
- ✅ "客户咨询基金配置方案，这是他的资产情况和风险测评" → 理财顾问的工作
- ✅ "员工对新个税政策有疑问，帮我做一个内部培训PPT" → HR培训的工作

### Stale or English material without approval

**Symptom:** Time-sensitive evidence is outdated, or English attachments are used without a project exception.

**Repair:** Verify the time anchor and current source. Keep English material `DRAFT` until explicitly whitelisted.

## Batch planning

For more than three requested tasks, first produce a matrix covering:

- expert role and business decision;
- controlled primary category and custom secondary category;
- task archetype;
- evidence pattern and attachment formats;
- core reasoning burden;
- deliverable and downstream user;
- time anchor and decision consequence.

Treat percentages as portfolio warnings. Confirm the matrix before producing full tasks. Verify and assign status to each task independently.
