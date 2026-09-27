# Style 08 — Meme / Changelog

Self-aware internet comedy. Impact-font captions, record-scratch freezes, intentionally awkward beats. Wins by being the only ad that doesn't feel like an ad.

Best for: indie apps, Gen Z consumer, dev-community products, anything with personality.

## Tokens

```ts
bg: whatever serves the joke — often flat "#FFFFFF" or screenshot full-bleed
caption: Impact/Anton 400, WHITE with 6px black stroke (text-shadow: 4 directions), ALL CAPS
accent: comic-sans-energy allowed for irony: use sparingly
FPS 30.
```

Motion grammar: deliberately cheap — linear tweens, instant cuts, sudden freeze-frames (hold a frame 20 frames mid-motion), zoom-punches (scale 1→1.4 in 3 frames, hold).

## Core mechanism

```tsx
// Impact caption bar — the style's atom:
const Caption: React.FC<{children; top?:boolean}> = ({children,top}) => (
  <div style={{position:"absolute", top:top?60:undefined, bottom:top?undefined:60,
    width:"100%", textAlign:"center", fontSize:64, fontFamily:anton,
    color:"#fff", textShadow:"3px 3px 0 #000,-3px -3px 0 #000,3px -3px 0 #000,-3px 3px 0 #000",
    textTransform:"uppercase", padding:"0 80px"}}>{children}</div>);
// Freeze-frame: gate the frame — const ff = Math.min(f, freezeAt) for a region.
// Zoom-punch: scale 1→1.35 in 4 frames + tiny rotate ±2°, hold 14 frames, cut.
// "wait" beat: black card, one line, held uncomfortably long (45+ frames).
```

## Scene grammar (8–12 rapid beats, 60–100s)

S01: hook meme framing ("POV: your group chat leaks") · S02–S07: feature-per-joke — setup caption → screenshot → punchline caption; alternating rhythm setup/punchline · interleave a "changelog" parody card ("v2.0: fixed your privacy (finally)") · S09+: record-scratch on the CTA ("ok actually download it") + end card.

Structure beats to breathe: joke beat 60–90 frames, breath = black card 30 frames.

## Audio

- Music: trap-lite 100–120 BPM — numpy: 808 glides (portamento sine sub), trap hats (16th rolls with velocity jitter), simple bell melody.
- SFX carry the comedy: record-scratch, vine-boom on punchlines, airhorn on the CTA, cricket silence on the "wait" beat.
- VO: conversational deadpan — read jokes flat, let captions shout. VN memes: keep internet phrasing ("khum", "gê").
- Mix: boom SFX hits -1dB ceiling; VO close.

## Signature details

Captions literal screen-shouting · the awkward-hold beat · fake version numbers as jokes · "sponsored? no. it's just good" energy · end card completely serious for contrast.

Anti-patterns: polished motion design, premium color systems, explaining the joke, more than 2 jokes per scene, sincerity >50% of runtime.
