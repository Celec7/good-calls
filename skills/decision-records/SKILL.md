---
name: decision-records
description: Use when creating, reviewing, updating, superseding, or retiring an ADR, RFC, or other durable engineering decision record.
---

# Decision Records

This skill is guidance, not a script. Preserve reasons a future maintainer cannot reliably recover from code. Record lasting choices and proposals, not routine implementation history.

## When not to use

- Temporary task state, plans, or investigation logs. Use [plan](../plan/SKILL.md) or the conversation.
- The current explanation of a system, or an incident story about a defect that escaped. Use [canonical-docs](../canonical-docs/SKILL.md).
- Wording of the record. Use [prose-standard](../prose-standard/SKILL.md).

## Inputs and authorization

- **Required:** the problem, the choice or proposal, and the alternatives actually considered. Never invent alternatives to fill a template. If the choice is unsettled, keep the record proposed and make open questions visible.
- **Authorization:** recording a status records reality; it grants no implementation permission.

## Method

Search for an existing owner first. A new record warrants a scoped search for active records about the same choice, mechanism, or rejected alternative. Update the owner when it is the same decision; when the choice changes, create a successor and link both records. Classify full and partial supersession as you write: preserve still-useful rationale and cross-link partial overlaps, and consolidate a fully superseded record only after preserving its unique rationale and repairing inbound links.

Record the problem, choice or proposal, meaningful constraints, genuine alternatives, consequences, and verification or evidence gaps that still affect judgment. State when reconsideration would be useful. Keep the format compatible with the project's established convention; these contents are guidance, not a required heading set.

### Place the record

Follow an existing, active ADR or RFC convention, including its amendment, retention, and immutability rules. When the user asks to establish a durable project convention, use [decision-records-setup](../decision-records-setup/SKILL.md). Otherwise, where the project has no rule, use `docs/agents/notes/<status>/YYYY-MM-DD-topic.md`, dated when first proposed, with status in the path: `proposed`, `implemented`, `rejected`, or `archived`. Avoid a dot-directory: some agents cannot write one, and search tools skip it. Create only needed directories, with no central index, category tree, or sidecar requirement. If the project cannot write this path, report that and use its documented alternative rather than failing silently. The fallback does not establish project policy.

### Maintain and retire

On implementation, replace the proposal with what actually shipped, and do not mark a partly delivered proposal complete. Keep implementation facts current, but do not rewrite the choice into a different decision. Reversing a decision needs a new record that names the old one. When a status transition moves a record, repair inbound links in the same change. Keep partially superseded records current and cross-linked; consolidate a fully superseded record only after preserving its unique rationale in the new owner. Archive a complete implemented record only when its reasons are unlikely to guide future work and its history still matters; reject an obsolete proposal; delete a rejection that no longer prevents a plausible mistake. Remove a purely mechanical or local record when it carries no durable constraint or rationale. Age and word count are not retention criteria.

Details and the status table: [the decision lifecycle](references/lifecycle.md).

## Validate and report

- Report the record added or changed, its status, and the scoped supersession check.
- Repair inbound links on any move; preserve frozen archives as history, not current authority.
- Maintain related records within the current task; a corpus-wide cleanup needs its own scope. No new record is often the right outcome.
