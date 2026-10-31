# AGENTS.md

Standing orders for AI coding agents working in this repository.

## 1. Project Invariants

- Good Calls is a collection of twenty independent, host-agnostic engineering skills.
- Better judgment, less ceremony: do not introduce mandatory workflow engines, centralized routers, CLI status ledgers, or rigid phase gates. Keep skills modular and decoupled.
- All 20 skills live in `skills/<name>/SKILL.md`. Never hardcode the suite name inside an individual skill body.

## 2. Documentation Discipline

Follow the documentation skills strictly when authoring or revising prose:

- **One home per fact ([canonical-docs](skills/canonical-docs/SKILL.md)):** never dump information into the nearest file. Architecture belongs in `docs/skill-architecture.md`; design trade-offs belong in ADRs; consumer contracts belong in `README.md`; code mechanics belong in JSDoc.
- **Current state only ([canonical-docs](skills/canonical-docs/SKILL.md)):** describe the system as it stands right now at HEAD. Never write change narration ("previously", "in this update we added", "was changed to avoid"). Commits and PR descriptions own change history.
- **Dense and economical prose ([prose-standard](skills/prose-standard/SKILL.md)):** state complete contracts in the fewest words. Eliminate preambles, transitional filler, and narrative setup. Avoid paragraph walls. Reserve bold emphasis strictly for clauses that alter behavior or prevent error.
- **Strip session residue ([trim-reasoning-leakage](skills/trim-reasoning-leakage/SKILL.md)):** run the slop checklist before saving. Remove step-by-step reasoning transcripts, review choreography ("as requested"), and status stamps ("implemented!").
- **Zero em-dash rule:** em dashes (`\u2014`) are strictly banned across all Markdown files. Use colons, commas, semicolons, or parentheses.

## 3. Architecture Decision Records (ADRs)

Apply [adr](skills/adr/SKILL.md) for lasting engineering trade-offs:

- **Proposing:** copy `skills/adr/templates/proposed.md` to `docs/agents/notes/proposed/YYYY-MM-DD-topic.md`. Retain the top HTML lifecycle comment.
- **Implementing:** when code lands, move the record to `docs/agents/notes/implemented/` in the same diff. Rewrite `## Proposal` into present-tense `## Decision`, replace acceptance/risks with `## Consequences` and `## Verification`, and commit the ADR together with the code.
- **Pruning and archiving:** use [adr-archive](skills/adr-archive/SKILL.md) only on explicit user request.

## 4. Verification and Tooling

Before completing any task, execute the checkers:

```bash
python3 scripts/check_skills.py
python3 skills/adr/scripts/check_adr.py
node scripts/check-skills.mjs
```

Python scripts must use standard library only, carry type annotations passing `ty check`, and comply with `ruff check` and `ruff format`.
