---
name: flutter-ump-consent-eea
description: >-
  Implement Google UMP (User Messaging Platform) GDPR/EEA consent flow in
  Flutter before initializing ad SDKs. Covers a singleton ConsentUtils with
  10s timeout, Completer-bridged callback API, EEA debug geography simulation,
  recursive form reload after privacy options change, three-level error
  fallthrough (request error, form-load error, form-show error, timeout,
  exception), premium-user skip, debug reset, and post-consent initialization
  of Google Mobile Ads + mediation SDKs (Yandex, AppLovin, etc.) + custom
  native SDKs. Use when integrating google_user_messaging_platform / the UMP
  bundled in google_mobile_ads, when building a GDPR consent layer for the
  European Economic Area, when wiring "ask consent before MobileAds.initialize",
  or when testing EEA flows from non-EEA devices.
---

# Flutter UMP Consent (EEA / GDPR) — implementation skill

This skill is a **drop-in template** for handling Google’s **User Messaging Platform** consent flow in a Flutter app before initializing **Google Mobile Ads** and any mediation/auxiliary SDKs. It encodes a production-tested pattern: a **single `ConsentUtils` singleton**, a **Completer bridge** over UMP’s callback API, a **dual timeout** (internal + caller), **EEA debug simulation**, a **recursive privacy-options re-load**, and a **graceful “always init ads even on failure”** policy so the app never gets stuck behind a broken consent SDK.

Adapt package names, DI (`get_it`/`injectable`/Riverpod/Provider), remote-config keys, and mediation SDKs to the target project.

---

## When to apply

- Adding GDPR / EEA consent to a Flutter app that monetizes with ads.
- Wrapping any ad SDK init (`MobileAds`, Yandex `MobileAds`, AppLovin SDK, custom native SDKs) so it only runs after `requestConsentInfoUpdate` resolves.
- Supporting premium / no-ads users who must **bypass** consent entirely (no SDK loaded).
- Testing the EEA flow from a **non-EEA** development device.
- Re-engineering a fragile consent layer that hangs the app on network failure, EEA timeout, or invalid form HTML.

---

## Dependencies and platform setup

- Add **`google_mobile_ads`** in `pubspec.yaml` — UMP types (`ConsentInformation`, `ConsentForm`, `FormError`, `ConsentDebugSettings`, `DebugGeography`, `ConsentRequestParameters`, `ConsentStatus`) are re-exported here.
- Add **mediation SDKs** as needed (e.g. `yandex_mobileads`, `applovin_max`); they each need their own `initialize()` after consent.
- DI helpers (any of `get_it`, `injectable`, Riverpod) — singleton lifetime is required for the consent state flag.
- **Android** `AndroidManifest.xml`:
  - `<meta-data android:name="com.google.android.gms.ads.APPLICATION_ID" .../>`
- **iOS** `Info.plist`:
  - `GADApplicationIdentifier`
  - `SKAdNetworkItems` list as required by AdMob.
  - `NSUserTrackingUsageDescription` only if you also call **ATT** (UMP itself does **not** trigger ATT — keep that flow separate if needed).
- **AdMob console**: Privacy & messaging → create a **GDPR message** for EEA + UK + a **privacy-options** form, and publish. Without a published message, `isConsentFormAvailable()` returns `false` even in EEA.

---

## Core principles (must hold)

1. **One singleton.** Consent flow runs exactly once per process. A re-entrant `initialize()` returns immediately.
2. **Never block the app.** Every error path, timeout, or exception must still call the post-consent SDK initializer so banners/interstitials work as soon as the network recovers.
3. **Premium users skip the whole flow.** No consent UI, no UMP request, no ad SDK init.
4. **Debug = repeatable.** `ConsentInformation.instance.reset()` in debug; **EEA debug geography** with **test identifiers**; production builds never reset.
5. **Dual timeout.** Internal timeout (≈10 s) inside `ConsentUtils` **and** a second caller-side timeout (≈10 s) — guards against the SDK never firing either callback.
6. **Initialize ad SDKs on every terminal path.** Success, form-not-required, form-load-error, form-show-error, request-error, timeout, exception → all funnel through one `_initializeConsentRefComponent()` method.

---

## Architecture

| Piece | Responsibility |
|-------|----------------|
| **`ConsentUtils`** (singleton) | Drives the UMP flow, owns `_isInitialized`, bridges callback API to `Future<FormError?>` via `Completer`. Calls the post-consent initializer on every terminal path. |
| **`_initializeConsentRefComponent`** (private) | Side-effect step: `MobileAds.instance.initialize()`, mediation SDK `initialize()`s, custom native bridge SDKs, analytics/crashlytics that depend on consent. |
| **`NativeBridge`** (optional) | `MethodChannel` to native side for SDKs without Flutter plugins, or for `enableGMATestMode`, `launchAdInspector`. |
| **Caller (`main`)** | Reads premium flag, gates the call by `kReleaseMode && !isPremium`, wraps in a second timeout + try/catch. |

---

## End-to-end startup sequence

```
WidgetsFlutterBinding.ensureInitialized()
  └─ EasyLocalization.ensureInitialized()
  └─ Firebase.initializeApp(...)
  └─ configureDependencies() + getIt.allReady()
  └─ RevenueCat / IAP manager .initialize()     ← determines isPremium
  └─ if (!isPremium && kReleaseMode) {
        await getIt<ConsentUtils>().initialize()
              .timeout(10s, onTimeout: () => null)   // caller-side safety
        // ad SDKs are now initialized (or gracefully degraded)
     }
  └─ FlutterError.onError = Crashlytics.recordFlutterFatalError  (release only)
  └─ runApp(...)
```

> **Do not** call `MobileAds.instance.initialize()` directly from `main`; let `ConsentUtils._initializeConsentRefComponent()` own it. This guarantees the SDK is only initialized once and always with the consent string already cached.

---

## UMP flow — every branch enumerated

```
ConsentUtils.initialize()
├── _isInitialized == true  ───────────────────────────────────────►  return null
│
└── (debug only) ConsentInformation.instance.reset()
    │
    └── _initializeWithTimeout()        ── 10 s outer timeout
        │
        ├── timeout fires
        │     └── _initializeConsentRefComponent()   // init ads anyway
        │         └── _isInitialized = true → return null
        │
        ├── exception caught
        │     └── _initializeConsentRefComponent()   // init ads anyway
        │         └── _isInitialized = true → return null
        │
        └── _performInitialization()
            │
            ├── build ConsentDebugSettings (debug only):
            │     DebugGeography.debugGeographyEea
            │     testIdentifiers: [hashed device IDs]
            │
            ├── ConsentInformation.instance.requestConsentInfoUpdate(params,
            │
            │   ┌── onConsentInfoUpdateSuccess
            │   │     ├── isConsentFormAvailable() == true
            │   │     │     └── _loadConsentForm()           // see below
            │   │     │
            │   │     └── isConsentFormAvailable() == false
            │   │           └── _initializeConsentRefComponent()
            │   │               └── complete(null)
            │   │
            │   │   ── exception in success handler
            │   │         └── _initializeConsentRefComponent()
            │   │             └── complete(null)
            │   │
            │   └── onConsentInfoUpdateFailure(error)
            │         └── _initializeConsentRefComponent()
            │             └── complete(error)   // ads still up
            │
            └── _loadConsentForm()
                │
                ├── ConsentForm.loadConsentForm
                │
                │   ┌── onSuccess(consentForm)
                │   │     ├── getConsentStatus()
                │   │     │
                │   │     │   ├── ConsentStatus.required
                │   │     │   │     └── consentForm.show(onDismiss)
                │   │     │   │           ├── formError != null
                │   │     │   │           │     └── _initializeConsentRefComponent()
                │   │     │   │           │         └── complete(formError)
                │   │     │   │           │
                │   │     │   │           └── formError == null  (user submitted)
                │   │     │   │                 └── _loadConsentForm()   // RECURSIVE: reload
                │   │     │   │                       so the next privacy-options open
                │   │     │   │                       reflects the new state
                │   │     │   │
                │   │     │   └── any other status (obtained / notRequired / unknown)
                │   │     │         └── _initializeConsentRefComponent()
                │   │     │             └── complete(null)
                │   │     │
                │   │     └── exception
                │   │           └── _initializeConsentRefComponent()
                │   │               └── complete(null)
                │   │
                │   └── onError(formError)
                │         └── _initializeConsentRefComponent()
                │             └── complete(formError)
```

**Invariants:**

- `_initializeConsentRefComponent()` is invoked on **every** terminal node above.
- `complete(...)` is called **exactly once** per `Completer`.
- The returned `FormError?` is **informational** for telemetry; it never blocks ads init.

---

## The "always-init" side-effect step

Centralize **all** post-consent SDK initialization in one private method so it’s impossible to forget on a new branch:

```dart
Future<void> _initializeConsentRefComponent() async {
  // Google Mobile Ads — primary
  await MobileAds.instance.initialize();

  // Mediation SDKs (only those your project actually uses)
  await yandex.MobileAds.initialize();
  // await AppLovinMAX.initialize('SDK_KEY');

  // Native bridge for SDKs without Flutter plugins,
  // or for AdMob test-mode toggles
  final NativeBridge nativeBridge = NativeBridge();
  await nativeBridge.initCustomSDKs();

  // Other components whose data collection depends on consent:
  //   FirebaseAnalytics.instance.setConsent(...)
  //   FirebaseCrashlytics.instance.setCrashlyticsCollectionEnabled(true)
}
```

If a vendor’s `initialize()` can throw, wrap **each** call in its own `try/catch` — one failing vendor must not cancel the rest.

---

## EEA debug simulation

In `kDebugMode` only:

```dart
ConsentDebugSettings debugSettings = ConsentDebugSettings(
  debugGeography: DebugGeography.debugGeographyEea,
  testIdentifiers: <String>[
    'D71F3B1579C1F3EADDE871CC7B4F4D6C', // example test device hash
    // add each engineer’s device hash here
  ],
);
final params = kDebugMode
    ? ConsentRequestParameters(consentDebugSettings: debugSettings)
    : ConsentRequestParameters();
```

How to obtain a `testIdentifier`:

1. Run the app once in debug, attempt `requestConsentInfoUpdate` **without** test identifiers.
2. Logcat / Xcode console prints a line of the form  
   `Use new ConsentDebugSettings.Builder().addTestDeviceHashedId("XXXX")...`
3. Copy the hashed ID into the list. **Do not** ship these IDs to release — gate them with `kDebugMode`.

`DebugGeography` values:

| Value | Effect in debug |
|-------|-----------------|
| `debugGeographyEea` | Treat device as EEA → form required when configured. |
| `debugGeographyNotEea` | Treat as non-EEA → status will be `notRequired`. |
| `debugGeographyDisabled` | Use real geolocation. |

---

## Premium / no-ads gate

Gate the **caller**, not the singleton — premium users should never even hash a UMP request:

```dart
final bool isPremium = getIt<PreferencesManager>()
        .getItem<bool>(PreferencesKey.IS_PURCHASE_NO_AD) ??
    false;

if (!isPremium && kReleaseMode) {
  try {
    await getIt<ConsentUtils>().initialize().timeout(
          const Duration(seconds: 10),
          onTimeout: () => null,
        );
  } catch (e) {
    if (kDebugMode) print('Ad initialization failed: $e');
  }
}
```

**At runtime** — when entitlement flips to premium (purchase / restore):

- Do **not** retroactively un-init ad SDKs — Google has no public deinit.
- Stop **requesting** new loads (gate every load with `shouldShowAds = kReleaseMode && !isPremium`).
- Dispose any visible banners/native ads.

---

## Privacy-options re-open (post-consent)

After the user has submitted the first form, the app should expose a “Manage privacy options” entry in Settings. Two patterns:

- **Recommended**: use the platform UMP API `ConsentInformation.instance.getPrivacyOptionsRequirementStatus()` and `ConsentForm.showPrivacyOptionsForm(...)` (see plugin version notes). Only show the menu entry when the status is `required`.
- **Pattern used by this template**: the `_loadConsentForm` recursion ensures the cached form reflects the latest consent state, so reopening it later through the privacy options menu shows the updated answers.

Always reuse `_initializeConsentRefComponent()` even from the privacy-options handler — the cached AdMob consent string updates automatically once `consentForm.show` resolves.

---

## Error and edge case matrix

| Scenario | Handling |
|----------|----------|
| User is premium | Skip entire flow; do not call `ConsentUtils.initialize()`. |
| Debug build, repeatable test | `ConsentInformation.instance.reset()` at start of `initialize()`. |
| `requestConsentInfoUpdate` succeeds, **form not available** | Skip form; init ads. Return `null`. |
| `requestConsentInfoUpdate` succeeds, form available, status `notRequired` / `obtained` / `unknown` | Init ads. Return `null`. |
| `requestConsentInfoUpdate` succeeds, status `required`, **user submits** form | Re-load form (recursive) so cache is fresh; init ads on next pass. |
| `requestConsentInfoUpdate` succeeds, status `required`, **show fails** with `FormError` | Init ads; return `formError`. |
| `requestConsentInfoUpdate` **fails** (network, invalid app ID, EEA service unreachable) | Init ads; return `formError`. |
| `ConsentForm.loadConsentForm` **fails** | Init ads; return `formError`. |
| Synchronous exception inside success handler | Init ads; return `null`. |
| Whole flow exceeds **internal 10 s timeout** | Init ads; return `null`. |
| Whole flow exceeds **caller 10 s timeout** | Caller proceeds with app boot; ads will be initialized lazily by next consent attempt or by the SDK on first ad load. |
| Uncaught exception bubbles up | Caller `try/catch` swallows; debug log only. |
| Re-entrant call to `initialize()` | `_isInitialized` short-circuits; returns `null` instantly. |
| Hot restart in debug | `_isInitialized` resets with the isolate; consent reset() runs again — safe. |
| Cold start without network | Internal timeout fires → ads SDK init likely also fails internally → first ad load triggers SDK retry; app remains usable. |
| Cold start in **EEA** with **published** message | Form shown blocking; user must complete or app continues degraded if form errors out. |
| Cold start in **EEA** without published message | `isConsentFormAvailable() == false`; ads init normally with limited (non-personalized) requests. |
| User on Android 13+ with consent cleared | UMP cache cleared; flow repeats — normal behavior. |
| Mediation SDK init throws inside `_initializeConsentRefComponent` | Catch per-vendor; never let one vendor block Google Mobile Ads init. |

---

## Code templates

The full, copy-paste-ready Dart templates live in [reference.md](reference.md):

1. `consent_utils.dart` — the singleton with timeout, Completer bridge, recursive form reload, every error branch wired.
2. `main_common.dart` caller block — premium gate + outer 10 s timeout + try/catch.
3. `native_bridge.dart` — optional `MethodChannel` wrapper for custom SDKs.
4. `AndroidManifest.xml` + `Info.plist` snippets.
5. DI registration variants — `get_it`/`injectable`, plain `get_it`, Riverpod, Provider.
6. Privacy-options re-open helper (`showPrivacyOptionsForm`).
7. How to obtain `testIdentifiers` for EEA debug simulation.

When implementing in a new project, **read `reference.md` first**, then adapt names/packages/DI to the target codebase.

---

## Testing checklist

- [ ] **Debug, EEA simulated** with valid `testIdentifier` → consent form appears on cold start.
- [ ] **Debug**, hot-restart → `reset()` runs, form reappears.
- [ ] **Debug, non-EEA geography** → `isConsentFormAvailable()` returns `false`; ads still init.
- [ ] **Release, real device in EEA** with published message → form appears, user submits, ads init.
- [ ] **Release, real device outside EEA** → no form; ads init.
- [ ] **Airplane mode at cold start** → internal 10 s timeout fires; `_initializeConsentRefComponent` runs; app boots without hang.
- [ ] **Premium toggle ON** at startup → `ConsentUtils.initialize()` is never called; no ad SDK loaded.
- [ ] **Premium toggle ON at runtime** after consent already initialized → existing SDKs remain loaded but no new ad requests fire.
- [ ] **Form load failure** simulated via invalid AdMob message config → `_initializeConsentRefComponent` runs; `FormError` is returned to caller.
- [ ] **Form show failure** (user kills Activity mid-form) → `_initializeConsentRefComponent` runs; `_isInitialized` stays `false` only if you returned before flipping it — verify the recursion path sets it correctly.
- [ ] **Second call to `initialize()`** in same process → returns instantly with `null`.
- [ ] **Mediation SDK throws** inside `_initializeConsentRefComponent` → other SDKs still initialize.
- [ ] **Privacy options re-open** from Settings → reflects the user’s last submission.
- [ ] **iOS ATT** (if used) — call ATT **after** UMP, not before; the order matters for some mediation SDKs.

---

## Common pitfalls

1. **Initializing `MobileAds` before UMP completes.** Personalization signals (NPA) won’t match the consent string; reviewers may reject. Always go through `_initializeConsentRefComponent`.
2. **Completing a `Completer` twice.** Each terminal node must complete **once**. The template in [reference.md](reference.md) already guards this — keep it that way when adding new branches.
3. **Forgetting `_isInitialized = true` on one path.** Causes the app to re-run the entire flow on every retry. Audit every terminal node.
4. **Shipping `testIdentifiers` to release.** They have no effect there but they reveal engineer device hashes. Gate with `kDebugMode`.
5. **Calling `ConsentInformation.instance.reset()` in release.** Forces re-consent on every cold start — bad UX and likely policy violation.
6. **Blocking the app behind consent.** Never `await` consent without an outer timeout; the SDK can stall on bad network or proxy.
7. **Letting a vendor SDK exception take down `_initializeConsentRefComponent`.** Wrap each `await` in its own try/catch when the vendor is unstable.
8. **Coupling consent to ad UI.** UI widgets should read **only** `shouldShowAds = kReleaseMode && !isPremium`. Consent state never travels to the UI.
9. **Re-using `ConsentRequestParameters` across calls.** Always build fresh in `_performInitialization` — the plugin caches internal handles.
10. **Mixing UMP with ATT in the wrong order on iOS.** Run **UMP first**, then **ATT** (`AppTrackingTransparency`). Some mediation SDKs (e.g. Meta) require IDFA, which depends on ATT, which depends on the user having seen the consent UI first.

---

## Summary for agents implementing a new project

1. Drop the `consent_utils.dart` template from [reference.md](reference.md) into `lib/core/common/utils/`.
2. Register as a **singleton** in your DI container.
3. Insert the **caller block** in `main` between IAP/premium check and `runApp`.
4. Centralize **all** ad / analytics / mediation SDK inits in `_initializeConsentRefComponent`.
5. Configure the AdMob console **GDPR message** and **privacy-options form**, then publish.
6. Add **hashed device IDs** to `testIdentifiers` (debug only).
7. Walk through the **error matrix** above and the **testing checklist** before shipping.
8. Never let a consent failure block the app — every branch must call `_initializeConsentRefComponent` and complete the `Completer` exactly once.

This skill is a **template**; reconcile with the current `google_mobile_ads` plugin version (API names for `loadConsentForm`, `showPrivacyOptionsForm`, and `getPrivacyOptionsRequirementStatus` have evolved across major versions).
