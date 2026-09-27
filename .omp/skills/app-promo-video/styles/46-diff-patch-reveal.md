# Style 46 — Diff / Patch Reveal

The promo as a pull request. Before-lines slide out in red, after-lines slide in green, with a line-number gutter and commit-hash scene markers.

Best for: devtools, API products, SDKs, dev-adjacent productivity, technical audiences.

## Tokens

```ts
editor bg "#0D1117" (github-dark)  gutter "#161B22"  line "#30363D"
del-bg "rgba(248,81,73,.15)" del "#F85149"   add-bg "rgba(63,185,80,.15)" add "#3FB950"
syntax: "#79C0FF" kw, "#A5D6FF" str, "#FF7B72" fn
Font: JetBrains Mono throughout — it IS a code editor.
FPS 30.
```

Motion grammar: patch application — removed lines slide left + fade over 10 frames, added lines slide in from right over 10 frames with 4-frame stagger per line; +/- gutter markers flip color; hunk headers `@@ -12,3 +12,7 @@` appear as separators.

## Core mechanism

```tsx
// Editor chrome: tab bar, breadcrumb, line-number gutter column — always visible.
// Diff line: <DelLine> (red bg, "- " prefix, slides left+out) /
//            <AddLine> (green bg, "+ " prefix, slides in)
// Apply per-hunk: lines transform in place — a removed block collapses
//   (height 24→0 over 8 frames) as the added block expands (0→24×n).
// Scene markers = commit cards: "a1f9c2e — feat: encrypt messages" with hash
//   as mono accent + relative-time "2 min ago".
// Screenshots: embedded as "files changed" — image preview inside the PR view,
//   or ASCII-thumbnail in a comment block.
// Cursor/selection: occasionally a blue selection block highlights the key line.
// Blame/hover: tooltip card pops on the important line.
```

## Scene grammar (7–9 scenes, 90–130s)

S01: repo opens — README types the product pitch · S02: problem shown as "current code" — flagged with a red BUG comment · S03–S07: each feature lands as a commit — commit card → diff applies (red out, green in) → result file = screenshot preview · S08: PR merged — green "Merged" pill, branch deleted, release tag `v1.0` → CTA as `npm i yourapp`.

## Audio

- Music: minimal synth pad + subtle beat 95 BPM — numpy: warm pad, tick hats; keep it nerdy-clean.
- SFX: keystroke clusters during diffs, commit "whoosh" on merge, notification ding on PR events, terminal confirm beep.
- VO: dev-voice — dry, precise, slightly ironic allowed. Or commentless — the diff tells it.

## Signature details

Commit-hash scene markers · red/green line choreography · collapsing/ expanding hunks · merged-pill payoff · `npm install` CTA · the blue selection accent.

Anti-patterns: non-mono fonts, prose paragraphs, fake code that doesn't parse logically (devs WILL read it — write real-looking code), missing gutter.
