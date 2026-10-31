# Documentation Overview

This directory houses the internal engineering documentation and architectural records for Good Calls.

Following the principle of one home per fact under [canonical-docs](../skills/canonical-docs/SKILL.md), each document owns a distinct role:

| Document | Purpose | Audience |
| :--- | :--- | :--- |
| [skill-architecture.md](skill-architecture.md) | **Architecture contract:** defines the three layers (Method, Binding, Calibration), frontmatter rules, allowed entries, and authoring constraints for skills. | Skill authors and contributors |
| [design-philosophy.md](design-philosophy.md) | **Design philosophy and evolution:** explains the core SWE gap, the role of developers as the intermediate layer, and the five historical evolution phases with empirical test data. | Engineers and evaluators seeking project rationale |
| [agents/notes/](agents/notes/implemented/2026-10-09-skill-architecture-contract.md) | **Architecture decision records (ADRs):** durable technical decisions and trade-offs made in this repository. Follows [adr](../skills/adr/SKILL.md). | Maintainers and contributors |
| [templates/SKILL.template.md](templates/SKILL.template.md) | **Authoring skeleton:** reusable starting skeleton for authoring new skills. Follows [skill-authoring](../skills/skill-authoring/SKILL.md). | Skill authors |

## Standing Agent Instructions

For operational rules and invariants governing AI coding sessions in this repository, see root [AGENTS.md](../AGENTS.md).

## Verification

To validate structural compliance, relative links, and formatting across documentation and skills:

```bash
python3 scripts/check_skills.py
python3 skills/adr/scripts/check_adr.py
```
