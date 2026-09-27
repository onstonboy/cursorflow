# Style 50 — Cozy Home Evening

Warm domestic comfort. Cream/terracotta palette, a lamp-glow vignette that flickers subtly, steam particles rising, content that "settles" into place like sinking into a couch.

Best for: food/recipe, home, family, slow-living, dating-lite, journaling — comfort brands.

## Tokens

```ts
room "#F5EDE1"  deeper "#EADFD0"  ink "#4A3B2E"
terracotta "#D98E6A"  olive "#8A9B6E"  butter "#F0D49A"  lamp glow "#FFE4B8"
Font: soft serif (Lora/Fraunces) headlines + warm sans (Nunito) body.
FPS 30.
```

Motion grammar: settling — elements arrive with a soft drop (30px down, rotate ±2°) and STAY — nothing exits mid-scene; scenes accumulate warmth. Lamp flicker: vignette warm overlay opacity breathes ±4% at random-ish intervals. Steam: blurred wisps rising and dissipating.

## Core mechanism

```tsx
// Lamp vignette (always on): radial warm glow from a corner + subtle flicker:
const flick = 0.92 + Math.sin(f/47)*0.04 + Math.sin(f/13.7)*0.04;
// Steam particle: narrow blurred div, translateY -120px over 90 frames,
//   opacity 0→.5→0, x wobbles ±8px sin — spawn 1 every ~40 frames at source.
// Settle entrance: opacity+translate(30px) 30 frames + rotate 2°→0 +
//   shadow compresses as it "lands". THEN IT STAYS — no exit animations
//   inside a scene (objects accumulate like a lived-in room).
// Cushion whitespace: layout leaves generous room — content occupies ~60% of
//   frame max.
// Screenshots: framed like a photo on a sideboard — thin warm border, soft
//   contact shadow, slight lean (rotate -1.5°) against the "wall".
// Scene transitions: warm crossfade + a lamp-brightness swell (cozy wipe) —
//   picture next part of the room revealed.
```

## Scene grammar (6–8 scenes, 100–140s)

S01: evening room fades in — lamp ignites, steam from a mug, title settles · S02: problem = cold blue "outside" window contrast · S03–S06: features as objects joining the room — each settles on a shelf/table (a recipe card, a photo frame holding the screenshot, a knit-textured chip) · S07: the whole warm room + logo glowing like the lamp itself → "come home to" CTA.

## Audio

- Music: lo-fi with vinyl crackle + rain — numpy: dusty Rhodes chords (sine+soft clip, lowpassed), brushed hat, rain noise bed + window-muffle lowpass, 75 BPM; crackle borrowed from Morsey recipe.
- SFX: rain on window constant-low, mug-clink, page-settle foley, fireplace pop occasionally.
- VO: close-mic warmth — like someone in the same room; smile audible; slow (-3%).

## Signature details

Objects never exit mid-scene (the room accumulates) · lamp flicker always on · steam wisps · photo-frame screenshots leaning on the wall · cold-outside/warm-inside problem framing.

Anti-patterns: cool palettes, fast exits, hard cuts, neon, empty minimalism (this is *warm clutter*), VO that sounds like a studio.
