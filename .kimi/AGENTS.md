# Project agent instructions (Kimi)

## Rules

Follow `.kimi-code/rules/` (especially `common/project_rule_common.mdc` and any `project-rule_*` files). Prefer shared building blocks already in the repo over one-offs.

Root `AGENTS.md` also applies.

## Commands

Cook / review and related prompts: `.kimi-code/commands/`.

## Skills

Project skills live in `.kimi-code/skills/` (and `.agents/skills/` when present). Prefer a matching skill before inventing a new approach.

## UI/UX

When UI/UX is in scope, consult `.kimi-code/uiux_reference/`.

## Source of truth

Canonical authoring path: `.cursor/`. Keep mirrors in sync with `./scripts/sync-packages.sh`.

See `.cursor/docs/MULTI_AGENT_SKILLS.md` and `.cursor/docs/AGENTS_SETUP.md`.
