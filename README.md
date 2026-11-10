# EchoGram — unofficial Telegram Android build

Based on Telegram Android **13.2.1**, upstream commit `7be672ead283d022812d75c729d3a04dd4c2a2c6`, custom build **7293**.

Current changes:
- EchoGram name and the supplied blue/purple icon, including adaptive launcher resources.
- Stop after current audio (enabled by default); manual Next and voice playback remain available.
- Disable Telegram-sponsored placements in channels, bot headers and video playback.
- Preserve locally received ordinary messages after remote deletion and display them faded; explicit deletion in this app still removes them. Secret chats retain upstream behavior. Telegram does not identify who performed remote deletion, including deletion on another device.
- Show precise message and available last-seen timestamps in 24-hour HH:mm:ss format; hidden status remains hidden.
- Read retention markers from an in-memory index, load/persist them on the storage queue, batch redraw notifications and preserve retained rows during channel synchronization.

Build workflow runs on `build/echogram-13.2.1-7293` or by workflow_dispatch.
The existing six Actions secrets supply Telegram API credentials and the signing keystore.
After a successful run, download **EchoGram-13.2.1-APK**, then extract **EchoGram-13.2.1.apk**.
The existing package/signing setup is retained for update compatibility; the version code is increased.

Local checks cover retention, account isolation, storage-queue ordering, rendering, audio controls, timestamps and launcher resources. Device performance and Android integration still require installing and testing the built APK.
