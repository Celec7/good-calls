---
name: prose-standard
description: Use when creating, editing, or reviewing maintained prose, or when a code, API, or behavior change may require updating its written contract. Applies to documentation, comments, JSDoc, tests, prompts, diagnostics, and user-visible text.
---

# Prose Standard

This skill is guidance, not a script. A contract is an obligation, invariant, precondition, postcondition, or compatibility promise that a caller, callee, implementer, producer, or consumer relies on. Write dense, economical prose: preserve the complete contract in the fewest words, then aggressively eliminate preambles, repetition, code restatements, and decorative fluff.

## When not to use

- Prose that takes the authoring session's vantage, such as dead citations, change narration, or review vantage. Use [trim-reasoning-leakage](../trim-reasoning-leakage/SKILL.md).
- Where documentation lives, its structure, and its audience. Use [canonical-docs](../canonical-docs/SKILL.md).
- Commit message shape or type. Use [conventional-commit](../conventional-commit/SKILL.md).
- A code or behavior defect. Prose cannot fix it.

## Inputs and authorization

- **Required:** an explicit scope of files, surfaces, or a diff. If it is missing, report it and stop.
- **Mode:** `automatic` (default) applies clear edits; `interactive` asks before rewriting. Enter interactive only when the user asks.
- **Authorization:** a review or audit is read-only. Edit only when the task asks for a fix or a trim. Treat generated catalogs, snapshots, and fixtures as derivatives: fix the owner, then regenerate.
- Exclude vendored code and frozen records. If the scope contains only excluded paths, report that nothing qualifies.

## Method

### Preserve the complete proposition

Before editing, identify every proposition in the passage. Preserve each relevant actor, action, condition, timing, modality (must, may, never), negative guarantee, exception, ownership, side effect, failure, and consequence.

Economy of words: eliminate preambles, transitional filler, and narrative setup. Every sentence must carry an operational fact, invariant, or constraint. Avoid paragraph walls by keeping each paragraph focused on one topic. Reserve bold or capitalized emphasis strictly for clauses that alter behavior or prevent critical misuse; if everything is emphasized, nothing stands out. Prefer concrete active prose and ordinary punctuation; this suite does not use em dashes.

### What each surface owes (and refuses)

- **Public JSDoc:** caller-visible return distinctions, throws or rejections, side effects, ownership, timing, cancellation, and durability. *Refuses: code walkthroughs, implementation steps, parameter lists the signature already carries.*
- **Internal comments:** non-local invariants, race ordering, ownership, security boundaries, and surprising failure behavior. *Refuses: restating what the adjacent code obviously does.*
- **Module comments:** role, dependencies, responsibilities, and non-obvious architecture choices linked to their owner. *Refuses: duplicating the module README.*
- **Tests:** non-obvious design choices, such as why a fixture, assertion, or indirect observation is necessary. *Refuses: step-by-step test walkthroughs.*
- **READMEs:** consumer contract: configuration, semantics, failures, limitations, extension points, and model-visible effects. *Refuses: JSDoc duplicates, change narratives, internal algorithm walkthroughs, architectural rationale (link to ADR).*
- **Decision records:** unique rationale, alternatives, consequences, and verification evidence. *Refuses: routine implementation history or tutorial steps.*
- **Postmortems:** incident sequence, evidence, causal chain, impact, and prevention. *Refuses: design advocacy.*
- **Prompts and visible strings:** wording is behavior. Follow owning localization and snapshot rules.
- **Diagnostics:** name the failing subject, violated rule, and correction when non-obvious.

### One owner per explanation

Keep a complete local contract at the point of use. Link architecture, rationale, algorithms, history, and extended examples to their single authoritative owner under [canonical-docs](../canonical-docs/SKILL.md). Edit the owner before its derivatives, then regenerate.

### Do not trim away an obligation

Keep non-obvious rationale when omitting it could cause misuse. Preserve modality, negation, and measured bounds. For paired bilingual prose, update the counterpart minimally and re-record the pair.

## Validate and report

- Re-read the full diff for propositions that were dropped, weakened, or added.
- Run checks for touched surfaces, such as documentation, snapshot, or translation-pairing gates.
- Report the scope inspected, clear changes, deliberate keeps, deferred cases, and checks run.

## References

- [Worked examples](references/examples.md)
