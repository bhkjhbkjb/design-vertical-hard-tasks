# Unified depth and realism gates

Do not assign a numeric difficulty score. Require evidence for every gate below.

## 1. Real-work gate

Require an expert-confirmed situation from actual work. Identify the expert's responsibility, real problem, user of the result, time pressure, decision consequence, and normal workflow.

Autonomously generated situations remain `DRAFT` until an expert confirms and corrects them.

## 2. Professional-barrier gate

Require domain knowledge, professional judgment, or experience that a general non-practitioner would not reliably possess. List the judgment points explicitly in the internal pack.

Reject tasks whose answer is mostly public common sense, generic advice, or document summarization.

## 3. Reasoning-depth gate

Require substantive work such as evidence reconciliation, nontrivial calculation, causal diagnosis, assumption testing, uncertainty handling, tradeoff analysis, scenario analysis, or professional risk judgment.

Do not count prompt length, attachment count, repeated subtasks, or formatting chores as depth.

## 4. Solvability gate

Make the task difficult but possible. Ensure that the required facts exist, source precedence is clear, formulas and units are coherent, missing-data behavior is defined, and no hidden critical input is required.

Block logical contradictions and requests to pretend that external execution occurred.

## 5. Deliverable gate

Require a deliverable that would be used in the stated workflow and follows its professional conventions. Prefer editable, inspectable artifacts. Define observable acceptance conditions without dictating the full solution path.

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
