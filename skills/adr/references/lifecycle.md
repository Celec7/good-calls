# The ADR Lifecycle

This reference details the status values, directories, and transitions for architecture decision records (ADRs).

## Lifecycle Statuses

| Status | Directory | Meaning |
| --- | --- | --- |
| `proposed` | `docs/agents/notes/proposed/` | Under discussion or awaiting implementation. Retains open questions, risks, and acceptance criteria. |
| `implemented` | `docs/agents/notes/implemented/` | Shipped in code and authoritative for current behavior. Speaks in the present tense. |
| `rejected` | `docs/agents/notes/rejected/` | Declined with an explicit reason that prevents repeating a plausible mistake. |
| `archived` | `docs/agents/notes/archived/` | Historical decision, frozen and no longer current authority. Managed via [adr-archive](../../adr-archive/SKILL.md). |

Status records reality; it grants no implementation permission. Plans, temporary logs, and handoff notes belong in conversational context or temporary work files, not decision records.

## On Implementation

When code implementing a proposed ADR ships:
1. Move the file from `docs/agents/notes/proposed/` to `docs/agents/notes/implemented/`.
2. Update the status header to `**Status:** implemented`.
3. Rewrite `## Proposal` into present-tense `## Decision` reflecting shipped reality.
4. Replace proposal-era sections (`## Acceptance criteria`, `## Risks`) with `## Consequences` and `## Verification`.
5. Repair inbound links and commit the updated ADR in the same change as the implementation.

## On Rejection

When a proposal is declined:
1. Move the file to `docs/agents/notes/rejected/`.
2. Update the status line with a one-line reason: `**Status:** rejected: <concise reason>`.
3. Retain the problem and alternatives to prevent re-litigating the same choice.

## Supersession

When a new decision reverses or alters an earlier record:
1. Author a new ADR rather than rewriting the old record into a different decision.
2. Cross-link both records explicitly.
3. For historical consolidation and archiving, use [adr-archive](../../adr-archive/SKILL.md).
