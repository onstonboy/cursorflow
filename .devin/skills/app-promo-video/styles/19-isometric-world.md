# Style 19 — Isometric World

A miniature city of features viewed from above at 45°. Screens stand as extruded slabs on an iso plane; the camera glides between "stations".

Best for: smart-home, ecosystem products, finance suites, productivity platforms, games, logistics.

## Tokens

```ts
bg: soft pastel sky "#DCE9F5" or dusk "#1B2A4A" (pick per brand)
slab faces: top "#FFFFFF" / left "#C9D8E8" / right "#A9BED8" — fake 3D via 3 tinted faces
accent: brand color for active elements
Font: clean geometric sans (Poppins/Inter 600) — friendly scale-model look.
FPS 30.
```

Motion grammar: camera = single container `translate+scale` gliding between stations (60–90 frame moves, `Easing.inOut`). Elements pop up from the ground plane (scaleY 0→1 origin-bottom with slight overshoot). Slab hover-bob ±4px.

## Core mechanism

```tsx
// Iso plane: <div style={{transform:"rotateX(55deg) rotateZ(45deg)", transformStyle:"preserve-3d"}}>
// Slab (fake extrusion): 3 absolutely-stacked copies of the face rect,
//   offset down-right to fake depth: copy k at translate(2k, 2k) darker tint.
// Or true 3D: rotateX(55) rotateZ(45) + translateZ layering with preserve-3d.
// Station: a slab cluster — e.g. "SECURITY STATION" = lock slab + shield slabs.
// Camera: const cam = interpolate(f,[s0,s1],[focusA.x,focusB.x]…) applied to a
//   world div ~2400px wide; scale 1.0↔1.5 for push-ins.
// Pops: buildings rise with scaleY + a dust-puff div at base.
// Screenshots: mounted as "billboards" ON slabs — image on the top face, skewed
//   to match plane OR standing upright as flat panels (readable) — prefer upright.
```

## Scene grammar (6–8 scenes, 100–140s)

S01: empty plane → city pops in piece by piece, camera pulls wide · S02: camera glides to Station 1 "problem district" (cracked slabs) · S03–S06: camera visits 4 feature stations — each pops up around the arriving camera, billboard screenshot faces camera · S07: flyover of the whole completed world → zoom to logo slab + CTA flag.

Transitions: none — continuous camera flight. (This style's signature: it never cuts.)

## Audio

- Music: cozy synth/electronic 95–105 BPM — numpy: soft square lead arpeggio, warm bass, light kick; key-change lift when camera pulls wide.
- SFX: pop-pops as buildings rise, wind whoosh on camera moves.
- VO: tour-guide friendly — "và đây là…" energy, moderate pace.

## Signature details

Never cuts — one continuous flight · stations pop as camera arrives · upright readable billboards vs skewed top-faces (choose readable) · dust puffs · final flyover pull-back.

Anti-patterns: hard cuts between scenes, flat 2D layouts (commit to the plane), dark heavy palettes, real perspective (stay iso = charming).
