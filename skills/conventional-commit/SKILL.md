---
name: conventional-commit
description: Use when drafting or reviewing commit messages or organizing changes into coherent conventional commits.
---

# Conventional Commit

This skill is guidance, not a script. Describe one coherent engineering change using Conventional Commits. The diff answers what changed and how; the commit message explains why and why not. Read the actual intended diff first; the original task title may no longer describe it.

## When not to use

- Organizing the work itself into reviewable slices. Use [plan](../plan/SKILL.md).
- Deciding whether a change is safe or complete. Use [code-review](../code-review/SKILL.md).
- A request for a commit message with no intention to commit; a message request authorizes no Git mutation.

## Inputs and authorization

- **Required:** the actual intended diff, not the original task title.
- **Authorization:** drafting a message authorizes no Git mutation. Committing requires an explicit request; inspect the exact staged content and preserve unrelated user work. Commit permission does not extend to push or history rewriting.

## Method

Implementation, tests, and related documentation can share one intent. Split independent changes when doing so improves review or reversal, not merely because files have different types. Do not force coupled edits into broken intermediate commits.

### Grammar

```text
<type>[optional scope][!]: <description>

[optional body]

[optional footers]
```

Choose the type by effect: `feat` adds capability, `fix` repairs behavior, and `refactor` changes structure without changing intended behavior. Use `docs` or `test` for changes confined to those concerns. Extend with the project's other canonical types, such as `build`, `ci`, `perf`, `style`, or `chore`, when they fit; `chore` is not a substitute for understanding the change.

Scope is optional and names a meaningful component or architecture domain. Reuse canonical project vocabulary or module directories from project documentation; omit it when no natural scope exists.

Write a concise description without a trailing period. In English, use the imperative. Follow the project's message language; Conventional Commits does not require English prose. Keep the type and machine-readable markers consistent. Never narrate agent session history or task numbers in the title.

### Body discipline

Atomic, self-explanatory changes may omit the body. Include a body whenever a future maintainer inspecting `git blame` six months later would need context to avoid breaking the code or re-introducing a bug. Following the Linux kernel commit tradition, explain the problem condition and why the chosen approach was preferred over intuitive alternatives.

Mandatory body triggers:
- **The why:** the concrete defect, failure condition, or motivation forcing the change.
- **Non-obvious trade-offs:** why straightforward or standard approaches were rejected (for example, bypassing upstream bugs, race conditions, or performance cliffs).
- **Invariants and red lines:** critical lifecycle constraints, execution ordering, or boundary assumptions future edits must not break.
- **Breaking impact:** migration steps or blast radius flagged for callers.

Refuse in the body:
- Do not restate the diff (for example, "Added function X"). The diff already shows what changed.
- Do not include agent prompt leakage or session narration. Use [trim-reasoning-leakage](../trim-reasoning-leakage/SKILL.md).

Separate the body from the title with a blank line and wrap prose around 72 columns. Use [prose-standard](../prose-standard/SKILL.md) for dense, economical wording.

### Compatibility and trailers

Mark a breaking contract with `!` or an uppercase `BREAKING CHANGE:` footer. Explain impact and migration when needed. Compatibility depends on what consumers can rely on, not diff size. Under Conventional Commits semantics, `fix` indicates PATCH, `feat` MINOR, and a breaking change MAJOR; other types have no implicit version effect.

Separate footers from the preceding text with a blank line. Use trailer forms such as `Refs: #123` or `Fixes #123`; hyphenate multiword tokens except `BREAKING CHANGE`. Include only real references and attribution.

```text
fix(export): preserve filters across paginated queries

Pass the active filter array into cursor-based pagination requests.
Cursor queries previously dropped filters after page 1, silently
exporting unfiltered records. Preserving the filter array in the page
request avoids resetting user-selected boundaries mid-export.

## Validate and report

- Before returning the message, check for omitted behavior, overstated results, breaking effects, and unrelated content.
- Use [prose-standard](../prose-standard/SKILL.md) for body wording: preserve the reason, impact, non-obvious trade-offs, and any compatibility promise.
- Report the staged scope you actually inspected when committing.

## References

- [Message examples](references/message-examples.md)
