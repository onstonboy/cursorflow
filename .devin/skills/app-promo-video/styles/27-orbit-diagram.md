# Style 27 — Orbit Diagram

The product as a solar system. App icon is the sun; feature nodes orbit it on rings; the camera zooms into a node, plays the feature, pulls back out.

Best for: suites/ecosystems, platforms, AI assistants, multi-feature products where the story is "one app, everything connected".

## Tokens

```ts
bg: deep space "#080B18" + faint star field (tiny dots, seeded)
rings: thin orbit lines at 10% white
core: brand gradient glow, icon centered
accent per node: mint/purple/cyan/pink cycle
Font: clean sans; node labels in small caps + mono orbit indices.
FPS 30.
```

Motion grammar: orbital mechanics — ring containers `rotate(speed*t)` while each node counter-rotates to stay upright; nodes bob ±3px; zoom = scale into node + fade ring opacity.

## Core mechanism

```tsx
const Orbit: React.FC<{radius:number; speed:number; children}> = ({radius,speed,children}) => {
  const f = useF();
  const a = f * speed;
  return <div style={{position:"absolute",inset:0,
    transform:`rotate(${a}deg)`}}>
    {React.Children.map(children,(c,i)=>{
      const angle = (i/React.Children.count(children))*360;
      return <div style={{position:"absolute",left:"50%",top:"50%",
        transform:`rotate(${angle}deg) translateX(${radius}px) rotate(${-angle-a}deg)`}}>
        {c}</div>;})}
  </div>;
};
// node rotates with ring; counter-rotation (-angle - a) keeps node upright.
// Zoom-in: whole system scales to node position (interpolate origin), rings fade,
//   node expands → crossfade into full-screen scene content.
// Zoom-out: reverse — snap back to system view, next node lights up.
// Elliptical rings optional: scaleY(0.6) on ring container for perspective feel.
```

## Scene grammar (7–10 scenes, 100–140s)

S01: ignition — core ignites, rings draw themselves, nodes pop onto rings · S02: overview drift (system rotates, labels intro) · S03–S08: per feature: camera zooms to that node (orbit pauses or slows 80%), node opens into scene content (screenshot + claim), pull back · S09: whole system aligns into a "constellation" logo → CTA center.

Ring/node mapping IS the information architecture — match node count to real features.

## Audio

- Music: ambient-electronic 90 BPM — numpy: deep pad (5ths detuned), slow arp pinging across stereo, sub pulse like a heartbeat of the system.
- SFX: lock-on chirp when camera selects a node (two-tone rising beep), whoosh in/out.
- VO: calm systems-voice — confident, slightly reverbed, declarative.

## Signature details

Counter-rotated upright nodes · elliptical rings for depth · lock-on chirps · zoom that never cuts · final constellation-alignment reveal.

Anti-patterns: nodes that rotate upside-down (missing counter-rotation), static camera the whole video, equal-speed rings (stagger speeds 0.9–1.3×), cluttering >2 rings.
