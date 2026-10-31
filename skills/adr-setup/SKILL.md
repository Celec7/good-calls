---
name: adr-setup
description: Use when the user asks to establish or revise a project convention for architecture decision records (ADRs) or durable engineering records.
disable-model-invocation: true
---

# ADR Setup

This skill establishes a small, maintainable project convention for durable architecture decision records. It is setup guidance, not a required format or a request to create a sample decision.

## When not to use

- Creating, proposing, or advancing a specific decision record under an established convention. Use [adr](../adr/SKILL.md).
- Choosing the wider documentation structure. Use [canonical-docs](../canonical-docs/SKILL.md).
- Pruning, consolidating, or archiving historical records. Use [adr-archive](../adr-archive/SKILL.md).

## Inputs and authorization

- **Required:** an explicit user request to establish or revise the convention, and access to the project's existing documentation and instructions.
- **Authorization:** this user-invoked skill permits a scoped convention change. It does not authorize unrelated documentation restructuring or inventing a decision to populate the new convention.

## Method

Inspect existing ADRs, RFCs, contributor guidance, and documentation rules before proposing changes. Reuse an established convention where possible; repair a specific gap instead of creating a parallel system. If the project has no convention, adopt Good Calls' recommended default: shared records under `docs/agents/notes/{proposed,implemented,rejected,archived}/` driven by [adr](../adr/SKILL.md), without scaffolding empty directories or copying duplicate templates. Decide who the records guide: project-wide decisions belong in shared records; personal local-only records guide only that developer's environment.

Define only the choices future authors need:

- What qualifies for a durable record, and what belongs in ordinary documentation or temporary task notes.
- Where records live and how readers find the current decision.
- How a proposal becomes implemented, rejected, or historical, including which records remain editable.
- Which information preserves judgment: problem, decision or proposal, genuine alternatives, consequences, and material evidence gaps or reconsideration conditions.
- How reversals and partial or full supersession are represented, and how links and unique rationale are preserved when records move or consolidate.

For personal local-only records, use `docs/agents/local/adr/` unless the project has a better established location. Keep the directory visible, ignore its contents through `.gitignore`, and record a brief agent instruction telling agents to inspect it explicitly; ordinary search skips ignored paths. Do not link to local-only records from shared documentation. State that records are per working tree and not backed up by Git. If the user wants no repository edits, use a per-clone exclude rule.

Record the convention minimally: add one or two lines to the project's existing instruction file (such as `AGENTS.md` or a development section in `README.md`) pointing to the chosen path and [adr](../adr/SKILL.md). Prefer the nearest existing documentation owner and the smallest useful convention. Do not scaffold empty directories, copy external metadata, or create placeholder templates. Keep setup separate from the first actual decision record.

## Validate and report

- Check that the convention has one clear owner, agrees with existing documentation, and links to the [adr](../adr/SKILL.md) skill that will apply it. For local-only records, confirm the ignore rule and explicit discovery instruction.
- Report the files changed and the lifecycle rules established. State any convention choices that remain unresolved; do not imply that a sample ADR or behavior check was performed.
