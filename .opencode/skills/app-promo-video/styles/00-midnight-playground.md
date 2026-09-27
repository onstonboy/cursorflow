# Style 00 — Midnight Playground (reference, production-proven)

The Morsey promo style: dark cinematic navy + mint, playful but premium, real screenshots in floating phone mockups, morse/teencode glyphs drifting behind, conversational VN voiceover over procedural lofi. Feels like a secret club, not a dev dashboard.

Best for: social/playful utilities, Gen Z consumer apps, privacy-but-fun products, any app whose brand is dark + neon accent.

## Tokens (src/theme.ts)

```ts
bg "#0B1120"  bg2 "#0F172A"  card "#151D33"  cardHi "#1C2742"  line "#2A3757"
mint "#7FE0A6"  mintDeep "#10B981"  purple "#7C3AED"  pink "#EC4899"  cyan "#57DFFE"
text "#F1F5F9"  muted "#94A3B8"
Fonts: Plus Jakarta Sans (400–800, vietnamese subset) — headlines/UI;
       JetBrains Mono (400/700) — code/morse/mono accents.
FPS 30. Scene starts: SCENE_START[] with OVERLAP = 12 crossfade frames.
```

Motion grammar: `Easing.bezier(0.16, 1, 0.3, 1)` everywhere. Entrances = opacity 0→1 + translate 46–90px → 0 + slight rotate 4°→0 over ~26–34 frames. No linear tweens, no CSS transitions.

## Core mechanisms (copy verbatim)

```tsx
const ScaleCtx = createContext(1);
export const useF = () => useCurrentFrame() * useContext(ScaleCtx);   // per-scene speed
export const useVertical = () => { const {width,height}=useVideoConfig(); return height>width; };
export const useRise = (f, at, dur=22, dy=46) => ({opacity, translate:`0 ${dy→0}px`}); // fade+rise

// <Scene speed={1.15..1.35}> wraps each scene; fade-in over first 12 frames.
// ALL scene animation uses useF(), never useCurrentFrame() directly.
```

Shared primitives (src/components.tsx): `Backdrop` (navy radial gradient + 26 drifting morse glyphs with sine opacity + two slow-moving color glows), `Kicker` (pill label, letterSpacing 4), `Headline` (800 weight, size ~72, letterSpacing -1.5), `Sub` (muted, size 30), `Phone` (screenshot in `#05080F` bezel r=66, colored glow shadow `0 40px 120px -20px {glow}33`, rotates/rises in), `Chip`, `Card`.

## Scene grammar (9 scenes, ~147s)

S01 logo decode (morse chars → logo, 11s) · S02 problem (chat mock + stamp, 11.5s) · S03 feature demo + real screenshot phone (19.5s) · S04 vibe carousel + screenshot (13s) · S05 security animation + 2 screenshots (23s) · S06 platform-integration story (14s) · S07 share/QR (QR renders cell-by-cell) (16s) · S08 benefits + emotion (18s) · S09 outro CTA + real app icon (21s).

Scene speed multipliers used: 1.15 / 1.35 / 1.15 / 1.25 / 1.2 / 1.25 / 1.25 / 1.2 / 1.25. Keep VO lead-in ~1.5–2s after each scene start; place `adelay` to match.

Vertical (9:16): same component; headline stack on top, phone centered below; pillar rows become horizontal icon-left rows.

## Audio recipe

- **Music**: `tools/make_music.py` — numpy procedural lofi: Am7→Fmaj7→Cmaj7→G6 pads (sine + detuned + sub, one-pole lowpass), sub bass roots, soft kick/rim/swung hats (8% swing), sparse pentatonic pluck w/ echo, vinyl crackle. 78 BPM. Optional signature beeps (morse of product name) in first 4.5s.
- **VO**: edge-tts `vi-VN-HoaiMyNeural --rate=+2% --pitch=-1Hz`; conversational script (particles "nè/á/đó/nha", ellipsis breaths). 9 segments `public/audio/vo/sNN.mp3`.
- **Mix**: adelay each segment to scene timeline → amix 9 → warmth EQ + acompressor → asplit → sidechain ducking of music → amix → alimiter → `mix.wav` (see SKILL.md for exact graph + the asplit bug).

## Signature details to preserve

Morse-glyph backdrop · teencode/typing transform animation · QR cell-by-cell fill · stamp "AI CŨNG ĐỌC ĐƯỢC" · hearts/rise particles for emotion scene · real launcher icon in outro · tagline "Cùng những từ ngữ đó, một thế giới khác" / "IYKYK".

Anti-patterns (explicitly banned): Matrix rain, dense HUD grids, fake telemetry/stats, glass overload, developer-dashboard look.
