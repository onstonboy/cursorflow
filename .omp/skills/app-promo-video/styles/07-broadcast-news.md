# Style 07 — Broadcast News

Prime-time urgency. Lower-thirds, tickers, red LIVE dots, segment slates — your app's features presented as breaking coverage.

Best for: news, finance, sports scores, weather alerts, market data, anything time-sensitive.

## Tokens

```ts
bg "#0B1526" (news navy)   plate "#122038"   accent "#E5173A" (breaking red)   amber "#FFB020"
ink "#FFFFFF"   muted "#8FA3C8"
Font: condensed sans (Archivo/Inter Tight) for lower-thirds UPPERCASE; mono for ticker numbers.
FPS 30.
```

Motion grammar: plates enter `translateX(-110%→0)` + skew(-8°→0) over 12 frames with `Easing.out(Easing.cubic)`; ticker = infinite `translateX` linear loop; LIVE dot pulses `opacity` 1↔0.3 every 15 frames.

## Core mechanism

```tsx
// Lower-third: red kicker tab + navy plate + headline — slides in, holds, slides out.
const LowerThird: React.FC<{kicker:string; title:string; at:number}> = ...
  // red tab above plate, both slide X with skew easing, 8px red accent bar on left edge
// Ticker: two copies of content for seamless loop:
<div style={{position:"absolute",bottom:0,height:56,background:"#081020",
  display:"flex", transform:`translateX(${-(f*4 % W)}px)`}}>
  {[0,1].map(k=><TickerContent key={k}/>)}</div>
// Segment slate: full-frame "ALERT" card — flashes in 3 frames, bg pulse.
```

## Scene grammar (7–9 scenes, 90–120s)

S01: "BREAKING" slate flash → studio-style open · S02: story intro with reporter-style VO lower-third · S03–S07: each feature = a "segment": slate card (SEGMENT 03 / SECURITY) → screenshot plate sliding in next to lower-third text, ticker runs continuously underneath · S08: "DEVELOPING…" → CTA card + stores.

Ticker content: fake-wire headlines about the app's benefits — it never stops.

## Audio

- Music: news-package bed — numpy: urgent ostinato strings-synth (saw through lowpass), timpani hits per segment, 118 BPM steady.
- SFX: stinger hit at every slate (brass-ish saw chord stab), teletype chatter under ticker.
- VO: authoritative anchor delivery — declarative, brisk (+5%), project like headlines not conversation.
- Mix: stingers loud, music ducks hard (ratio 10:1) under VO.

## Signature details

"● LIVE" pulsing corner bug · clock in corner matching video time · segment numbering · ticker that never stops · "DEVELOPING STORY" suspense before CTA.

Anti-patterns: soft rounded cards, pastel, slow crossfades, whimsical motion, casual VO tone.
