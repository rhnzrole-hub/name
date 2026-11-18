# Telegram Plus 13.2.2 — update build 7305

This build updates the previous `org.telegram.plus.beta` installation using the existing signing Secrets and a higher build number (7305). ARM32 and ARM64 remain supported.

Latest changes: chat-list times HH:mm while message/last-seen times retain seconds; six default categories in full Forward and compact share pickers; refined launcher artwork; cached recipient filtering, search/folder state and forum-topic stability fixes. All earlier functionality remains.

Reproduce: checkout DrKLO/Telegram `21f7d109da6ab3506c9e9577f98c6a38771ab335`, apply the existing published changes.patch, existing updates.patch (build 7304), then updates-7305.patch once. The new delta contains no Firebase configuration or API credential changes. The workflow uses existing API/signing Secrets at runtime.

Upgrade guard: download the previous successful build 7304 artifact from run 43883049257, verify its package and configured keystore certificate before compilation, then verify the new signed APK has the same package/certificate and a strictly higher version code. A mismatch fails the workflow. The artifact includes an update-compatibility report and APK SHA-256.

Previous APK: https://github.com/rhnzrole-hub/name/actions/runs/43883049257 . The final new APK still requires installation/device testing.
