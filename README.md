# Telegram Plus 13.2.2 — branding, 10 accounts, ad removal and moderate transfer tuning

Upstream: https://github.com/DrKLO/Telegram
Pinned commit: `21f7d109da6ab3506c9e9577f98c6a38771ab335` (13.2.2 / 7303).

- AppName and AppNameBeta: Telegram Plus in all bundled locales.
- Default launcher icon: supplied artwork, retaining transparency, in all five Android densities and adaptive icon resources, including standalone.
- Base application ID: org.telegram.plus. Debug builds append .beta; standalone builds append .web. These are separate from EchoGram's org.telegram.messenger.beta.
- Account limit: 10, with or without Premium. Java account slots and limits, native JNI capacity and connection instances are updated together.
- Channel/bot sponsored-message requests and chat insertion are disabled. Video ad cache reuse, loading and initial scheduling are disabled.
- Global search sponsored-result requests are disabled and any in-memory sponsored search results are cleared. Ordinary search results, posts, bot messages and external web/mini-app content are unchanged.
- Alternative built-in icon choices remain available.

`changes.patch` contains the complete source modifications, including binary icon resources. Apply to the pinned, clean upstream checkout with `git apply changes.patch`.

Alternatively, install Pillow and run `python branding/apply_branding.py /path/to/Telegram branding/icon.png` to reproduce the resource conversion from the supplied original, then apply `git apply account_limits.patch` for 10-account support, followed by `git apply ads.patch` for channel/bot/video/global-search ad removal.

No APK build has been started. No Actions workflows are included. Changes are saved locally and as a private file; no GitHub upload was performed.

Validation: Java/native account routing checked; no channel/bot/video ad request construction remains; patch whitespace and reverse application checked. No APK build or on-device test has been run.

Validation update: all application Java sources scanned; no channel/bot/video sponsored-message fetches or sponsored-search fetches remain. Ad-account revenue management links are retained as administrator tools. No build started.

## Moderate transfer tuning

- Eligible regular downloads of at least 1 MiB on non-slow networks: non-Premium in-flight budget 2 to 3 MiB. Premium budget remains 16 MiB. Existing server-controlled downloader killswitch is respected.
- Large unencrypted uploads on non-slow networks: in-flight budget 8 to 10 MiB (20 rather than 16 requests with 512 KiB parts).
- Connection counts, part sizes, slow-network budgets, small-file behavior, secret-chat upload budget, retry handling and server wait handling are unchanged. Story and animation-stream downloads are not boosted.
- `transfer_speed.patch` contains only these transfer changes. If using the scripts plus separate patches instead of the cumulative `changes.patch`, apply it after `ads.patch`.
- Static diff and patch checks passed. Transfer speed, memory use and stability on a real device have not been measured. No APK build has been started.

## Six default local category tabs

Main chat and archived-chat screens always show six fixed icon tabs: All chats, Bots, Users, Groups, Supergroups, Channels. Tabs have equal pixel-distributed widths with no horizontal scrolling or reordering. The selected category is highlighted and unread-chat badges are shown; full titles remain available to accessibility services.

Groups means groups without a public username, including private megagroups. Supergroups means groups with a public username. Broadcast channels (private or public) are in Channels. Bot accounts are excluded from Users. Secret chats belong to Users when their peer is available. These are local views, not Telegram server folders; saved server folders are not edited. The archive row is preserved in every main category. Opening it carries the selected category into the archive, where all six tabs remain visible. Archive badges count archived dialogs only; main badges count main dialogs only. Empty archive categories, including a fully empty archive after deletions/unarchiving, retain the category bar. Normal search and share/forward selection screens retain upstream behavior.

The main and archive ordinary dialog lists are filtered independently. Ordinary pin/archive/read operations are retained; pinned reordering also updates the underlying global list. Category tabs suppress unrelated contact suggestions and cannot be mistaken for editable server folders.

`folders.patch` contains this feature; apply after `transfer_speed.patch` when using individual patches. The cumulative `changes.patch` includes everything.

Validation: actual category helper compiled and tested against isolated model fixtures covering bots, people, basic/private/public groups, public/private broadcast channels, secret chats, archive entry retention, order and unread counts. All four changed/new Java files passed compiler syntax parsing without Android compilation. Icon XML parsed. Six-slot width arithmetic tested at widths from 240 to 1440 pixels. No APK build or on-device UI test was performed.

Archive navigation update: each category passes `plusCategory` when opening folder 1; archive creation clamps and restores it, and its corresponding icon is selected immediately. No second ViewPage is required for archived tabs; category transitions use the same direct-selection path. Archive empty-folder auto-close paths are suppressed for this local-category screen. All six archived-category fixtures, archive-only unread counts, empty archive and actual enable-predicate routing tests passed, along with Java parsing. No APK build performed.

## Hidden chats

Long-press a chat (or select several), open the top-right three-dot menu, and choose Hide chat. The IDs are stored locally in account-specific preferences and scoped to the signed-in user ID. The source lists and Telegram archive membership are not moved or deleted. Main and archive local category views and their badges exclude these IDs; archive-row chat-name previews exclude them too.

Long-press the magnifying-glass icon in the search field (or the action-bar search icon where shown) to open Hidden chats. It inherits the current one of six categories and shows hidden dialogs from both main and archive lists. All six icon tabs remain available. Its own badges count hidden dialogs. Archive history is also loaded as needed. The secondary view identifies itself as Hidden chats and uses normal back navigation, not root-list navigation.

In Hidden chats, the same selected-chat menu offers Unhide chat. This restores visibility in the chat's original main/archive location. Dragging, pin/reorder and archive actions are suppressed in the combined hidden view; restore visibility before using these folder-specific operations. Read/delete/mute behavior otherwise remains upstream. This is local list visibility; global search and notifications retain upstream behavior.

Apply `hidden_chats.patch` after `folders.patch` when using individual patches. The complete `changes.patch` already contains the entire project modification.

Validation: actual visibility and persistence helpers compiled with isolated model/preferences fixtures; tested main/archive exclusion, hidden lists and badges, bot/group category selection, empty hidden categories, unhide and source-folder/order retention, preference-cache reload, separate accounts and a different login reusing the same account slot. Existing six-category/archive tests still pass. Five affected Java sources pass compiler syntax parsing; icon XML and incremental/cumulative reverse patch checks pass. No Android APK build or device UI test performed.

## Add to folder / Remove from folder

The selected-chat three-dot menu in main, archive and Hidden chats now offers Add to folder and Remove from folder. Each opens a picker containing all six local folders. Multiple selected dialogs are supported. Any chat type can be included in any category: a private group can be added to Supergroups; a channel to Users; a bot to Groups, etc. Adding a membership never removes a membership in another folder. Remove suppresses only the chosen folder, including automatic membership; Add reverses the suppression. All chats also supports explicit include/exclude choices.

Overrides are local, persistent and scoped to the account slot plus signed-in user ID. The same overrides are used by main, archive and Hidden chats and their unread badges. They never change server folder IDs, archive membership or hidden status. The archive entry itself cannot be added/removed as a chat. Global-list pin reordering avoids swapping a shared backing list twice.

Apply `folder_membership.patch` after `hidden_chats.patch` if using separate patches. The cumulative `changes.patch` includes every change.

Validation: actual membership, visibility and hidden-state helpers compiled with isolated model/preferences fixtures. Cases passed: unrestricted membership in all six folders; private group in Supergroups while retaining Groups; target-only default removal and Add reversal; multiple selections; duplicate prevention; archive filtering; hidden precedence and badges; account separation; preference-cache reload and a different login using the same account slot. Four affected Java files passed compiler syntax parsing; incremental and cumulative patch checks passed. No Android build or on-device test was performed.

## Stop after current audio

Music/audio file playback now has a persistent Stop after current audio toggle, enabled by default. It appears in the expanded player's three-dot menu (checked) and repeat/order submenu (active color). Disable it to restore upstream automatic advancement. Explicit Next/Previous remains available.

At natural music completion, stopping takes precedence over repeat/shuffle/playlist restoration. The saved-music restoration state is cleared before the standard player cleanup so that a prior queue cannot resume automatically. The end-of-track path and automatic-advance path are both guarded. Voice-message playback retains upstream behavior. The preference uses the same global main settings scope as repeat/shuffle.

Apply `audio_stop.patch` after `folder_membership.patch` when using incremental patches. The cumulative `changes.patch` includes it.

Validation: actual stopping helper and preference setter executed in an isolated Java fixture: enabled/disabled music, non-music/voice, null message, cleanup flags, stop service, saved-queue prevention and preference persistence passed. Guard ordering before saved-queue restore/repeat and the unchanged explicit Next path checked. All three changed Java sources passed compiler syntax parsing; patch checks passed. No APK build or on-device audio test performed.

## Folder icon long-press actions

Long-press any of the six fixed folder icons (selected or not) to open Clear cache and Mark as read. The target category is taken from the pressed icon, independently of the current tab. Main uses visible main dialogs; archive uses visible archived dialogs; Hidden chats uses hidden dialogs from both main/archive. Explicit folder memberships and exclusions are honored; the archive placeholder is excluded.

Before either action, the relevant dialog pages are loaded to the server-end marker (main or archive; both for Hidden chats). Loading can be cancelled and times out after 120 seconds with an error and no action instead of silently processing a partial list. Mark as read dispatches in UI batches of 20 and uses the native per-dialog read, forum/monoforum topics, mentions and reactions APIs.

Clear cache has an in-app confirmation explaining that chat history is kept. The account file database selects paths by target dialog IDs, in batches of 200 IDs, excluding locally-created original files. The cleaner runs on the file queue, accepts only managed cache/media directories after canonical path validation, and deletes cache files and derived encrypted/thumb/key companions. Current playback, active downloads and upload/recording-locked files are skipped. Exported paths outside managed media roots are kept. Successfully removed file ownership metadata is removed using the native API and download indicators refreshed. Completion reports bytes removed, skipped records and failures; lookup errors perform no deletion. Only indexed chat cache can be attributed and cleared per folder; generic/unattributed app cache is not removed.

Apply `folder_actions.patch` after `audio_stop.patch` when applying individual patches. The cumulative `changes.patch` includes all features.

Validation: actual cache/read helpers compiled and executed with filesystem/model fixtures, including byte counts, encrypted files/thumb/key, active playback/download/recording locks, external/original files, another dialog's cache, path traversal and external symlinks, deletion failures and failed DB lookup. SQLite scope/original-file exclusion query tested against a real in-memory SQLite database. Four affected Java files pass compiler syntax parsing; cumulative/incremental reverse patch checks passed. No Android APK build or on-device UI/network test was performed.

## Media info

Channel/group media message menus now include Media info. The expanded photo/video viewer's three-dot menu includes it for media from group/channel dialogs too. The exact tapped message is used, including album items. The dialog shows the document's supplied filename or explicitly labeled Telegram-generated name, server size in readable units and exact bytes, MIME type when provided, dimensions, duration, audio title/artist, local sent time including seconds and timezone, edited time, original forwarded time when supplied, and Message ID. Copy copies the complete info text.

No download, local-file scan or codec probing is needed. Telegram Photo objects do not supply an original filename or MIME type, so the app-generated photo name is labeled and missing MIME/size is shown as not provided. Progressive photo sizes use the largest available variant and byte count; document sizes use 64-bit values. Missing fields are not invented. Private-chat/viewer avatars and non-media messages do not gain this channel/group action.

Apply `media_info.patch` after `folder_actions.patch` for incremental patches; the cumulative `changes.patch` contains all changes.

Validation: actual metadata helper compiled and executed with document/audio/progressive-photo fixtures: 5 GB size, dimensions, fractional duration, local sent/edit/forward timestamps, generated fallback names, missing metadata and newline cleanup passed. ChatActivity, PhotoViewer and the helper passed compiler syntax parsing; incremental and cumulative patch checks passed. No APK build or on-device menu test performed.

## Reorder accounts

The account switcher popups in MainTabsActivity and DialogsActivity now offer Reorder accounts when more than one account is active. Long-pressing an account row opens the same editor. Account rows in SettingsActivity and UserInfoActivity also open it on long-press. The editor shows all active accounts, current-account checkmark, avatars and drag handles; long-press a row or drag its handle to move it vertically. The list scrolls for up to 10 accounts. Ordering is persisted after each move; Done closes the editor. Swipe-to-dismiss is disabled in the sheet to avoid conflicting with vertical account dragging.

The same display-order policy is used in both switchers and the two Settings account lists (the current profile card remains the selected profile; the other-account subset follows the saved relative order). Display order lives in independent app preferences, keyed by account-slot/user-ID/login-time identity. Inactive identities are pruned, stale entries ignored, and newly activated/replaced/logged-in identities append after saved accounts. No account slots, login timestamps, session data or selected account are modified by ordering.

Apply `account_order.patch` after `media_info.patch` for individual patches; `changes.patch` contains everything.

Validation: actual order manager compiled/executed with Android-preferences/UserConfig fixtures covering first-use ordering, persistent order after context recreation, subset ordering, new-account append even with an earlier timestamp, logout, reused slot/new login, duplicate/invalid requested entries, stale stored entries, 10-account reverse order, and unchanged login/user/selection state. Six affected Java sources pass compiler syntax parsing; incremental/cumulative patch checks passed. No APK build or on-device dragging test was performed.

## Download resume after stop/retry

The existing Telegram partial-file resume mechanism is retained and strengthened. Ordinary cancellation retains .temp/.pt files; the final missing-range snapshot is queued after earlier checkpoint writes and synced to disk. Normal checkpoint writes are serialized across operation instances and shortened maps truncate stale trailing records. Checkpoints retain the native big-endian count/range format.

Restart reads validate record counts, file-size bounds, non-overlap and actual partial-file extent. Native split ranges can be unordered, so they are sorted before validation. A valid map resumes only missing intervals, including sparse/out-of-order downloads; its restored progress uses the existing native progress reporting. Invalid/missing maps are treated conservatively instead of assuming a sparse file's length proves contiguous completion. Native sequential/encryption/IV handling remains unchanged. Cache deletion or missing/corrupt partial data can require re-downloading, and native chunk alignment may repeat an incomplete chunk.

Late completion/cancellation/progress from an older operation is prevented from resetting a restarted operation's UI. Queue cleanup removes an operation mapping only when its identity matches. Pending UI-load runnables are retained rather than overwritten. Folder Clear cache additionally checks active operation artifact paths, including .temp/.pt/IV/preload files, rather than only final download filenames.

Apply `download_resume.patch` after `account_order.patch` for individual patches. The cumulative `changes.patch` contains all changes.

Validation: actual checkpoint helper compiled/executed against real temporary files. A 4 MiB out-of-order partial download was reopened, only missing ranges filled, and the final SHA-256 matched the original. Tests also covered complete checkpoints, shorter rewrites, truncated counts, overlap/negative/out-of-bounds ranges, sparse-file extent checks, concurrent writer/reader access and operation-identity map removal. Existing folder-cache/read helper tests passed after the active-artifact guard. Four affected Java sources passed compiler syntax parsing; cumulative/incremental patch checks passed. No APK build or real Telegram/device transfer test was performed.

## Stability audit, 2026-11-16

See `AUDIT_UZ.md` for findings, validation evidence and remaining limits. Fixed repeated category badge scans/settings work, added a dialog-ID cache lookup index, and cached icon color filters. All six badge counts are computed in one pass, including archive/hidden membership overrides. Isolated helper suites, 20,000-dialog counter/list equivalence, 100,000-file SQLite query-plan checks, 31 Java syntax parses, 20 XML parses and the native 10-account dispatch fixture passed. No Android build or device profiling was performed.

**Firebase package mapping update:** the five JSON configurations now also contain `org.telegram.plus`, `.beta` and `.web` client mappings. Original clients remain for the library/upstream variants. This removes the static package-matching blocker using the existing public Telegram Firebase backend identifiers; it does not create Firebase-console Android registrations. Runtime FCM token issuance and background delivery with the custom package/signature still require device verification. Notifications and Google Services plugins remain enabled.

Apply `stability_audit.patch` after `download_resume.patch` when using incremental patches. The cumulative `changes.patch` includes everything.


## Firebase package mapping, 2026-11-16

`firebase_package.patch` follows `stability_audit.patch` for incremental application. `changes.patch` includes the fix. Alternatively, after branding and the other incremental patches, run `python firebase/apply_package_mapping.py /path/to/Telegram` once; it is idempotent and preserves an existing custom client instead of overwriting it.

All five JSON files parse, each contains exactly one mapping for every custom and original variant, and public upstream project/client/API identifiers are retained. Running the mapper twice leaves files byte-identical. Source whitespace and incremental/cumulative reverse-application checks pass. No Gradle/Google Services task, Android compilation, APK build or runtime FCM test was run.

See `firebase/README.md` for the distinction between local package mapping and actual Firebase registration.
