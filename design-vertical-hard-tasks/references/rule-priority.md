# Rule priority and current policy

## Priority order

Apply rules in this order:

1. The user's or project leader's latest explicit written update.
2. The current live submission template and controlled field values.
3. `垂域高难度题目项目--二期要求 (1).docx` for requirements that have not been superseded.
4. `SZ-垂域高难度题目生产--在线交互式标注指引手册.docx` only for downstream account, trajectory, and submission operations.
5. Examples in either document. Use examples as patterns, never as ground truth.

If a later rule conflicts with an older source, record the override and follow the later rule. Do not silently blend them.

## Current explicit overrides

- Do not use L1/L2/L3 or another hidden difficulty tier.
- Recruit experts to contribute problems from their real professional work.
- Require very strong depth and professionalism for every task.
- Allow the skill to propose topics and search for materials, but keep those tasks `DRAFT` until an expert confirms that the scenario is real.
- Preserve all other applicable second-phase requirements unless a later update changes them.

## Resolved operating policies

- `READY` means ready for human review; it never means project approval.
- Missing or unverified required material forces `DRAFT`.
- A fabricated, unusable, or contradictory core source can force `BLOCKED`.
- English attachments cannot enter `READY` without an explicit project whitelist confirmation.
- An anonymized copy remains `DRAFT` until the user confirms that the core information and logic were preserved.
- Generate an internal evidence pack by default and keep it out of the prompt.
- Use a unified depth gate and credible human-time breakdown. Do not use a numeric “difficulty score.”
- Ask at most three blocking questions at a time. Continue as `DRAFT` when reasonable rather than inventing facts.

## Known legacy ambiguities

- The legacy document heading says there are eight primary categories, while its visible table contains nine distinct primary labels. Use the current live catalog rather than relying on the stated count.
- Legacy examples contain factual and typographical errors. Validate every date, number, source, and logical dependency independently.
- Attachment, format, and prompt-length percentages are batch signals, not per-task hard requirements.
- Per-turn like/dislike feedback and later four-dimension artifact scoring are different workflows; this skill performs neither.

## Version note

Treat this reference as the current local ruleset distilled on 2026-07-23. When a new leader update arrives, update this file first, then review the schema, gates, and validator for affected assumptions.
