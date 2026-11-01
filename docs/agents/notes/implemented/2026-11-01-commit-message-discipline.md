# Commit message discipline upgrade

**Status:** implemented
**Date:** 2026-11-01
**Owner:** [skills/conventional-commit/SKILL.md](../../../../skills/conventional-commit/SKILL.md)

## Problem

The `conventional-commit` skill previously defined syntactic grammar and brief type semantics, but treated the commit body as an undifferentiated optional block. In practice, this produced two recurring failure modes in commit authoring:

1. **Omission under complexity:** Non-obvious trade-offs, upstream bug workarounds, and fragile system invariants were left undocumented because the body was labeled optional.
2. **Diff duplication and session slop:** When a body was included, it often restated the diff ("Added function X to file Y") or leaked agent session narration ("As requested by user"), rather than answering why the change existed and why alternative approaches were rejected.

The skill lacked the disciplined distinction championed by the Linux kernel commit tradition: the diff answers *what* and *how*, while the commit message answers *why* and *why not*.

## Decision

Retain the original `conventional-commit` text and structure as the foundation, enhancing it with targeted commit discipline:

- **Division of labor:** The diff answers what changed and how; the commit message explains why and why not. Establish the maintainer heuristic: write messages so future maintainers reading `git blame` six months later understand hidden traps before altering or reverting code.
- **Mandatory body triggers:** Keep bodies optional for atomic, self-explanatory commits. Require a body whenever changes involve root defect conditions ("The why"), rejected intuitive alternatives ("Non-obvious trade-offs"), lifecycle or ordering constraints ("Invariants and red lines"), or breaking impacts.
- **Explicit body refusals:** Prohibit mechanical diff restatement and agent session leakage. Delegate leakage removal to [trim-reasoning-leakage](../../../../skills/trim-reasoning-leakage/SKILL.md) and sentence concision to [prose-standard](../../../../skills/prose-standard/SKILL.md).
- **Extensible types and domain scope:** Preserve extensible type compatibility (`feat`, `fix`, `refactor`, `docs`, `test`, `chore`, plus project types like `build`, `ci`, `perf`, `style`). Scopes reuse canonical project vocabulary or module directories from documentation.
- **Linux-kernel-style calibration:** Add contrast examples in [references/message-examples.md](../../../../skills/conventional-commit/references/message-examples.md) illustrating weak diff restatements alongside strong trade-off and invariant documentation.

## Alternatives considered

- **Create a new standalone skill (`git-commit-discipline`):** Rejected. `conventional-commit` is already the established owner of commit formatting and intent. Adding a parallel skill violates the one-owner-per-fact invariant and introduces routing confusion.
- **Strictly lock type vocabulary to six choices:** Rejected. Different ecosystems rely on canonical types such as `perf`, `build`, or `ci`. Locking types degrades portability across diverse codebases.
- **Enforce commit body rules via git hooks or linters only:** Rejected. Mechanical linters can validate regex formats and line lengths, but cannot assess semantic depth: whether an explanation articulates trade-offs, invariants, or diff duplication.
- **Inline full domain lists in SKILL.md:** Rejected. Hardcoding domain names violates host-agnostic portability. Project scopes belong in project documentation (Binding layer); illustrative patterns belong in `references/` (Calibration layer).

## Consequences

- **Positive impacts:** Commit messages document rationale, workarounds, and constraints in plain language, preventing future maintainers from breaking fragile code. Agents stop leaking prompt choreography and diff restatements into history.
- **Costs and obligations:** Non-trivial commits require authors to articulate rejected alternatives and invariants. Trivial atomic commits remain light without forced ceremony.

## Verification

- Structural and contract validation passes: `python3 scripts/check_skills.py`, `python3 skills/adr/scripts/check_adr.py`, `node scripts/check-skills.mjs`.
- `skills/conventional-commit/SKILL.md` stays well under the 520-word budget (440 words).
- Zero em dashes (`\u2014`) across all touched files.
- Calibration examples in `references/message-examples.md` demonstrate both atomic omission and complex trade-off calibration.

## Conditions to reconsider

- Automated git tooling reliably extracts trade-off rationale without human or agent prose.
- The word budget or skill structure requires deeper restructuring across foundational skills.
