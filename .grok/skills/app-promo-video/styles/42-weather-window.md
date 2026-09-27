# Style 42 — Weather Window

Every scene is a sky. Dawn, noon, dusk, storm — the mood of each feature rendered as weather outside a window; the app sits calmly inside.

Best for: weather (obviously), mindfulness, journaling, mood apps, sleep, daily-ritual products.

## Tokens

```ts
skies: dawn "#2A2A4E→#E8A88F", noon "#5B9FD8→#C8E4F5", golden "#E8965C→#F5D9A8",
  dusk "#3A2A5E→#C86B8F", storm "#232B35→#4A5568", night "#0B1026→#1A2A4E"
window: interior frame edge + sill — content behind glass
Font: soft sans (Quicksand/Nunito), low contrast, weathered feel.
FPS 30.
```

Motion grammar: atmosphere — parallax cloud layers (3 depths, speeds 0.15/0.4/0.9 px/frame), occasional rain streak layer or sun-ray rotation; interior elements still; transitions = sky gradients CROSS-FADING into the next weather (20–40 frames, the only "motion" needed).

## Core mechanism

```tsx
// Sky per scene = animated vertical gradient (interpolate colors between stops
//   over the scene) + cloud layers: blurred ellipse divs (blur 40px) drifting.
// Rain: 60 thin 1.5px lines falling at slight angle, opacity 0.3, reset loop —
//   render only inside window region.
// Sun rays: conic-gradient light wedges slowly rotating behind content.
// Window frame: inner-room vignette — dark edges top/sides + a sill bar at
//   bottom. Raindrops ON the glass: few blurred dots with refraction highlight.
// Content cards: frosted pane (blur 10px, white 10%) hanging "in the window".
// Screenshots: behind glass too — slight glass sheen gradient over them.
// Time progress: sky hue shifts continuously through the whole video —
//   video IS a day passing (dawn open → night close).
```

## Scene grammar (6–8 scenes, 100–140s — meditative pace)

S01: dawn — title materializes with morning light · S02: problem = gray overcast/mist · S03–S06: features as weather shifts — clarity = clouds parting to noon sun; connection = golden hour; protection = storm safely outside while interior warm · S07: night — stars fade in (tiny dots), warm interior glow, logo + CTA like a lamp on the sill.

## Audio

- Music: ambient piano+strings 65–75 BPM — numpy: sparse felt-piano notes, string pad swells timed to sky changes, rain noise bed during storm scene (filtered pink noise).
- SFX: weather ambience per sky — wind, rain patter, birds at dawn (tiny chirps = sine chirps 4–5kHz quiet), distant thunder rumble.
- VO: weather-calm delivery — soft, unhurried, soothing.

## Signature details

The day-progress arc (sky keeps changing across the whole video) · parallax cloud depths · raindrops on glass · weather-matches-mood mapping · storm-outside-warm-inside as the security metaphor.

Anti-patterns: busy interiors, harsh cuts (weather blends), saturated UI colors fighting the sky, motion other than atmosphere.
