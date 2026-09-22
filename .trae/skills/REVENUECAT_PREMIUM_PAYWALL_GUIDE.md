# RevenueCat Premium Paywall — Flutter Implementation Guide

> Use this as a step-by-step blueprint when
> wiring RevenueCat + Riverpod premium gating into a new Flutter app.

---

## Table of Contents

1. [Overview & Architecture](#1-overview--architecture)
2. [RevenueCat Dashboard Setup](#2-revenuecat-dashboard-setup)
3. [Flutter Dependencies](#3-flutter-dependencies)
4. [Secrets & Environment Keys](#4-secrets--environment-keys)
5. [Core SDK Layer](#5-core-sdk-layer)
6. [Domain Layer](#6-domain-layer)
7. [Data Layer](#7-data-layer)
8. [Presentation Layer — Providers](#8-presentation-layer--providers)
9. [UI — Hub Screen, Upsell Dialog & Status Card](#9-ui--hub-screen-upsell-dialog--status-card)
10. [Feature Gating (Free-Tier Limits)](#10-feature-gating-free-tier-limits)
11. [Settings Integration](#11-settings-integration)
12. [Error Handling](#12-error-handling)
13. [Debug Tooling](#13-debug-tooling)
14. [Telemetry Events](#14-telemetry-events)
15. [Testing](#15-testing)
16. [End-to-End Flow](#16-end-to-end-flow)
17. [Checklist](#17-checklist)

---

## 1. Overview & Architecture

The integration follows **Clean Architecture** with **Riverpod** state management:

```
┌─────────────────────────────────────────────────────────────────────┐
│  Presentation                                                        │
│  ┌──────────────────────────────────────┐  ┌──────────────────────┐ │
│  │  isPremiumProvider (bool)            │  │  subscriptionWrite   │ │
│  │  billingCustomerInfoProvider         │  │  PolicyProvider      │ │
│  │  (AsyncNotifier<Snapshot>)           │  │                      │ │
│  └──────────┬───────────────────────────┘  └──────────┬───────────┘ │
│             │ watches                                  │ reads        │
├─────────────┼─────────────────────────────────────────┼─────────────┤
│  Domain     │                                         │              │
│  ┌──────────▼───────────────────┐  ┌──────────────────▼──────────┐  │
│  │  BillingRepository (abstract)│  │  SubscriptionWritePolicy    │  │
│  │  PremiumEntitlementPort      │  │  (free/unlimited)           │  │
│  │  BillingCustomerSnapshot     │  │                             │  │
│  └──────────────────────────────┘  └─────────────────────────────┘  │
├─────────────────────────────────────────────────────────────────────┤
│  Data                                                                │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  RevenueCatBillingRepository                                  │   │
│  │  Purchases.getCustomerInfo() / restorePurchases()             │   │
│  │  billingSnapshotFromCustomerInfo()  (mapper)                  │   │
│  └──────────────────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────────────────┤
│  Core / SDK Bootstrap                                                │
│  ┌────────────────────┐  ┌─────────────────────────────────────┐    │
│  │  initializeRevCat  │  │  RevenueCatCustomerInfoBroadcaster  │    │
│  │  (Purchases.       │  │  (Stream<void> — SDK listener)      │    │
│  │   configure)       │  │                                     │    │
│  └────────────────────┘  └─────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
```

**Key naming clarity:**
- `BillingCustomerSnapshot` / `isPremium` = RevenueCat entitlement state.
- "Subscription entity" = user-created items tracked in the app. These are different concepts.

---

## 2. RevenueCat Dashboard Setup

Before writing any code, complete the RevenueCat configuration:

### 2.1 Create Project & Apps

1. Sign in at [app.revenuecat.com](https://app.revenuecat.com).
2. Create a new **Project**.
3. Add an **App** for each platform (iOS → App Store Connect, Android → Google Play).
4. Copy the **API keys** for each platform (starts with `appl_` or `goog_`).

### 2.2 Products

| Platform | Where to create |
|----------|----------------|
| iOS | App Store Connect → In-App Purchases |
| Android | Google Play Console → In-App Products / Subscriptions |

Create your products there first, then in RevenueCat:

- Go to **Products** and add each product ID.

### 2.3 Entitlements

1. Go to **Entitlements** → **+ New Entitlement**.
2. Name: `premium` (this string must match `RevenueCatIds.premiumEntitlement` in code).
3. Attach all products that unlock this entitlement.

### 2.4 Offerings & Paywall

1. Go to **Offerings** → **+ New Offering** → set as **Default**.
2. Add **Packages** (e.g. Monthly, Annual, Lifetime) and assign products.
3. Go to **Paywalls** → create/configure a paywall for your offering.
   - `RevenueCatUI.presentPaywallIfNeeded(entitlementId)` reads this automatically.

---

## 3. Flutter Dependencies

```yaml
# pubspec.yaml
dependencies:
  purchases_flutter: ^9.15.0          # Core RevenueCat SDK
  purchases_ui_flutter: ^9.15.0       # RevenueCat UI (paywall, customer center)
  flutter_riverpod: ^2.x.x            # State management
  shared_preferences: ^2.x.x          # Persist last-known premium state
  envied: ^0.x.x                      # Secure API key obfuscation (optional but recommended)

dev_dependencies:
  envied_generator: ^0.x.x
  build_runner: ^2.x.x
```

After adding, run:

```bash
flutter pub get
dart run build_runner build --delete-conflicting-outputs  # if using envied
```

### iOS minimum deployment target

`purchases_flutter` requires iOS 13+. In `ios/Podfile`:

```ruby
platform :ios, '13.0'
```

### Android minimum SDK

In `android/app/build.gradle`:

```groovy
minSdkVersion 21
```

---

## 4. Secrets & Environment Keys

Never hard-code API keys. Use `envied` (or your preferred obfuscation) to read them from `.env` files that are **gitignored**.

### 4.1 `.env` files (gitignored)

```
# dev.env
REVENUECAT_API_KEY_ANDROID=goog_xxxxxxxxxxxxxxxx
REVENUECAT_API_KEY_IOS=appl_xxxxxxxxxxxxxxxx
```

### 4.2 Envied binding

```dart
// lib/core/env/app_env.dart
import 'package:envied/envied.dart';
part 'app_env.g.dart';

@Envied(path: 'dev.env', obfuscate: true)
abstract final class AppEnv {
  @EnviedField(varName: 'REVENUECAT_API_KEY_ANDROID')
  static final String revenueCatApiKeyAndroid = _AppEnv.revenueCatApiKeyAndroid;

  @EnviedField(varName: 'REVENUECAT_API_KEY_IOS')
  static final String revenueCatApiKeyIOS = _AppEnv.revenueCatApiKeyIOS;
}
```

Repeat for a `prod_env.dart` pointing at `prod.env` and swap at `main_dev.dart` / `main_prod.dart`.

---

## 5. Core SDK Layer

Create a `lib/core/revenuecat/` directory for all SDK bootstrap files.

### 5.1 Entitlement & Product IDs

```dart
// lib/core/revenuecat/revenuecat_ids.dart
abstract final class RevenueCatIds {
  /// Must match the Entitlement identifier created in the RevenueCat dashboard.
  static const String premiumEntitlement = 'premium';

  /// Optional: reference your product IDs for manual purchase flows.
  static const String lifetimeStoreProduct = 'com.yourapp.lifetime_premium';
}
```

### 5.2 Activation flag

```dart
// lib/core/revenuecat/revenuecat_activation.dart
abstract final class RevenueCatActivation {
  static bool isConfigured = false;
}
```

This single flag prevents calling `Purchases.*` methods on unsupported platforms
(web, desktop) or when `configure` failed.

### 5.3 Customer-info broadcast stream

The RevenueCat SDK fires a listener callback when `CustomerInfo` changes (e.g. after
a purchase, app foregrounding). Bridge that into a Dart `Stream` so Riverpod
providers can reactively refresh:

```dart
// lib/core/revenuecat/revenuecat_customer_info_broadcast.dart
import 'dart:async';

abstract final class RevenueCatCustomerInfoBroadcaster {
  static final StreamController<void> _controller =
      StreamController<void>.broadcast();

  static Stream<void> get stream => _controller.stream;

  static void emit() {
    if (!_controller.isClosed) _controller.add(null);
  }
}
```

### 5.4 Initializer

```dart
// lib/core/revenuecat/revenuecat_initializer.dart
import 'package:flutter/foundation.dart';
import 'package:purchases_flutter/purchases_flutter.dart';

import 'revenuecat_activation.dart';
import 'revenuecat_customer_info_broadcast.dart';

// Guard against attaching the listener twice (e.g. hot restart in dev).
var _listenerAttached = false;

String _platformApiKey({
  required String androidKey,
  required String iosKey,
}) {
  if (kIsWeb) return '';
  return switch (defaultTargetPlatform) {
    TargetPlatform.android => androidKey.trim(),
    TargetPlatform.iOS => iosKey.trim(),
    _ => '',
  };
}

Future<void> initializeRevenueCat({
  required String androidApiKey,
  required String iosApiKey,
}) async {
  final key = _platformApiKey(androidKey: androidApiKey, iosKey: iosApiKey);
  if (key.isEmpty) {
    debugPrint('RevenueCat: no key for this platform, skipping.');
    RevenueCatActivation.isConfigured = false;
    return;
  }
  await Purchases.setLogLevel(kDebugMode ? LogLevel.debug : LogLevel.warn);
  try {
    await Purchases.configure(PurchasesConfiguration(key));
    RevenueCatActivation.isConfigured = true;
    if (!_listenerAttached) {
      _listenerAttached = true;
      Purchases.addCustomerInfoUpdateListener((_) {
        RevenueCatCustomerInfoBroadcaster.emit();
      });
    }
  } catch (e, st) {
    RevenueCatActivation.isConfigured = false;
    debugPrint('RevenueCat configure failed: $e\n$st');
  }
}
```

### 5.5 Bootstrap call site

Call `initializeRevenueCat` early in your app bootstrap, **before** `runApp`:

```dart
// lib/bootstrap.dart (or main.dart)
Future<void> bootstrap() async {
  WidgetsFlutterBinding.ensureInitialized();
  // ... other initializations ...
  await initializeRevenueCat(
    androidApiKey: AppEnv.revenueCatApiKeyAndroid,
    iosApiKey: AppEnv.revenueCatApiKeyIOS,
  );
  runApp(const ProviderScope(child: MyApp()));
}
```

---

## 6. Domain Layer

The domain layer is pure Dart — **no Flutter, no RevenueCat imports**.

### 6.1 Billing snapshot entity

```dart
// lib/features/billing/domain/billing_customer_snapshot.dart
final class BillingCustomerSnapshot {
  const BillingCustomerSnapshot({required this.isPremium});

  final bool isPremium;
}
```

### 6.2 Billing repository interface

```dart
// lib/features/billing/domain/repositories/billing_repository.dart
import '../billing_customer_snapshot.dart';

abstract interface class BillingRepository {
  /// Fetch latest customer info from RevenueCat.
  Future<BillingCustomerSnapshot> refreshCustomer();

  /// Restore previous purchases and return updated snapshot.
  Future<BillingCustomerSnapshot> restorePurchases();
}
```

### 6.3 Premium entitlement port

This is a **secondary port** (hexagonal architecture) that cross-feature code
(coordinators, background services) uses to read premium status **without**
importing any billing UI or Riverpod providers:

```dart
// lib/core/premium/premium_entitlement_port.dart

/// Read-only premium access. Cross-feature code depends on this interface,
/// not on billing providers directly.
abstract interface class PremiumEntitlementPort {
  bool get isPremiumNow;

  /// Best-effort wait for billing state to load (with timeout).
  Future<void> awaitCustomerInfoReady();
}
```

### 6.4 Write policy (optional — for free-tier gating)

If the app has a free-tier row cap:

```dart
// lib/core/premium/subscription_write_policy.dart
import '../constants/free_tier_limits.dart';

final class SubscriptionWritePolicy {
  const SubscriptionWritePolicy({required this.maxActiveItems});

  final int? maxActiveItems; // null = unlimited

  static const unlimited = SubscriptionWritePolicy(maxActiveItems: null);
  static const freeTier  = SubscriptionWritePolicy(
    maxActiveItems: kFreeTierMaxItems,
  );
}
```

```dart
// lib/core/constants/free_tier_limits.dart
const int kFreeTierMaxItems = 5;

bool isFreeTierLimitError(Object error) =>
    error is StateError && error.message == 'free_tier_limit';

bool isPremiumRequiredError(Object error) =>
    error is StateError && error.message == 'premium_required';
```

---

## 7. Data Layer

### 7.1 Customer-info mapper

```dart
// lib/features/billing/data/customer_info_mapper.dart
import 'package:purchases_flutter/purchases_flutter.dart';
import '../../../../core/revenuecat/revenuecat_ids.dart';
import '../domain/billing_customer_snapshot.dart';

BillingCustomerSnapshot billingSnapshotFromCustomerInfo(CustomerInfo info) {
  final isActive =
      info.entitlements.all[RevenueCatIds.premiumEntitlement]?.isActive ??
      false;
  return BillingCustomerSnapshot(isPremium: isActive);
}
```

### 7.2 Repository implementation

```dart
// lib/features/billing/data/revenue_cat_billing_repository.dart
import 'package:flutter/services.dart';
import 'package:purchases_flutter/purchases_flutter.dart';
import '../../../../core/revenuecat/revenuecat_activation.dart';
import '../domain/billing_customer_snapshot.dart';
import '../domain/repositories/billing_repository.dart';
import 'customer_info_mapper.dart';

final class RevenueCatBillingRepository implements BillingRepository {
  const RevenueCatBillingRepository();

  static const _fallback = BillingCustomerSnapshot(isPremium: false);

  @override
  Future<BillingCustomerSnapshot> refreshCustomer() async {
    if (!RevenueCatActivation.isConfigured) return _fallback;
    try {
      final info = await Purchases.getCustomerInfo();
      return billingSnapshotFromCustomerInfo(info);
    } on PlatformException {
      return _fallback;
    }
  }

  @override
  Future<BillingCustomerSnapshot> restorePurchases() async {
    if (!RevenueCatActivation.isConfigured) return _fallback;
    try {
      final info = await Purchases.restorePurchases();
      return billingSnapshotFromCustomerInfo(info);
    } on PlatformException {
      rethrow; // Let the UI layer handle specific codes (cancelled, network, etc.)
    }
  }
}
```

### 7.3 Repository provider

```dart
// lib/features/billing/data/billing_repository_provider.dart
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../domain/repositories/billing_repository.dart';
import 'revenue_cat_billing_repository.dart';

final billingRepositoryProvider = Provider<BillingRepository>(
  (_) => const RevenueCatBillingRepository(),
);
```

---

## 8. Presentation Layer — Providers

### 8.1 Preference key

```dart
// lib/core/constants/billing_preferences.dart

/// Persisted so isPremiumProvider stays accurate before RevenueCat
/// responds on cold start.
const String kLastKnownIsPremiumPrefKey = 'app_last_known_is_premium';
```

### 8.2 `BillingCustomerInfoNotifier`

```dart
// lib/features/billing/presentation/providers/billing_providers.dart
import 'package:flutter/foundation.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../../../core/constants/billing_preferences.dart';
import '../../../../core/revenuecat/revenuecat_customer_info_broadcast.dart';
import '../../../../core/providers/shared_preferences_provider.dart';
import '../../data/billing_repository_provider.dart';
import '../../domain/billing_customer_snapshot.dart';

// ─── Primary async provider ──────────────────────────────────────────────────

final billingCustomerInfoProvider =
    AsyncNotifierProvider<BillingCustomerInfoNotifier, BillingCustomerSnapshot>(
  BillingCustomerInfoNotifier.new,
);

class BillingCustomerInfoNotifier
    extends AsyncNotifier<BillingCustomerSnapshot> {
  @override
  Future<BillingCustomerSnapshot> build() async {
    // Re-fetch whenever the RevenueCat SDK fires an update.
    final sub = RevenueCatCustomerInfoBroadcaster.stream.listen((_) {
      ref.invalidateSelf();
    });
    ref.onDispose(sub.cancel);

    final repo = ref.read(billingRepositoryProvider);
    final snapshot = await repo.refreshCustomer();
    await _persist(snapshot.isPremium);
    return snapshot;
  }

  Future<void> reload() async {
    state = const AsyncLoading();
    state = await AsyncValue.guard(() async {
      final snapshot = await ref.read(billingRepositoryProvider).refreshCustomer();
      await _persist(snapshot.isPremium);
      return snapshot;
    });
  }

  Future<void> _persist(bool isPremium) async {
    try {
      await ref
          .read(sharedPreferencesProvider)
          .setBool(kLastKnownIsPremiumPrefKey, isPremium);
    } catch (_) {
      // Non-fatal; best-effort persistence.
    }
  }
}

// ─── Derived sync provider ────────────────────────────────────────────────────

final isPremiumProvider = Provider<bool>((ref) {
  // Debug override (debug builds only).
  if (kDebugMode && ref.watch(debugForcePremiumProvider)) return true;

  final billing = ref.watch(billingCustomerInfoProvider);
  return billing.when(
    data: (s) => s.isPremium,
    loading: () => _staleOrCached(ref, billing),
    error: (_, __) => _staleOrCached(ref, billing),
  );
});

bool _staleOrCached(Ref ref, AsyncValue<BillingCustomerSnapshot> billing) {
  // Prefer previous value if still available (avoids flicker on refresh).
  if (billing.valueOrNull?.isPremium != null) {
    return billing.valueOrNull!.isPremium;
  }
  // Fall back to SharedPreferences last-known value from previous session.
  return ref
          .watch(sharedPreferencesProvider)
          .getBool(kLastKnownIsPremiumPrefKey) ??
      false;
}

// ─── Write policy provider (if using free-tier gating) ───────────────────────

final subscriptionWritePolicyProvider = Provider<SubscriptionWritePolicy>((ref) {
  return ref.watch(isPremiumProvider)
      ? SubscriptionWritePolicy.unlimited
      : SubscriptionWritePolicy.freeTier;
});
```

### 8.3 `PremiumEntitlementPort` implementation

Wire the domain port to the Riverpod provider so cross-feature coordinators
get premium status without binding to presentation:

```dart
// lib/features/billing/presentation/providers/premium_entitlement_port_provider.dart
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../../../core/premium/premium_entitlement_port.dart';
import 'billing_providers.dart';

final premiumEntitlementPortProvider = Provider<PremiumEntitlementPort>(
  (ref) => _ProviderBackedEntitlementPort(ref),
);

final class _ProviderBackedEntitlementPort implements PremiumEntitlementPort {
  _ProviderBackedEntitlementPort(this._ref);
  final Ref _ref;

  @override
  bool get isPremiumNow => _ref.read(isPremiumProvider);

  @override
  Future<void> awaitCustomerInfoReady() async {
    try {
      await _ref
          .read(billingCustomerInfoProvider.future)
          .timeout(const Duration(seconds: 12));
    } on Object catch (e) {
      debugPrint('Premium entitlement wait failed: $e');
    }
  }
}
```

---

## 9. UI — Hub Screen, Upsell Dialog & Status Card

### 9.1 Paywall helper function

Create a reusable function that any screen can call:

```dart
// lib/features/billing/presentation/widgets/premium_upsell_dialog.dart
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:purchases_ui_flutter/purchases_ui_flutter.dart';
import '../../../../core/revenuecat/revenuecat_ids.dart';
import '../billing_error_localizer.dart';
import '../providers/billing_providers.dart';

Future<void> showPremiumUpsellDialog({
  required BuildContext context,
  required WidgetRef ref,
  required String message,  // Feature-specific reason text
}) async {
  final proceed = await showDialog<bool>(
    context: context,
    builder: (ctx) => AlertDialog(
      title: const Text('Upgrade to Premium'),
      content: Text(message),
      actions: [
        TextButton(
          onPressed: () => Navigator.of(ctx).pop(false),
          child: const Text('Not Now'),
        ),
        FilledButton(
          onPressed: () => Navigator.of(ctx).pop(true),
          child: const Text('Continue'),
        ),
      ],
    ),
  );

  if (proceed != true || !context.mounted) return;

  try {
    await RevenueCatUI.presentPaywallIfNeeded(RevenueCatIds.premiumEntitlement);
    // Refresh billing state after the paywall is dismissed.
    ref.invalidate(billingCustomerInfoProvider);
    try {
      await ref.read(billingCustomerInfoProvider.future);
    } on Object catch (_) {
      // Non-fatal; provider will self-heal via the broadcast stream.
    }
  } on Object catch (e) {
    if (!context.mounted) return;
    final msg = billingErrorSnackMessage(context, e);
    if (msg != null) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(msg)));
    }
  }
}
```

**Usage at any call site:**

```dart
if (!ref.read(isPremiumProvider)) {
  await showPremiumUpsellDialog(
    context: context,
    ref: ref,
    message: 'Unlimited subscriptions require Premium.',
  );
  return;
}
```

### 9.2 Billing Hub Screen

A dedicated screen users reach from Settings → Plan:

```
┌──────────────────────────────────────┐
│  ←  My Plan                          │
├──────────────────────────────────────┤
│  ┌────────────────────────────────┐  │
│  │  ★ Premium  /  Free Plan      │  │
│  │  "Enjoy unlimited access..."  │  │
│  └────────────────────────────────┘  │
│                                      │
│  [  Upgrade to Premium  ]  ← CTA    │
│  [  Restore Purchases   ]            │
│                                      │
│  Subscription terms disclaimer...   │
└──────────────────────────────────────┘
```

Key actions:

| Action | Code |
|--------|------|
| **Upgrade** | `RevenueCatUI.presentPaywallIfNeeded(entitlementId)` → `ref.invalidate(billingCustomerInfoProvider)` |
| **Restore** | `billingRepositoryProvider.restorePurchases()` → `ref.invalidate(billingCustomerInfoProvider)` |
| **Manage (premium users)** | `RevenueCatUI.presentCustomerCenter()` |
| **Promo code (iOS)** | `Purchases.presentCodeRedemptionSheet()` |

**Always check `RevenueCatActivation.isConfigured` before calling restore** (show
"Service unavailable" error if false).

**Always `ref.invalidate(billingCustomerInfoProvider)` and await the future** after
any paywall or restore operation so the UI reflects the new state immediately.

### 9.3 Error localizer

```dart
// lib/features/billing/presentation/billing_error_localizer.dart
import 'package:flutter/services.dart';
import 'package:purchases_flutter/purchases_flutter.dart';

/// Returns a user-facing message or null (null = silent, e.g. user cancelled).
String? billingErrorSnackMessage(BuildContext context, Object error) {
  if (error is PlatformException) {
    final code = PurchasesErrorHelper.getErrorCode(error);
    return switch (code) {
      PurchasesErrorCode.purchaseCancelledError => null,   // silent
      PurchasesErrorCode.networkError ||
      PurchasesErrorCode.offlineConnectionError => 'No internet. Please try again.',
      PurchasesErrorCode.storeProblemError => 'Store error. Please try again later.',
      PurchasesErrorCode.configurationError ||
      PurchasesErrorCode.invalidCredentialsError => 'Service temporarily unavailable.',
      _ => error.message ?? 'Something went wrong.',
    };
  }
  return 'Something went wrong.';
}
```

---

## 10. Feature Gating (Free-Tier Limits)

### 10.1 Enforce at the repository boundary

Never enforce limits in the UI — do it in the data layer so the policy is
consistent across all entry points (UI, CSV import, background sync):

```dart
// In SubscriptionRepositoryImpl.upsert()
Future<void> upsert(ItemEntity item) async {
  final isNewItem = await _db.findById(item.id) == null;
  if (isNewItem) {
    final max = _writePolicy.maxActiveItems;
    if (max != null) {
      final count = await _countActiveItems();
      if (count >= max) {
        throw StateError(max == 0 ? 'premium_required' : 'free_tier_limit');
      }
    }
  }
  // ... proceed with insert/update
}
```

### 10.2 Handle the errors in the UI

```dart
try {
  await ref.read(subscriptionRepositoryProvider).upsert(item);
} on StateError catch (e) {
  if (isFreeTierLimitError(e) && context.mounted) {
    await showPremiumUpsellDialog(
      context: context,
      ref: ref,
      message: 'You have reached the 5-item limit. Upgrade for unlimited.',
    );
  }
}
```

### 10.3 Inject the policy

The write policy is injected via Riverpod — switching from free to premium tier
**automatically** updates all repository instances because the policy provider
re-evaluates when `isPremiumProvider` changes:

```dart
final itemRepositoryProvider = Provider<ItemRepository>((ref) {
  final db = ref.watch(appDatabaseProvider);
  final policy = ref.watch(subscriptionWritePolicyProvider);
  return ItemRepositoryImpl(db, policy);
});
```

### 10.4 React to premium state changes

Listen for premium changes in the main shell to synchronize side-effects
(home widgets, reminders, etc.):

```dart
// In your main tabs / shell widget
ref.listen(isPremiumProvider, (previous, next) {
  if (previous == next) return;
  // e.g. sync home widgets, refresh reminders
  ref.read(homeWidgetSyncServiceProvider).syncNow();
});
```

---

## 11. Settings Integration

Recommended settings section structure:

```dart
// Settings → Plan section
ListTile(
  title: const Text('Plan'),
  subtitle: Text(isPremium ? 'Premium' : 'Free'),
  trailing: const Icon(Icons.chevron_right),
  onTap: () => Navigator.of(context).push(
    MaterialPageRoute(builder: (_) => const BillingHubScreen()),
  ),
),

// Premium-only: Manage Subscription
if (isPremium)
  ListTile(
    title: const Text('Manage Subscription'),
    onTap: () async {
      await RevenueCatUI.presentCustomerCenter();
    },
  ),

// iOS-only: Promo Code
if (Platform.isIOS)
  ListTile(
    title: const Text('Redeem Promo Code'),
    onTap: () async {
      await Purchases.presentCodeRedemptionSheet();
    },
  ),
```

---

## 12. Error Handling

### Mapping `PurchasesErrorCode` to UX

| Error Code | UX Behaviour |
|------------|-------------|
| `purchaseCancelledError` | Silent — user explicitly dismissed |
| `networkError` / `offlineConnectionError` | Show "No internet" message |
| `storeProblemError` | "Store error, try later" |
| `configurationError` / `invalidCredentialsError` | "Service unavailable" |
| `purchaseNotAllowedError` | "Purchases not enabled on this device" |
| `productAlreadyPurchasedError` | Refresh billing state, show success |
| Any other `PlatformException` | Show `error.message` or generic fallback |

### Pattern

```dart
try {
  await RevenueCatUI.presentPaywallIfNeeded(RevenueCatIds.premiumEntitlement);
} on PlatformException catch (e) {
  final code = PurchasesErrorHelper.getErrorCode(e);
  if (code == PurchasesErrorCode.purchaseCancelledError) return; // silent
  final msg = billingErrorSnackMessage(context, e);
  if (msg != null && context.mounted) {
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(msg)));
  }
}
```

---

## 13. Debug Tooling

Add a **force-premium** toggle in debug builds so you can test gated UI without
making a real purchase:

```dart
// lib/core/providers/debug_force_premium_provider.dart
import 'package:flutter/foundation.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'shared_preferences_provider.dart';

final debugForcePremiumProvider =
    NotifierProvider<DebugForcePremiumNotifier, bool>(
  DebugForcePremiumNotifier.new,
);

class DebugForcePremiumNotifier extends Notifier<bool> {
  static const _key = 'debug_force_premium';

  @override
  bool build() {
    if (!kDebugMode) return false;
    return ref.watch(sharedPreferencesProvider).getBool(_key) ?? false;
  }

  Future<void> setForced(bool value) async {
    if (!kDebugMode) return;
    await ref.read(sharedPreferencesProvider).setBool(_key, value);
    state = value;
  }
}
```

In `isPremiumProvider`, check this flag first:

```dart
final isPremiumProvider = Provider<bool>((ref) {
  if (kDebugMode && ref.watch(debugForcePremiumProvider)) return true;
  // ... normal logic
});
```

Expose the toggle in a debug settings panel only visible in debug mode:

```dart
if (kDebugMode)
  SwitchListTile(
    title: const Text('[DEBUG] Force Premium'),
    value: ref.watch(debugForcePremiumProvider),
    onChanged: (v) {
      ref.read(debugForcePremiumProvider.notifier).setForced(v);
    },
  ),
```

---

## 14. Telemetry Events

Track these events to measure paywall performance:

| Event name | When |
|------------|------|
| `premium_paywall_viewed` | User sees the paywall (before purchase) |
| `premium_purchase_started` | User taps "Buy" on paywall |
| `premium_purchase_completed` | Purchase succeeds |
| `premium_purchase_failed` | Purchase fails (include `errorType` param) |
| `restore_purchases_started` | User taps Restore |
| `restore_purchases_completed` | Restore succeeds (include `result: premium/no_entitlements`) |
| `restore_purchases_failed` | Restore fails |

Pass a `source` parameter (e.g. `'hub_screen'`, `'upsell_dialog'`, `'settings'`) to
identify which entry point triggered the paywall.

---

## 15. Testing

### Unit — `isPremiumProvider`

```dart
test('isPremiumProvider returns true when snapshot is premium', () {
  final container = ProviderContainer(
    overrides: [
      billingCustomerInfoProvider.overrideWith(
        () => _FakeNotifier(
          const BillingCustomerSnapshot(isPremium: true),
        ),
      ),
    ],
  );
  expect(container.read(isPremiumProvider), isTrue);
});
```

### Unit — free-tier limit

```dart
test('upsert throws free_tier_limit when at cap', () async {
  final repo = ItemRepositoryImpl(
    fakeDb,
    SubscriptionWritePolicy.freeTier, // 5 items
  );
  // seed 5 items...
  await expectLater(
    () => repo.upsert(newItem),
    throwsA(isA<StateError>().having((e) => e.message, 'message', 'free_tier_limit')),
  );
});
```

### Widget — override billing in tests

```dart
testWidgets('shows locked icon when not premium', (tester) async {
  await tester.pumpWidget(
    ProviderScope(
      overrides: [
        isPremiumProvider.overrideWithValue(false),
      ],
      child: const MyApp(),
    ),
  );
  expect(find.byKey(const Key('premium_lock_icon')), findsOneWidget);
});
```

---

## 16. End-to-End Flow

```
App cold start
     │
     ▼
bootstrap()
  ├─ Load secrets (envied / .env)
  └─ initializeRevenueCat(androidKey, iosKey)
       ├─ Purchases.configure(key)
       ├─ RevenueCatActivation.isConfigured = true
       └─ addCustomerInfoUpdateListener → emit on RevenueCatCustomerInfoBroadcaster
     │
     ▼
ProviderScope mounts
  └─ billingCustomerInfoProvider.build()
       ├─ subscribes to RevenueCatCustomerInfoBroadcaster.stream
       │    (any future SDK update → invalidateSelf → re-fetch)
       ├─ RevenueCatBillingRepository.refreshCustomer()
       │    └─ Purchases.getCustomerInfo()
       │         └─ billingSnapshotFromCustomerInfo()
       │              └─ entitlements.all['premium']?.isActive
       └─ persists kLastKnownIsPremiumPrefKey
     │
     ▼
isPremiumProvider resolves
  ├─ DEBUG: check debugForcePremiumProvider
  ├─ AsyncData → snapshot.isPremium
  └─ AsyncLoading/Error → stale value or SharedPrefs last-known
     │
     ▼
subscriptionWritePolicyProvider → freeTier | unlimited
  └─ injected into ItemRepositoryImpl
       └─ enforces row cap on insert
     │
     ▼
User taps premium feature (e.g. add 6th item)
  └─ repository throws StateError('free_tier_limit')
       └─ UI catches → showPremiumUpsellDialog(context, ref, message)
            └─ AlertDialog: [Not Now] | [Continue]
                 └─ [Continue] →
                      RevenueCatUI.presentPaywallIfNeeded('premium')
                        ├─ RevenueCat reads Default Offering from dashboard
                        └─ Displays paywall UI
                             │
                             ▼ (purchase or dismiss)
                      ref.invalidate(billingCustomerInfoProvider)
                      await billingCustomerInfoProvider.future
                             │
                             ▼
                      isPremiumProvider → true (if purchased)
                      subscriptionWritePolicyProvider → unlimited
                             │
                             ▼
                      side-effects: homeWidgetSync, reminder schedules, etc.
```

---

## 17. Checklist

### RevenueCat Dashboard
- [ ] Project + apps created for iOS and Android
- [ ] Products created in App Store Connect / Google Play
- [ ] Products added to RevenueCat Products
- [ ] Entitlement `premium` created and all products attached
- [ ] Default Offering created with packages
- [ ] Paywall configured for Default Offering

### Code
- [ ] `purchases_flutter` + `purchases_ui_flutter` added to `pubspec.yaml`
- [ ] API keys stored in `.env` files (gitignored), loaded via `envied` or equivalent
- [ ] `RevenueCatIds.premiumEntitlement` matches dashboard entitlement identifier
- [ ] `initializeRevenueCat` called before `runApp`
- [ ] `RevenueCatCustomerInfoBroadcaster` wired to `addCustomerInfoUpdateListener`
- [ ] `BillingRepository` interface in domain, `RevenueCatBillingRepository` in data
- [ ] `billingCustomerInfoProvider` subscribes to broadcaster stream
- [ ] `isPremiumProvider` handles loading/error with stale value + SharedPrefs fallback
- [ ] `showPremiumUpsellDialog` invalidates + awaits `billingCustomerInfoProvider` after paywall
- [ ] `billingErrorSnackMessage` silences `purchaseCancelledError`, messages others
- [ ] Free-tier limit enforced in repository layer (not UI layer)
- [ ] `subscriptionWritePolicyProvider` injected into repositories
- [ ] Restore Purchases button on Hub screen
- [ ] `RevenueCatActivation.isConfigured` guard before calling `restorePurchases`
- [ ] Debug force-premium toggle (debug builds only)
- [ ] Telemetry events for paywall viewed, started, completed, failed, restore
- [ ] `isPremiumProvider` listener in main shell for side-effect sync
- [ ] iOS `Purchases.presentCodeRedemptionSheet()` in Settings (if applicable)
- [ ] `RevenueCatUI.presentCustomerCenter()` for premium manage flow

### Testing
- [ ] Unit test: `isPremiumProvider` with mocked `billingCustomerInfoProvider`
- [ ] Unit test: free-tier limit in repository
- [ ] Widget test: ProviderScope override for `isPremiumProvider`
- [ ] Manual: purchase flow on sandbox (TestFlight / Google Play internal track)
- [ ] Manual: restore purchases
- [ ] Manual: paywall dismiss is silent (no error shown)
- [ ] Manual: no internet — shows network error snack

---
