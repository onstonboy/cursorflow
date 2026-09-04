# Project agent instructions

## Rules

Follow coding standards in `.agents/rules/` (especially `common/project_rule_common.mdc` and any `project-rule_*` files). Prefer shared building blocks already in the repo over one-offs.

## Workflows

Cook / review and related long prompts: `.agents/workflows/` (including `common/` and generated `specify/` files when present).

## Skills

Project skills live in `.agents/skills/`. When a task matches a skill `description`, read that skill’s `SKILL.md` and follow it before inventing a new approach.

## UI/UX

When UI/UX is in scope, consult `.agents/uiux_reference/`.

## Source of truth

Canonical authoring path: `.cursor/`. Keep mirrors in sync with `./scripts/sync-packages.sh`.

See `.cursor/docs/MULTI_AGENT_SKILLS.md` and `.cursor/docs/AGENTS_SETUP.md`.
