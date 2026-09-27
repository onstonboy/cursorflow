# Style 15 — VHS / CRT

Tape-era broadcast. Chromatic aberration, scanlines, tracking errors, a blinking PLAY icon — nostalgia rendered authentically, applied AFTER the design like a film stock.

Best for: retro games, music, photo-filter, synthwave-adjacent brands, nostalgia products, "old vs new" angle.

## Tokens

```ts
bg "#0E0E12"  phosphor "#E8E6DF"
accent "#FF6B9D" + "#5BE3E3" (tape-era pink/cyan)
Font: VCR OSD mono (VCR OSD Mono / JetBrains Mono) for on-screen-display text; headline may be a bold 80s chrome-look via gradient text.
FPS 30. Optionally open letterboxed 4:3 (1440×1080 centered) → expand to full after intro.
```

Motion grammar: underlying content moves normally, BUT the whole frame rides a constant jitter: `translate((f%3===0)?1.5:0, sin(f/7)*1.2)` + occasional tracking glitch (entire frame shears: a horizontal band offset +40px for 3 frames).

## Core mechanism

```tsx
// Post-process overlay applied to EVERY scene (wrap root):
const VHSLayer = () => <>
  {/* scanlines */}
  <AbsoluteFill style={{background:"repeating-linear-gradient(0deg, rgba(0,0,0,.28) 0 2px, transparent 2px 4px)"}}/>
  {/* chromatic aberration is done per-element, see below */}
  {/* tracking band that occasionally rolls down */}
  <div style={{position:"absolute", top: (f*3)%1080, height:90, width:"100%",
    background:"rgba(255,255,255,0.06)", filter:"blur(2px)",
    transform:`translateX(${Math.sin(f/2)*14}px)`}}/>
  {/* vignette + OSD */}
  <AbsoluteFill style={{boxShadow:"inset 0 0 180px rgba(0,0,0,.75)"}}/>
  <div style={{position:"absolute",top:40,left:60,fontFamily:vcr,color:"#E8E6DF",
    fontSize:36}}>PLAY ▶ {timecode}</div>
</>;
// Chromatic text/screens: render element 3x offset ±3px with blend screen,
//   tinted R/G/B: filter sepia+hue-rotate trick OR simpler: two colored shadow copies.
// Simpler reliable approach: content once + colored ghost at translate(3px,0) rgba(255,0,80,.35)
//   and (-3px,0) rgba(0,220,255,.35), mix-blend-mode:screen.
// Tape-stop transition: all motion eases to halt + pitch-drop audio, then resumes.
```

## Scene grammar (8–10 scenes, 90–120s)

S01: OSD "INSERT TAPE" → static burst → logo with rainbow-chrome text · S02: problem in "PAUSED" frame wobble · S03–S07: features as "scenes" on tape — OSD counter runs (SP 0:03:12), each feature card slightly overbright with halation; screenshots shown like captured broadcast · S08: tracking-error chaos moment → "REWIND" → clean logo + CTA.

Include ONE deliberate "someone hit the tracking" glitch mid-video — the signature beat.

## Audio

- Music: synthwave 100–110 BPM — numpy: detuned saw pad (2 saws ±0.5%), gated reverb snare (noise burst + fast decay + tail), arp 16ths; add wow/flutter: global `sin(t*0.9)*0.004` pitch wobble on the whole mix.
- SFX: tape-insert clunk, tracking static bursts, rewind whine.
- VO: through the tape — bandpass 400–3400Hz + slight distortion `tanh(v*1.8)` + reverb tail. Sounds like it's coming off the cassette.

## Signature details

OSD counter running real frames · ±3px chroma ghosts · rolling tracking band · halation on bright elements · the big mid-video glitch · "BE KIND REWIND" style end joke.

Anti-patterns: clean rendering (always through the VHS layer), modern flat design showing without texture, smooth audio without wow, skipping the OSD chrome.
