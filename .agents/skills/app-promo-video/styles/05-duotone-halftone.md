# Style 05 — Duotone Halftone

Sports-poster aggression. Two colors, halftone texture, giant skewed numerals, cuts on every beat.

Best for: fitness, sports, running, challenge apps, music-event products.

## Tokens

```ts
c1 "#0A0A0A" (ink)   c2 "#E8FF00" (electric lime) — or brand pair (purple+orange, navy+coral)
Only these two + their halftone mix. No third color, no mid-grays except via dither.
Font: condensed display 900 (Druk/Archivo Black), numerals skewed -8°. Mono for stat labels.
FPS 30.
```

Motion grammar: hard cuts on beat + explosive scale-ins (0.9→1.0 over 6 frames, `Easing.out(Easing.exp)`). Elements never "fade" — they CUT or SLAM.

## Core mechanism

```tsx
// Preprocess screenshots to duotone halftone BEFORE Remotion (do once, commit result):
//   magick shot.png -colorspace Gray -ordered-dither o8x8,8 \
//     +level-colors "#0A0A0A","#E8FF00" shot-duo.png
// Halftone bg texture: repeating radial-gradient dots at 6px, opacity pulsing with beat.
// Giant scene numerals: fontSize 400+, skewY(-8deg), clipped to bottom edge:
<div style={{fontSize:420, fontWeight:900, transform:"skewY(-8deg)",
  position:"absolute", bottom:-60, left:40, color:c2, letterSpacing:"-0.04em"}}>01</div>
// Beat quantize: const BEAT = FPS*60/BPM; all `at` times are integer multiples of BEAT.
```

## Scene grammar (8–10 scenes, 60–100s — punchy)

S01: numeral "01" + verb word SLAM ("RUN.") · S02–S06: feature = numeral + 2-word claim + duotone screenshot flash-cropped (no frame — bleed to edges, clip-path parallelogram skewed -8°) · S07: stat triple (numbers count up in 20 frames) · S08: wordmark + badge, held exactly 1 bar of music.

Zero crossfades. Transitions = cut on kick drum.

## Audio

- Music: 128–140 BPM aggressive drums — numpy: saturated kick (`tanh(sin*4)`), clap noise bursts, distorted 808 sub on roots, siren/riser noise sweeps between scenes.
- VO: short imperative bursts ("Track. Compete. Win.") — or VO-free with bold captions. If VN: punchy, no particles.
- Mix: music dominant; VO ducks music only -3dB.

## Signature details

Halftone dots that scale with the beat · -8° world skew · number counting SFX-tick · scene numerals as the ONLY scene markers · flash frames (1-frame white/lime invert) on drop beats.

Anti-patterns: soft easing, whitespace, thin fonts, pastel anything, rounded friendly cards, fades.
