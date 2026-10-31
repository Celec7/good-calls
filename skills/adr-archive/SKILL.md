---
name: adr-archive
description: Use when the user asks to audit, prune, consolidate, or archive historical architecture decision records (ADRs).
disable-model-invocation: true
---

# Archive Architecture Decision Records

This skill is guidance, not a script. Audit and prune the active decision corpus without erasing historical rationale that can still guide work. Judge every record semantically; word count and age are not archival criteria.

## When not to use

- Authoring, proposing, or advancing an active decision record. Use [adr](../adr/SKILL.md).
- Establishing or revising project ADR conventions. Use [adr-setup](../adr-setup/SKILL.md).
- General documentation cleanup or website maintenance. Use [canonical-docs](../canonical-docs/SKILL.md).

## Inputs and authorization

- **Required:** an explicit user request to audit, consolidate, or archive decision records, and an inspected scope of records.
- **Authorization:** this user-invoked skill authorizes pruning, archiving, and link updates within the requested scope. It does not authorize altering current active architectural decisions.

## Method

Audit active decision records under `docs/agents/notes/` (or the project's ADR directory) against current code, tests, and documentation.

### Classify implemented records

For each record in `docs/agents/notes/implemented/`:
- **Delete mechanical notes:** delete records that only describe minor adjustments or purely mechanical refactors with unchanged behavior, and clean up inbound links. Substantive architectural, security, or boundary decisions do not qualify for deletion merely because their code footprint was small.
- **Retain active notes:** keep records whose rationale, alternatives, negative guarantees, wire contracts, or reintroduction conditions continue to guide future changes.
- **Archive historical decisions:** move substantive historical decisions that are complete and unlikely to guide future work to `docs/agents/notes/archived/`. Once moved, freeze the record as historical snapshot: do not alter its body or treat it as current authority. Update inbound links from active prose to cite current documentation or the archived snapshot explicitly.

### Handle proposed and rejected records

- **Never archive a proposal:** keep live proposals under `proposed/`. If a proposal is no longer pursued, move it to `docs/agents/notes/rejected/` and append a one-line explanation to the status line: `**Status:** rejected: <concise reason>`.
- **Retain rejections with lasting value:** keep rejected records when their reasoning prevents repeating a plausible, costly mistake. Delete rejections whose premises have become obsolete.

### Consolidate superseded records

When a new decision fully absorbs an older record:
1. Ensure the successor record preserves every unique rationale, alternative considered, and constraint from the older record.
2. Repair all inbound links to target the successor.
3. Remove or archive the superseded record in the same change.

## Validate and report

- Report records deleted, retained active, moved to rejected, and archived.
- Confirm inbound links from active documentation are redirected or cleaned up.
