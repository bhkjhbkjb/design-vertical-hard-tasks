# Source and attachment verification

## Verification record

Record each required material with:

- stable material ID;
- exact title or file name;
- file type and primary language;
- publisher or owning organization;
- publication date when available;
- direct source URL rather than a site homepage;
- local preserved path when downloaded;
- download or access time;
- SHA-256 for local bytes;
- task requirements supported by the material;
- privacy or sensitivity notes;
- English whitelist confirmation when applicable;
- status: `VERIFIED`, `UNVERIFIED`, or `FAILED`.

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

A legitimate no-attachment task can be `READY` only when `附件策略` is `not_required` and the task remains professionally deep and verifiable without attachments.

## Source preservation

Allow downloading, hashing, and faithful format conversion. Keep the original file alongside any converted copy. Do not change source facts, delete inconvenient rows, synthesize missing values, translate an English source into a Chinese “original,” or use a summary as a substitute for the source.

When anonymization is necessary, create a separate copy, document every transformed field, and retain the unmodified original only when the user is authorized to store it. Never expose private source contents in the task record.

Use `scripts/build_source_manifest.py` to create an `UNVERIFIED` local-file manifest. Verification must still be performed by reading the materials.
