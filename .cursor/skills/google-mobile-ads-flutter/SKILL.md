---
name: google-mobile-ads-flutter
description: >-
  Implement Google Mobile Ads (AdMob) in Flutter with Clean Architecture: UMP
  consent, MobileAds init, banner/interstitial/app open/rewarded/native ads,
  remote config ad units, premium gating, frequency caps, fullscreen
  coordination, and error handling. Use when integrating AdMob, google_mobile_ads,
  UMP consent, app open ads, or mediation-ready ad stacks in Flutter.
---

# Google Mobile Ads (AdMob) — Flutter implementation skill

This skill distills a production-shaped pattern: a **facade `AdManager`**, specialized **`*AdManager` classes** extending **`BaseAdManager`**, **remote-config-driven ad unit IDs**, **release-only monetization** with **test IDs in debug**, **UMP consent before `MobileAds.initialize`**, **global fullscreen coordination**, and **explicit dispose/load-fail/retry** paths.

Adapt package names, DI (`get_it` / `injectable` / Riverpod), and remote-config keys to the target project.

---

## When to apply

- Adding or refactoring `google_mobile_ads` integration.
- Wiring **banner**, **interstitial**, **rewarded**, **app open**, or **native** ads.
- Handling **GDPR/UMP**, **premium / no-ads**, **ad fatigue** (intervals, session caps), and **mediation** prerequisites.

---

## Dependencies and version constraints

- Add `google_mobile_ads` in `pubspec.yaml`. Pin or note conflicts if using **Yandex** or other mediation SDKs that require a specific `google_mobile_ads` major version.
- **Android**: `AndroidManifest.xml` — `com.google.android.gms.ads.APPLICATION_ID` with your AdMob app ID.
- **iOS**: `Info.plist` — `GADApplicationIdentifier` with your AdMob app ID.
- Optional: **User Messaging Platform (UMP)** for consent (`ConsentInformation`, `ConsentForm`) — initialize ads **after** consent flow completes or fails gracefully.

---

## Startup sequence (critical order)

1. **`WidgetsFlutterBinding.ensureInitialized()`**
2. Firebase / DI / prefs (if you read premium flag from storage).
3. **If user is premium (no ads)** → **skip** consent + `MobileAds.instance.initialize()` entirely when your policy is “no SDK load for subscribers.”
4. **Non-premium, release**: run **UMP** (`ConsentUtils`-style), then inside the completion path call **`await MobileAds.instance.initialize()`**.
5. Apply **timeout** around consent + init (e.g. 10s): on timeout or exception, still attempt **`MobileAds.instance.initialize()`** so the app works offline / when consent SDK stalls.
6. **Debug**: optionally `ConsentInformation.instance.reset()` to test forms; use **test ad unit IDs** (see below).

Reference flow: consent completion → `_initializeConsentRefComponent()` → `MobileAds.instance.initialize()`.

---

## Architecture layers

| Piece | Responsibility |
|--------|----------------|
| **`BaseAdManager`** | Shared rules: remote-config keys, **test vs prod IDs**, **`shouldShowAds`**, **`canShowAnyAd()`** interval, **`updateLastAdShowTime()`**, **`setAdCurrentlyShowing`**, platform-specific ID getters. |
| **`BannerAdManager`**, **`InterstitialAdManager`**, **`AppOpenAdManager`**, **`RewardedAdManager`**, **`NativeAdManager`** | Own ad instances, load/show/dispose, format-specific callbacks. |
| **`AdManager`** | Thin facade: exposes getters, `init*`, `show*`, `dispose*`, delegates to specialized managers. |
| **`AppLifecycleReactor`** (optional) | Listens to `AppStateEventNotifier.appStateStream`; on **`AppState.foreground`** calls **`showOpenAdIfAvailable()`** for app open ads. |

Register managers as **singletons** so preload state survives across routes.

---

## Base rules (must implement consistently)

### `shouldShowAds`

Use a single gate, typically:

- **`kReleaseMode && !isPremium`**

Debug builds use **Google test ad units** via `getTrue*AdId()` so you never accidentally click fraud on real units during development.

### Test ad unit IDs (official samples)

Keep **Android vs iOS** test IDs in `BaseAdManager` statics for: banner, interstitial, rewarded, native. **App open** test id often uses the documented **sample** string (verify against current plugin docs).

### Remote config

Store **per-platform** keys (e.g. `BannerAd_Id_First` / `_iOS`) so you can rotate units without app updates. **Validate**: empty string from remote config should fall back to test ID in debug or skip load in release with logging — avoid passing empty `adUnitId` to `*.load`.

### Global fullscreen guard

Fullscreen formats **interstitial**, **rewarded**, **app open** must cooperate:

- Static **`_isAnyAdCurrentlyShowing`** (or equivalent) set **`true`** in **`onAdShowedFullScreenContent`**, **`false`** on dismiss or failed show.
- **`canShowAnyAd()`** returns false when `_isAnyAdCurrentlyShowing` is true **or** interval since **`LAST_AD_SHOW_TIME`** is too small.

This prevents overlapping fullscreen ads and weird SDK states.

### Interval between fullscreen impressions

Persist **`LAST_AD_SHOW_TIME`** (epoch ms) when an ad **successfully shows** (`onAdShowedFullScreenContent`), not only on dismiss. Read **`interstitialInterval`** (seconds) from remote config; compare `now - last >= interval * 1000`.

Edge case: **first launch** — `last == null` → allow show if other gates pass.

### Dispose discipline

- After **dismiss** or **failed to show**: **`ad.dispose()`**, null out reference, **preload** next if policy requires.
- On **route dispose** / widget `dispose`: dispose **banner** instances tied to that route.
- **Native**: dispose per slot id when cell scrolls away or page closes; maintain a **map** `id → NativeAd` to avoid duplicate loads for the same slot.

---

## Banner ads

### Loading

- Early-return if **`!shouldShowAds`** or banner instance already exists.
- Build `BannerAd(adUnitId:, size:, request: AdRequest(), listener: ...)`, then **`load()`**.
- Size: `AdSize.banner` vs `AdSize.fullBanner` from remote config flag.

### UI integration

- Use **`ValueNotifier<BannerAd?>`** and **`ValueNotifier<double>`** for height; in **`onAdLoaded`**, set notifier to the loaded ad and **`ad.size.height`** for layout.
- Reserve height **0** when premium, ads off, or ad not loaded — avoids layout jump; optional placeholder height using **`getSmartBannerHeight(MediaQuery)`** helper for consistent spacing while loading.

### Errors

- Implement **`onAdFailedToLoad`** in `BannerAdListener`: log `LoadAdError` (code, domain, message); optionally retry with backoff — avoid infinite tight loops.

### Edge cases

- **Hot restart**: dispose old `BannerAd` before creating a new one.
- **Tablet / orientation**: smart height helper uses width/height thresholds — adjust for your design.

---

## Interstitial ads

### Placement types

Use an **enum** (e.g. `LED_DISPLAY` vs `GIF_GENERATING`) with **separate `InterstitialAd?` fields** if different placements need different ad unit configs.

### Show gate

If **`!shouldShowAds`** or **`!canShowAnyAd()`** → invoke **`onAdsDismiss`** (or “continue flow”) **immediately** and return — user should never wait on a missing ad.

### Show flow

1. If no loaded ad → trigger **preload** path and **return** (or optionally load-then-show with a loading UX — not in minimal pattern).
2. Set **`fullScreenContentCallback`** **before** **`show()`**:
   - **`onAdShowedFullScreenContent`**: `setAdCurrentlyShowing(true)`, `updateLastAdShowTime()`.
   - **`onAdFailedToShowFullScreenContent`**: `setAdCurrentlyShowing(false)`, dispose, null reference, **retry preload** with `isLoadFail: true` if using backoff.
   - **`onAdDismissedFullScreenContent`**: `setAdCurrentlyShowing(false)`, dispose, null reference, **`onAdsDismiss`**, schedule **preload**.
3. Wrap **`show()`** in **try/catch** — log in debug only; SDK can throw in edge race conditions.

### Preload and session caps

- Maintain **session counters** per placement; increment only when you intend to **request** a load. Cap with **`MAX_INTERSTITIAL_*_COUNT`** to avoid hammering users in one session.
- **`handleLoadInterstitialAdModInIntervalTime`**: only load when **`canShowAnyAd()`** is true.
- **`handlePreloadInterstitialAdModInIntervalTime`**: after dismiss or load fail, optionally delay retries using **`isLoadFail`** branch — mirror **app open** backoff pattern (store last attempt time in prefs).

### Load errors

- **`onAdFailedToLoad`**: log `LoadAdError`; optionally chain **`handlePreloadInterstitialAdModInIntervalTime(..., isLoadFail: true)`**.

### Pitfall to avoid

- Do **not** call **`onAdsDismiss`** both inside **`onAdDismissedFullScreenContent`** and again unconditionally after **`show()`** — that double-invokes completion. Complete user flow **only** from dismiss callback (and from early-return paths when no ad).

---

## App open ads

### Load API variant

This project uses **`AppOpenAd.loadWithAdManagerAdRequest`** with **`AdManagerAdRequest()`** — appropriate for **Ad Manager** inventory. For standard AdMob-only, use the **`AppOpenAd.load`** overload that matches your account type (verify plugin API).

### State

- Track **`_isShowingOpenAd`**, **`_appOpenLoadTime`**, **`maxCacheDuration`** (e.g. 4 hours). If cached ad is **stale**, dispose, null, reload.

### Show gate

- Respect **`isShowAppOpenAds`** remote flag, **`shouldShowAds`**, **`canShowAnyAd()`**, and **not** already showing.

### Failed load backoff

- On **`onAdFailedToLoad`**, call **`handlePreloadAppOpenAdModInIntervalTime(isLoadFail: true)`** which writes **`APP_OPEN_AD_LOAD_TIME`** and only retries after **interval** elapsed (reuse same seconds as interstitial or dedicated remote key).

### Lifecycle

- **`AppLifecycleReactor`**: on foreground, **`showOpenAdIfAvailable()`**. Ensure cold start does not fight splash/navigation — some apps delay first app open until after home screen is visible.

---

## Rewarded ads

### Multiple units by feature

Use **`RewardAdsType`** enum mapping to:

- Remote config **first / second / third** ad unit ids.
- Feature flags: e.g. **`isShowRewardAdsSavingLed`**, **`isShowRewardAdsBackgroundImage`**.

### Preload

- **`preloadRewardedAd(type:, onAdLoaded:, onAdFailed:)`** — early exit if **`!_shouldShowAdForType`**, or ad already loaded.

### Show

- If **`!shouldShow`** or **no loaded ad** → **`onAdFailed`** (caller grants or denies reward policy-side).
- Set **`fullScreenContentCallback`**; on dismiss, **`preloadRewardedAd`** if **`isPreloadNext`**.

### Reward callback

- Use **`ad.show(onUserEarnedReward: ...)`** — **only** grant in-app value when this fires (subject to your compliance rules).

### Edge cases

- User backgrounds app during reward → handle via lifecycle if needed.
- Failed show → clear instance, **`onAdFailed`**, optional reload.

---

## Native ads

### Loading

- **`NativeAd`** with **`NativeTemplateStyle`** (small template is common for list rows).
- Cache by **stable `adId`** (e.g. list index or composite key) to prevent duplicate requests for the same row.

### Widget

- Wrap with **`AdWidget(ad: nativeAd)`** inside a sized **`Container`**; clip for rounded corners.

### List placement

- Optional helpers: **random position per group** of N items (`calculateAdPositions`) to vary native insertion points.

### Errors

- **`onAdFailedToLoad`**: **`ad.dispose()`**, remove from map, call **`onAdFailed`**.

---

## Consent (UMP) — behaviors to handle

| Situation | Action |
|-----------|--------|
| Consent form available + required | Show form; on error, still init ads if policy allows |
| Consent not required | Init ads |
| `requestConsentInfoUpdate` error | Fall through to `MobileAds.initialize()` |
| Timeout | Still init ads |
| Debug | Reset consent in debug for repeatable tests; use EEA debug geography **only** in debug builds |

Remove hard-coded production device IDs from shipping code or gate them behind **`kDebugMode`**.

---

## Premium and purchase restoration

- On **`IS_PURCHASE_NO_AD`** / entitlement change **at runtime**: stop scheduling new loads; dispose visible ads; lifecycle reactor should no-op when ads disabled.

---

## Logging and analytics

- Log **`LoadAdError.code`**, **`domain`**, **`message`** — helps map to **no fill**, **invalid request**, **network**.
- Optionally send non-PII events: load_failed, show_failed, dismissed.

---

## Testing checklist

- [ ] Debug: all formats show **Google test ads**.
- [ ] Release internal build: **real units** on **test devices** registered in AdMob.
- [ ] Airplane mode: consent/init timeout → app usable; no crash on show.
- [ ] Rapid navigation: no double fullscreen; flags reset on dismiss.
- [ ] Premium toggle: ads disappear; no new loads.
- [ ] App open: cold start + resume from background.
- [ ] Interstitial: interval enforced between placements.

---

## Minimal dependency wiring (pseudo)

```dart
// After consent / timeout path:
await MobileAds.instance.initialize();

// Optional:
MobileAds.instance.updateRequestConfiguration(
  RequestConfiguration(testDeviceIds: ['YOUR_DEVICE_ID']),
);
```

Use **test devices** in debug to avoid invalid traffic warnings.

---

## Summary for agents implementing a new project

1. **Consent → MobileAds.initialize** with timeout and fallback.
2. **`BaseAdManager`**: test IDs, remote IDs, `shouldShowAds`, interval + fullscreen flag, prefs timestamps.
3. **One facade + per-format managers**; singletons; explicit dispose.
4. **Banners**: notifiers + listener; **Interstitials/Rewarded/App open**: `FullScreenContentCallback` + try/catch on show.
5. **Never** fire completion callbacks twice for one impression.
6. **Platform manifests** and **AdMob app IDs** must be set or ads silently fail.

This skill is a **template**; align with latest **`google_mobile_ads`** breaking changes and your mediation vendor’s required init order.
