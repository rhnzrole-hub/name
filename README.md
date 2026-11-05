# Unofficial Telegram Android build

This repository stores a patch against Telegram Android commit `3de37c8cfb039452be7398909461da6288babf15`, and a manually triggered GitHub Actions build. The patch hides sponsored channel messages and adds a stop-after-current-audio playback option.

Before running the workflow, configure repository Actions secrets `TELEGRAM_API_ID`, `TELEGRAM_API_HASH`, `ANDROID_KEYSTORE_BASE64`, `ANDROID_KEY_ALIAS`, `ANDROID_KEY_PASSWORD`, and `ANDROID_STORE_PASSWORD`. Use your own Telegram API credentials and a stable private signing key. Never commit them. The build uses the upstream debug variant and upstream sample Google configuration; validate sign-in, push notifications, and the APK before use. It is an unofficial client.

Download the `telegram-custom-apk` artifact after a successful Actions run. The upstream source is available at https://github.com/DrKLO/Telegram and is licensed under GPL-2.0-or-later; this patch is distributed under the same terms.
