---
name: revenuecat-premium-paywall
description: Implement RevenueCat premium entitlement + paywall flows in Flutter (purchases_flutter / purchases_ui_flutter) using Clean Architecture and Riverpod, including secrets handling, initialization, repository+providers, feature gating, restore, and testing. Use when the user mentions RevenueCat, purchases_flutter, purchases_ui_flutter, paywall, entitlement, premium gating, subscriptions, restore purchases, or Customer Center.
---

# RevenueCat Premium Paywall (Flutter)

## Quick start

When implementing RevenueCat premium gating:

1. Read the full reference guide ([`../REVENUECAT_PREMIUM_PAYWALL_GUIDE.md`](../REVENUECAT_PREMIUM_PAYWALL_GUIDE.md)). Same content is mirrored for each agent:
   - Cursor: `@.agents/skills/REVENUECAT_PREMIUM_PAYWALL_GUIDE.md`
   - Codex / Antigravity: `@.agents/skills/REVENUECAT_PREMIUM_PAYWALL_GUIDE.md`
   - Claude Code: `@.claude/skills/REVENUECAT_PREMIUM_PAYWALL_GUIDE.md`
2. Confirm the product model:
   - Entitlement id (recommended: `premium`)
   - Offering/paywall strategy (default offering, packages)
   - User identity strategy (anonymous vs app user id; when to `logIn`/`logOut`)
3. Implement the integration using Clean Architecture boundaries and Riverpod providers.
4. Validate restore, offline/last-known premium behavior, and error states.

## Non-negotiables

- **No secrets in git**: Never commit RevenueCat API keys; load from env/config; optionally use obfuscation (e.g. Envied) where appropriate.
- **Dev-only diagnostics**: Any verbose logs/prints/stacks must be development-only.
- **Idempotent initialization**: Configure Purchases once at app startup; avoid reconfiguring in widgets.
- **Separation of concerns**: UI reads providers; domain defines contracts; data implements RevenueCat calls; core bootstraps SDK and listeners.

## Implementation workflow (checklist)

### 1) RevenueCat dashboard setup (before code)
- [ ] Create project + iOS/Android apps
- [ ] Create products in stores, then attach in RevenueCat
- [ ] Create entitlement id (e.g. `premium`)
- [ ] Create offering (Default) + packages
- [ ] Configure paywall (if using RevenueCat UI)

### 2) Dependencies + configuration
- [ ] Add `purchases_flutter` and (optional) `purchases_ui_flutter`
- [ ] Decide persistence for “last known” premium state (e.g. SharedPreferences)
- [ ] Add environment key loading (and obfuscation strategy if needed)

### 3) Core / SDK bootstrap
- [ ] `Purchases.configure(...)` at app startup (single place)
- [ ] Configure SDK log level only in debug builds
- [ ] Set up listener/broadcaster if using reactive updates from SDK callbacks

### 4) Domain layer (contracts)
- [ ] Define repository port (e.g. `BillingRepository`)
- [ ] Define domain entities/value objects for entitlement snapshot
- [ ] Define use cases (fetch snapshot, restore, present paywall if needed, etc.)

### 5) Data layer (RevenueCat implementation)
- [ ] Implement repository using `Purchases.getCustomerInfo()`, `restorePurchases()`, and offerings/packages APIs as needed
- [ ] Map `CustomerInfo` → domain snapshot (`isPremium`, active entitlements, expiration)
- [ ] Map SDK errors into domain failures (no raw SDK exceptions leaking to UI)

### 6) Presentation layer (Riverpod)
- [ ] `AsyncNotifier`/providers that expose:
  - [ ] current customer snapshot
  - [ ] `isPremium` boolean convenience
  - [ ] actions: restore, purchase flow / present paywall
- [ ] UI states: loading / error / empty / success

### 7) UI flows
- [ ] Paywall entry points:
  - [ ] Upsell button/action (manual)
  - [ ] “present if needed” (entitlement gate)
- [ ] Premium status card / settings entry
- [ ] Customer Center / manage subscriptions entry (if desired)

### 8) Feature gating policy
- [ ] Centralize free-tier limits vs premium-unlimited in a policy service/provider
- [ ] Ensure gates are enforced in the correct layer (domain/policy), not only UI

### 9) Testing and validation
- [ ] Validate on sandbox (iOS) and license test (Android)
- [ ] Test restore purchases
- [ ] Test new install anonymous user → purchase → entitlement becomes premium
- [ ] Test log in/out transitions if using app user ids
- [ ] Test offline behavior / cached snapshot

## Output expectations

When asked to “add RevenueCat premium paywall” to a Flutter app, produce:

- A concrete architecture plan (files + providers + domain/data boundaries)
- A clear identity strategy (`Purchases.logIn` usage)
- A security plan for keys and logging
- A test plan covering purchase/restore and key edge cases

## Reference

- Full implementation guide: [`../REVENUECAT_PREMIUM_PAYWALL_GUIDE.md`](../REVENUECAT_PREMIUM_PAYWALL_GUIDE.md)
  - Cursor: `@.agents/skills/REVENUECAT_PREMIUM_PAYWALL_GUIDE.md`
  - Codex / Antigravity: `@.agents/skills/REVENUECAT_PREMIUM_PAYWALL_GUIDE.md`
  - Claude Code: `@.claude/skills/REVENUECAT_PREMIUM_PAYWALL_GUIDE.md`

