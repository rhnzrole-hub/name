# Telegram Plus 13.2.2 — update build 7304

Signed ARM32/ARM64 update, package `org.telegram.plus.beta`, separate from EchoGram.

This update includes HH:mm:ss message/last-seen times, horizontal folder swipes, refined six-category icons, Telegram Plus title, avatar-to-profile navigation and the follow-up cache/UI stability fixes. Earlier features — 10 accounts, ad removal, transfer tuning, main/archive/hidden categories, folder membership/actions, audio stop, media info, account ordering and partial-download resume — remain in the base.

Source: DrKLO/Telegram commit `21f7d109da6ab3506c9e9577f98c6a38771ab335`. Apply the existing published `changes.patch`, then `updates.patch` once. Do not apply other incremental patches afterwards. The workflow sets build number 7304 and configures ARM architectures and existing signing/API Secrets at runtime.

The Firebase configurations and API identifiers are unchanged from the previously published successful build `0f36e5f4794a7c67f50e6b34a4b95ae87d08a1dd`. The new updates.patch contains no Firebase configuration files or API credential values. Applying base + update was verified to produce the same source tree as the complete private cumulative patch before build-specific version/ABI/secret configuration.

Previous successful build: https://github.com/rhnzrole-hub/name/actions/runs/43860056285 . Device testing is still required for the new update. Existing helper and syntax checks passed; the new Android build will compile and verify the signed APK.
