# Telegram Plus 13.2.2 — update build 7306

Back leaves the current archive/Hidden chats screen or follows normal app exit from the main screen, without selecting All first. Auto video playback and automatic downloads share one variant, reuse a cached quality, and switch to other qualities on explicit selection. Startup avoids heavy services for unused account slots; connectivity still reaches existing login connections. Immutable folder membership snapshots are reused until changed.

Apply changes.patch, updates.patch, updates-7305.patch and updates-7306.patch in order to upstream 21f7d109da6ab3506c9e9577f98c6a38771ab335. Only the last delta is new; it contains no Firebase/API configuration changes or signing material. Existing repository Secrets are used at runtime.

This build keeps package org.telegram.plus.beta and the existing signing key, and increases APP_VERSION_CODE to 7306. The workflow verifies the configured key against successful build 7305 (run 44236188437), then checks the new APK has the same package/certificate and a higher versionCode. Mismatches fail the build. ARM32/ARM64 are supported. Device startup and installation tests remain necessary.
