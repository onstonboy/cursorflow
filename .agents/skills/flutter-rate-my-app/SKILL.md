---
name: flutter-rate-my-app
description: >-
  Implements app-store rating prompts in Flutter using rate_my_app (thresholds,
  persisted state, custom dialog) plus store_redirect for manual review links.
  Covers init lifecycle, RateMyAppEventType mapping, duplicate-dialog guards,
  context.mounted, error handling, localization, premium gating, and optional
  in_app_review. Use when adding "rate the app", review prompts, store listing
  links, or migrating/refactoring rating UX.
---

# Flutter: Rate My App (rate_my_app + store_redirect)

## When this skill applies

- Prompt users to rate after N launches or days.
- Settings row "Review app" opening Play Store / App Store.
- Avoid duplicate dialogs, wrong timing, or missing `callEvent` updates.
- Pair with premium (skip ads and optionally skip nag prompts).

## Stack (default template)

| Piece | Role |
|-------|------|
| `rate_my_app` | Persists launches/days; `shouldOpenDialog`; `showRateDialog`; events |
| `store_redirect` | Opens correct store listing from package/bundle IDs |
| Optional `in_app_review` | In-app review sheet where the OS allows (see [reference.md](reference.md)) |

Add to `pubspec.yaml`:

```yaml
dependencies:
  rate_my_app: ^2.3.1
  store_redirect: ^2.0.1
```

Pin versions to your lockfile policy.

## Configuration checklist

1. **Unique `preferencesPrefix`** per app (and per flavor if flavors share device): e.g. `rateMyApp_MyProduct`.
2. **`googlePlayIdentifier`**: Android applicationId (not the display name).
3. **`appStoreIdentifier`**: Numeric Apple ID from App Store Connect (same as used in `itms-apps` links), not bundle id.
4. **Thresholds**: `minDays`, `minLaunches`, `remindDays`, `remindLaunches` tuned to product; document chosen values in README or remote config.
5. **Strings**: All dialog strings localized (easy_localization, ARB, intl, etc.).

## Architecture placement (Clean / BLoC-friendly)

- **UI-only**: `RateMyApp` instance can live in a root `StatefulWidget` (e.g. home shell) or a dedicated `RatingPromptCoordinator` widget injected above tabs.
- **Do not** put rating persistence logic inside unrelated BLoCs unless you need analytics events from domain layer; keep `RateMyApp` API calls in presentation.

## Core behavior (must implement)

### 1. Construct `RateMyApp` once

Initialize fields in `initState` (or inject a singleton factory). Example shape:

```dart
_rateMyApp = RateMyApp(
  preferencesPrefix: 'rateMyApp_${YourAppConstants.appSlug}',
  minDays: 1,
  minLaunches: 7,
  remindDays: 1,
  remindLaunches: 5,
  googlePlayIdentifier: YourAppConstants.androidApplicationId,
  appStoreIdentifier: YourAppConstants.iosAppStoreNumericId,
);
```

### 2. Run init once per session (not every `build`)

**Anti-pattern:** calling `_rateMyApp.init()` from `build()` causes repeated async work on every rebuild.

**Template:** after first frame, or from `initState` with a `bool _ratingFlowScheduled`:

```dart
@override
void initState() {
  super.initState();
  _initRateMyAppConfig();
  WidgetsBinding.instance.addPostFrameCallback((_) {
    if (mounted) _tryShowRateDialog();
  });
}

Future<void> _tryShowRateDialog() async {
  if (_isPremium) return;
  if (_isRateMyAppShow) return;
  try {
    await _rateMyApp.init();
  } catch (_) {
    return;
  }
  if (!mounted) return;
  if (!_rateMyApp.shouldOpenDialog || _isRateMyAppShow) return;
  _isRateMyAppShow = true;
  _rateMyApp.showRateDialog(
    context,
    title: AppStrings.pleaseRateTitle,
    message: AppStrings.pleaseRateBody,
    rateButton: AppStrings.rate,
    noButton: AppStrings.noThanks,
    laterButton: AppStrings.maybeLater,
    actionsBuilder: (dialogContext) => [
      TextButton(
        onPressed: () {
          _rateMyApp.callEvent(RateMyAppEventType.noButtonPressed);
          Navigator.pop(dialogContext);
        },
        child: Text(AppStrings.noThanks),
      ),
      TextButton(
        onPressed: () {
          _rateMyApp.callEvent(RateMyAppEventType.laterButtonPressed);
          Navigator.pop(dialogContext);
        },
        child: Text(AppStrings.maybeLater),
      ),
      TextButton(
        onPressed: () {
          _rateMyApp.callEvent(RateMyAppEventType.rateButtonPressed);
          Navigator.pop(dialogContext);
          _openStoreListing();
        },
        child: Text(AppStrings.rate),
      ),
    ],
    listener: (button) => true,
    onDismissed: () {
      _rateMyApp.callEvent(RateMyAppEventType.laterButtonPressed);
    },
  );
}
```

Use `dialogContext` for `Navigator.pop` so pops target the dialog route, not the page below.

### 3. Duplicate dialog guard

Keep `bool _isRateMyAppShow = false` set to true **before** `showRateDialog`. If the user rotates device or dialog fails to show, reset only when you know the dialog was dismissed without opening (optional advanced: reset in `onDismissed` if you did not open store — usually unnecessary if prefix prevents immediate re-show).

### 4. Event contract (`callEvent`)

| User action | Required `RateMyAppEventType` |
|-------------|-------------------------------|
| No / "No thanks" | `noButtonPressed` |
| Later / dismiss / back | `laterButtonPressed` |
| Rate / positive | `rateButtonPressed` before opening store |

If you omit `callEvent`, counters and "do not show again" semantics break.

### 5. Open store listing (success path)

```dart
Future<void> _openStoreListing() async {
  await StoreRedirect.redirect(
    androidAppId: YourAppConstants.androidApplicationId,
    iOSAppId: YourAppConstants.iosAppStoreNumericId,
  );
}
```

Wrap in `try/catch` if your `store_redirect` version throws; log failures, do not crash.

### 6. Manual "Review app" in settings

Reuse `_openStoreListing()` from a list tile. No `RateMyApp` dialog required; optionally log analytics.

## Error and failure cases

| Case | Handling |
|------|----------|
| `init()` throws (SharedPreferences rare failures) | `try/catch`; exit silently; user not blocked |
| `context` unmounted after `await init()` | `if (!mounted) return` before `showRateDialog` |
| `showRateDialog` with invalid context | Only call when `mounted` and root navigator exists |
| Wrong Android id | Store may 404 or open wrong app; validate CI constants |
| Wrong iOS numeric id | Same; verify in App Store Connect |
| Premium user | Skip `_tryShowRateDialog` entirely (product choice) |
| Child accounts / parental restrictions | Store sheet may fail; catch around redirect |
| Web / desktop targets | Guard with `kIsWeb` / `Platform` checks; skip `rate_my_app` or no-op |

## Edge cases

- **Cold start + many overlays:** defer rating until home is stable (post-frame + optional 300–500 ms delay) so ATT / paywall / update dialog order is defined.
- **Multiple entry routes:** single coordinator widget avoids two hosts both calling `init`.
- **Debug / QA:** expose `RateMyApp.reset()` behind `kDebugMode` or hidden gesture; document in internal QA doc.
- **Reinstall:** new prefs → thresholds restart (expected).
- **Restore from backup:** prefs may restore → dialog may not show (expected).

## Success criteria (definition of done)

- [ ] Prefix and store IDs verified on real devices (Android + iOS).
- [ ] No `init()` spam from `build()`.
- [ ] All three buttons and `onDismissed` call correct `callEvent`.
- [ ] `mounted` checked after every `await` before UI.
- [ ] Settings path opens store without dialog.
- [ ] Premium (if any) does not see prompt (if product requires).
- [ ] `flutter analyze` clean for touched files.

## Optional upgrades

See [reference.md](reference.md) for:

- `in_app_review` hybrid (in-app sheet then store fallback).
- Analytics event names.
- Ordering vs ATT / GDPR / paywall.

## Reference implementation in this repo

LED Board uses `RateMyApp` on the home page with `preferencesPrefix: 'rateMyApp_LedBoard'`, thresholds above, custom `actionsBuilder`, `onDismissed` → `laterButtonPressed`, and `StoreRedirect` from `AppConstant` IDs. Settings uses `SettingReview` + the same redirect. When porting, prefer the **post-frame + mounted + try/catch** pattern over invoking init from `build()`.
