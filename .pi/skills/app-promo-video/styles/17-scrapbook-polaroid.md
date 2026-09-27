# Style 17 — Scrapbook Polaroid

A desk covered in memories. Screenshots as polaroids that drop onto a table with tape and handwritten captions; the camera drifts across the collage.

Best for: photo apps, journal/diary, family, travel journals, memory features, wedding/event apps.

## Tokens

```ts
desk "#C9B79C" (wood/cork warm) or "#8A9B7E" (felt)
polaroid "#FDFDF8"  tape "rgba(240,225,170,.65)"  ink "#3B3328"
caption font: handwriting (Caveat/Kalam) — captions are ALWAYS handwritten.
FPS 30.
```

Motion grammar: gravity + settle — polaroids fall from above with rotate (drop 300px, rotate ±8°, land with a tiny bounce 4 frames + shadow snap-on). Camera = ONE parent container slowly translated/zoomed (Ken Burns) across the whole desk — all items pinned inside it.

## Core mechanism

```tsx
// World container: 2600×1600 desk surface, everything absolute inside.
// Camera: <div style={{transform:`translate(${cx}px,${cy}px) scale(${z})`}}>
//   cx/cy/z interpolated between per-scene focus points.
const Polaroid: React.FC<{src:string; caption:string; at:number; x:number;y:number;rot:number}>
// white padded card (paddingBottom large), Img inside, caption handwritten below,
// tape strip on top edge at slight rotate; entry = drop+rotate+bounce;
// shadow appears ON landing (opacity ramps in 5 frames after drop completes).
// Extras: string-clipped prints, ticket stubs, washi tape pieces, dried-flower divs —
//   scatter deterministic via seed.
```

## Scene grammar (7–9 scenes, 90–130s)

S01: camera drifts over empty-ish desk → first polaroid drops with the app title caption · S02: problem polaroids ("screenshots that got screenshotted") · S03–S07: feature polaroids accumulate — camera pans between them; real screenshots IN the polaroid frames; handwritten arrows connect related cards · S08: final overhead pull-back revealing the full collage that spells/shapes the logo → title card.

Transitions: camera drift IS the transition — never cut.

## Audio

- Music: warm folk/indie 95–105 BPM — numpy: fingerpicked-ish sine plucks (quick arpeggio pattern), upright bass, tambourine shakes, maybe melodica-timbre lead (triangle wave + vibrato).
- SFX: soft shutter click on each polaroid landing, paper thud, tape stretch.
- VO: warm storyteller, personal ("remember when…"), gentle pace -3%.

## Signature details

Camera drift replaces cuts · tape strips always slightly rotated · captions handwritten in margins · the big pull-back reveal · each polaroid's shadow snaps only on landing.

Anti-patterns: device frames (polaroid IS the frame), dark themes, digital-perfect alignment, fast cuts, holographic/neon anything.
