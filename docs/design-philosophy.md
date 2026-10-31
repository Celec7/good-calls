# Design Philosophy and Evolution

This document records the engineering philosophy, background, and evolution of Good Calls (formerly Beyond Code). It explains why this suite provides independent, on-demand skills rather than a mandatory workflow engine, CLI protocol, or persistent task ledger.

## 1. The Core Problem: The SWE Gap

A capable language model can write code with few syntax or algorithmic errors. However, software engineering is not merely generating code that runs.

Between an initial, often ambiguous user requirement and reliable software delivery lies a significant gap:

- Clarifying what problem actually needs solving before writing code, rather than guessing intent.
- Dividing work into verifiable, decoupled slices rather than monolithic edits.
- Diagnosing the root cause of failures before applying superficial band-aids.
- Knowing when to introduce an abstraction and when to keep code simple.
- Evaluating whether tests provide genuine behavioral evidence or superficial green checks.
- Preserving non-obvious engineering decisions and trade-offs that cannot be recovered from code alone.

Before artificial general intelligence, models cannot reliably bridge this gap through raw token prediction alone. Guessing in the face of ambiguity leads to misaligned implementations, hidden regressions, and unmaintainable architectures.

Developers, working together with coding agents, form the intermediate layer responsible for navigating this path. The role of these skills is auxiliary: to equip developers and agents with proven engineering judgment methods at critical decision points, without dictating how they work.

## 2. Core Principles

### Better judgment. Less ceremony.

Good software is the product of sound engineering decisions, not adherence to bureaucratic rituals.

The value of an engineering skill is measured by whether it improves a concrete decision: when to ask for clarification, how to isolate a bug, what evidence to trust, and which rationale to preserve. A skill that only adds steps without changing decisions adds overhead without value.

Skills earn their place by changing a decision.

### Guidance over control

An agent should retain autonomy over its execution.

Skills provide methods, heuristics, failure modes, and verification criteria. They do not force every task through a fixed sequence of phases, approval gates, or role handoffs.

A straightforward fix should not be forced through spec drafting, formal planning, multi-agent review, and archival ledgers simply because a skill suite is installed. Not invoking a skill is often the correct choice. The developer and the agent decide when help is needed, and which specific skill to call.

### Avoiding context and protocol pollution

Early iterations of this project explored detailed process constraints, hard gates, deviation logs, and state ledgers. In practice, these mechanisms revealed a critical failure mode: context and protocol pollution.

When an agent is burdened with maintaining framework state, entering and exiting gates, updating progress files, and proving compliance with a protocol, its limited attention budget is diverted away from the real engineering task. The agent becomes skilled at following the framework's protocol, yet fails to deliver sound software.

Good Calls opposes turning framework mechanics into tasks the agent must continually manage. External environments can enforce genuine system invariants (such as build gates or file permissions); skills should focus on engineering judgment.

### Adapting to stronger models

As models improve, their baseline reasoning, code generation, and instruction following advance. Detailed operational rules intended to compensate for weaker model weaknesses yield diminishing returns and eventually become context drag.

Skills must not freeze today's model limitations into permanent prompt rituals. The stronger the model becomes, the more skills should concentrate on hard-to-derive engineering trade-offs, edge cases, and judgment, leaving mechanical execution to the model's native capabilities.

## 3. Design Evolution

The current architecture is the result of multiple rounds of real-world development, experimentation, and pruning.

```
2026-06: Light conversational flow (Think -> Plan -> Build -> Verify -> Archive)
  │
2026-07: Heavy process & hard gates (HARD-GATE, gate.md, deviation thresholds)
  │
2026-08: De-bureaucratization (removed gate.md, dropped project-docs)
  │
2026-09: Paired experiment pivot -> modular engineering guardrails -> discrete skills
  │
2026-10: Architecture contract (Method / Binding / Calibration) -> 19 independent skills
```

### Phase 1 (June 2026): Early light workflow

The initial implementation (commit `952c02c`) established the premise that the user sets the pace while the agent provides structure. It organized work through natural conversational phases (clarify, plan, build, verify, archive) without requiring heavy tooling or CLI harnesses.

### Phase 2 (July 2026): Hard gates and task ledgers

In an attempt to maximize agent predictability, the suite introduced formal workflow enforcement (commit `a57b9a8`):
- Mandatory `HARD-GATE` checks before coding.
- RFC 2119 requirement levels.
- Pre-execution bounds and file access constraints.
- Multi-document state tracking (`spec.md`, `plan.md`, `gate.md`).
- Deviation logs with automatic stop thresholds.

While these controls reduced certain careless actions, they imposed heavy cognitive overhead and maintenance costs on every prompt turn.

### Phase 3 (August 2026): Streamlining and removal of state bloat

Experience showed that managing synchronization between multiple task documents was counterproductive. The project removed `project-docs` and eliminated `gate.md` in favor of keeping task context minimal and focused (commit `831b923`).

### Phase 4 (September 2026): The paired experiment and pivot

On September 11, 2026, the project conducted a paired subagent experiment: twelve runs across six distinct development scenarios, comparing agents loaded with the workflow skills against a control group with no skills installed (commit `859da74`).

Every scenario reached the intended technical outcome in both arms. The workflow rules did not alter task completion rates.

This empirical finding was a turning point. It demonstrated that rigid workflow enforcement does not automatically produce better software. The project repositioned the suite from an error-correction mechanism to a collection of modular engineering guardrails (commit `598d031`), and subsequently decomposed the suite into discrete, independent skills (commit `f16f88a`).

### Phase 5 (October 2026): The skill architecture contract

The suite established a formal architectural contract (commit `4e36f0d` and `b5b5498`, documented in [docs/skill-architecture.md](skill-architecture.md)):
- **Method**: Portable engineering decision procedures in `SKILL.md`.
- **Binding**: Project-specific facts, resolved dynamically from existing project documentation rather than duplicated in skill files.
- **Calibration**: Concrete examples and reference scenarios under `references/`.

Four foundation skills were introduced to own cross-cutting concerns: `skill-authoring`, `error-handling`, `prose-standard`, and `trim-reasoning-leakage`. With the subsequent addition of `decision-records-setup` (commit `c1e9edf`), the suite reached its current catalog of nineteen independent skills.

## 4. Relationship to Other Tools

Good Calls does not compete with or replace:
- Task runners and build tools: Compilation, formatting, and test execution belong to standard project tooling.
- Multi-agent orchestration platforms: Good Calls does not orchestrate subagent swarms or manage distributed runtime processes.
- Specialized domain libraries: Frontend design systems, framework-specific generators, or browser automation skills serve as optional companions alongside Good Calls.

Good Calls provides the engineering discipline and decision-making heuristics that help an agent navigate from requirements to delivery.
