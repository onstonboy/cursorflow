# Style 14 — Origami Fold

Elegant paper-fold reveals in 3D space. Cards unfold from flat, content arrives by folding open — precision + softness.

Best for: premium/lifestyle, meditation, design tools, fashion, journaling — brands selling quiet craft.

## Tokens

```ts
bg "#EFEAE4" (warm paper) or deep "#1C1B1E" for contrast version
paper tones: "#FFFFFF", "#F4EEE5", "#DCCFC0", brand color used on ONE face
ink "#2A2620"
Font: light grotesk (Inter 300/500) + serif italic accents. Thin typography suits folds.
FPS 30.
```

Motion grammar: hinge folds — `perspective(1400px)` + `rotateX(-90→0)` or `rotateY(±90→0)` around a shared edge, `transform-origin` pinned to the fold edge. Easing `Easing.bezier(0.34, 1.2, 0.4, 1)` — slight settle. Shadows must move WITH the fold: a darkening gradient overlay whose opacity = sin(fold angle).

## Core mechanism

```tsx
const Fold: React.FC<{at:number; axis?:"x"|"y"; children}> = ({at,axis="x",children}) => {
  const f = useF();
  const a = interpolate(f,[at,at+36],[-90,0],{extrapolateLeft:"clamp",
    extrapolateRight:"clamp",easing:Easing.bezier(0.34,1.2,0.4,1)});
  return <div style={{transformOrigin: axis==="x"?"50% 100%":"0% 50%",
    transform:`perspective(1400px) ${axis==="x"?`rotateX(${a}deg)`:`rotateY(${a}deg)`}`,
    position:"relative"}}>
    {children}
    <div style={{position:"absolute",inset:0,background:"#000",
      opacity:Math.abs(Math.sin(a*Math.PI/180))*0.35, pointerEvents:"none"}}/>
  </div>;
};
// Chain folds: multi-panel card = nested Folds, each 8–10 frames delayed, alternating axis.
// Unfold a 4-panel brochure to reveal a screenshot — panels get progressively lighter
//   (lit paper) as they open.
```

## Scene grammar (6–8 scenes, 90–120s — slower, deliberate)

S01: logo mark folds up from flat paper · S02: problem card unfolds into a creased, messy state · S03–S06: each feature = a brochure unfolding to reveal screenshot on inner panels · S07: everything refolds into a clean package → wordmark + CTA.

Transitions: scene content folds flat, next unfolds from same plane — continuity of the "paper".

## Audio

- Music: shakuhachi/harp/celesta 70–80 BPM — numpy: plucked sines with 1.5s decay + air noise breaths, pentatonic, long rests.
- SFX: paper crease (filtered noise creak 150ms) at each fold hinge — this sound sells the whole illusion.
- VO: soft-spoken, almost ASMR, generous pauses (-4%).

## Signature details

Fold-edge shadows tracking angle · progressive panel lighting · nested fold chains · the "crease" SFX · final refold into package as the CTA metaphor.

Anti-patterns: rotateZ motion, bouncy scale pops, heavy flat shadows that ignore fold angle, >2 folds animating simultaneously.
