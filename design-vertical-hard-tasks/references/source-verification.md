# Source and attachment verification

## Mandatory active research

For every design, ideation, or repair:

1. Use the available search or browser tool; do not merely recommend search terms.
2. Search authoritative or first-party material for rules, mechanisms, specifications, or product facts.
3. Search scenario-specific data, cases, or comparable practice needed to make the task solvable.
4. Open the candidate page or file and inspect the relevant content.
5. Reject search-result pages, snippets, generic homepages, inaccessible links, and AI summaries as evidence.
6. Re-check existing sources during repair; do not trust the old title, date, or URL without opening it.

Normally open at least two candidate sources, then retain only the smallest sufficient evidence set. When the task relies on public claims, keep at least one primary source whenever one exists.

If browsing is prohibited, unavailable, or unsafe because of confidentiality, keep the design `DRAFT`. In the `附件来源` field, state the limitation and the exact material still needed. Never invent a plausible-looking source.

## Verification record

Record each required material with:

- stable material ID;
- exact title or file name;
- file type and primary language;
- publisher or owning organization;
- source type: official, first-party, standards body, authoritative institution, industry institution, user-provided internal material, or another reliable source;
- publication date when available;
- direct source URL rather than a site homepage;
- local preserved path when downloaded;
- download or access time;
- SHA-256 for local bytes;
- task requirements supported by the material;
- privacy or sensitivity notes;
- English whitelist confirmation when applicable;
- status: `VERIFIED`, `UNVERIFIED`, or `FAILED`.

Map every `相关附件` item one-to-one to an `附件来源` entry. Use the same exact attachment name in both fields.

## Verification procedure

1. Open the direct URL or source file.
2. Confirm title, publisher, date, format, language, and accessibility.
3. Inspect the relevant pages, sheets, tables, figures, code, or logs.
4. Map the material to a real task requirement; reject filler attachments.
5. Confirm that the material contains enough information for its assigned role.
6. Compare sources for contradictions, stale periods, incompatible units, and inconsistent definitions.
7. Preserve the original bytes or a faithful public-page snapshot when practical.
8. Record gaps and conflicts in the task rather than silently resolving them.

## READY gate

For `READY`:

- every required material must be `VERIFIED`;
- no core source may be fabricated, corrupted, inaccessible, or only a homepage;
- every attachment must support at least one task requirement;
- English material must have explicit project whitelist confirmation;
- anonymized material must have user confirmation that core facts and logic were preserved;
- the prompt and internal pack must distinguish source fact, professional inference, and information still missing.
- the standard six-field output must contain no unmatched attachment or source entry.

Under the current six-field contract, a task card must include at least one relevant attachment and a matching source entry before it can be `READY`. For a primarily internal problem, use an authorized internal snapshot, log, specification, data extract, or other real input; public methodology may supplement it but must not substitute for missing internal facts.

## Source preservation

Allow downloading, hashing, and faithful format conversion. Keep the original file alongside any converted copy. Do not change source facts, delete inconvenient rows, synthesize missing values, translate an English source into a Chinese “original,” or use a summary as a substitute for the source.

When anonymization is necessary, create a separate copy, document every transformed field, and retain the unmodified original only when the user is authorized to store it. Never expose private source contents in the task record.

Use `scripts/build_source_manifest.py` to create an `UNVERIFIED` local-file manifest. Verification must still be performed by reading the materials.
