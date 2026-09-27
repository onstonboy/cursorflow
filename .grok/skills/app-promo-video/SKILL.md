---
name: app-promo-video
description: Build polished app promo/ad videos (Remotion + TTS voiceover + procedural music). Includes 51 completely distinct visual styles — pick one per app genre. Use when the user asks to make a promo/ad/trailer video for a mobile or web app, show real screenshots, add voiceover/music, or export 16:9 + 9:16 cuts. Invoke when user says "làm video quảng cáo app", "promo video", "app trailer", "tiktok ad".
---

# App Promo Video

End-to-end recipe for shipping a rendered promo MP4 for an app. Proven on a real production promo (147s, 1080p, VN voiceover + procedural music, dual 16:9/9:16 outputs).

## Workflow (7 stages — follow in order)

1. **Discover the app.** Read product/spec docs, design tokens (`DESIGN.md` or theme files), and list real screenshots (`docs/screenshot/`, `.grok/stitch/`). Pick 4–7 screens that best show features. NEVER use fake/mockup UI when real screenshots exist.
2. **Pick a style.** Ask the user's genre or choose from `styles.md` index (50 styles + the proven reference `styles/midnight-playground.md`). Each style file says its implementation recipe — they are NOT recolors; they differ in technique (SVG draw-on, iso planes, react-three-fiber, procedural audio, etc).
3. **Write VO script FIRST.** `tools/vo_script.txt`, one line per scene: `sNN|text`. Write spoken language, not written copy — short sentences, discourse particles, questions, ellipsis for breaths (see "VO that doesn't sound robotic" below). Generate with edge-tts, measure durations, then derive the scene timeline FROM the audio lengths (never squeeze VO into a fixed timeline).
4. **Generate music procedurally** with numpy (no licensing risk) — see `styles/midnight-playground.md` for a working lofi recipe. Match BPM/mood to the chosen style.
5. **Scaffold Remotion** (`remotion`, `@remotion/media`, `@remotion/google-fonts`): `src/theme.ts` (tokens + `SCENE_START` + `FPS`), `src/components.tsx` (shared primitives), `src/scenes/SNN*.tsx`, `src/Composition.tsx` (two `<Composition>`s sharing one component: 1920×1080 and 1080×1920).
6. **Mix audio** with the ffmpeg filter graph below. **Always verify speech is present** with faster-whisper before rendering — the sidechain bug below silently produces voiceless videos.
7. **Render + verify.** Still-frame each scene first (`npx remotion still`), fix layout, then full render. ffprobe codec/dims/duration; whisper-check speech on the final MP4.

## VO that doesn't sound robotic (proven)

- Write how people TALK: "Ui… tin nhắn nào cũng y chang nhau vậy, nhàm thấy mồ luôn á!" not "Tin nhắn đều giống nhau."
- edge-tts: `edge-tts --voice vi-VN-HoaiMyNeural --rate=+2% --pitch=-1Hz`. Rate +8%+ sounds rushed; pitch -1Hz is warmer; -3Hz for deeper.
- VN voices: `vi-VN-HoaiMyNeural` (F, friendly), `vi-VN-NamMinhNeural` (M, warm/deep).
- If `NoAudioReceived`: transient rate-limit — wait a few seconds and retry; test with a one-word file first.
- In the mix, add vocal warmth: `highpass=f=70,equalizer=f=200:t=q:w=1.2:g=2.5,equalizer=f=3200:t=q:w=1:g=1.2,acompressor=threshold=-22dB:ratio=2.5:attack=8:release=120`.

## CRITICAL ffmpeg mix gotcha (cost a full render once)

`sidechaincompress` consumes the voice stream as its key input. If you also feed that stream to `amix` WITHOUT `asplit`, ffmpeg silently routes it only to the sidechain → **video has zero voice but ducking still "works"**. Always:

```
[a1][a2]...[a9]amix=inputs=9:normalize=0,<voice EQ chain>,volume=2.0,apad=whole_dur=DUR,asplit[v1][v2];
[0:a][v1]sidechaincompress=threshold=0.015:ratio=8:attack=20:release=600[m];
[m][v2]amix=inputs=2:normalize=0,alimiter=limit=0.95[out]
```

(`adelay=MS|MS` each VO input before amix to place it on the timeline.)

## Verification that catches real bugs

```bash
ffmpeg -ss <t> -t 10 -i out/promo.mp4 -ar 16000 -ac 1 /tmp/seg.wav
python -c "from faster_whisper import WhisperModel; m=WhisperModel('tiny'); \
print([s.text for s in m.transcribe('/tmp/seg.wav', language='vi')[0]])"
```

If transcription is empty, the mix is broken — do NOT render. A missing voice is invisible in waveforms.

## Other hard-won gotchas

- **Emoji don't render** in Remotion headless Chromium. Use SVG or `<Img>` for icons/logos (even Apple  → hand-drawn SVG).
- **Time-scale per scene**: wrap scenes in a context that multiplies `useCurrentFrame()` (`useF()` in the reference style) so you can retime pacing (`speed={1.35}`) without touching keyframes.
- **Dual aspect**: ONE component, two `<Composition>`s; branch layout via `useVertical()` (`height > width`). Refactor layout for 9:16 — don't crop.
- **Timeline math**: `SCENE_START` array + `OVERLAP=12` crossfade; last scene ends at `TOTAL`.
- Screenshots: copy to `public/screens/`, load via `staticFile('screens/x.png')` + `<Img>`, inside a shared `Phone` mockup component (dark bezel, colored shadow glow, slight rotate-in).
- Preview cheaply: `npx remotion still <comp> <frame> out.png` before any full render.

## Render

```bash
npx remotion render <Comp> out/promo.mp4 --codec=h264 --crf=18
```

## Style index

Every style has a FULL spec file in `styles/` — `styles/00-midnight-playground.md` through `styles/50-cozy-home-evening.md`. Each file is self-contained: palette/font tokens, core mechanism code, scene grammar, audio recipe, signature details, anti-patterns.

`styles.md` = the index/summary catalog (vibe, app fit, recipe one-liner, genre→style table). Read it to CHOOSE a style, then read that style's file under `styles/` to BUILD it.

Choose ONE style per video. If the user doesn't specify, pick by app genre from the table in `styles.md`, then follow that style's file literally — the techniques differ deliberately.
