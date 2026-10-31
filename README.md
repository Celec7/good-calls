# Good Calls

**Better engineering judgment for coding agents.**

*Good code starts with good calls.*
*Less ceremony. Better decisions.*

[![skills.sh](https://skills.sh/b/Celec7/good-calls)](https://skills.sh/Celec7/good-calls)

A collection of twenty independent skills that help coding agents make sound engineering decisions without imposing a workflow. Formerly Beyond Code.

English | [中文](README_zh-CN.md)

## Why this exists

Modern coding agents can generate code with few low-level syntax or algorithmic bugs. However, generating runnable code is not the same as delivering software.

Between an ambiguous user request and a reliable production deployment lies a significant software engineering gap:

- Discerning what needs clarification before touching code, rather than guessing intent.
- Decomposing changes into verifiable, decoupled slices instead of high-risk monolithic edits.
- Diagnosing root causes with systematic evidence rather than patching symptoms.
- Knowing when to introduce an abstraction and when to keep code simple.
- Evaluating whether test assertions provide genuine proof or superficial reassurance.
- Deciding which engineering trade-offs warrant lasting architectural records.

Developers act as the essential bridge across this gap. The purpose of Good Calls is to assist developers and agents at critical decision points. The skills serve an auxiliary role: providing disciplined engineering judgment when needed, without taking over the developer's workflow or forcing tasks into a rigid process.

## Philosophy

### Better judgment. Less ceremony.

Good software results from sound engineering choices, not bureaucratic compliance. Instructions are direct, modular, and scoped. There are no mandatory startup hooks, central router skills, or compulsory execution chains.

### Skills earn their place by changing a decision

A software engineering principle is only worth placing in a skill if it materially improves an agent's decision: when to ask, how to divide work, what evidence to trust, and which reasons to preserve. If a capable model already handles a situation reliably, repeating that rule only consumes context without adding value.

### Guidance over control

An agent retains full autonomy over how it executes. A simple one-line fix should never be forced through specification drafting, formal planning, multi-role review, and archival ceremonies simply because a skill suite is installed. Not invoking any skill is often the correct choice.

### Avoiding context and protocol pollution

Early iterations of this project experimented with strict phase gates, task ledgers, and deviation thresholds. In practice, these mechanisms distracted agents from the real engineering task. When an agent spends its attention budget tracking framework state, updating ledger files, and proving compliance with a protocol, code quality and architectural clarity suffer. Good Calls keeps process overhead minimal and leaves task state in normal conversation.

### Adapting to stronger models

As underlying models advance, skills should not cling to outdated workarounds designed for past model limitations. The stronger a model becomes, the more skills should focus on non-trivial engineering trade-offs and judgment, leaving mechanical execution to the model's native reasoning.

For a detailed history of the project's evolution and paired subagent experiments, see [docs/design-philosophy.md](docs/design-philosophy.md).

## What it is and what it is not

- **It is** a collection of independent, on-demand engineering skills that provide decision methods for clarification, design, planning, debugging, testing, review, and documentation.
- **It is not** a rigid workflow engine or lifecycle orchestrator.
- **It is not** a multi-agent swarm framework or background service manager.
- **It is not** a persistent CLI state management protocol or file-based task ledger.
- **It is not** an exhaustive encyclopedia of software engineering rules.

## Skills

Invocation modes:
- **Automatic**: The agent may select the skill when relevant; users can also invoke it explicitly.
- **User only**: Reserved for changes in conversational mode, requiring an explicit user request.

### Foundation

Foundation skills carry judgment that other skills reuse.

| Skill | Judgment it provides | Invocation |
| --- | --- | --- |
| [skill-authoring](skills/skill-authoring/SKILL.md) | Decide when a skill earns its place, and write its description, body, and tests | Automatic |
| [error-handling](skills/error-handling/SKILL.md) | Define failures, their owners, and what remains safe after failure | Automatic |
| [prose-standard](skills/prose-standard/SKILL.md) | Preserve every proposition and state what each prose surface owes | Automatic |
| [trim-reasoning-leakage](skills/trim-reasoning-leakage/SKILL.md) | Remove prose that takes the authoring session's vantage | Automatic |

### Domain

Domain skills provide engineering methods across typical development phases.

| Skill | Judgment it provides | Invocation |
| --- | --- | --- |
| [clarify](skills/clarify/SKILL.md) | Resolve consequential ambiguity in problems, outcomes, and scope | Automatic |
| [codebase-design](skills/codebase-design/SKILL.md) | Place responsibility and complexity behind useful interfaces | Automatic |
| [plan](skills/plan/SKILL.md) | Arrange verifiable slices, dependencies, and staged migrations | Automatic |
| [tdd](skills/tdd/SKILL.md) | Build one behavior through red, green, and refactoring | Automatic |
| [debug](skills/debug/SKILL.md) | Distinguish causes with evidence before repairing behavior | Automatic |
| [simplify](skills/simplify/SKILL.md) | Remove complexity only after understanding what it earns | Automatic |
| [test-reliability](skills/test-reliability/SKILL.md) | Control timing, isolation, resource ownership, and teardown | Automatic |
| [code-review](skills/code-review/SKILL.md) | Inspect requirements, implementation, and evidence independently | Automatic |
| [canonical-docs](skills/canonical-docs/SKILL.md) | Give accurate explanations one appropriate owner | Automatic |
| [adr](skills/adr/SKILL.md) | Preserve and maintain reasons that code cannot recover | Automatic |
| [adr-setup](skills/adr-setup/SKILL.md) | Establish a project's ADR convention from its existing documentation | User only |
| [adr-archive](skills/adr-archive/SKILL.md) | Audit, prune, consolidate, and archive historical decision records | User only |
| [conventional-commit](skills/conventional-commit/SKILL.md) | Express a coherent change using the chosen commit convention | Automatic |

### Modes

Modes offer distinct conversational postures for exploration, learning, and reflection.

| Skill | Judgment it provides | Invocation |
| --- | --- | --- |
| [grilling](skills/grilling/SKILL.md) | Explore ideas without imposing a goal or inventing the user's motives | User only |
| [teach](skills/teach/SKILL.md) | Build understanding through explanation and application | User only |
| [retro](skills/retro/SKILL.md) | Derive concrete improvements from real work | User only |

A task can enter anywhere. A clear defect can start directly with diagnosis; an existing pull request can start with review. Small tasks stay small.

For architecture rules, the Method/Binding/Calibration separation, and authoring constraints, see [docs/skill-architecture.md](docs/skill-architecture.md).

## Installation and invocation

```bash
npx skills add Celec7/good-calls
```

*Note: For repositories still referencing the earlier package path, `npx skills add Celec7/beyond-code` remains compatible.*

You can install the entire collection or select individual skills. Skill bodies are written in English; the catalog documentation is maintained in both English and Chinese.

### Host metadata

For `adr-setup`, `adr-archive`, `grilling`, `teach`, and `retro`, `SKILL.md` declares `disable-model-invocation: true`, and `agents/openai.yaml` declares `policy.allow_implicit_invocation: false`. These flags encode user-only intent for supporting platforms. The skill instructions also instruct models to require an explicit user prompt. Other skills remain automatically discoverable.

To verify structural integrity locally, run:

```bash
node scripts/check-skills.mjs
```

This checks frontmatter, required sections, valid relative links, catalog alignment, and formatting rules.

## Pairing with companion skills

Good Calls focuses on core software engineering judgment. For specialized tasks, select companion skills from [Matt Pocock's skills](https://github.com/mattpocock/skills) or other community sources:

| Companion | When it helps | Fit with this workflow |
| --- | --- | --- |
| [writing-for-agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md) | Writing skills or agent instructions such as AGENTS.md | Adds guidance on discovery, information hierarchy, and removing ineffective instructions; not a prerequisite for other skills. |
| [prototype](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md) | Exploring state behavior interactively or comparing UI variants | Supplies experiment formats. Agree on artifact retention beforehand; default behavior includes temporary branches and repository-local prototypes. |
| [wizard](https://github.com/mattpocock/skills/blob/main/skills/engineering/wizard/SKILL.md) | Guiding setup steps that require human credentials or actions | Generates an interactive script; use it for genuinely human-only steps and retain only when reusable. |
| [handoff](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md) | Explicitly handing work over to a fresh agent or session | Produces a redacted handoff in the OS temporary directory, referencing existing records rather than creating a parallel history. |

Select companions individually rather than installing overlapping packages wholesale. If duplicate skill names exist (such as `tdd` or `code-review`), choose one active definition and configure project conventions accordingly.

## Code, documentation, and decisions

- **Code is the source of truth for actual behavior.** Requirements and approved decisions describe intended behavior. A discrepancy may indicate a bug rather than permission to change requirements. Tests provide evidence and can themselves be flawed.
- **Documentation respects the project's structure.** When no convention exists and documentation is needed, `canonical-docs` provides standard options, including an optional tier taxonomy for larger codebases. No empty scaffold is created on setup.
- **Decisions belong in lightweight records.** When lasting rationale cannot be deduced from code, `adr` records the context, options, and consequences using `docs/agents/notes/{proposed,implemented,rejected,archived}/YYYY-MM-DD-topic.md` (or the repository's existing ADR format). Advance proposed records to implemented when shipping changes.
- **Task state remains ephemeral.** Keep temporary notes in conversational context. When a shared handover file is needed, `plan` offers an optional `docs/agents/work/<task>.md` template that is cleaned up or promoted upon task completion.

## Limitations

Good Calls does not promise bug-free software or replace developer judgment.

- **Model dependency**: The effectiveness of each skill depends on the underlying model's reasoning capabilities. While skills provide decision criteria, they cannot force a model to execute beyond its baseline reasoning limits.
- **Contextual value**: Skills earn their place only when a task involves meaningful ambiguity or non-trivial engineering trade-offs. For trivial edits, loading skills offers negligible gain.
- **Host support**: Invocation controls rely on platform-specific tool-calling and metadata support (`openai.yaml`, frontmatter conventions). Host behavior across different agent environments may vary.

## License

[MIT](LICENSE)
