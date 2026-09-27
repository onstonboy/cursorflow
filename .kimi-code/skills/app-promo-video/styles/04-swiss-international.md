# Style 04 — Swiss International

Museum-poster discipline. A visible mathematical grid, three colors, perfect hierarchy. The grid is shown, not hidden.

Best for: B2B SaaS, productivity, news/media, finance, architecture-adjacent products.

## Tokens

```ts
bg "#FFFFFF"   ink "#111111"   accent "#E30613" (signal red — ONE element per scene may use it)
line "#111111" hairlines
Font: Inter Tight / Helvetica Now — headlines 500 weight deliberately (Swiss uses medium, not black), size 60–90, tight tracking -0.02em. Mono (IBM Plex Mono) for labels/indices only.
FPS 30.
```

Motion grammar: `Easing.bezier(0.4, 0, 0.2, 1)`. Movement along GRID AXES ONLY — horizontal wipes or vertical reveals. Rotation and diagonal motion are banned. Transitions = wipe blocks sweeping on-axis.

## Core mechanism

```tsx
// The grid IS visible: 12-col lines rendered as 1px divs at 8% black, always on screen.
// Elements reveal via clip-path inset wipes along an axis:
clipPath: `inset(0 ${(1-t)*100}% 0 0)`   // left→right reveal
// Panels slide horizontally to their grid column — never float free.
// Rule of accent: compute per scene — exactly ONE red element allowed (a rule line, a keyword, an index number).
// Index labels: "01 —", "02 —" in mono, top-left of each panel.
```

## Scene grammar (8–10 scenes, 100–140s)

S01: wordmark left-aligned col 1–6, thin rule under, nothing else · S02: problem as a numbered statement "01 / Your data is public" · S03–S08: feature modules — screenshot flush in grid cell (cropped to fill, no device frame, no radius), caption in mono gutter · S09: colophon-style end card (name / category / stores) like a poster imprint.

Transitions: a red or black bar wipes on-axis carrying the new scene.

## Audio

- Music: minimal techno or modular synth 100–115 BPM, mechanical precision, no swing — numpy: pure sine bass sequence + precise click hats, dry.
- VO: measured, neutral-anchor voice. Short factual sentences. No exclamation.
- Mix: very subtle duck (ratio 6:1), music level low overall — this style is quiet.

## Signature details

Visible gridlines that never leave · flush-bleed images · mono captions · the single red accent per scene · ragged-right type, never justified, never centered (except final mark).

Anti-patterns: centered layouts, rounded cards, shadows, more than 3 colors, serif fonts, bouncy easing, anything diagonal.
