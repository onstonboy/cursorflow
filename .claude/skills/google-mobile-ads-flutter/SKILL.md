---
name: google-mobile-ads-flutter
description: >-
  Implement Google Mobile Ads (AdMob) in Flutter with Clean Architecture: UMP
  consent, MobileAds init, banner/interstitial/app open/rewarded/native ads,
  remote config ad units, premium gating, per-format load throttling, adaptive
  banners, lazy native loading, show-rate optimization, and error handling. Use
  when integrating AdMob, google_mobile_ads, UMP consent, app open ads, improving
  impressions/show rate, or mediation-ready ad stacks in Flutter.
---

# Google Mobile Ads (AdMob) — Flutter implementation skill

Production pattern for this repo: **facade `AdManager`**, specialized **`*AdManager`** extending **`BaseAdManager`**, **remote-config ad units**, **UMP before `MobileAds.initialize`**, **per-format load throttling** (`AdLoadCategory` + `AdLoadThrottle`), **fullscreen coordination**, and **load-only-when-likely-to-show**.

Adapt package names, DI (`get_it` / `injectable`), and remote-config keys to the target project.

---

## When to apply

- Adding or refactoring `google_mobile_ads` integration.
- Wiring **banner**, **interstitial**, **rewarded**, **app open**, or **native** ads.
- **Low show rate / low impressions per DAU** (AdMob account review feedback).
- GDPR/UMP, premium gating, frequency caps, mediation setup.

---

## Lessons learned (must read before changing ads)

These caused real revenue and show-rate drops in production. Avoid repeating them.

| Issue | Symptom in AdMob | Root cause | Fix |
|-------|------------------|------------|-----|
| Double `onAdsDismiss` | Low show rate, broken UX after interstitial | Calling `onAdsDismiss` **after** `show()` instead of only in `onAdDismissedFullScreenContent` | Complete user flow **only** in dismiss/fail callbacks |
| Eager preload on Home/init | Low show rate, wasted requests | Preloading interstitial/native/rewarded before user reaches placement | **Load on intent** (navigation tap, dialog open, visibility) |
| Single global load timestamp | Formats block each other; missed interstitials | One `LAST_AD_LOAD_TIME` for banner + fullscreen + native | **Per-format throttle** via `AdLoadCategory` |
| Banner refresh without UI update | Refresh requests but no new impressions in UI | New `BannerAd` in manager; `ValueNotifier` still holds disposed ad | **Compose listener** so every `onAdLoaded` updates UI |
| Load then show immediately | Interstitial never shows | `Navigator.push` + `show()` in `initState` before load finishes | `ensureInterstitialLoaded()` then `showInterstitialAdsWhenReady()` |
| Wrong ad unit on preload | Poor fill / wrong placement metrics | Preload path used different config ID than show path | Map **one config ID per `InterstitialAdsType`** everywhere |
| Session cap not incremented | Unbounded loads or cap never applied | `getCount()` without `count()` after check | Increment cap **when issuing** a load request |
| Duplicate load while in-flight | Two `InterstitialAd.load` for same placement | Preload + `ensureInterstitialLoaded` overlap | `_isLoading*` flag + `_waitForInterstitialLoad`; skip cap if already loading |
| `isPremium` frozen on singleton | Ads after IAP until restart | `final bool isPremium` at construction | `bool get isPremium` reading prefs each time |
| Load when `!canShowAnyAd()` | Wasted fullscreen requests | `ensure` before interval check | `showInterstitialAdsWhenReady` returns early if `!canShowAnyAd()` |
| Native preload all rows | Low show rate, spam requests | `load()` for every list slot at `initState` | **VisibilityDetector** — load when row is ~visible |
| Duplicate app-open preload | Redundant requests on cold start | `preloadOpenAd()` + `handlePreloadAppOpenAdModInIntervalTime()` both on Home init | **One** entry point for app-open preload |

---

## Best practices for impressions (without hurting UX)

### 1. Request only when show is likely

> AdMob guidance: preloading at screens users never reach hurts **show rate** and account quality.

- **Interstitial**: load when user taps “Preview” / opens GIF dialog — not on Home `initState`.
- **Rewarded**: load on **first tap** on gated feature (`showRewardedAd` → load-on-demand), not on config page init.
- **Native**: load when list row enters viewport (`VisibilityDetector`, `visibleFraction > 0.1`).
- **App open**: preload once when remote flag enabled + lifecycle show on foreground — avoid duplicate preload calls.

### 2. Separate load throttles by format

Use `AdLoadCategory` + `AdLoadThrottle` (pure logic, unit-testable):

| Category | Used for | Prefs key (example) |
|----------|----------|---------------------|
| `banner` | Banner initial + refresh | `LAST_BANNER_AD_LOAD_TIME` |
| `fullscreen` | Interstitial, app open | `LAST_FULLSCREEN_AD_LOAD_TIME` |
| `rewarded` | Rewarded | `LAST_REWARDED_AD_LOAD_TIME` |
| `native` | Native list slots | `LAST_NATIVE_AD_LOAD_TIME` |

```dart
bool canRequestAdLoad({AdLoadCategory category = AdLoadCategory.fullscreen});
void recordAdLoadRequest({required AdLoadCategory category});
Duration remainingLoadCooldown({AdLoadCategory category});
```

Remote config: `ad_load_min_interval_seconds` (default **30**) — minimum gap between requests **per category**.

### 3. Show fullscreen only when ready

```dart
// Facade API (delegate to InterstitialAdManager)
Future<bool> ensureInterstitialLoaded(InterstitialAdsType type, {Duration timeout});
Future<void> showInterstitialAdsWhenReady(type, {onAdsDismiss, loadTimeout});
```

Flow:

1. Before navigation to screen that shows interstitial → `await ensureInterstitialLoaded(LED_DISPLAY)`.
2. On target screen → `showInterstitialAdsWhenReady()` (waits up to ~5s, then show or skip with `onAdsDismiss`).

Preload after dismiss still respects `canShowAnyAd()` and session caps.

**In-flight guard:** per placement `_isLoadingLedDisplay` / `_isLoadingGifGenerating`; `_loadInterstitialAd` no-ops if already loading or loaded; `ensureInterstitialLoaded` waits via `_waitForInterstitialLoad` instead of second `load()`.

**`showInterstitialAdsWhenReady`:** skip load entirely when `!canShowAnyAd()` — call `onAdsDismiss` immediately.

### 4. Adaptive banners + refresh

- Size: `AdSize.getCurrentOrientationAnchoredAdaptiveBannerAdSize(width)` when `is_use_adaptive_banner` (RC, default true).
- Refresh: `banner_refresh_interval_seconds` (default **30**) via `Timer.periodic`.
- On refresh: dispose old ad, load new, fire **`onAdLoaded` through composed listener** so `ValueNotifier` updates.
- If throttled: `_scheduleBannerRefreshRetry` using `remainingLoadCooldown(category: banner)`.

### 5. Preload interstitial rules

- `handleLoadInterstitialAdModInIntervalTime`: load when `canShowAnyAd()`.
- `handlePreloadInterstitialAdModInIntervalTime`: after dismiss — require `canShowAnyAd()`; on load fail — respect fullscreen throttle only.
- Session cap: `MAX_INTERSTITIAL_*_COUNT` per placement; increment when **starting** a load, not on show.

### 6. Rewarded placement (AdMob account tips)

- Tie to **premium actions** (save/share, unlock background) — user opts in.
- Visible entry (toolbar icon / sheet) increases **rewarded show rate**.
- `showRewardedAd`: if null → `preloadRewardedAd` then show; grant value **only** in `onUserEarnedReward`.

### 7. Never spam requests

- Do not request again within `ad_load_min_interval_seconds` for the same category.
- Do not preload interstitial + app open + 3 rewarded on the same screen init.
- Banner refresh uses **banner** category only — does not block interstitial.

---

## Architecture (this project)

| Piece | Responsibility |
|--------|----------------|
| **`BaseAdManager`** | Test/prod IDs, `shouldShowAds`, `canShowAnyAd()`, per-category load throttle, `updateLastAdShowTime()`, fullscreen flag |
| **`AdLoadThrottle`** | Pure `canRequest` / `remainingCooldown` (unit tests) |
| **`BannerAdManager`** | Adaptive size, refresh timers, composed `BannerAdListener` |
| **`InterstitialAdManager`** | Per-type instances, `ensureInterstitialLoaded`, `showInterstitialAdsWhenReady` |
| **`RewardedAdManager`** | Load-on-demand, per `RewardAdsType` |
| **`NativeAdManager`** | Map `adId → NativeAd`, throttle per native load |
| **`AppOpenAdManager`** | Stale cache (4h), fullscreen throttle |
| **`AdManager`** | Facade — pages call this, not individual managers |
| **`AppLifecycleReactor`** | Foreground → `showOpenAdIfAvailable()` |

Register managers as **singletons**.

---

## Startup sequence

1. `WidgetsFlutterBinding.ensureInitialized()`
2. DI / prefs (premium flag).
3. **Premium** → skip UMP + `MobileAds.initialize()` if policy is no SDK for subscribers.
4. **Non-premium release**: UMP → `await MobileAds.instance.initialize()` (10s timeout, still init on failure).
5. **Debug**: test ad units via `getTrue*AdId()`; never click prod units in debug.

---

## Base rules

### `shouldShowAds`

`kReleaseMode && !isPremium`

### Global fullscreen guard

- `_isAnyAdCurrentlyShowing` set in `onAdShowedFullScreenContent`, cleared on dismiss/fail.
- `canShowAnyAd()`: not showing AND `now - LAST_AD_SHOW_TIME >= interstitial_interval` (RC, e.g. 180s).

### Dispose discipline

- After dismiss/fail: `dispose()`, null reference, conditional preload.
- Route `dispose`: cancel banner timers, `disposeBannerAd*`, `disposeNativeAd(id)` for each loaded slot.
- Native: remove from manager map when disposing — **do not** only dispose in widget without `disposeNativeAd`.

---

## Banner ads

```dart
// Compose user listener with internal assign + onAdLoaded forward
BannerAdListener _composeBannerListener({
  required void Function(BannerAd ad) onAssign,
  BannerAdListener? userListener,
});
```

UI: `ValueNotifier<BannerAd?>` + height notifier; update in **`onAdLoaded`** every time (including refresh).

---

## Interstitial ads

### Critical show flow

```dart
// WRONG — fires dismiss before ad closes
_interstitialAd?.show();
onAdsDismiss?.call(); // NEVER

// RIGHT — dismiss only in FullScreenContentCallback
onAdDismissedFullScreenContent: (_) {
  dispose(); null; onAdsDismiss?.call(); schedulePreload();
}
```

### Placement pattern (LED Board)

```dart
// Config page — before push
await adManager.ensureInterstitialLoaded(InterstitialAdsType.LED_DISPLAY);

// LED board — on enter
await adManager.showInterstitialAdsWhenReady(
  InterstitialAdsType.LED_DISPLAY,
  onAdsDismiss: () { /* continue */ },
);

// GIF dialog — preload on dialog open; show when user confirms
adManager.handlePreloadInterstitialAdModInIntervalTime(
  adsType: InterstitialAdsType.GIF_GENERATING,
);
// on confirm → showInterstitialAdsWhenReady(GIF_GENERATING, ...)
```

Use **correct config ID per `InterstitialAdsType`** in both load and preload paths.

---

## App open ads

- Single preload on Home: `if (isShowAppOpenAds()) preloadOpenAd()` inside `_handleLoadAppOpenAd()` only.
- Throttle: `AdLoadCategory.fullscreen`.
- Stale ad: reload if older than `maxCacheDuration` (4h).

---

## Rewarded ads

- Preload **on demand** inside `showRewardedAd` when instance is null.
- Throttle: `AdLoadCategory.rewarded`.
- Optional `preloadRewardedAd` after successful dismiss if `isPreloadNext`.

---

## Native ads

```dart
VisibilityDetector(
  key: Key('native_ad_visibility_$adIndex'),
  onVisibilityChanged: (info) {
    if (info.visibleFraction > 0.1) _loadNativeAdAtIndex(adIndex);
  },
  child: placeholderSizedBox,
);
```

Track `_requestedAdIndices` to avoid duplicate loads. On widget `dispose`: `nativeAdManager.disposeNativeAd('native_ad_$index')`.

---

## Remote config keys (Firebase)

| Key | Default | Purpose |
|-----|---------|---------|
| `interstitial_interval` | 180 | Min seconds between fullscreen **shows** |
| `ad_load_min_interval_seconds` | 30 | Min seconds between **loads** per category |
| `banner_refresh_interval_seconds` | 30 | Banner auto-refresh |
| `is_use_adaptive_banner` | true | Anchored adaptive banner size |
| `is_show_app_open_ads` | false | App open toggle |
| Per-format ad unit keys | — | Platform-specific unit IDs |

Publish RC keys before expecting production behavior.

---

## Consent (UMP)

| Situation | Action |
|-----------|--------|
| Form required | Show form; on error fall through if policy allows |
| Not required | Init ads |
| Timeout / error | Still `MobileAds.initialize()` |

---

## Testing checklist

- [ ] Debug: Google **test** units only.
- [ ] No `onAdsDismiss` after `show()` — grep for anti-pattern.
- [ ] Interstitial: load on preview tap → ad shows on LED board (or graceful skip).
- [ ] Banner: refresh updates `ValueNotifier` (no disposed `AdWidget`).
- [ ] Banner refresh does not block interstitial load (separate throttle keys).
- [ ] Native: scroll list — ads load only for visible rows.
- [ ] Rapid navigation: no double fullscreen; flags reset.
- [ ] Premium: no new loads; dispose visible ads.
- [ ] Unit tests: `AdLoadThrottle` cooldown logic.
- [ ] Run `flutter analyze` on `lib/core/common/utils/*_ad_manager.dart`.

---

## Agent implementation checklist

1. Consent → `MobileAds.initialize` with timeout.
2. `BaseAdManager` + `AdLoadCategory` throttle — **never** one global load timestamp.
3. Facade + per-format singleton managers; explicit dispose.
4. **Load on intent**, not on distant screen init.
5. Interstitial: `ensureInterstitialLoaded` + `showInterstitialAdsWhenReady`; **never** double `onAdsDismiss`.
6. Banner: adaptive size + composed listener + refresh with UI update.
7. Native: visibility-based load + `disposeNativeAd` on list dispose.
8. Publish Firebase RC keys for throttle/refresh/adaptive flags.
9. A/B `interstitial_interval` in AdMob/RC for revenue vs retention.

---

## Reference files in this repo

| File | Purpose |
|------|---------|
| `lib/core/common/enum/ad_load_category.dart` | Throttle categories |
| `lib/core/common/utils/ad_load_throttle.dart` | Pure throttle logic |
| `lib/core/common/utils/base_ad_manager.dart` | Shared gates + RC |
| `lib/core/common/utils/*_ad_manager.dart` | Format-specific logic |
| `test/core/common/utils/ad_load_throttle_test.dart` | Throttle unit tests |

Align with latest `google_mobile_ads` API and mediation vendor init order.
