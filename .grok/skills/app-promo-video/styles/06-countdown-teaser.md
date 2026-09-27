# Style 06 — Countdown Teaser

Pre-launch mystery. Mechanical split-flap numerals, one cryptic line per beat, product withheld until the last 5 seconds. Sells anticipation, not features.

Best for: launches, waitlists, v2 announcements, event apps, stealth products.

## Tokens

```ts
bg "#0C0C0E"   surface "#17171B"   numeral "#F5F2EA"   accent: brand color (used ONLY in final reveal)
Font: numerals in mono or DIN-condensed 700; copy in clean grotesk 400.
FPS 30.
```

Motion grammar: split-flap physics — top half hinges down via `rotateX(0→-85deg)` with `transform-origin: bottom` + `backface-visibility:hidden`, lands with a 1-frame overshoot. NO other motion type exists in this style.

## Core mechanism

```tsx
const FlapDigit: React.FC<{digit:string; at:number}> = ({digit,at}) => {
  const f = useF();
  const t = interpolate(f,[at,at+8],[0,1],{easing:Easing.in(Easing.quad),
    extrapolateLeft:"clamp",extrapolateRight:"clamp"});
  return (
    <div style={{position:"relative",width:110,height:150,fontSize:110,fontFamily:mono}}>
      <div style={{position:"absolute",inset:0,background:"#17171B",borderRadius:8,
        overflow:"hidden"}}>{/* static lower half */}</div>
      <div style={{position:"absolute",inset:0,borderRadius:8,overflow:"hidden",
        transformOrigin:"50% 100%",
        transform:`perspective(600px) rotateX(${-85*t}deg)`,
        backfaceVisibility:"hidden",background:"#1F1F24"}}>{digit}</div>
      {/* horizontal hinge line at 50%: 1px darker div */}
    </div>);
};
// Multiple digits cascade: digit[i] flips at = base + i*3.
```

## Scene grammar (5–7 scenes, 60–90s)

S01: "10" flap → "09" flap → … descend ~4 numerals while copy line appears ("SOMETHING IS COMING") · S02–S05: each flap reveals a cryptic feature hint ("A LANGUAGE" flap "NOBODY" flap "CAN READ") — hints get less cryptic · S06: FLAP → screenshot finally appears (color floods in — first color in the video) · S07: wordmark + "Coming {date}" + notify-me CTA.

Every transition = flap cascade.

## Audio

- Music: tension drone — numpy: low sine drone (55Hz + 55.5Hz beating), slow noise riser per scene, heartbeat sub-thump every 2s.
- SFX: THE flap clack is the protagonist — sharp filtered noise burst ~40ms per flap, cascades in rolls.
- VO: minimal or none. If used: whispered/close, very few words ("Ba ngày nữa.").
- End: drone resolves to a single clean chord at reveal.

## Signature details

Numerals cascade like an airport board · hinge line detail · the FIRST appearance of brand color = the product reveal (before that: pure mono) · hold the final reveal 3s in silence before tagline.

Anti-patterns: showing UI early, smooth fades, multiple colors before reveal, busy backgrounds, fast cuts.
