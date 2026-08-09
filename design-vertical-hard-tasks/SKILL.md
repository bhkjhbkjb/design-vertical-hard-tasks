---
name: design-vertical-hard-tasks
description: Design or revise Chinese vertical-domain high-difficulty Agent annotation tasks from experts' real professional work problems. Use when Codex needs to turn an expert's authentic business scenario and verified materials into the project's 16-field submission record, create a DRAFT topic through research, repair an AI-written or shallow task, plan a diverse batch, derive hidden key steps and scoring checklists, or decide whether a task is DRAFT, READY, or BLOCKED. Do not use to solve the task, score completed artifacts, or run Doubao interaction trajectories.
---

# Design Vertical Hard Tasks

Design expert-authored, professionally deep tasks. Treat the task as a real work assignment, not as a long prompt-writing exercise.

## Core contract

- Use the latest explicit project or leader update over older manuals and examples.
- Do not use the deprecated L1/L2/L3 scheme anywhere in a new record.
- Require the expert to confirm that the scenario comes from their real work before marking a task `READY`.
- Allow autonomous ideation and web research, but keep the result `DRAFT` until the expert confirms the real scenario.
- Treat `READY` as “ready for human review,” never as project approval.
- Keep the user-facing prompt, key steps, scoring checklist, and internal evidence pack separate.
- Never fabricate, rewrite, or “improve” source materials or source data.

## Load the right references

Read these files before designing or revising a task:

- `references/rule-priority.md` for current overrides and conflicts.
- `references/task-record-schema.md` for the 16 submission fields and internal record.
- `references/depth-and-realism-gates.md` for the unified professional-depth gate.
- `references/prompt-and-internal-pack.md` for prompt disclosure and output structure.

Also read:

- `references/source-verification.md` whenever files, links, public research, downloads, snapshots, or anonymization are involved.
- `references/taxonomy.md` whenever selecting or checking the three-level domain catalog.
- `references/anti-patterns-and-repairs.md` for repair mode, batch mode, or final quality review.

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

### 2. Verify sources and attachments

Map every required source to a task requirement. Prefer original or first-party sources and direct file links. Open and inspect each material before calling it verified.

Preserve public source files and provenance. Keep English materials unapproved by default; require an explicit project whitelist before allowing them in `READY`. Keep anonymized material `DRAFT` until the user confirms that anonymization did not alter core facts or logic.

Use `scripts/build_source_manifest.py` to hash local files when useful. Follow `references/source-verification.md` for the full gate.

### 3. Build the task blueprint before the prompt

Define:

- the real decision or professional outcome;
- necessary evidence and source precedence;
- calculations, units, assumptions, and missing-data rules;
- professional tradeoffs, conflicts, and uncertainty;
- editable and verifiable deliverables;
- expected human workflow and time breakdown;
- critical omissions and prohibited fabrications.

Reject shallow complexity. Prompt length, attachment count, and decorative output requirements do not prove difficulty.

### 4. Write the prompt with minimum sufficient disclosure

Write a natural first-person work request. Include the real goal, necessary context, time anchor, source boundary, core deliverable, decisive calculation definitions, and failure behavior.

Do not expose the standard solution path, expected conclusion, complete scoring checklist, or internal evidence map. Remove any instruction that does not affect authentic intent or verifiable acceptance.

### 5. Produce the submission and internal pack

Populate the 16 fields exactly as defined in `references/task-record-schema.md`. Use a real task archetype such as operating diagnosis, investment research, compliance review, product solution design, or data modeling for `任务类型`; never use a difficulty tier.

Start structured work from `assets/task-record.template.json` so that no submission or internal gate field is omitted.

Create an `INTERNAL—禁止写入题面` evidence pack containing evidence mapping, required facts, calculations, judgment points, uncertainties, expected deliverables, critical omissions, and prohibited fabrications. This pack is not a full answer.

### 6. Run the gates and assign status

Assign exactly one status:

- `DRAFT`: A useful design exists, but expert confirmation, source verification, anonymization confirmation, or another required gate is incomplete.
- `READY`: The expert confirmed the real scenario, all required materials passed verification, the unified quality gates passed, and human work is credibly at least four hours. This means ready for human review only.
- `BLOCKED`: A core source is fabricated or unusable, essential information is unavailable, the scenario is unsafe or non-authentic, or the task cannot be made solvable without changing its purpose.

Never mark a task `READY` merely because it looks polished.

### 7. Validate structured records

When a JSON task record exists, run:

```bash
python scripts/validate_task_record.py path/to/task-record.json
```

Fix all reported errors before using `READY`. Treat warnings as review prompts, not automatic failures.

## Output contract

Return these sections unless the user requests a narrower format:

1. Status and concise reason.
2. Final user-facing prompt.
3. The 16-field submission record.
4. `INTERNAL—禁止写入题面` evidence pack.
5. Quality-gate report, assumptions, and remaining confirmation items.

For `READY`, always state: “READY 仅表示可提交人工审核，不代表项目审核通过。”

## Batch discipline

Vary business role, decision type, domain, attachment type, deliverable, reasoning burden, and time anchor. Evaluate each task independently. Treat project percentages as batch-planning signals rather than single-task requirements.

Block rename-only variants. Changing the company, industry, or numbers while preserving the same reasoning and deliverable skeleton is template duplication.
