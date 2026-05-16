# Rate My App — extended reference

## LED Board mapping (source of truth in repo)

| Location | Responsibility |
|----------|----------------|
| `lib/pages/home/home_page.dart` | `_initRateMyApp`, `_runRateMyApp`, dialog, `_goToReviewApplication` |
| `lib/pages/setting/setting_page.dart` | `SettingReview` → `_goToReviewApplication` |
| `lib/pages/setting/widgets/setting_review.dart` | List row UI; `onTap` inline closure |
| `lib/core/common/contant/app_constant.dart` | `ANDROID_STORE_ID`, `IOS_STORE_ID` |
| `lib/core/common/helper/translate_helper.dart` | `pleaseRateThisApp`, `pleaseTakeABitTimeToReviewApp`, `rate`, `noThanks`, `maybeLater`, `reviewApplication` |

Dialog wiring in home uses:

- `actionsBuilder` with three `TextButton`s each calling `callEvent` + `Navigator.pop`.
- `listener: (button) => true` (allow default handling to proceed; adjust if you customize listener behavior).
- `onDismissed` → `laterButtonPressed` (treat swipe-away / tap-outside as “later”).

## `listener` return value

`showRateDialog` `listener` receives the tapped action. Returning `true` typically means “continue / accept.” If you return `false` to block an action, ensure you still update state so the user is not stuck. Default template: `listener: (button) => true` unless you branch on `button` for analytics only.

## Optional: `in_app_review` hybrid

Use when you want the native **in-app review** dialog (quota-controlled by Apple/Google) before falling back to store URL.

Flow:

1. If `InAppReview.instance.isAvailable()` then `requestReview()` (may no-op silently).
2. Still call `RateMyAppEventType.rateButtonPressed` when user chose “Rate” so local counters stay consistent.
3. Optionally open `StoreRedirect` after a short delay only if product policy requires always landing on store (often unnecessary).

Note: `in_app_review` does not guarantee a visible UI; treat success as “request submitted.”

## Ordering with other first-run modals

Suggested priority (adjust per product):

1. Critical: forced update blocking UI.
2. Legal: GDPR / UMP consent before ads.
3. iOS: ATT when required (often after value moment, not before first paint).
4. Paywall / soft IAP nudges.
5. Rating prompt last or on Nth session to avoid “modal fatigue.”

Use `addPostFrameCallback` + `Future.delayed` only when you must yield to another dialog’s `Navigator` stack.

## Analytics (optional)

Emit events with stable names, for example:

- `rating_prompt_shown`
- `rating_prompt_dismiss_later`
- `rating_prompt_declined`
- `rating_prompt_rate_tapped`
- `store_listing_opened` (+ platform)

Log **after** `callEvent` so backend funnels align with `rate_my_app` state.

## Testing matrix

| Scenario | Expectation |
|----------|-------------|
| First install, launches &lt; min | No dialog |
| Launches ≥ min, days ≥ min | Dialog if not declined / not rated |
| “No thanks” | No repeat until policy reset (library rules) |
| “Later” | Respects `remindLaunches` / `remindDays` |
| “Rate” | Store opens; events updated |
| Hot restart during dialog | Prefer guard flag; avoid double `showRateDialog` |
| Rotate with dialog open | OS recreates; avoid second init from `build()` |

## Debug helpers

- `RateMyApp.reset()` in debug builds to clear prefs for QA (confirm package API on your version).
- Android: verify `applicationId` matches Play Console package.
- iOS: verify numeric ID matches App Store “Apple ID” in App Information.

## Store redirect failure

If `StoreRedirect.redirect` fails (no handler, plugin error):

- Catch and optionally `launchUrl` to `https://apps.apple.com/app/id{iosAppId}` or Play market intent as last resort.
- Never block critical navigation on failure.

## Web / desktop

`rate_my_app` and `store_redirect` are mobile-oriented. Short-circuit:

```dart
if (kIsWeb) return;
```

or use `defaultTargetPlatform` / `Platform.isAndroid || Platform.isIOS` before scheduling the prompt.
