# APK yig‘ish holati — 2026-11-16

Tayyorlangan workflow: `.github/workflows/build.yml`.

- Manba: Telegram 13.2.2, commit `21f7d109da6ab3506c9e9577f98c6a38771ab335`.
- Barcha o‘zgarishlar: `changes.patch`.
- Build: `:TMessagesProj_App:assembleAfatDebug`.
- Paket: `org.telegram.plus.beta`; EchoGram’dan alohida o‘rnatiladi.
- ARM32 va ARM64; Redmi 9A uchun ARM32 mavjud.
- Avvalgi repozitoriyadagi API va Android signing Secrets ishlatiladi; ularning qiymatlari ushbu fayllarga yozilmagan.
- APK imzosi, paket nomi, ilova nomi, ARM32 mavjudligi va SHA-256 yakuniy bosqichda tekshiriladi.
- YAML, shell va ichki Python sintaksisi tekshirildi.

Bu muhitda Android SDK yo‘q. Gradle distributivini yuklash sinovi tarmoq cheklovi bilan tugadi. Shuning uchun oldin ishlatilgan GitHub Actions konfiguratsiyasi asosida alohida build branch tayyorlandi: `build/telegram-plus-13.2.2-7303`.

Foydalanuvchi kod va workflow’ni ommaviy `rhnzrole-hub/name` repozitoriyasiga joylashga hamda GitHub Actions’da yig‘ishga aniq ruxsat berdi. Build branch yuborishga tayyor; ishga tushgan run havolasi GitHub Actions orqali tekshiriladi. APK hali yaratilmagan.

Workflow mahalliy commit: `6ba70ae`. ZIP ushbu tayyor workflow’ni ham o‘z ichiga oladi. Firebase token va fon bildirishnomalari APK/qurilma sinovini kutmoqda.
