# Style 03 — Kinetic Type

The words ARE the footage. Maximum energy typography — huge, fast, beat-locked. Screenshots exist only to prove the product is real.

Best for: entertainment, music, social, sports, events — anything sold on energy not features.

## Tokens

```ts
bg: flat color that CHANGES per scene (cycle brand hues: "#FF4D00", "#0F0F0F", "#F5F0E6", "#1E3BFF")
ink: highest contrast vs bg
Font: ONE display face at 140–240px — Druk-style condensed, Archivo Black, or Inter Tight 900. Condensed > wide.
FPS 30.
```

Motion grammar: per-letter stagger (index × 2 frames), letters fly in with `translateX(-60→0)` + `filter: blur(8→0)`, exits whip UP. Words slam: scale 1.3→1 with `Easing.out(Easing.exp)`. Everything ≤14 frames.

## Core mechanism

```tsx
const Word: React.FC<{text:string; at:number; size?:number}> = ({text,at,size=200}) => (
  <div style={{display:"flex"}}>{text.split("").map((ch,i)=>{
    const f=useF();
    const t = interpolate(f,[at+i*2, at+i*2+10],[0,1],{easing:Easing.out(Easing.exp),extrapolateRight:"clamp",extrapolateLeft:"clamp"});
    return <span style={{opacity:t, filter:`blur(${(1-t)*8}px)`,
      transform:`translateX(${(1-t)*-60}px)`,fontSize:size,fontWeight:900,
      letterSpacing:"-0.03em",lineHeight:0.95}}>{ch===" "?"\u00A0":ch}</span>;
  })}</div>);
// Beat-lock: compute frame times from BPM — at = Math.round(beatIdx * FPS*60/BPM).
// Motion blur on transitions: scaleY(1→1.06) during movement frames.
```

## Scene grammar (10–14 micro-scenes, 60–90s — this style is SHORT)

Word-per-beat opening (4–6 beats: "STOP" "BEING" "BORING") · 3–4 feature words each slammed on beat with one supporting line at 40px · screenshots: ONE phone that appears at 80% mark, tilts in with the same letter-physics · CTA word + app icon, hold 2s, smash to logo.

No scene overlaps — hard cuts on beat only.

## Audio

- Music: phonk/hyperpop/electronic 128–150 BPM — numpy: driving sub kick every beat, offbeat open hats (noise bursts hp-filtered), saw bass `np.sign(sin)`, riser = noise sweep before each section.
- VO: OPTIONAL — this style often works text-only with a killer beat. If used: punchy 3–5 word lines, VO sits ON the beat.
- Mix: music LOUD (it IS the message), light ducking ratio 4:1.

## Signature details

Letters that overshoot · strobing bg color on drops · a single word held full-screen in silence before the drop · end card = just wordmark + store badges.

Anti-patterns: paragraphs, sub-lines >6 words, slow fades, pastel palettes, decorative cards, any element that takes >15 frames to appear.
