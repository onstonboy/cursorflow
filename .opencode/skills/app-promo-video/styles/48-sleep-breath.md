# Style 48 — Sleep Breath

The slowest promo ever made on purpose. One master breathing sine drives everything — scale, opacity, glow — like the app exhaling you to sleep.

Best for: sleep, meditation, anxiety/mental-health, baby sleep, ASMR-adjacent products.

## Tokens

```ts
deep indigo "#0D1029" → "#1A1640" gradient; moon "#F5EED8" soft
lavender "#8B7FD8"  accent glow "rgba(139,127,216,.3)"
ink "#C9C4E8" (low contrast ON PURPOSE)
Font: light rounded (Quicksand 300/400, Nunito Light); large x-height, soft.
FPS 30.
```

Motion grammar: **one breath clock** — `breath = Math.sin(f * 2π / BREATH)` where BREATH ≈ 300 frames (10s in-out). Everything derives: master scale 1+0.03·breath, glow opacity 0.7+0.3·breath, y-drift ±6px·breath. Nothing moves faster than the breath. Entrances take 60+ frames.

## Core mechanism

```tsx
const BREATH = 300; // frames per full breath cycle
const breath = Math.sin(useF() * Math.PI * 2 / BREATH);
// Apply globally: root scale = 1 + breath*0.02; glows = .7+.3*breath;
//   floating elements y += breath*8.
// Phases: align VO lines to exhale moments — content arrives as the breath
//   releases (feels like the video is breathing WITH the viewer).
// Elements: soft blurred orbs (blur 30px) drifting ±10px; stars = tiny dots
//   twinkling slowly (sin, random phase, amplitude .3).
// Screenshots: dimmed to 70% + slight blur(.5px) + glow halo — screens shown
//   as if in dark room (lighter elements bloom gently).
// Optional real moon-phase arc across scenes.
// Text: one line at a time; each line lives a full breath then releases.
```

## Scene grammar (5–7 scenes, 110–150s — yes, longer is fine here)

S01: darkness → breath begins, logo fades up over 60 frames · S02: the day's noise = tight jittery elements that gradually SYNC to the breath (the metaphor!) · S03–S05: features shown like constellations — breathe in, feature glows; breathe out, caption appears · S06: everything slows further → wordmark barely breathing → "rest now" CTA.

Rule: if a moment feels too slow, it's probably right.

## Audio

- Music: drone ambient — numpy: 432Hz-ish sine pad stack (root + 5th + octave, beating ±0.3Hz), ocean/pink noise bed very low, occasional single piano note (decay 4s) every ~8s. NO percussion.
- SFX: none sharp. Soft chime ONLY at breath peaks.
- VO: whisper-slow — rate -8%, pitch -1Hz, long pauses between phrases; "breathe with me" delivery. VN: giọng mẹ ru.
- Mix: music constant + low; VO floats above like breath.

## Signature details

The single breath clock driving all motion · noise elements syncing to breath (the thesis scene) · dimmed+blooming screenshots · 60-frame entrances · a video that could actually help someone sleep.

Anti-patterns: any fast motion, bright whites, percussion, >1 idea per 10 seconds, jump cuts, exclamation marks.
