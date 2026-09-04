# Multi-agent packages (Cursor, Codex, Claude Code, Antigravity)

CursorFlow packages are authored once under `.cursor/`, then mirrored so every supported coding agent can load them from its native paths.

## Canonical source

**Edit only under `.cursor/`**, then run:

```bash
./scripts/sync-packages.sh
```

(`./scripts/sync-skills.sh` is a deprecated alias for the same script.)

| Package | Source (Cursor) | Codex / Antigravity | Claude Code |
|---------|-----------------|---------------------|-------------|
| Rules | `.cursor/rules/` | `.agents/rules/` | `.claude/rules/` |
| Commands / workflows | `.cursor/commands/` | `.agents/workflows/` | `.claude/commands/` |
| Skills | `.cursor/skills/` | `.agents/skills/` | `.claude/skills/` |
| UI/UX reference | `.cursor/uiux_reference/` | `.agents/uiux_reference/` | `.claude/uiux_reference/` |
| Docs (this guide) | `.cursor/docs/` | `.agents/docs/` | `.claude/docs/` |

Sync **rewrites** internal path references in rules/commands/skills/uiux so each mirror points at its own tree (e.g. `.cursor/rules` → `.agents/rules` or `.claude/rules`). Docs are copied **verbatim** so the multi-agent map stays accurate.

## Agent notes

### Cursor
Uses `.cursor/` natively. No root instruction file required for discovery.

### Codex (OpenAI)
- Skills + shared packages: `.agents/`
- Optional root: `AGENTS.md` (see [AGENTS_SETUP.md](AGENTS_SETUP.md))

### Antigravity (Google; “anti”)
- Same project layout as Codex: `.agents/`
- Skills: `.agents/skills/` (legacy `.agent/skills/` may still work in older builds)
- Optional root: `AGENTS.md`

### Claude Code
- Rules: `.claude/rules/`
- Commands: `.claude/commands/`
- Skills: `.claude/skills/`
- Optional root: `CLAUDE.md`

## Skill package shape

```
<skill-name>/
├── SKILL.md          # required
├── reference.md      # optional
└── scripts/          # optional
```

## Adding or changing a package checklist

1. Edit under `.cursor/` (rules, commands, skills, uiux_reference, or docs).
2. Run `./scripts/sync-packages.sh`.
3. Confirm the same files exist under `.agents/` and `.claude/` (commands live as `workflows` on `.agents`).
4. Smoke-test at least one non-Cursor agent if that path matters for your team.

## Verify discovery

| Agent | Quick check |
|-------|-------------|
| Cursor | Rules/commands/skills under `.cursor/` |
| Codex | `.agents/skills`, `.agents/workflows`, `.agents/rules` |
| Antigravity | `/skills` or skill picker; workspace `.agents/` |
| Claude Code | `/skills`; `.claude/rules`, `.claude/commands`, `.claude/skills` |
