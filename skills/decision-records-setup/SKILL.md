---
name: decision-records-setup
description: Use when the user asks to establish or revise a project's convention for ADRs, RFCs, or durable engineering decision records.
disable-model-invocation: true
---

# Decision Records Setup

This skill establishes a small, maintainable project convention for durable decision records. It is setup guidance, not a required format or a request to create a sample decision.

## When not to use

- Creating or maintaining a specific decision record under an established convention. Use [decision-records](../decision-records/SKILL.md).
- Choosing the wider documentation structure. Use [canonical-docs](../canonical-docs/SKILL.md).

## Inputs and authorization

- **Required:** an explicit user request to establish or revise the convention, and access to the project's existing documentation and instructions.
- **Authorization:** this user-invoked skill permits a scoped convention change. It does not authorize unrelated documentation restructuring or inventing a decision to populate the new convention.

## Method

Inspect existing ADRs, RFCs, contributor guidance, and documentation rules before proposing changes. Reuse an established convention where possible; repair a specific gap instead of creating a parallel system. Decide who the records guide: project-wide decisions belong in shared records; a personal local-only mode is authoritative only for that developer's environment. In collaborative work, promote decisions that constrain others into shared records.

Define only the choices future authors need:

- What qualifies for a durable record, and what belongs in ordinary documentation or temporary task notes.
- Where records live and how readers find the current decision.
- How a proposal becomes implemented, rejected, or historical, including which records remain editable.
- Which information preserves judgment: problem, decision or proposal, genuine alternatives, consequences, and material evidence gaps or reconsideration conditions.
- How reversals and partial or full supersession are represented, and how links and unique rationale are preserved when records move or consolidate.

For personal local-only records, use `docs/agents/local/adr/` unless the project has a better established documentation location. Keep the directory visible, ignore its contents through a project `.gitignore` rule, and track a short agent instruction that names it and tells agents to inspect it explicitly; ordinary searches often skip ignored files. Do not link to local-only records from shared documentation. State that records are per working tree, are not backed up by Git, and may be lost with the local checkout. If the user does not want any repository changes, use a per-clone exclude rule and state that each clone needs its own setup.

Prefer the nearest existing documentation owner and the smallest useful convention. Do not copy another repository's paths, status names, required headings, indexes, metadata, archive mechanics, or validation tools as universal rules. Add automation only when the project has a concrete mechanical invariant worth enforcing. Keep setup separate from the first actual decision record.

## Validate and report

- Check that the convention has one clear owner, agrees with existing documentation, and links to the decision-record skill that will apply it. For local-only records, confirm the ignore rule and explicit discovery instruction.
- Report the files changed and the lifecycle rules established. State any convention choices that remain unresolved; do not imply that a sample ADR or behavior check was performed.
