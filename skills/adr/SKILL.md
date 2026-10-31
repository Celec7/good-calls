---
name: adr
description: Use when recording, proposing, or implementing an architectural decision record (ADR) or lasting engineering trade-off. Use adr-setup to establish a project convention; use adr-archive to prune or archive records.
---

# Architecture Decision Records

This skill is guidance, not a script. Preserve reasons a future maintainer cannot reliably recover from code. Record lasting architectural choices, constraints, and proposals, not routine implementation history.

## When not to use

- Temporary task state, execution plans, or work logs. Use [plan](../plan/SKILL.md) or conversation context.
- Current system explanations or defect incident postmortems. Use [canonical-docs](../canonical-docs/SKILL.md).
- Establishing or changing a project ADR storage convention. Use [adr-setup](../adr-setup/SKILL.md).
- Pruning, consolidating, or archiving historical records. Use [adr-archive](../adr-archive/SKILL.md).
- Fine-tuning record prose and sentence contracts. Use [prose-standard](../prose-standard/SKILL.md).

## Inputs and authorization

- **Required:** the problem, the choice or proposal, and genuine alternatives actually evaluated. Never invent artificial alternatives. If a choice is unsettled, keep the record proposed and expose open questions.
- **Authorization:** recording a status records reality; it grants no implementation permission. Durable records belong under version control and must be committed alongside the code they document.

## Method

Search for an existing owner first. A new record warrants a scoped search for active records about the same choice, mechanism, or rejected alternative. Update the owner when it is the same decision; when the choice changes, create a successor and link both records.

### Creating a proposal

When a design involves meaningful architectural ambiguity or trade-offs:
1. Copy [templates/proposed.md](templates/proposed.md) to `docs/agents/notes/proposed/YYYY-MM-DD-topic.md` (dated when first proposed), or the project's established ADR path.
2. Retain the top HTML lifecycle guidance comment. It instructs future agent runs on how to advance the record upon implementation.
3. Record the problem, proposed technical direction, genuine alternatives, observable acceptance criteria, and explicit risks.

### Advancing to implemented

When code implementing a proposed ADR ships:
1. Move the file from `docs/agents/notes/proposed/` to `docs/agents/notes/implemented/`.
2. Follow the structure in [templates/implemented.md](templates/implemented.md): change `Status: proposed` to `Status: implemented`, rewrite `## Proposal` into present-tense `## Decision`, and fold acceptance criteria and risks into `## Consequences` and `## Verification`.
3. Repair inbound and relative links in the same change.
4. Commit the moved and updated record in the same change as the implementation. Never leave implemented records uncommitted or stranded in proposed status.

Details on statuses, transitions, and supersession: [the decision lifecycle](references/lifecycle.md).

Validate records locally with the lifecycle checker:
```bash
python3 skills/adr/scripts/check_adr.py
```

## Validate and report

- Report the record created or transitioned, its status, and the scoped supersession check.
- Confirm inbound links are preserved and the record is staged or committed with the corresponding code change.
