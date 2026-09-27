# Style 31 — Three.js Device Orbit

Flagship-product cinematics. A real 3D phone (or abstract object) with your screenshots texture-mapped onto it, lit and dollied like a car commercial.

Best for: premium flagship apps, fintech, health+device companions, any brand wanting Apple-keynote energy.

## Tokens

```ts
bg: studio gradient "#0A0A0C" → "#1A1A22" (dark) OR clean "#E9EAEE" studio sweep
rim/accent: brand color as a light source (colored rim light is the signature)
Font: minimal — floating grotesk captions, huge whitespace discipline.
FPS 30.
```

Requires `@remotion/three` + `three` + `@react-three/fiber` + `@react-three/drei`.

## Core mechanism

```tsx
import {ThreeCanvas} from "@remotion/three";
// Phone: RoundedBox geometry + screen plane with screenshot as texture:
<mesh><boxGeometry args={[1.4,2.9,0.08]}/><meshStandardMaterial color="#0B0B0F"
  metalness={0.7} roughness={0.3}/></mesh>
<mesh position={[0,0,0.045]}>
  <planeGeometry args={[1.3,2.78]}/>
  <meshBasicMaterial map={screenshotTexture}/></mesh>
// Camera: orbit rig — cam.position set by interpolated spherical coords
//   (radius 4→2.6 push-ins, theta sweeps 30°–60° per scene).
// Lighting: key SpotLight + rim PointLight in brand color + ambient 0.15.
//   envMap: drei <Environment preset="studio"/> for reflections.
// Reflection floor: <ContactShadows> or a mirror plane (drei MeshReflectorMaterial).
// Scene handoffs: 3D device shots alternate with full-frame typography cards —
//   cutting between 3D and 2D is the rhythm (device never shares frame with big type).
```

## Scene grammar (7–9 scenes, 90–130s)

S01: black → rim light ignites → device rotates out of darkness · S02: problem — device shows the "before" screen, camera low angle · S03–S07: orbit moves — each feature a camera setup (top-down, 45°, profile); screen texture swaps per feature (crossfade 8 frames); typography cards cut between orbit shots · S08: hero orbit (slow 180° sweep, logo glow) → device settles face-on → CTA overlays.

## Audio

- Music: orchestral-hybrid / cinematic-electronic 90–100 BPM — numpy: string-pad (detuned saws lowpassed), sub-bass drops at cuts, taiko-ish hits on reveals.
- SFX: whoosh on camera moves, deep boom on cut-to-type cards.
- VO: trailer-voice — deep, sparse lines, lots of space. -3Hz pitch, deliberate.

## Signature details

Colored rim light · contact shadows/reflection floor · texture swaps as feature transitions · alternating 3D/2D rhythm · the slow hero-orbit finale.

Anti-patterns: 3D device sharing frame with paragraphs, static camera, flat unlit materials (metalness+env required), screenshots too small on screen (maximize texture area), cuts mid-orbit.
