# Telegram Plus — unofficial Android build

This repository builds Telegram Android **13.2.1 (custom build 7292)** from upstream commit
`7be672ead283d022812d75c729d3a04dd4c2a2c6` and applies `changes.patch`.

The patch adds the Telegram Plus app name; local icon tabs for private chats, groups,
channels, bots, favorites and unread chats; HH:mm:ss message and last-seen times;
disables Telegram channel/bot/video sponsored ads; adds the English
**Stop after current audio** toggle (enabled by default, without changing voice messages);
and opens the selected peer's profile bio when its avatar is tapped in the chat list.
Favorites are stored locally per account. Up to **10 accounts** can be added without Premium;
the Java account slots and native connection instances have both been expanded.

## Build

The **Build Telegram Plus APK** workflow runs when the patch/workflow is pushed to
`main`, or manually from **Actions → Build Telegram Plus APK → Run workflow**.
After success, download **telegram-plus-13.2.1-10accounts-apk** from the run's Artifacts section.
Extract the ZIP to obtain the signed universal APK.

The existing six repository Actions secrets are reused:
`TELEGRAM_API_ID`, `TELEGRAM_API_HASH`, `ANDROID_KEYSTORE_BASE64`,
`ANDROID_KEY_ALIAS`, `ANDROID_KEY_PASSWORD`, `ANDROID_STORE_PASSWORD`.
Do not commit credentials or signing keys. Keep the original signing key to update
an existing installation. The build retains the previous `org.telegram.messenger.beta`
package and signed `afatDebug` variant. It uses the upstream sample Google configuration;
validate sign-in, notifications, and behavior on a device.

This is an unofficial client. Telegram source and this patch are distributed under
GPL-2.0-or-later; upstream: https://github.com/DrKLO/Telegram.
