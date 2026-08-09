# Prompt and internal evidence pack

## Keep four layers separate

1. **User-facing prompt**: the natural work request shown to the Agent.
2. **Key steps**: the expert's expected work sequence in the submission record.
3. **Scoring checklist**: observable acceptance checks used for evaluation.
4. **Internal evidence pack**: source-backed truths and reasoning controls that must never enter the prompt.

Do not copy one layer into another.

## Minimum sufficient disclosure

**Register rule:** Match the communication form to the real workflow. A colleague chat may be loose; a legal, compliance, technical, or executive assignment may be formal. Authenticity comes from the evidence-to-decision relationship, not compulsory casual phrasing.

Put in the prompt:

- the trigger event and why the work is needed now;
- the real goal and necessary business context;
- decision-critical observations, anomalies, operating figures, and known alternatives;
- the time anchor;
- source and data boundaries;
- the judgment, decision, diagnostic order, or next action required;
- core deliverables and editability requirements;
- the downstream user and intended use when they affect the artifact;
- formulas or definitions that affect correctness or uniqueness;
- missing-data, uncertainty, and prohibited-fabrication behavior;
- hard constraints that a real requester would state.

Keep out of the prompt:

- the standard solution path;
- the expected conclusion or answer;
- complete scoring weights and checklist;
- attachment-by-attachment summaries that replace source reading;
- decorative requirements added only to create apparent complexity;
- choices the Agent should make through professional judgment;
- **ANY instruction telling the model which attachment to use for which purpose** (RAG审核系统 #1 打回原因). This includes "参照附件X""用附件Y的数据""按照附件Z的格式""附件A里有…""Sheet1是…". Describe OUTPUT requirements, not ATTACHMENT prescriptions.

Explicit output formats and section requirements are allowed when the recipient or workflow genuinely needs them. Numbered requirements and exact figures are allowed when they constrain analysis or acceptance. Remove them when they are ornamental, duplicated, or used only to manufacture complexity.

Keep the prompt self-framing but not self-solving:

- Include enough internal facts and decision stakes to understand the problem.
- Keep detailed source evidence, raw records, and extraction work in attachments.
- Do not summarize an attachment so completely that the Agent no longer needs it.

Run a leakage check: if removing a sentence does not change authentic intent, solvability, decision quality, or observable acceptance, move it out of the prompt.

## Internal evidence pack

Label the pack exactly `INTERNAL—禁止写入题面`. Include:

- evidence-to-requirement map;
- required facts with page, sheet, table, section, or URL anchors;
- source precedence and conflict treatment;
- calculations, formulas, units, assumptions, and expected intermediate checks;
- professional judgment points and acceptable alternative reasoning;
- uncertainty, missing information, and conditions requiring caveats;
- expected deliverables and professional conventions;
- critical omissions and severe failure conditions;
- prohibited fabrications.

Do not write a complete model answer. Store only enough ground truth to prove solvability and support later review.

## Default output

State the status and concise reason, then always return:

1. `题目`
2. `题目领域一级目录`
3. `题目领域二级目录`
4. `相关附件`
5. `附件来源`
6. `后续交互思路`

Use the same six fields for a new design and a repair. Do not emit the internal evidence pack or legacy 16-field record unless explicitly requested.

In `后续交互思路`, plan later turns that test evidence use, challenge weak reasoning, resolve uncertainty, or improve the requested artifact. Include an objective, evidence trigger, follow-up direction, and stop or redirect condition. Do not leak the expected conclusion, answer, or scoring checklist.

For `DRAFT`, identify exactly what prevents `READY`, especially unverified attachments or unconfirmed real-work facts. For `BLOCKED`, distinguish a missing user decision from a fundamentally invalid task.
