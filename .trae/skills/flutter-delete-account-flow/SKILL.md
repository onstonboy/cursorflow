---
name: flutter-delete-account-flow
description: Implement a store-compliant "delete account" flow in Flutter apps backed by Firebase Auth + Firestore. Covers forced re-authentication, typed DELETE confirmation, soft-delete archival to a users_deleted collection (with restore-on-signup), provider sign-out, local DB wipe, and navigation reset. Written for Bloc/Cubit + Repository + DataSource + get_it/injectable, adaptable to Riverpod/Provider. Use when the user asks to add account deletion, satisfy Apple App Store guideline 5.1.1(v) / Google Play account-deletion policy, or port a delete-user flow to another project. See REFERENCE.md for the full annotated source implementation.
---

# Flutter Delete Account Flow

Reusable pattern for implementing account deletion in a Flutter + Firebase app.
Extracted from a production app; see `REFERENCE.md` in this directory for the
complete annotated implementation and file map.

## Why this design

Both Apple (guideline 5.1.1(v)) and Google Play require apps that offer account
creation to also offer in-app account deletion. A safe implementation must:

1. **Re-authenticate the user** — deleting an account is a destructive action;
   the session token may be stale, and stores expect proof the requester owns
   the account.
2. **Require explicit confirmation** — typing a keyword (`DELETE`) prevents
   accidental taps.
3. **Delete server data AND local data** — Firestore document, cached user,
   provider sessions.
4. **Reset the navigation stack** — drop the user back on the sign-in page so
   no authed screens remain reachable.
5. **(Optional but valuable) Archive before delete** — copying the user doc to
   a `users_deleted` collection lets a re-registering user recover credits /
   entitlements (soft delete with restore).

## Flow overview

```
ProfilePage (footer link "Delete account")
  └─> TermAndPrivacy widget  ──Navigator.push──>  DeleteUserPage
        ├─ 1. Explanation text ("sign in again to verify ownership")
        ├─ 2. Platform-aware re-auth button:
        │       iOS     → Sign in with Apple  → signInFirebaseByApple()
        │       other   → Sign in with Google → signInFirebaseByGoogle()
        │     (fresh Firebase sign-in ALSO recreates/restores the
        │      Firestore user doc — this is how "restore" works)
        ├─ 3. On AuthSignInSuccess → adaptive_dialog text input:
        │       user must type exactly "DELETE"  → authBloc.deleteAccount()
        │       wrong text / cancel              → pop page
        └─ 4. AuthBloC.deleteAccount():
                a. userRepository.deleteAccount(id)      → Firestore archive+delete
                b. authRepository.signOutGoogle()        → provider sign-out (Google only)
                c. userRepository.signOutAllUser()       → wipe local DB rows
                d. emit UserSignOutSuccess / UserSignOutFail
ProfilePage BlocListener
  └─ on UserSignOutSuccess → pushAndRemoveUntil(SignInPage)  (stack fully reset)
     on UserSignOutFail    → toast "something went wrong"
```

## Implementation checklist

Work through the layers in this order. Genericized templates below; adapt names
(`AppUser`, collection names, state classes) to the target project.

- [ ] 1. Firestore constants: `users`, `users_deleted` collections
- [ ] 2. `UserDeletedStoredRequest` model (json_serializable) holding the
      fields worth restoring (credits, entitlement/premium type, timestamps)
- [ ] 3. Remote data source `deleteAccount(id)` — archive then delete
- [ ] 4. `createUser` — restore-from-`users_deleted` logic (soft delete)
- [ ] 5. Local data source `signOutAllUser()` — delete all cached user rows
- [ ] 6. Repository pass-throughs for both
- [ ] 7. Bloc/Cubit `deleteAccount()` orchestrating remote delete → provider
      sign-out → local wipe → emit result state
- [ ] 8. `DeleteUserPage` — re-auth button + typed confirmation dialog
- [ ] 9. Entry point on profile/settings page + `UserSignOutSuccess` listener
      that resets the nav stack to the sign-in page
- [ ] 10. Translation keys for all user-facing strings
- [ ] 11. Firestore security rules allowing doc delete + users_deleted write
- [ ] 12. (Recommended, see "Gaps") delete the Firebase Auth record itself and
      revoke the Apple token

## Layer-by-layer templates

### 1–2. Constants + archive model

```dart
class FirebaseConstant {
  static const kUsersCollection = "users";
  static const kUsersDeletedCollection = "users_deleted";
}
```

```dart
@JsonSerializable()
class UserDeletedStoredRequest {
  String id;
  int credit;
  int premiumCredit;
  int stateCredit;
  int timestampDailyUpdate;
  PremiumSubscribeType premiumSubscribeType;

  UserDeletedStoredRequest({
    required this.id,
    this.credit = 0,
    this.premiumCredit = 0,
    this.stateCredit = 0,
    this.timestampDailyUpdate = 0,
    this.premiumSubscribeType = PremiumSubscribeType.kNone,
  });

  factory UserDeletedStoredRequest.fromJson(Map<String, dynamic> json) =>
      _$UserDeletedStoredRequestFromJson(json);
  Map<String, dynamic> toJson() => _$UserDeletedStoredRequestToJson(this);
}
```

Only copy fields that are *valuable to restore* — never passwords or PII you
promised to erase. An archive is not GDPR-erasure; if your privacy policy says
"data is deleted", keep the archive minimal or skip this pattern entirely.

### 3. Remote data source — archive then delete

```dart
@override
Future<State<AppUser, Failures>> deleteAccount({required String id}) async {
  try {
    final users = firestore.collection(FirebaseConstant.kUsersCollection);
    final usersDeleted =
        firestore.collection(FirebaseConstant.kUsersDeletedCollection);
    final userMap = (await users.doc(id).get()).data();
    if (userMap != null) {
      final userRemote = AppUser.fromJson(userMap);

      await usersDeleted.doc(id).set(UserDeletedStoredRequest(
        id: id,
        credit: userRemote.credit,
        stateCredit: userRemote.stateCredit,
        premiumCredit: userRemote.premiumCredit,
        timestampDailyUpdate: userRemote.timestampDailyUpdate,
        premiumSubscribeType: userRemote.premiumSubscribeType,
      ).toJson());
      await users.doc(id).delete();

      return State.success(userRemote);
    }
    return State.error(FailureHelper.getFailure("No user found to delete!!"));
  } catch (e) {
    return State.error(FailureHelper.getFailure(e.toString()));
  }
}
```

### 4. Restore on sign-up (inside `createUser`)

When creating a user doc, first check `users_deleted/{id}` and seed the new doc
with archived values instead of defaults:

```dart
final isUserExist = (await users.doc(user.id).get()).exists;
if (!isUserExist) {
  final deletedMap = (await usersDeleted.doc(user.id).get()).data();
  final restored = deletedMap != null
      ? UserDeletedStoredRequest.fromJson(deletedMap)
      : null;

  await users.doc(user.id).set(AppUserRequest(
    id: user.id,
    name: user.name,
    authType: user.authType,
    photoUrl: user.photoUrl,
    credit: restored?.credit ?? AppConstant.kDefaultCredit,
    stateCredit: restored?.stateCredit ?? kDefaultStateCredit,
    premiumCredit: restored?.premiumCredit ?? 0,
    premiumSubscribeType:
        restored?.premiumSubscribeType ?? PremiumSubscribeType.kNone,
    timestampDailyUpdate: restored?.timestampDailyUpdate ?? 0,
  ).toJson());
}
```

This makes the re-auth step in `DeleteUserPage` double as "re-verify + load the
user into memory" so the bloc has a valid `_user` to delete.

### 5. Local wipe

Drift DAO — delete every cached user row:

```dart
Future<dynamic> signOutAllUser() {
  return (delete(userLocalEntities)).go();
}
```

### 7. Bloc/Cubit orchestration

Order matters: remote first (still has a valid auth token + doc), then provider
sign-out, then local wipe, then emit.

```dart
Future<void> deleteAccount() async {
  if (_user == null) return;

  final result = await userRepository.deleteAccount(id: _user!.id);
  result.fold(success: (user) async {
    if (_user!.authType == AuthType.kGoogle) {
      final signOutResult = await authRepository.signOutGoogle();
      signOutResult.fold(success: (isSignedOut) async {
        if (isSignedOut != null) await _signOutAllUser();
      }, error: (error) {
        emit(UserSignOutFail(timeStamp: DateTime.now().millisecondsSinceEpoch));
      });
    } else {
      _signOutAllUser();
    }
  }, error: (error) {
    emit(UserSignOutFail(timeStamp: DateTime.now().millisecondsSinceEpoch));
  });
}

Future<void> _signOutAllUser() async {
  final result = await userRepository.signOutAllUser();
  result.fold(success: (isSignedOut) {
    _user = null;
    if (isSignedOut != null) {
      emit(UserSignOutSuccess(isSignedOut: isSignedOut));
    }
  }, error: (error) {
    emit(UserSignOutFail(timeStamp: DateTime.now().millisecondsSinceEpoch));
  });
}
```

### 8. DeleteUserPage (UI)

Key behaviors:

- `BlocListener` gated by `listenWhen` on `AuthSignInSuccess | AuthSignInFail |
  UserSignOutFail`.
- On `AuthSignInSuccess` → stop loading, open typed-confirmation dialog.
- On fail states → `Navigator.pop(context)`.
- Confirmation uses `adaptive_dialog`'s `showTextInputDialog` with
  `style: AdaptiveStyle.iOS` and a `DialogTextField`; proceeds **only** when
  `texts.first == "DELETE"` (exact, case-sensitive).
- Sign-in button is platform-aware: `Platform.isIOS` → Apple button, else
  Google button, each wired to the matching bloc method and a
  `ValueNotifier<bool>` loading flag.

```dart
static const kDeleteKeyword = "DELETE";

void _showConfirmDeleteUserDialog() async {
  final texts = await showTextInputDialog(
    context: context,
    title: TranslateHelper.noticeConfirmDeleteAccount,
    message: TranslateHelper.pleaseTypeDeleteToConfirm,
    style: AdaptiveStyle.iOS,
    textFields: [DialogTextField(hintText: TranslateHelper.type)],
    okLabel: TranslateHelper.delete,
  );

  if (texts != null && texts.isNotEmpty && texts.first == kDeleteKeyword) {
    _authBloC.deleteAccount();
  } else {
    Navigator.pop(context);
  }
}
```

Full page source: see `REFERENCE.md` §4.

### 9. Entry point + nav reset

- Put a small "Delete account" text link in the profile page footer (this
  project reuses a `TermAndPrivacy` footer widget with an
  `isShowDeleteAccount` flag).
- The **profile page** (which stays under `DeleteUserPage` in the stack) owns
  the `UserSignOutSuccess` listener and does:

```dart
if (state is UserSignOutSuccess) {
  Navigator.pushAndRemoveUntil(context, SignInPage.route(), (r) => false);
}
```

`pushAndRemoveUntil` with `(r) => false` clears every authed route — including
`DeleteUserPage` — so no back-button path into the deleted session remains.

### 10. Translation keys

```
delete_account                  "Delete account"
delete_user_description         "Before continuing with the user deletion.
                                 Please sign in again to verify that you are
                                 the account owner"
notice_confirm_delete_account   "Are you sure you want to delete the account?"
please_type_delete_to_confirm   "Please type 'DELETE' to confirm"
delete                          "Delete"
type                            "Type"
cancel                          "Cancel"
sign_in_with_google             "Sign in with Google"
sign_in_with_apple              "Sign in with Apple"
something_went_wrong_please_try_again  (generic error toast)
```

### 11. Firestore security rules (minimum)

```
match /users/{uid} {
  allow read, update, delete: if request.auth != null && request.auth.uid == uid;
  allow create: if request.auth != null;
}
match /users_deleted/{uid} {
  allow read, write: if request.auth != null && request.auth.uid == uid;
}
```

## Gaps in the source implementation (fix when porting)

The reference implementation works and passes store review, but has known
holes. When applying this pattern to a new project, prefer fixing them:

1. **Firebase Auth record is never deleted.** The flow deletes the Firestore
   doc but never calls `FirebaseAuth.instance.currentUser?.delete()` nor
   `FirebaseAuth.signOut()`. The auth account survives. Fix: after the
   re-auth (step 2) succeeds, call `currentUser.reauthenticateWithCredential(cred)`
   then `currentUser.delete()` — this is also the officially recommended
   Firebase pattern ("re-authenticate then delete").
2. **Apple token is never revoked.** Apple expects apps using Sign in with
   Apple to revoke the user's Apple token server-side on deletion. Add a
   backend call (or Cloud Function) hitting Apple's revoke endpoint.
3. **No loading state during actual deletion.** After typing DELETE the page
   sits idle while remote work runs. Disable the UI / show a spinner.
4. **Partial-failure state.** If Firestore delete succeeds but provider
   sign-out fails, the user is left with local data but no remote doc.
   Consider emitting a dedicated `AccountDeletedButSignOutFailed` state or
   making cleanup best-effort-but-always-navigate.
5. **`UserSignOutSuccess` doubles as "account deleted" signal.** Reusing the
   sign-out state works (profile listener navigates on it) but a dedicated
   `AccountDeleteSuccess` state reads better and avoids conflating flows.
6. **Keyword check is case-sensitive exact match** (`"DELETE"`). Decide
   deliberately; a trimmed/case-insensitive compare may be friendlier.
7. **Stale-session edge:** `AuthBloC.deleteAccount()` early-returns when
   `_user == null`. The re-auth step repopulates `_user`, so this is fine —
   but keep the re-auth mandatory, don't skip it.
8. **The re-auth is a full sign-in, not `reauthenticateWithCredential`.** It
   recreates the Firestore user if missing — which is what powers the restore
   feature — but also means a user who cancelled deletion mid-flow has still
   re-created their doc. Usually harmless; be aware.

## Dependencies used (pubspec)

`flutter_bloc`, `get_it`, `injectable`, `cloud_firestore`, `firebase_auth`,
`google_sign_in` (^7.x — `GoogleSignIn.instance` + `authenticate()`),
`sign_in_with_apple`, `adaptive_dialog` (typed confirmation), `drift` (local
DB), `easy_localization` (`tr()` helper), `equatable` (states), `oktoast`
(toasts), `url_launcher` (terms/privacy links).

## Verification checklist

- [ ] Fresh install → sign in → profile → Delete account → re-auth → type
      DELETE → lands on sign-in page, no back navigation possible
- [ ] `users/{uid}` doc removed in Firestore console; `users_deleted/{uid}`
      contains archived fields
- [ ] Local DB empty (relaunch app → goes to sign-in, not home)
- [ ] Re-register same account → credits/premium restored from archive
- [ ] Wrong keyword / cancel / sign-in failure → returns to profile, nothing
      deleted
- [ ] Google account → `googleSignIn.signOut()` invoked (next Google sign-in
      shows account picker)
- [ ] (If fixed) Firebase Auth user gone from Authentication console; Apple
      credential revoked
