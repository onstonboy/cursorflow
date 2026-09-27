# Style 02 — Brutalist Terminal

Raw engineering document. Declassified-blueprint energy: monospace, boxes, stamps, hard snaps. Ugly-on-purpose executed perfectly.

Best for: devtools, security, infra, CLI apps, data tools, anything developers respect.

## Tokens

```ts
bg "#0D0D0D" or paper "#F2F0E9" (pick ONE per video, dark preferred for devtools)
ink "#E8E8E3" (dark mode) / "#111" (paper)
accent "#FF3B00" // signal orange-red — stamps/warnings only
mono: JetBrains Mono / IBM Plex Mono 400,700 — ALL text including headlines.
Grid: visible 8px baseline grid via repeating-linear-gradient at 6% opacity.
FPS 30.
```

Motion grammar: `steps()` everywhere — elements appear in 3–4 discrete jumps, NOT smooth. `interpolate` with `easing: (t)=>Math.floor(t*4)/4`. Instant snaps read as "machine".

## Core mechanism

```tsx
// Stepped easing — the whole style's feel lives here:
const snap = (t:number) => Math.floor(t*5)/5;
// ASCII chrome as text components, not images:
<Box title="FEED.LOG">  // renders ┌─ FEED.LOG ──────────┐ + content + └─────────────┘
// Stamps: uppercase mono, accent border 3px, rotate -6deg, scale in 1 frame + shake 2px
// Blinking cursor █ at end of every typed line: opacity = f%30<15
// Typewriter: chars appear 2/frame, monotone
```

## Scene grammar (6–9 scenes, 90–140s)

S01: boot sequence — fake log lines scroll fast `[OK] app.init` · S02: problem framed as ERROR stamp · S03–S07: each feature = ASCII-boxed module; screenshots inside `┌ screenshot.png ────┐` border frames, 8px grid-aligned · S08: `$ app --install` CTA typed out.

Transitions: hard cut or screen-clear (instant black→content), NEVER fades.

## Audio

- Music: square-wave bassline 120 BPM + noise hats (numpy: `np.sign(np.sin())` squares, `randn` bursts), deliberately dry.
- SFX matter more than music: keyclicks, beeps, glitch-hit on stamps.
- VO: terse, fast (+5%), declarative. OR skip VO entirely — text-only with typing SFX is in-style.
- Mix: voice pushed forward (volume 2.5), ducking threshold 0.02.

## Signature details

Corner registration crosses `+` · frame counter `F/4410` bottom-right · red ERROR stamps · all-caps with tracking · version strings `v2.4.1` · deliberate 1px misalignments that snap correct.

Anti-patterns: rounded corners >2px, gradients, smooth easing, drop shadows, any font that isn't mono, emoji (ASCII `:)` allowed).
