# Style 10 — Risograph Collage

Indie zine aesthetic. Misregistered ink plates, heavy grain, torn magazine fragments — printed-media energy with deliberate imperfection.

Best for: creative tools, photo/video apps, fashion, music, indie magazines, portfolio products.

## Tokens

```ts
bg "#F3EDE3" (newsprint)
inks: "#004F8B" (riso blue) "#FF4848" (riso red/flo-pink) "#FFD800" (riso yellow) "#1A1A1A"
Font: display serif condensed (Instrument Serif / Playfair) headlines + grotesk captions. Headlines may sit ON images.
FPS 30.
```

Motion grammar: elements settle into place like glued fragments — rotate -3..3°, arrive with a paper-stick "thud" (scale 1.06→1 in 8 frames). Plates drift: the 3 color channels of a screenshot slide INTO registration over ~20 frames (and back out on exit).

## Core mechanism

```tsx
// Misregistration = the whole look. Screenshot rendered 3x:
{["#004F8B","#FF4848","#FFD800"].map((c,k)=>(
  <Img src={shot} style={{position:"absolute",inset:0, mixBlendMode:"multiply",
    filter:"grayscale(1) brightness(1.15)", background:c, opacity:0.9,
    transform:`translate(${(1-t)*(k-1)*14}px, ${(1-t)*(1-k)*10}px)`}}/>))}
// then one clean copy blends in on top at t=1 (opacity ramp).
// Torn edges: clip-path polygon with 16–24 irregular points (frozen seed).
// Grain: animated noise overlay — generate 4 noise PNGs, cycle by frame (f%4)
//   at mix-blend-mode:overlay, opacity 0.5 → living print grain.
// Halftone dots on ink areas: repeating radial-gradient 7px dots.
```

## Scene grammar (7–8 scenes, 90–120s)

S01: masthead-style title (serif, huge, maybe rotated -2°) · S02: collage page builds — fragments stick in · S03–S06: each feature a "spread" — screenshot plate registers + serif claim + torn paper scraps with captions · S07: index-card CTA stapled center, "issue no.01" details.

Transitions: page-wipe = a large torn fragment slides across.

## Audio

- Music: jazzy lo-fi 82–88 BPM — numpy: swung hats, upright-ish bass (sine+soft clip), rhodes chord stabs (see make_music pluck recipe, detune ±0.4%).
- SFX: page-turn swishes, tape/staple clicks, tape-stop (pitch-drop 300ms) transitions.
- VO: artsy, relaxed — like describing a zine. Slight saturation/tape warmth on voice EQ (add `equalizer=f=400:g=2`).

## Signature details

Ink-plate registration slides · cycling grain (f%4) · staples/pins visible · torn clip-path edges · issue-number masthead · halftone on flat color fills.

Anti-patterns: clean digital edges, perfect alignment, gradients, glows, minimalism (this style is layered and busy-on-purpose).
