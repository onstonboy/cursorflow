# Style 34 — Neon Arcade

Night-city glow. Everything is light on darkness — stacked glows, perspective grid floor racing to the horizon, chrome type.

Best for: music, nightlife, gaming, dating, events, anything that lives after dark.

## Tokens

```ts
night "#0A0014"  neon set: "#FF2E88" (pink), "#00F0FF" (cyan), "#B8FF00" (acid), "#7B2EFF" (violet)
chrome text: linear-gradient "#E8E8F0"→"#8A8AB8"→"#F0F0FF"
Font: wide display (Orbitron-style / stretched sans) for titles; mono for HUD bits.
FPS 30.
```

Motion grammar: speed + glow-pulse — grid floor scrolls continuously (`translateY` on a perspective-tiled div, wrapping); neon pulses via shadow-intensity oscillation; elements slide in with light-trail ghosts (2–3 trailing copies fading).

## Core mechanism

```tsx
// Neon glow recipe (on text AND shapes):
textShadow: `0 0 8px ${c}, 0 0 24px ${c}88, 0 0 48px ${c}44` — stack 3 radii.
// Grid floor: bottom 45% of frame, div with repeating-linear-gradient lines,
//   transform: perspective(500px) rotateX(60deg); scroll = offsetY loop.
// Chrome headline: background gradient on text with backgroundClip:"text".
// Light trails: element renders 3x — same content, opacity 0.5/0.25/0.1,
//   translateX trailing -12/-24/-36px behind motion direction.
// Screenshots: framed as "neon signs" — screen inside a rounded rect with
//   dual-color glow border (pink+cyan gradient stroke), floating above grid.
// Occasional glitch: 3-frame RGB split + slice shift on beat hits.
```

## Scene grammar (8–10 scenes, 80–110s)

S01: horizon ignites, logo in chrome rises from grid · S02: problem in flickering broken-sign aesthetic · S03–S07: each feature = a neon sign igniting (flicker-on sequence: 3 rapid opacity toggles then stable) with light-trail entries; screenshots as glowing signage · S08: drive-through finale — camera pushes toward horizon, CTA as the biggest sign.

## Audio

- Music: synthwave/synthpop 110 BPM — numpy: saw pad chord stabs, octave bass, gated snare (noise + verb tail), arp lead; sidechain pads pump on kick.
- SFX: neon buzz (90Hz + harmonics low volume always), ignition flicker crackles, car-pass whoosh.
- VO: cool night-DJ energy — relaxed, confident, slight reverb.

## Signature details

Triple-radius glow · scrolling perspective floor · flicker-on ignitions · light-trail ghosts · chrome type · RGB-split glitch on drops.

Anti-patterns: daylight palettes, matte surfaces (everything glows), sans-serif body at small sizes (use mono), clean cuts without trails, conservative spacing.
