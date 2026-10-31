---
name: canonical-docs
description: Use when writing or reviewing maintained engineering documentation, choosing its location, or resolving drift between documentation and implementation.
---

# Canonical Docs

This skill is guidance, not a script. Give every fact one authoritative owner. Code is the source of truth for actual behavior; requirements and valid decisions define intended behavior. Tests are evidence, not infallible authority.

## When not to use

- Sentence-level contracts, paragraph density, or fluff removal. Use [prose-standard](../prose-standard/SKILL.md).
- Prose that takes the authoring session's vantage, such as change narration. Use [trim-reasoning-leakage](../trim-reasoning-leakage/SKILL.md).
- Architectural rationale, trade-offs, and rejected alternatives. Use [adr](../adr/SKILL.md).

## Inputs and authorization

- **Required:** the reader and the judgment or operation the text helps them perform.
- **Authorization:** a scoped edit does not authorize restructuring the whole corpus. Establish a new documentation structure only after the user chooses among options.

## Method

Follow the project's established documentation structure. If none exists, adopt the recommended defaults below.

### One home per fact

Never dump information into the nearest file. Locate the single authoritative home for each kind of truth:

- **Bugs and escapes:** incident records under postmortems; not ordinary documentation. If no convention exists, use `docs/postmortem/YYYY-MM-DD-topic.md`.
- **Design rationale and rejected alternatives:** [adr](../adr/SKILL.md); link there with a one-line reference, never dump rationale into READMEs.
- **Current system architecture:** architecture overview or subsystem maps; never include local implementation details.
- **Module and package contracts:** module READMEs for configuration, public interfaces, extension points, and limits; never restate JSDoc or internal algorithms.
- **Procedures and guides:** cookbooks with ordered steps and verification checks; never mix with reference lookup.
- **Task and working state:** conversational context or ephemeral work files; never commit task state into formal documentation.

See [the documentation tiers reference](references/documentation-tiers.md) for full taxonomy details.

### Document current state only

Documentation describes how the system behaves right now at HEAD. It is not a changelog or a diary.

- **Never write change narration:** phrases like "previously", "in this update we added", "was changed to avoid", or "fixed an issue where" belong in Git commit messages or PR descriptions, never maintained documentation.
- **Never add status annotations:** labels such as "(implemented!)", "(new in v2)", or "(planned for next sprint)" rot quickly. State current behavior as a present-tense fact.
- **Never hand-restate code:** do not manually copy type definitions, parameter tables, or CLI option lists that source code, JSDoc, or automated generators already provide.

### Place before writing

Identify the reader and the exact operation the text helps them perform. Extend an existing owner before creating a new document. If no structure exists, offer a few proportionate options (such as a root README, module READMEs, and `docs/`) and establish it after the user chooses.

### Incident records

Own the postmortem tier: a backward-looking record of a defect that reached a user, a merged change, or a release. Write one when the defect is subtle, systemic, and costly to rediscover, following [incident records](references/incident-records.md).

### Verify and maintain

Check behavior claims against current code, and run documented operations before publishing. State verification limits rather than claiming an unobserved result. Never document a known defect as intended behavior merely to reconcile text with code.

## Validate and report

- Confirm every changed claim has one home and no change narration was introduced.
- Run relevant documentation checks and inspect final text for factual accuracy.
- Report verification limits, deliberate keeps, and any unresolved drift.
