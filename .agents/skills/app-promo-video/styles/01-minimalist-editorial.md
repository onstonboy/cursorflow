# Style 01 — Minimalist Editorial

Calm, premium, print-like. The anti-spectacle: confidence through restraint, whitespace, and perfect type. Screenshots are evidence, not decoration.

Best for: wellness, finance-lite, journaling, premium productivity, D2C consumer brands.

## Tokens

```ts
bg "#FAF8F4"      // warm ivory
surface "#FFFFFF" // cards
line "#E4E0D6"    // hairlines only
ink "#1A1A18"     // near-black
muted "#8A867B"
accent "#2B5BFF"  // OR brand color, used <5% of pixels
Font: Inter Tight or Söhne-like (600/700 headlines) + optional serif (Tiempos/Newsreader italic) for ONE pull-quote word per scene.
FPS 30.
```

Motion grammar: `Easing.bezier(0.25, 0.1, 0.25, 1)` — smooth, unhurried. ONLY opacity + translateY ≤24px over 30–45 frames. No rotation, no scale pops, no blur, no particles.

## Core mechanism

```tsx
// 12-col bento grid measured in px. Cards are flat — NO shadow ever.
const Grid: React.FC = ({children}) => (
  <div style={{display:"grid", gridTemplateColumns:"repeat(12, 1fr)",
    gap: 24, padding: "96px 120px", height:"100%"}}>{children}</div>);
// Entrance: single shared helper — fade + rise 24px over 40 frames. Nothing else animates.
// Screenshots: NO phone frame. 1px border, borderRadius 12, natural aspect — like a print plate.
```

Hairline rules draw themselves: width 0→100% over 30 frames. Section numbers "01 / 02" in small mono or tracked caps.

## Scene grammar (7–8 scenes, 120–150s)

S01: single sentence headline centered, nothing else 3s · S02: hairline + problem statement · S03–S06: one feature per scene — left column text (rarely right), right column screenshot plate; bento alternates · S07: quiet testimonial/stat in serif italic · S08: wordmark + "Available on…" text-only CTA.

Scene speed: all 1.0 — never speed-scale this style. Density comes from cuts, not motion.

## Audio

- Music: felt piano or solo cello, 55–65 BPM, huge silences; numpy: single sine-piano notes (3 harmonics, exp decay 2.5s), no drums, no bass below A1.
- VO: slower than conversational (-5% rate), low energy, intimate close-mic feel. Sentences end before scene ends — leave 1.5s of music-only air.
- Mix: ducking ratio 12:1 (aggressive), threshold 0.01.

## Signature details

Page-number footer persistent · em-dash typography · ONE italic serif word per scene max · hairline rules as transitions.

Anti-patterns: gradients, shadows, rounded "cute" corners >16px, icons, emoji, more than 2 font families, anything that bounces.
