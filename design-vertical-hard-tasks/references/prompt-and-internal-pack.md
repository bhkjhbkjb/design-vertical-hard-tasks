# Prompt and internal evidence pack

## Keep four layers separate

1. **User-facing prompt**: the natural work request shown to the Agent.
2. **Key steps**: the expert's expected work sequence in the submission record.
3. **Scoring checklist**: observable acceptance checks used for evaluation.
4. **Internal evidence pack**: source-backed truths and reasoning controls that must never enter the prompt.

Do not copy one layer into another.

## Minimum sufficient disclosure

Put in the prompt:

- the real goal and necessary business context;
- the time anchor;
- source and data boundaries;
- core deliverables and editability requirements;
- formulas or definitions that affect correctness or uniqueness;
- missing-data, uncertainty, and prohibited-fabrication behavior;
- hard constraints that a real requester would state.

Keep out of the prompt:

- the standard solution path;
- the expected conclusion or answer;
- complete scoring weights and checklist;
- mechanical descriptions of every attachment;
- decorative requirements added only to create apparent complexity;
- choices the Agent should make through professional judgment.

Run a leakage check: if removing a sentence does not change authentic intent, solvability, or observable acceptance, move it out of the prompt.

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

Return:

1. Status with reason.
2. Final prompt.
3. Sixteen-field submission record.
4. Internal evidence pack.
5. Gate report, assumptions, and pending confirmations.

For `DRAFT`, identify exactly what prevents `READY`. For `BLOCKED`, distinguish a missing user decision from a fundamentally invalid task.
