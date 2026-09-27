# Style 33 — AR Desk Overlay

UI floating in your room. A fake camera POV — soft room-gradient background, handheld drift — with product panels pinned in space, tapped by a hand cursor.

Best for: utilities, camera/photo, home, education, productivity — "app in your life" positioning.

## Tokens

```ts
room: subtle gradient — warm interior "#3A3532"→"#2A2521" or daylight "#8FA3B8"→"#B8C4CE" per scene mood
UI: clean light cards, soft real shadows (they sit in "space", not glass)
accent: brand color on interactive points
Font: product's own sans for UI cards; minimal captions.
FPS 30.
```

Motion grammar: handheld POV — the ENTIRE frame rides a random-walk drift (±5px translate, ±0.4° rotate, ~0.5Hz noise via summed sines); UI panels pinned to a perspective floor grid, parallax-shifting against the camera; tap = ripple + panel pushes back slightly.

## Core mechanism

```tsx
// Handheld rig at root:
const shake = (f) => ({
  x: Math.sin(f/23)*3 + Math.sin(f/7.7)*2,
  y: Math.cos(f/19)*2.5 + Math.sin(f/11)*1.5,
  r: Math.sin(f/31)*0.35 });
// Floor grid: perspective plane (rotateX 65deg) with faint grid lines fading
//   toward horizon — grounds the floating UI.
// Panels: cast contact shadow = blurred ellipse directly beneath (opacity by
//   hover height); parallax offset = depth * shake * -1 (nearer moves more).
// Hand cursor: SVG hand/finger that drifts to interactive points; tap =
//   ripple ring expand + panel dips (scale .97, 4 frames) + soft tap SFX.
// Screenshots: displayed as floating "windows" with room reflection —
//   subtle gradient overlay at top simulating ceiling light.
```

## Scene grammar (6–8 scenes, 90–120s)

S01: POV wakes — room fades in, first panel materializes · S02: clutter of "before" panels crowd the desk · S03–S06: finger cursor taps through features; each tap opens a floating window (screenshot) that rises and enlarges · S07: panels tidy themselves into a neat arc → hand taps CTA → logo.

## Audio

- Music: minimal ambient-electronic 85–95 BPM — numpy: soft mallets, warm sub, room-tone noise bed underneath always.
- SFX: finger taps (short woody clicks), panel whoosh, room ambience (low rumble + occasional soft environmental noise).
- VO: natural second-person — "you tap here, and this happens" intimacy; conversational.

## Signature details

Handheld drift never stops · contact shadows under panels · parallax depth shifts · finger-cursor taps driving the story · room-light reflections on windows.

Anti-patterns: locked-off camera (dead giveaway), flat UI without shadows, crisp digital edges on "room" elements, dark-mode-only thinking.
