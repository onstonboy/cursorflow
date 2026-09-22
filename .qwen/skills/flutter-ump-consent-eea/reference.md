# Reference — code templates

Copy-paste templates that match the patterns described in `SKILL.md`. Adapt package names, DI annotations, mediation SDKs, and preference keys to the target project.

---

## 1. `lib/core/common/utils/consent_utils.dart`

```dart
import 'dart:async';

import 'package:flutter/foundation.dart';
import 'package:google_mobile_ads/google_mobile_ads.dart';
import 'package:injectable/injectable.dart';
// Replace with the mediation SDKs your project actually uses:
import 'package:yandex_mobileads/mobile_ads.dart' as yandex;
// Replace with your project's native bridge:
import 'package:your_app/core/common/utils/native_bridge.dart';

@singleton
class ConsentUtils {
  static const int _timeoutSeconds = 10;

  bool _isInitialized = false;

  Future<FormError?> initialize() async {
    if (_isInitialized) return null;

    if (kDebugMode) {
      ConsentInformation.instance.reset();
    }

    return _initializeWithTimeout();
  }

  Future<FormError?> _initializeWithTimeout() async {
    try {
      return await _performInitialization().timeout(
        const Duration(seconds: _timeoutSeconds),
        onTimeout: () {
          _initializeConsentRefComponent();
          _isInitialized = true;
          return null;
        },
      );
    } catch (e) {
      await _initializeConsentRefComponent();
      _isInitialized = true;
      return null;
    }
  }

  Future<FormError?> _performInitialization() async {
    final ConsentDebugSettings debugSettings = ConsentDebugSettings(
      debugGeography: DebugGeography.debugGeographyEea,
      testIdentifiers: const <String>[
        // Replace with hashed device IDs printed by UMP at runtime.
        'D71F3B1579C1F3EADDE871CC7B4F4D6C',
      ],
    );

    final Completer<FormError?> completer = Completer<FormError?>();
    final ConsentRequestParameters params = kDebugMode
        ? ConsentRequestParameters(consentDebugSettings: debugSettings)
        : ConsentRequestParameters();

    ConsentInformation.instance.requestConsentInfoUpdate(
      params,
      () async {
        try {
          if (await ConsentInformation.instance.isConsentFormAvailable()) {
            final FormError? result = await _loadConsentForm();
            completer.complete(result);
          } else {
            await _initializeConsentRefComponent();
            _isInitialized = true;
            completer.complete(null);
          }
        } catch (_) {
          await _initializeConsentRefComponent();
          _isInitialized = true;
          completer.complete(null);
        }
      },
      (FormError error) {
        _initializeConsentRefComponent().then((_) {
          _isInitialized = true;
          completer.complete(error);
        }).catchError((_) {
          _isInitialized = true;
          completer.complete(error);
        });
      },
    );

    return completer.future;
  }

  Future<FormError?> _loadConsentForm() async {
    final Completer<FormError?> completer = Completer<FormError?>();

    ConsentForm.loadConsentForm(
      (ConsentForm consentForm) async {
        try {
          final ConsentStatus status =
              await ConsentInformation.instance.getConsentStatus();
          if (status == ConsentStatus.required) {
            consentForm.show((FormError? formError) async {
              if (formError != null) {
                await _initializeConsentRefComponent();
                completer.complete(formError);
              } else {
                final FormError? result = await _loadConsentForm();
                _isInitialized = true;
                completer.complete(result);
              }
            });
          } else {
            await _initializeConsentRefComponent();
            _isInitialized = true;
            completer.complete(null);
          }
        } catch (_) {
          await _initializeConsentRefComponent();
          completer.complete(null);
        }
      },
      (FormError? error) async {
        await _initializeConsentRefComponent();
        completer.complete(error);
      },
    );

    return completer.future;
  }

  Future<void> _initializeConsentRefComponent() async {
    final NativeBridge nativeBridge = NativeBridge();

    await MobileAds.instance.initialize();
    await yandex.MobileAds.initialize();
    await nativeBridge.initCustomSDKs();

    // Hook other consent-dependent components here:
    //   FirebaseAnalytics.instance.setConsent(...)
    //   AppLovinMAX.initialize('SDK_KEY')
  }
}
```

---

## 2. Caller — `lib/main_common.dart`

```dart
Future<void> mainCommon({required EnvironmentType env}) async {
  DartPluginRegistrant.ensureInitialized();
  WidgetsFlutterBinding.ensureInitialized();

  EnvironmentConfig.setEnvironment(env);
  await EasyLocalization.ensureInitialized();
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);

  configureDependencies();
  await getIt.allReady();
  await getIt<RevenueCatPaymentManager>().initialize();

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

  if (kReleaseMode) {
    FlutterError.onError =
        FirebaseCrashlytics.instance.recordFlutterFatalError;
  }

  runApp(const MyApp());
}
```

---

## 3. Native bridge — `lib/core/common/utils/native_bridge.dart`

```dart
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';

class NativeBridge {
  static const MethodChannel _channel =
      MethodChannel('com.yourcompany.yourapp/native');

  Future<void> initCustomSDKs() async {
    try {
      await _channel.invokeMethod('initCustomSDKs');
    } catch (e) {
      if (kDebugMode) print('initCustomSDKs failed: $e');
    }
  }

  static Future<void> enableGMATestMode(List<String> testDeviceIds) async {
    try {
      await _channel
          .invokeMethod('enableGMATestMode', {'deviceIds': testDeviceIds});
    } catch (e) {
      if (kDebugMode) print('enableGMATestMode failed: $e');
    }
  }

  Future<void> launchAdInspector() async {
    try {
      await _channel.invokeMethod('launchAdInspector');
    } catch (e) {
      if (kDebugMode) print('launchAdInspector failed: $e');
    }
  }
}
```

---

## 4. Android manifest snippet — `android/app/src/main/AndroidManifest.xml`

```xml
<manifest ...>
  <application ...>
    <meta-data
        android:name="com.google.android.gms.ads.APPLICATION_ID"
        android:value="ca-app-pub-XXXXXXXXXXXXXXXX~YYYYYYYYYY"/>
  </application>
</manifest>
```

---

## 5. iOS `Info.plist` snippet

```xml
<key>GADApplicationIdentifier</key>
<string>ca-app-pub-XXXXXXXXXXXXXXXX~YYYYYYYYYY</string>
<key>SKAdNetworkItems</key>
<array>
  <!-- Items per AdMob console "Update Info.plist" guide -->
</array>
<!-- Only if you also wire ATT separately: -->
<key>NSUserTrackingUsageDescription</key>
<string>We use your data to deliver more relevant ads.</string>
```

---

## 6. DI registration variants

### get_it + injectable

```dart
@singleton
class ConsentUtils { ... } // annotation already in template above

// Run codegen:
//   dart run build_runner build --delete-conflicting-outputs
```

### Plain get_it

```dart
getIt.registerSingleton<ConsentUtils>(ConsentUtils());
```

### Riverpod

```dart
final consentUtilsProvider = Provider<ConsentUtils>((ref) => ConsentUtils());

// Caller:
await ref.read(consentUtilsProvider).initialize().timeout(
      const Duration(seconds: 10),
      onTimeout: () => null,
    );
```

### Provider

```dart
Provider<ConsentUtils>(create: (_) => ConsentUtils())
```

---

## 7. Privacy-options re-open (Settings → Manage privacy options)

If your `google_mobile_ads` version exposes the newer privacy-options API:

```dart
Future<void> openPrivacyOptions() async {
  final status = await ConsentInformation.instance
      .getPrivacyOptionsRequirementStatus();
  if (status != PrivacyOptionsRequirementStatus.required) return;

  await ConsentForm.showPrivacyOptionsForm((FormError? error) async {
    if (error != null && kDebugMode) {
      print('Privacy options error: ${error.message}');
    }
  });
}
```

Otherwise reuse `ConsentUtils._loadConsentForm()` indirectly by re-invoking `initialize()` after `ConsentInformation.instance.reset()` (debug only) or by exposing a public method that wraps `_loadConsentForm`.

---

## 8. Obtaining `testIdentifiers`

1. Run the app once in debug **without** `testIdentifiers`.
2. Look in logcat (Android) or the Xcode console (iOS) for a line containing  
   `Use new ConsentDebugSettings.Builder().addTestDeviceHashedId("XXXXXXXX...")`.
3. Copy the hashed ID into the `testIdentifiers` list in `_performInitialization`.
4. Repeat for every engineer's device.
5. Keep the list **only** inside `kDebugMode` branches.
