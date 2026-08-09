# Lessons from accepted task prompts

Use these lessons as calibration, not as a template or authority. They were distilled from 66 previously accepted prompts across compliance, data, engineering, finance, legal, operations, and scientific work. A historical pass does not override current leader rules, source controls, safety boundaries, the expert-reality requirement, or the four-hour depth gate.

## What consistently carries the task

### 1. A concrete trigger creates real work

Start from an event that made work necessary: an upcoming review, declining metric, failed migration, production anomaly, customer complaint, release deadline, disputed interpretation, or investment decision.

Avoid generic “research this topic” framing. State why someone needs an answer now and what happens if the direction is wrong.

### 2. Decision-critical facts replace decorative backstory

Include facts that change the analysis:

- current and prior metrics;
- observed anomalies and their concentration;
- system states and allowed transitions;
- dates, budgets, staffing, deadlines, or thresholds;
- known source limitations;
- candidate explanations or options already raised by the team.

Exact figures are a strength when they are observed operational facts, calculation inputs, thresholds, or evidence. They are a weakness when copied from generic research merely to make the prompt look authoritative.

### 3. Professional depth comes from competing explanations

Good prompts rarely ask only for a summary. They force the Agent to distinguish alternatives, for example:

- requirement gap versus local implementation judgment;
- data quality versus model drift versus business change;
- several technical fixes under a release constraint;
- real signal versus measurement or labeling error;
- short-term cash outcome versus long-term return;
- continue, repair, limit, postpone, or collect more evidence.

Require the Agent to explain what evidence supports or weakens each alternative and to recommend at the level the evidence allows.

### 4. Constraints make judgment testable

Use authentic constraints such as fixed deadlines, limited staff, capped experiments, locked campaign dates, unavailable logs, incomplete interviews, no retraining, no new hardware, or a named source boundary.

If a final conclusion is not supportable, the professional task may be to choose the next metric, experiment, review sample, or mitigation. Do not force certainty beyond the evidence.

### 5. Scope exclusions protect the core decision

Accepted prompts often state what not to do: no full remediation program, no procurement, no unrelated controls, no third route, no fabricated error rate, or no claim beyond the available records.

Use exclusions to keep the deliverable focused. Do not add them as a long generic disclaimer list.

### 6. The work product has a real consumer

Tie the artifact to a recipient and action: leadership discussion, technical review, regulator response, customer communication, release approval, migration cutover, model review, or investment committee decision.

It is valid to specify Word, Excel, Markdown, PDF, a one-page comparison, required columns, or a named file when that is how the work will be used. Format requirements become artificial only when they do not affect use or acceptance.

### 7. Evidence discipline increases credibility

Separate:

- source or standard statements;
- local observations;
- professional inference;
- unresolved uncertainty.

Ask for official or first-party sources when the answer depends on current standards, policy, product rules, or technical mechanisms. Require source names and access dates when useful. Tell the Agent not to invent clause numbers, statistics, execution results, or missing records.

## Reusable prompt shapes

Choose the shape that matches the real work; do not merge all of them.

- **Gap assessment:** authoritative requirement + current practice → gaps, evidence, and priority.
- **Diagnostic triage:** anomaly pattern + competing causes → verification order and conditional action.
- **Constrained choice:** candidate routes + deadline/resources/risks → one defensible choice and reasons to defer the others.
- **Evidence-limited decision:** incomplete but meaningful evidence → strongest current conclusion, uncertainty, and highest-value next test.
- **Workflow control:** inconsistent records or handoffs → ownership boundaries, blocking rules, and executable control artifact.
- **Quantitative choice:** verified rules + complete inputs + calculation conventions → comparable outcomes and recommendation.

## Compact construction sequence

Build the prompt in this order:

1. Trigger and stakes.
2. Current state and decision-critical evidence.
3. Competing explanations, options, or risks.
4. Real constraints and known information gaps.
5. Judgment or action required.
6. Source and fabrication boundaries.
7. Downstream artifact, recipient, and focused exclusions.

This sequence is a reasoning checklist, not a mandatory seven-paragraph format.

## Do not overlearn from historical passes

- Do not copy fictionalized roles, shallow hardware selection, or bloated legal scenarios merely because similar prompts passed before.
- Do not restore L1/L2/L3, hidden difficulty scoring, or legacy workflow rules.
- Do not treat a named output format, exact number, first-person role, formal tone, or numbered list as an AI-writing defect by itself.
- Do not treat historical acceptance as proof that facts, sources, law, safety, or solvability were correct.
- Do not reuse the same trigger-evidence-choice-artifact skeleton with only nouns and numbers changed.
