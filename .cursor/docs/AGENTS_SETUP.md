# Setup notes: Codex, Claude Code, Antigravity

Companion to [MULTI_AGENT_SKILLS.md](MULTI_AGENT_SKILLS.md) (covers **all** packages, not only skills).

After copying CursorFlow into a project, run `./scripts/sync-packages.sh` whenever you change `.cursor/`.

---

## Package map

| Concern | Cursor | Codex / Antigravity | Claude Code |
|---------|--------|---------------------|-------------|
| Rules | `.cursor/rules/` | `.agents/rules/` | `.claude/rules/` |
| Commands | `.cursor/commands/` | `.agents/workflows/` | `.claude/commands/` |
| Skills | `.cursor/skills/` | `.agents/skills/` | `.claude/skills/` |
| UI/UX | `.cursor/uiux_reference/` | `.agents/uiux_reference/` | `.claude/uiux_reference/` |
| Docs | `.cursor/docs/` | `.agents/docs/` | `.claude/docs/` |

---

## Codex (OpenAI)

Optional root file `AGENTS.md`:

```markdown
# Project agent instructions

## Rules
Follow `.agents/rules/` (especially `common/project_rule_common.mdc`).

## Workflows
Use prompts under `.agents/workflows/` (cook, review, common/*).

## Skills
Use matching skills under `.agents/skills/` before inventing a new approach.

## UI/UX
When UI is in scope, consult `.agents/uiux_reference/`.
```

---

## Claude Code

Optional root file `CLAUDE.md`:

```markdown
# Claude Code — project notes

## Rules
Follow `.claude/rules/` (especially `common/project_rule_common.mdc`).

## Commands
Use `.claude/commands/` for cook / review and common prompts.

## Skills
Prefer matching skills in `.claude/skills/` (`/skills` to list).

## UI/UX
When UI is in scope, consult `.claude/uiux_reference/`.
```

---

## Antigravity (Google; “anti”)

Uses the same `.agents/` layout as Codex. Reuse the `AGENTS.md` starter above. Confirm skills with `/skills` when using the CLI.

---

## Install into another project

1. Copy `.cursor/`, `.agents/`, `.claude/`, and `scripts/sync-packages.sh` into the target repo root.
2. Optionally copy root `AGENTS.md` and `CLAUDE.md`.
3. After editing anything under `.cursor/`, run `./scripts/sync-packages.sh`.
