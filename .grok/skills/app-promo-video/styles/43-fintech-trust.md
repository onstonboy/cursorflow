# Style 43 — Fintech Trust

Clean institutional polish. Light theme, animated charts, number count-ups, hairline rules — competence you can feel.

Best for: banking, investing, insurance, budgeting, expense, B2B finance.

## Tokens

```ts
bg "#F6F8FB"  card "#FFFFFF"  line "#E2E8F0"
primary: brand navy/blue "#1B4BD8"  positive "#10B981"  negative "#EF4444"
ink "#0F172A"  muted "#64748B"
Font: Inter (500/600 UI) + tabular figures for numbers (`fontVariantNumeric:"tabular-nums"` — required so counters don't jitter).
FPS 30.
```

Motion grammar: precision — numbers count up over 30 frames (interpolate, round, tabular-nums); SVG chart strokes draw on via dashoffset; bars grow from baseline (scaleY origin-bottom); every ease `Easing.bezier(0.33,0,0.2,1)` — decisive, no bounce.

## Core mechanism

```tsx
// CountUp: const v = Math.round(interpolate(f,[at,at+30],[0,target]));
//   render with tabular-nums + comma formatting.
// Line chart: path with pathLength normalized; dashoffset → draws left→right;
//   end dot pulses at draw completion; area fill fades in after stroke.
// Bar chart: columns scaleY from baseline with 4-frame stagger.
// Donut: stroke-dasharray arcs rotating in.
// Screenshots: slim device frame (subtle — 8px bezel, soft shadow only) OR
//   floating flat with hairline border; chart echoes behind (blurred, 8%).
// Micro-ticks: small "+" deltas, green arrows — reassuring micro-signifiers.
// Cards: radius 16, border line, shadow "0 4px 24px -8px rgba(15,23,42,.08)".
```

## Scene grammar (7–9 scenes, 90–130s)

S01: logo + a single confident number counts up · S02: the problem framed as a red-loss chart that flattens · S03–S07: features each proven by a visualization — growth line, allocation donut, comparison bars; screenshot plates alternate left/right · S08: dashboard recap assembles → trust badges row → CTA.

Numbers should feel audited — every claim backed by a visual.

## Audio

- Music: confident minimal electronic 90–100 BPM — numpy: clean kick, sub bass on roots, plucked marimba-ish notes, occasional string swell at wins; NO surprises.
- SFX: tick on counters, soft chime on green-delta reveals.
- VO: clear fiduciary tone — precise, calm, slightly formal. Numbers read clearly.

## Signature details

Tabular-nums discipline · stroke-drawn charts · green-delta micro-signifiers · hairline rules · screenshot-as-evidence plating · the audited-recap finale.

Anti-patterns: bounce easing, gradients for decoration, emotional copy, dark mode (this style is light-mode confidence), charts that don't actually correspond to claims.
