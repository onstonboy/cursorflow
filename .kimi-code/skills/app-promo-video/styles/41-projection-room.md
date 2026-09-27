# Style 41 — Projection Room

A screening in a dark gallery. Scenes project onto a wall plane; dust motes in the light cone; slides advance with a mechanical clunk.

Best for: portfolio/creative tools, photo/video apps, design products, agencies, film-adjacent brands.

## Tokens

```ts
room "#0C0B0D"  wall "#2A2726" (warm dark)  light cone: radial "#FFF2D8" warm
projected content gets slight warm cast
Font: gallery serif (Playfair/Cormorant) titles + small mono catalog numbers.
FPS 30.
```

Motion grammar: projection mechanics — content sits on a perspective wall plane (slight trapezoid via rotateY ~3° + scale); slide advance = content cuts + white-light flash frame + projector clunk; dust motes float through the cone continuously; light flickers subtly (cone opacity ±3%).

## Core mechanism

```tsx
// Room: wall plane centered (70% frame), projector cone = big soft triangular
//   gradient from top-right "projector" position to wall, opacity flickering.
// Dust: ~50 tiny dots inside cone region only, drifting downward-sideways
//   slowly (seeded), twinkle opacity.
// Slide change: black 2 frames → white flash 1 frame → new content 12-frame
//   fade + a "settle" jitter (translate 3px→0) like the slide dropping in gate.
// Content: screenshots projected with warm cast + slight blur(0.4px) +
//   trapezoid — light never perfectly sharp.
// Wall details: picture-frame molding lines, catalog number plate below each
//   slide ("No. 04").
// Occasionally: slide jams — 3-frame double-image wobble (overlapping ghost).
```

## Scene grammar (6–8 scenes, 90–130s — gallery pace)

S01: projector warms up (cone ignites, dust appears, first slide clunks in: title) · S02: the problem hung like an exhibit with a curator's card · S03–S06: each feature = an exhibition piece — projected screenshot + serif title + catalog plate · S07: house lights rise slightly → final slide: logo + CTA etched like a gallery closing card.

## Audio

- Music: reverb-drenched piano/ambient — numpy: piano-sines with long decay + convolution-ish echo (delay repeats 0.4s), sparse, room-y.
- SFX: projector fan hum (constant low), slide clunk (metallic thunk 80ms) on every transition — the style's heartbeat; occasional shutter.
- VO: quiet docent/curator — reverbed slightly, reverent tone.

## Signature details

Clunk+flash transitions · dust only inside the light cone · warm projection cast on everything · catalog plates · the occasional slide-jam wobble · house-lights ending.

Anti-patterns: sharp digital content (degrade to projection quality), missing clunk, bright room, fast cuts, breaking the wall-plane illusion.
