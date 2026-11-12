# EchoGram — unofficial Telegram Android build

Based on Telegram Android **13.2.1**, upstream commit `7be672ead283d022812d75c729d3a04dd4c2a2c6`, custom build **7297**.

Current changes:
- EchoGram name and the supplied blue/purple icon, including adaptive launcher resources.
- Stop after current audio (enabled by default); manual Next and voice playback remain available.
- Disable Telegram-sponsored placements in channels, bot headers and video playback.
- Preserve locally received ordinary messages after remote deletion and display them faded; explicit deletion in this app still removes them. Secret chats retain upstream behavior. Telegram does not identify who performed remote deletion, including deletion on another device.
- Show precise message and available last-seen timestamps in 24-hour HH:mm:ss format; hidden status remains hidden.
- Read retention markers from an in-memory index, load/persist them on the storage queue, batch redraw notifications and preserve retained rows during channel synchronization.

Build workflow runs on `build/echogram-13.2.1-7297` or by workflow_dispatch.
The existing six Actions secrets supply Telegram API credentials and the signing keystore.
After a successful run, download **EchoGram-13.2.1-7297-APK**, then extract **EchoGram-13.2.1.apk**.
The existing package/signing setup is retained for update compatibility; the version code is increased.

Local checks cover retention, account isolation, storage-queue ordering, rendering, audio controls, timestamps and launcher resources. Device performance and Android integration still require installing and testing the built APK.

Startup compatibility fix: preserve the ten account storage slots used by earlier Telegram Plus installs, with eleven distinct native connection slots including the reserved slot. Validate a stored selected-account index before it is used during initialization. The default add-account limit is unchanged. No auth data or account databases are deleted or migrated.

Received cloud-chat disappearing photo/document media, including view-once audio/video, is normalized for local retention before display and database insertion. Existing media-expiry tasks skip deletion of received media/file payloads. Outgoing and secret-chat media keep upstream behavior; already expired or unavailable media cannot be recovered. Normal local cache cleanup still applies.

Join-link preview sheets show Telegram-provided subscriber/member totals below the title before joining. Known invite/full-chat totals are reused; missing totals may be fetched once using the existing chat access details, with the request cancelled on dismissal. Unknown totals stay hidden, and viewing the count never joins the chat.

Edited-message history is stored in an indexed per-account SQLite table before cached content is replaced. Received live edits and later history refreshes preserve available prior text/caption versions; formatting changes are fingerprinted too. The one-tap message menu exposes **Edits history**, with 50-version keyset pages and individual full-text views. Local media edits snapshot the previous cached version before optimistic replacement. Explicit local message deletion or dialog-history clearing removes associated history. Older media file bytes are not separately archived, and unseen versions cannot be recovered. No SQL runs while drawing messages or constructing the context menu.

Retained remotely deleted messages also show a small trash icon inline with the timestamp. A cached, paint-tinted vector span reserves its width in time/bubble measurement. Visible cells rebind only when their retained-deletion marker changes; fading remains enabled and normal messages do not show the icon.

**Burn media** is available in the message menu for downloaded received disappearing media with a known original TTL. Original TTL and acknowledged Burn state are stored in local-only message custom params (high flags, version-1 compatible). The explicit action sends Telegram read-content receipts, checks acknowledgement, preserves local file payloads, suppresses duplicate in-flight requests and permits retry on failure. Sender expiry follows Telegram and the original timer; no server-side forced-expiry or local delete request is sent. Media normalized by older builds may lack its original TTL marker until Telegram supplies the original media metadata again.

Review before the next build: member-count requests now use the sheet account for message-based access and cancel only after dismissal is accepted; Burn result bulletins are suppressed after account changes. The existing update-compatible build variant keeps its package and signing configuration but disables debuggable/JNI-debug flags and default private/debug diagnostic mode. No new Android APK/device profile was produced during this review. Java syntax, resource references, storage/history pagination, Burn acknowledgement/params compatibility, retention rendering and native account-slot regression checks passed locally.

Build retry after GitHub reported a hosted-runner communication loss: pin Ubuntu 24.04, free unused preinstalled tools, record memory/disk resources before compilation, use one Gradle worker and a 4 GiB heap, restrict native compile/link jobs via a shared Ninja pool, and use ThinLTO with one backend worker. The APK now targets arm64-v8a and armeabi-v7a only, including Redmi 9A; x86 emulator architectures are not packaged. Timeout is 180 minutes. The exact cause of the prior runner disconnect was not established because the build log blob was unavailable.

A dedicated Java-compilation step now runs before APK/native packaging so Java type errors fail early.

Protected forwarding change: protected group/channel Forward sends ordinary text or re-uploads photos, videos, audio and documents as new messages. Source files are never moved or deleted. Existing downloads are copied into a private UUID directory; otherwise FileLoadOperation downloads straight into that private directory without normal cache registration or source read/content receipts. The server must acknowledge sending before temporary files are removed. Failure, logout, inactivity timeout and the next process startup also clean private files. Captions, entities, document attributes, spoilers, forum-topic destinations, silent/scheduled sends and confirmed Stars amounts are retained. Source content is snapshotted before asynchronous work. A batch is serial and stops on failure; already sent messages are not automatically resent.

Current scope: one destination chat at a time; albums are copied as separate chronological messages; send additional comments separately. Polls, service/hidden/paid/secret content and monoforum destinations are excluded. Other actions such as opening media or independent auto-downloads continue to have their normal effects. Local verification passed 60 helper behavior checks with Android/transport stubs plus Java syntax/resource checks and the prior audio, disappearing-media, edit-history and Burn regression suites. No real Telegram-network test or full Android compilation has been performed for this pending change.

Pre-build stability review: move FileLoadOperation.start (temporary-file opens/seeks) off the UI thread onto the dedicated file queue, with cancellation serialized after initialization. Re-check originating user identity and source/picker lifetime after a deferred paid-message confirmation. Route short acknowledgements from channels through channel pts updates. Fix downloader cancellation completion for null/empty/zero-token request lists and count pending cancellations before callbacks. These changes preserve source media/cache/read state.

Validation: 60 forwarding behavior checks, 9 extracted downloader-cancellation checks, 6 deferred-confirmation identity/lifecycle checks; previous retention, audio, disappearing-media, edit history, Burn/params, trash-marker and invite-count lifecycle suites passed. A fresh worker-thread retention check verified ordering and publication; 250,000 retention lookups performed no preferences reads and 100 changes coalesced into one refresh. Rendering/time-format/account-slot checks passed, including 88,000 concurrent native account lookups. All 25 modified Java files pass syntax parsing, changed XML parses, and the cumulative binary patch applies cleanly to upstream. No Android SDK/NDK is installed locally; full Android compilation and Redmi 9A frame-rate/RAM/network testing remain pending. This review did not start a GitHub workflow or APK build.

Build 7297 packages the reviewed forwarding changes and stability fixes. It retains the existing package and signing identity for an in-place update. The preceding 7296 retry completed successfully; its workflow configuration is reused.
