# Style 32 — Hologram Float

Projection-in-air futurism. UI panels hover tilted over a dark void, edges chromatic-split, scanline sweeps, translucent light.

Best for: AI, AR/spatial, devtools, security, sci-fi-flavored brands.

## Tokens

```ts
void "#05060E"  holo: cyan "#5FE8FF" + magenta "#FF5FD0" split edges
panel fill: "rgba(95,232,255,0.06)" — translucent tint, not opaque
Font: techy sans (Space Grotesk/Inter) + mono data labels.
FPS 30.
```

Motion grammar: hovering physics — panels bob `sin(f/40)*6px` on offset phases, tilt ±2°; ignite = opacity + scanline sweep top→bottom (a bright 20px band travels the panel); edges flicker (opacity jitter 2 frames occasionally).

## Core mechanism

```tsx
// Holo panel: translucent fill + double-edge glow:
border:"1.5px solid rgba(95,232,255,.5)",
boxShadow:"0 0 24px rgba(95,232,255,.25), inset 0 0 30px rgba(95,232,255,.06)",
backdropFilter:"blur(2px)"
// Chromatic edges: duplicate panel content at translate(±2px,0), tinted
//   magenta/cyan, blend screen, opacity .5 — reads as hologram fringe.
// Scanline sweep: bright band div animates top→bottom across panel on entry
//   (and slow ambient sweeps continue).
// Emitter: panels project FROM a device/base — small cone-gradient below each
//   panel sells the projection illusion.
// Perspective: panels tilted rotateY ±12° facing a virtual center camera;
//   parallax drift: panels at different depths shift on camera pan.
// Screenshots: shown AS holograms — screenshot with cyan tint overlay +
//   scanlines + 80% opacity + fringe edges.
```

## Scene grammar (7–9 scenes, 90–120s)

S01: emitter boot — base lights, first panel scans into existence · S02: threat/problem holograms flicker red-shifted · S03–S07: each feature = a holo panel igniting around a central device; camera drifts between panels · S08: all panels collapse to points of light → reform as logo + CTA panel.

## Audio

- Music: airy synthwave/ambient-tech 100 BPM — numpy: glassy pad (sine+major7ths), arp pings, sub floor.
- SFX: hologram ignition (rising sine sweep + shimmer noise), data blips, sweep hums.
- VO: slightly reverbed, calm-techy. VN: giọng trầm, chậm, tự tin.

## Signature details

Cyan/magenta fringe split · scanline ignition sweeps · projection cone from emitter · bobbing physics · red-shifted enemy panels · collapse-to-points finale.

Anti-patterns: opaque panels, warm colors, flat front-on composition (tilt everything), missing emitter source (holograms need a source), over-fast motion.
