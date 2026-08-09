# Unified depth and realism gates

Do not assign a numeric difficulty score. Require evidence for every gate below.

## 1. Real-work gate

Require an expert-confirmed situation from actual work. Identify the trigger event, expert's responsibility, observed facts, current disagreement or uncertainty, user of the result, time or resource pressure, decision consequence, and normal workflow.

Autonomously generated situations remain `DRAFT` until an expert confirms and corrects them.

**个人生活场景互斥检查（必检 — 不通过则直接打回，不进入后续 gates）：**
- 题目场景是否以个人/家庭生活决策为核心？如果是 → 直接打回。
- 判断标准：决策的**主要受益方**是谁？
  - 提问者本人或家庭 → **个人生活场景，打回**
  - 雇主、客户、专业组织 → **工作场景，继续**
- 常见伪装模式：在个人决策中提及"HR""公司""同事""领导"等职场元素，但核心问题仍是个人选择。例如：
  - "HR让我选年终奖计税方式" → 个人税务优化，不是HR工作
  - "公司有补充医保方案让我选" → 个人消费决策
  - "同事推荐了几支基金" → 个人投资（除非提问者是专业理财顾问）
  - "领导让我考虑一下职业规划" → 个人职业决策
- 合法的工作场景变体（通过）：
  - "客户让我帮他做年终奖税务筹划" → 税务顾问服务客户
  - "公司要给员工统一选补充医保供应商，帮我评估方案" → HR/行政工作
  - "客户咨询基金配置，这是他的资产情况" → 理财顾问工作
  - "要帮团队做明年的薪酬预算，参考一下个税新政的影响" → 管理者工作

## 2. Professional-barrier gate

Require domain knowledge, professional judgment, or experience that a general non-practitioner would not reliably possess. List the judgment points explicitly in the internal pack.

Reject tasks whose answer is mostly public common sense, generic advice, or document summarization.

## 3. Reasoning-depth gate

Require an evidence-to-decision chain: interpret the facts, distinguish competing explanations or options, apply professional constraints, and make a defensible judgment. Substantive work may include evidence reconciliation, nontrivial calculation, causal diagnosis, assumption testing, uncertainty handling, tradeoff analysis, scenario analysis, or professional risk judgment.

Do not count prompt length, attachment count, repeated subtasks, or formatting chores as depth.

**RAG审核系统步数门槛（L2 硬性要求）：**
- **L1**：无硬性步数要求，但推理链必须完整且每步有实质内容。
- **L2**：关键推理步骤必须 ≥ 8 步。低于 8 步将被三审打回。步骤需满足：
  - 每步包含实质推理内容（非流水账或行政操作）
  - 不能把"阅读附件"拆成多步凑数
  - 不能把"打开Excel""新建文件""保存文档"等操作算作推理步骤
  - 步数统计以 `关键步骤` 字段中列举的推理步骤为准

## 4. Solvability gate

Make the task difficult but possible. Ensure that the required facts exist, source precedence is clear, formulas and units are coherent, missing-data behavior is defined, and no hidden critical input is required. When evidence cannot support a final conclusion, require a bounded interim judgment or next verification step rather than false certainty.

Block logical contradictions and requests to pretend that external execution occurred.

## 5. Deliverable gate

Require a deliverable that would be used in the stated workflow and follows its professional conventions. Naming Word, Excel, Markdown, PDF, tables, or sections is appropriate when the recipient needs them. Prefer editable, inspectable artifacts. Define observable acceptance conditions without dictating the full solution path.

## 6. Human-time gate

Require at least four credible hours of expert work. Break the estimate into real stages such as source review, extraction, calculation, judgment, drafting, artifact creation, and QA.

Reject inflated estimates. The sum must match the stated total, and each stage must correspond to necessary work.

## 7. Integrity gate

Require traceable facts, explicit inference, uncertainty labels, and prohibited-fabrication rules. Ensure private or sensitive information is authorized and appropriately handled.

## 8. Non-template gate

Compare the business decision, evidence pattern, reasoning burden, and deliverable structure with nearby tasks. Block rename-only variants and tasks that reuse the same skeleton with different companies or numbers.

## READY requirements

Mark `READY` only when all eight gates pass, the expert confirms reality, all required materials pass verification, English and anonymization exceptions are approved, and no blocking gap remains.

State clearly that READY does not mean project approval.
