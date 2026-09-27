# Style 37 — Live Cursor Demo

The honest demo. Real screen-recorded footage driven by a scripted cursor, punch-ins on details — "show, don't tell" taken literally.

Best for: SaaS, productivity, utilities — products where the UI itself is the selling point.

## Tokens

```ts
bg: neutral dark "#101014" framing the device capture, or clean "#F5F5F7"
cursor: custom SVG arrow/hand, slight shadow
zoom punch: scale 1→1.25–1.6 targeting detail
Font: product-adjacent sans for sparse labels only.
FPS 30.
```

Motion grammar: cursor choreography — the cursor moves on smooth bezier paths (interpolate position through waypoints with `Easing.inOut`), accelerates on travel, decelerates on approach; click = cursor scale .9 squash + ripple ring + the recorded UI responds in sync.

## Core mechanism

```tsx
// CAPTURE FIRST: record the app running (simulator screen record / QuickTime) —
//   4–7 short clips, one per feature flow. Put under public/clips/.
// In Remotion: <Video src={staticFile("clips/flow1.mp4")}/> inside a device
//   frame; Remotion's frame-accurate seeking keeps actions aligned.
// Scripted cursor: waypoint list per clip:
//   [[t0,x0,y0],[t1,x1,y1],...] → cursor position = catmull-rom/bezier interp
//   between keyframes; waypoint times synced to when the recorded UI responds.
// Zoom punch: container scale+translate toward action point, easeInOut 15
//   frames in, hold, ease back. Never zoom mid-gesture.
// Click ripple: expanding ring at cursor, 300ms, plus 1-frame "press" flash.
// Caption labels: small floating tags pointing at the clicked control.
```

## Scene grammar (7–10 scenes, 90–140s)

S01: device frame fades in idle → cursor wakes · S02: the problem flow played straight ("watch someone do it the hard way") · S03–S07: clip per feature — cursor performs the flow; punch-ins on the clever details · S08: fast-cut recap montage of best moments → CTA.

Cursor path design is the craft — plan waypoints to look INTENT, not wandering.

## Audio

- Music: minimal beat 95–105 BPM — numpy: clean kick+hat, simple bassline, thin melodic pluck — stays under everything.
- SFX: mouse click (short transient + tick), subtle keystrokes on typing clips, whoosh on zoom punches.
- VO: practical explainer — "Watch this: one tap." Second-person, efficient.

## Signature details

Frame-accurate cursor/footage sync (off by 5+ frames = uncanny) · punch-in on details only · click ripples · the problem-flow "before" played straight · honest footage (no fake UI).

Anti-patterns: cursor drifting during narration, zooming while UI animates, fake UI mockups when real capture exists, music louder than clicks, embellishing a flow the app can't do.
