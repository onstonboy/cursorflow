# Style 38 — Documentary Handheld

A camera operator is filming this product. Handheld shake, rack focus pulls, interview-style lower thirds — authenticity through imperfection.

Best for: mission-driven products, health, education, indie apps, social-impact, founder-story brands.

## Tokens

```ts
look: warm natural grade — slightly lifted blacks, "#F4EFE8"-ish highlights; desaturate 10%
lower-third: simple white card + thin rule, mono name tag
Font: documentary serif for titles (Source Serif/Lora) + mono slate labels.
FPS 30.
```

Motion grammar: imperfect camera — everything sits inside one rig: random-walk translate (±6px, low-frequency — sum of 2–3 sines at different periods), ±0.4° rotate, occasional reframe settle (camera drifts to "find" the subject after cuts). Focus pulls: blur 4px→0 over 20 frames on the subject entering.

## Core mechanism

```tsx
// Handheld rig wrapping every scene (share rig across scenes — same camera op):
const rig = (f) => ({x:sin(f/31)*4+sin(f/13)*2, y:cos(f/27)*3+sin(f/9)*1.5,
  r:sin(f/41)*0.4});
// Reframe beat: after each cut, camera drifts 15px→0 settling over ~20 frames —
//   the "operator found the shot" feel.
// Rack focus: two layers — foreground detail starts blur(4px), subject blur(0);
//   swap focus mid-scene (focus pulls to the screenshot).
// Interview lower-thirds: "SCENE 03 — ONBOARDING" mono tag + rule slide-in.
// Screenshots: shot like B-roll — slight angle (rotate ±1.5°), handheld drift,
//   occasionally a finger briefly enters frame edge on taps.
// Timecode corner + "REC ●" subtle — present but tasteful.
```

## Scene grammar (7–9 scenes, 110–150s — doc pace is slower)

S01: establishing — logo "filmed" on a surface, rack-focus pull · S02: "interview" framing of the problem (title card + ambient) · S03–S07: B-roll style coverage of each feature — camera finds screenshots, focus pulls, lower-third slates · S08: closing shot — focus pull to logo, camera settles, fade.

Cuts happen; each cut followed by reframe-settle.

## Audio

- Music: acoustic ambient — numpy: warm guitar plucks (sine + harmonics, spaced), cello-pad (saw lowpassed hard + slow attack), room tone bed constant.
- SFX: camera operation sounds — focus motor tick, handling bumps; room/ambience per scene.
- VO: interview intimacy — like answering an off-camera question; natural pauses, imperfect delivery (keep breaths).

## Signature details

Reframe-settle after every cut · focus pulls as punctuation · mono slate labels · finger-in-frame authenticity · lifted-black grade throughout.

Anti-patterns: locked shots, digital-perfect centering, snappy motion graphics, saturated brand colors (grade everything to the film look), missing ambience.
