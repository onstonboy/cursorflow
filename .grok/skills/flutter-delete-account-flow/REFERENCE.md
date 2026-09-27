# Delete Account Flow — Reference Implementation (ai_caption)

Complete, annotated documentation of the account-deletion flow as implemented in
the `ai_caption` project. `SKILL.md` (same directory) contains the portable
how-to; this file is the ground truth it was extracted from.

Stack: Flutter, Bloc/Cubit (`flutter_bloc`), `get_it` + `injectable` DI,
Firebase Auth, Cloud Firestore, Google Sign-In, Sign in with Apple, Drift
(SQLite) local DB, `adaptive_dialog`, `easy_localization`.

---

## 1. File map

| Layer | File | Role |
|---|---|---|
| Entry UI | `lib/pages/profile/profile_page.dart` | Footer link; owns `UserSignOutSuccess` → nav reset |
| Entry widget | `lib/widgets/views/term_and_privacy.dart` | "Delete account" link → pushes `DeleteUserPage` |
| Delete UI | `lib/pages/deleteuser/delete_user_page.dart` | Re-auth button + typed `DELETE` confirmation |
| State mgmt | `lib/bloc/blocs/auth_bloc.dart` | `deleteAccount()` orchestration |
| States | `lib/bloc/states/auth_state.dart` | `UserSignOutSuccess`/`Fail`, `AuthSignInSuccess`/`Fail` |
| Repository | `lib/repositories/user_repository.dart` | `deleteAccount`, `signOutAllUser` pass-throughs |
| Auth repo | `lib/repositories/auth_repository.dart` | `signInFirebaseByGG/Apple`, `signOutGoogle` |
| Remote DS | `lib/data/source/remote/datasources/user_remote_data_source.dart` | Firestore archive + delete (L489–523) |
| Google DS | `lib/data/source/remote/datasources/google_remote_data_source.dart` | `authenticate()` + `signInWithCredential`, `signOut()` |
| Apple DS | `lib/data/source/remote/datasources/apple_remote_data_source.dart` | `getAppleIDCredential` + nonce + `signInWithCredential` |
| Local DS | `lib/data/source/local/datasources/user_local_data_source.dart` | `signOutAllUser()` → DAO |
| DAO | `lib/data/source/local/database/daos/user_dao.dart` | `delete(userLocalEntities).go()` |
| Models | `lib/data/model/user.dart`, `.../request/user_deleted_stored_request.dart` | `ACUser`, archive payload |
| Constants | `lib/config/firebase/firebase_constant.dart` | `users`, `users_deleted` collections |
| Result type | `lib/data/source/state.dart` | `State<T,E>` + `fold(success:, error:)` |
| Errors | `lib/data/source/remote/api/error/failures.dart` | `Failures`, `ServerFailure`, `UnhandledFailure` |
| Strings | `lib/core/common/helper/translate_helper.dart` + `assets/translations/*.json` | all UI copy |

---

## 2. End-to-end sequence

```
User on ProfilePage
  │  footer: TermAndPrivacy(isShowDeleteAccount: true,
  │                         isShowTermAndPrivacy: false)
  ▼
tap "Delete account"          term_and_privacy.dart:146
  │  Navigator.push(DeleteUserPage.route())
  ▼
DeleteUserPage
  │  shows: "Before continuing with the user deletion.
  │         Please sign in again to verify that you are the account owner"
  │  button: Platform.isIOS ? Apple : Google        (L96–101)
  ▼
tap sign-in button            _isLoading.value = true
  │  iOS:    _authBloC.signInFirebaseByApple()     auth_bloc.dart:146
  │  else:   _authBloC.signInFirebaseByGoogle()    auth_bloc.dart:79
  ▼
DataSource (google/apple)
  │  provider credential → FirebaseAuth.signInWithCredential → ACUser
  ▼
AuthBloC._createUserFirebase   auth_bloc.dart:171
  │  userRepository.createUserFirebase(user)
  │  → remote: if users/{id} missing → seed doc, restoring credit /
  │    stateCredit / premiumCredit / premiumSubscribeType /
  │    timestampDailyUpdate from users_deleted/{id} if archived
  │  → addUserLocal(user, isSignIn: true)  →  emit AuthSignInSuccess
  ▼
DeleteUserPage BlocListener   delete_user_page.dart:52–68
  │  AuthSignInSuccess → _isLoading=false → _showConfirmDeleteUserDialog()
  │  AuthSignInFail / UserSignOutFail → pop page
  ▼
showTextInputDialog (adaptive_dialog, AdaptiveStyle.iOS)
  │  "Are you sure you want to delete the account?"
  │  "Please type 'DELETE' to confirm"  + text field + okLabel "Delete"
  ▼
texts.first == "DELETE" ?     delete_user_page.dart:167
  ├─ yes → _authBloC.deleteAccount()
  └─ no/cancel → Navigator.pop
  ▼
AuthBloC.deleteAccount()      auth_bloc.dart:108–132
  │  guard: _user == null → return
  │  1) userRepository.deleteAccount(id: _user.id)
  │       → remote: read users/{id}
  │                 → write users_deleted/{id}  (credit, stateCredit,
  │                    premiumCredit, timestampDailyUpdate,
  │                    premiumSubscribeType)
  │                 → delete users/{id}
  │  2) if authType == kGoogle → authRepository.signOutGoogle()
  │       → googleSignIn.signOut()
  │     else (apple/none) → skip provider sign-out
  │  3) _signOutAllUser() → userRepository.signOutAllUser()
  │       → local DAO: delete ALL rows in user_local_entities
  │       → _user = null; emit UserSignOutSuccess(isSignedOut)
  │  any failure → emit UserSignOutFail
  ▼
ProfilePage BlocListener      profile_page.dart:58–74
  │  UserSignOutSuccess → Navigator.pushAndRemoveUntil(SignInPage.route(),
  │                       (route) => false)   // whole stack cleared
  │  UserSignOutFail → toast "Something went wrong, please try again"
```

Key architectural point: `DeleteUserPage` never handles the *success* of the
deletion. The `ProfilePage` underneath it is still subscribed to `AuthBloC`
(a get_it singleton), so when `UserSignOutSuccess` is emitted, the profile
page clears the whole navigation stack — `DeleteUserPage` included.

---

## 3. Deep dive — remote delete (soft delete + archive)

`user_remote_data_source.dart` L488–523:

```dart
@override
Future<State<ACUser, Failures>> deleteAccount({required String id}) async {
  try {
    CollectionReference users =
        firestore.collection(FirebaseConstant.kUsersCollection);
    CollectionReference usersDeleted =
        firestore.collection(FirebaseConstant.kUsersDeletedCollection);
    final userMap = (await users.doc(id).get()).data();
    if (userMap != null) {
      final userRemote = ACUser.fromJson(userMap as Map<String, dynamic>);
      final storedCredit = userRemote.credit;
      final storedStateCredit = userRemote.stateCredit;
      final storedPremiumCredit = userRemote.premiumCredit;
      final storedTimestampDailyUpdate = userRemote.timestampDailyUpdate;
      final storedPremiumSubscribeType = userRemote.premiumSubscribeType;

      await usersDeleted.doc(id).set(ACUserDeletedStoredRequest(
            id: id,
            credit: storedCredit,
            stateCredit: storedStateCredit,
            premiumCredit: storedPremiumCredit,
            timestampDailyUpdate: storedTimestampDailyUpdate,
            premiumSubscribeType: storedPremiumSubscribeType,
          ).toJson());
      await users.doc(id).delete();

      return State.success(userRemote);
    } else {
      final failure = FailureHelper.getFailure("No user found to delete!!");
      return State.error(failure);
    }
  } catch (e) {
    final failure = FailureHelper.getFailure(e.toString());
    return State.error(failure);
  }
}
```

Two writes, sequential (not batched): archive set → source delete. If the
archive write succeeds and the delete throws, the doc remains but an archive
exists — acceptable; the doc would just be re-archived on retry.

### The mirror: restore on `createUserFirebase` (L101–158)

This is the other half of the soft-delete pattern. When a deleted user signs
up again, `users/{id}` no longer exists, so the create path runs — and it
seeds the new doc from `users_deleted/{id}`:

```dart
final isUserExist = (await users.doc(user.id).get()).exists;
if (!isUserExist) {
  final userDeletedStoredMap =
      (await usersDeleted.doc(user.id).get()).data();
  ACUserDeletedStoredRequest? userDeletedStoredRemote;
  if (userDeletedStoredMap != null) {
    userDeletedStoredRemote = ACUserDeletedStoredRequest.fromJson(
        userDeletedStoredMap as Map<String, dynamic>);
  }

  await users.doc(user.id).set(ACUserRequest(
        id: user.id,
        name: user.name,
        authType: user.authType,
        photoUrl: user.photoUrl,
        credit: userDeletedStoredRemote?.credit ?? AppConstant.kDefaultCredit,
        stateType: StateType.kHappy,
        stateCredit: userDeletedStoredRemote?.stateCredit ??
            PremiumHelper.kMaxStateCreditNonPremiumDefault,
        premiumCredit: userDeletedStoredRemote?.premiumCredit ?? 0,
        premiumSubscribeType: userDeletedStoredRemote?.premiumSubscribeType ??
            PremiumSubscribeType.kNone,
        timestampDailyUpdate:
            userDeletedStoredRemote?.timestampDailyUpdate ?? 0,
      ).toJson());
}
```

Archived doc is **not** removed from `users_deleted` after restore — it just
gets overwritten on the next delete.

---

## 4. Deep dive — DeleteUserPage

`delete_user_page.dart` (177 lines). Notable details:

- `kDeleteKeyword = "DELETE"` — exact, case-sensitive comparison at L167.
- `_authBloC = getIt()` in `initState` — singleton cubit shared with the rest
  of the app. `deleteAccount()` works because the re-auth sets `_user`.
- `_isLoading` is a `ValueNotifier<bool>`; only the sign-in button shows a
  spinner. Nothing indicates progress during the *actual deletion*.
- `BlocListener.listenWhen` filters to `AuthSignInSuccess | AuthSignInFail |
  UserSignOutFail` — `UserSignOutSuccess` is deliberately absent (handled by
  the profile page below it in the stack).
- Platform split: `Platform.isIOS → _buildAppleButton`, else Google. Apple
  requires Apple sign-in on iOS when other social logins exist; the delete
  flow reuses the same rule.
- Confirmation via `showTextInputDialog` (`adaptive_dialog`,
  `AdaptiveStyle.iOS` forced on all platforms):

```dart
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
  _popPage();
}
```

---

## 5. Deep dive — Bloc orchestration

`auth_bloc.dart` L108–132 + L221–232:

```dart
Future<void> deleteAccount() async {
  if (_user == null) return;

  final result = await userRepository.deleteAccount(id: _user!.id);
  result.fold(success: (user) async {
    if (_user!.authType == AuthType.kGoogle) {
      final result = await authRepository.signOutGoogle();
      result.fold(success: (isSignedOut) async {
        if (isSignedOut != null) {
          await _signOutAllUser();
        }
      }, error: (error) {
        emit(UserSignOutFail(timeStamp: DateTime.now().millisecondsSinceEpoch));
        _onGetError(error);
      });
    } else {
      _signOutAllUser();
    }
  }, error: (error) {
    emit(UserSignOutFail(timeStamp: DateTime.now().millisecondsSinceEpoch));
    _onGetError(error);
  });
}
```

Observations:

- **Ordering**: remote delete → provider sign-out (Google only) → local wipe.
  Remote first is correct: it needs a still-valid auth session.
- **Apple path**: no provider sign-out at all — goes straight to local wipe.
  (`sign_in_with_apple` has no sign-out; but `FirebaseAuth.signOut()` is also
  never called — see Gaps.)
- `signOutGoogle()` returns `State<bool>`; local wipe runs whenever the
  payload is non-null — effectively always on success.
- `_signOutAllUser()` (L221): `userRepository.signOutAllUser()` → DAO delete
  all → `_user = null` → `emit(UserSignOutSuccess(isSignedOut))`. `isSignedOut`
  is `rowsDeleted > 0`; the emit happens whenever non-null (i.e., always on
  local success — even if 0 rows were deleted, it emits with `false`, and the
  profile page navigates on the state type, not the flag).
- Any error anywhere → `UserSignOutFail` → both `DeleteUserPage` (pop) and
  `ProfilePage` (toast) react.

### Sign-in methods reused for re-auth

`signInFirebaseByGoogle` (L79) / `signInFirebaseByApple` (L146) → repository →
datasource performs provider auth + `FirebaseAuth.signInWithCredential` →
`_createUserFirebase` → `createUserFirebase` (the restore-aware create) →
`addUserLocal(isSignIn: true)` → sets `_user` + emits `AuthSignInSuccess`.

Google DS L52–80: `googleSignIn.authenticate()` → `GoogleAuthProvider.credential(idToken:)` → `signInWithCredential` → builds `ACUser(id: uid, authType: kGoogle, ...)`.

Apple DS L51–102: `rawNonce`/`sha256` nonce → `SignInWithApple.getAppleIDCredential(nonce:)` → `OAuthProvider("apple.com").credential(...)` → `signInWithCredential` → `ACUser(authType: kApple, ...)`.

---

## 6. Local data layer

`user_dao.dart` (Drift):

```dart
Future<dynamic> signOutAllUser() {
  return (delete(userLocalEntities)).go();   // wipes every row
}
```

`user_local_data_source.dart` L51–62 wraps it: `State.success(result > 0)`.

The local `user_local_entities` table stores `id, name, authType, photoUrl,
captionLanguage` — everything needed to rehydrate `ACUser` offline via
`ACUser.fromLocal`. Deletion clears it entirely, so next launch →
`getUserSignedIn()` returns null → sign-in flow.

---

## 7. Entry points

`TermAndPrivacy` (`lib/widgets/views/term_and_privacy.dart`) is a reusable
dot-separated footer: `Restore • Terms • Privacy • Delete account`, each
toggled by flags. `isShowDeleteAccount: true` is only set from
`ProfilePage._buildFooter` (L215–223). Sign-in / paywall footers use the
default (no delete link).

```dart
void _goToDeleteUserPage(context) {
  Navigator.push(context, DeleteUserPage.route());
}
```

`DeleteUserPage.route()` is a plain `MaterialPageRoute` — pushed on top of
profile, which is why the profile listener stays alive to catch
`UserSignOutSuccess`.

---

## 8. Result type & failure handling

All datasource/repository calls return `State<T, Failures>`
(`lib/data/source/state.dart`) — a hand-rolled Either:

```dart
result.fold(
  success: (data) { ... },
  error:   (failure) { ... },
);
```

`Failures` subtypes: `ServerFailure` (wraps `BaseException`, carries
`statusCode`), `UnhandledFailure` (raw message). `FailureHelper.getFailure(e)`
converts exceptions at the datasource boundary. The bloc logs errors via
`Logger().e` and always maps them to a user-visible fail state.

---

## 9. Copy / translations

| Key | English (`en-US.json`) | Used at |
|---|---|---|
| `delete_account` | "Delete account" | footer link |
| `delete_user_description` | "Before continuing with the user deletion. Please sign in again to verify that you are the account owner" | delete page body |
| `notice_confirm_delete_account` | "Are you sure you want to delete the account?" | dialog title |
| `please_type_delete_to_confirm` | "Please type 'DELETE' to confirm" | dialog message |
| `delete` | "Delete" | dialog OK |
| `type` | "Type" | text-field hint |
| `cancel` | "Cancel" | cancel button |

Accessed via `TranslateHelper.<key>` → `easy_localization`'s `tr()`.
Translations exist for en, es, ru, vi, zh-CN.

---

## 10. Known gaps & edge cases

These are facts of the current implementation — review before copying:

1. **Firebase Auth user is never deleted.** No `FirebaseAuth.instance
   .currentUser.delete()`, no `FirebaseAuth.signOut()`. The Firestore doc is
   gone, but the auth account (and its session token) remains valid until
   expiry. For full deletion, reauthenticate then `currentUser.delete()`.
2. **Apple token not revoked.** Sign in with Apple deletion should also POST
   to Apple's token-revocation endpoint (usually via backend/Cloud Function).
3. **Google-only provider sign-out.** Apple users get local wipe only.
4. **No progress UI during deletion.** `_isLoading` resets when
   `AuthSignInSuccess` arrives; the archive+delete+signout+wipe stretch runs
   with no indicator (usually < 1s, but on bad networks the page looks dead).
5. **Partial failure window.** If Firestore delete succeeds but Google
   sign-out fails → `UserSignOutFail`, page pops, but local user row still
   exists pointing at a deleted remote doc.
6. **`UserSignOutSuccess` doubles as delete-success.** Works because the only
   listener navigates unconditionally, but conflates sign-out and deletion.
7. **`deleteAccount()` is a silent no-op when `_user == null`** — fine here
   (re-auth always precedes it), but don't call it without the re-auth step.
8. **Keyword is exact `"DELETE"`** — `texts.first == kDeleteKeyword`, no trim
   or case fold.
9. **Restore is unlimited in time** — `users_deleted` docs never expire; if
   you advertise "permanent deletion", archive TTL is a policy question.
10. **Firestore rules must permit both ops** — client-side `users.delete()`
    and `users_deleted.set()` need matching security rules, and Firestore
    subcollections under `users/{id}` (if any) are NOT deleted by doc delete.
11. **`UserDB` local entity vs remote fields** — local rows don't store
    credits/premium; nothing extra to scrub locally beyond the row itself.
    If your app caches more (SharedPreferences, files), extend
    `signOutAllUser`.
