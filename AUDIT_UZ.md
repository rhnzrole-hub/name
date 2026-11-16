# Telegram Plus 13.2.2 — kod va barqarorlik tekshiruvi

Sana: 2026-11-16. Asos: DrKLO/Telegram, `21f7d109da6ab3506c9e9577f98c6a38771ab335` (7303).

Tekshiruv barcha qo‘shilgan/o‘zgartirilgan funksiyalar, ularning bir-biriga ta’siri va interfeysni sekinlashtiradigan takroriy ishlarni qamrab oldi. Bu butun Telegram kodining xatosizligi yoki telefonda qotmasligi haqida kafolat emas. APK yig‘ilmadi.

## Topilgan va tuzatilgan joylar

| Joy | Muammo | Tuzatish |
| --- | --- | --- |
| O‘qilmagan chatlar hisoblagichlari | Olti folder uchun alohida ro‘yxatlar tuzilib, chatlar qayta-qayta ko‘rib chiqilardi | Barcha olti hisoblagich bitta o‘tishda hisoblanadi; interfeys tayyor massivdan foydalanadi |
| Hidden chats va qo‘lda berilgan folderlar | Har bir chatda akkaunt identifikatori qayta tuzilib, sinxronlangan sozlama tekshiruvi bajarilardi | Bir hisoblash davri uchun mustaqil holat nusxalari olinadi; chat boshiga takroriy sozlama chaqiruvlari olib tashlandi |
| Folder Clear cache | `dialog_id` bo‘yicha indeks yo‘q edi; har 200 ta chatlik so‘rov kesh jadvalini to‘liq ko‘rib chiqishi mumkin edi | Yangi va mavjud bazalarda indeks yaratiladi; indeks yaratish xatosi mavjud bazani tiklash/almashtirish yo‘lini ishga tushirmaydi |
| Folder ikonkalari | Har chizishda yangi rang filtri yaratilardi | Rang filtri faqat rang yoki ikonka o‘zgarganda yangilanadi |

Main, Archive va Hidden chats bir xil a’zolik/qisman chiqarish qoidalaridan foydalanishda davom etadi. Qo‘lda qo‘shilgan chat boshqa folderdan olib tashlanmaydi. Yashirilgan chat asosiy/arxiv ro‘yxatlariga chiqmaydi.

## Bajarilgan tekshiruvlar

| Tekshiruv | Natija va chegarasi |
| --- | --- |
| 31 ta o‘zgargan/yangi Java fayli | Kompilyator sintaksis tahlilidan o‘tdi; Android turlari bilan to‘liq kompilyatsiya emas |
| 20 ta o‘zgargan XML | XML tuzilishi to‘g‘ri; Android resurslarini linklash hali bajarilmadi |
| Folder/Hidden/a’zolik yordamchilari | Haqiqiy yordamchi kod izolyatsiyalangan Telegram model va sozlama fixturelari bilan kompilyatsiya qilindi; olti kategoriya, qo‘lda qo‘shish/olib tashlash, arxiv, yashirish, saqlash va akkaunt ajratilishi o‘tdi |
| 20 000 chatli aralash ro‘yxat | Hisoblagichlar ko‘rinadigan ro‘yxatlar bilan mos; unread mark/mention, arxiv, yashirilgan takroriy ID va holat nusxasi ajratilishi tekshirildi |
| 100 000 kesh yozuvli SQLite | So‘rov yangi indeksdan foydalanishi va mahalliy original fayllar chiqarib tashlanishi tasdiqlandi |
| Clear cache va Mark as read | Haqiqiy yordamchi kod fixture bilan bajarildi: to‘g‘ri chatlar, topics/mentions/reactions, haqiqiy vaqtinchalik fayllar, encrypted/thumb/key, band/original fayllar, katalog chegaralari va xato holatlari o‘tdi |
| Audio | Hozirgi kod bilan aynan mos yordamchi va sozlama usullari tekshirildi: joriy musiqadan keyin to‘xtash, ovozli xabar istisnosi, qo‘lda boshqarish yo‘li saqlanishi va oldingi playlist qayta tiklanmasligi |
| Media info | Haqiqiy formatlovchi: 64 bit hajm, progressiv foto, audio, vaqt zonasi, kasr davomiylik va yetishmaydigan metadata holatlari o‘tdi |
| Akkaunt tartibi | Haqiqiy tartiblash yordamchisi: 10 akkaunt, yangi/o‘chirilgan/qayta kirilgan akkaunt, noto‘g‘ri/takroriy qiymatlar va login holati o‘zgarmasligi o‘tdi |
| Native akkauntlar | Haqiqiy C++ `getInstance` tanlash kodi alohida kompilyatsiya qilindi; 10 ta alohida doimiy instansiya tasdiqlandi. Butun tgnet/JNI yig‘ilmagan |
| Yuklashni davom ettirish | Haqiqiy checkpoint yordamchisi: 4 MiB bo‘laklangan faylni qayta ochib faqat yetishmagan oraliqlar to‘ldirildi, yakuniy SHA-256 mos keldi; buzilgan xarita, qisqa fayl va parallel o‘qish/yozish holatlari o‘tdi |
| Patchlar | Bo‘sh joy/conflict va yakuniy/incremental patchni teskari qo‘llash tekshiruvlari o‘tdi |

Izolyatsiyalangan yordamchi sinovlari Android UI, JNI yoki haqiqiy Telegram serveridagi tarmoq sinovini almashtirmaydi.

## Tezlik o‘lchovi

Kompyuterdagi 20 000 chatli fixture, qizdirishdan keyin 100 takrorning o‘rtachasi:

| Hisoblash yo‘li | Vaqt |
| --- | --- |
| Olti ko‘rinadigan ro‘yxatdan alohida hisoblash | 10,481 ms |
| Yangi bitta o‘tishda barcha hisoblagichlar | 0,813 ms |

Taqqoslash bir xil ma’lumotdagi ikki hisoblash yo‘liga tegishli. Bu telefon FPS, ilova ochilish tezligi, tarmoq tezligi yoki butun ilova shuncha marta tezlashishini bildirmaydi. Snapshot optimizatsiyasidan oldingi kod alohida vaqt o‘lchovidan o‘tkazilmagan.

## Firebase paket mosligi — tuzatish kiritildi

Dastlab beshta `google-services.json` faylida faqat `org.telegram.messenger`, `.beta`, `.web` mijozlari bor edi. Endi har birida `org.telegram.plus`, `.beta`, `.web` uchun ham bittadan mahalliy klient mosligi yozuvi bor. Original yozuvlar saqlandi; Firebase backend/project/app identifikatorlari va API qiymatlari uydirilmadi yoki almashtirilmadi.

Shu bilan Google Services plaginidagi yangi application ID ga mos klient topilmasligi sababi konfiguratsiya darajasida bartaraf qilindi. JSON va paket tanlash shartlari tekshirildi; plagin vazifasi yoki Gradle ishga tushirilmagan. Google Services va bildirishnoma kodi yoqilgan holda qoldi.

Bu Firebase konsolida yangi Android ilova ro‘yxatdan o‘tkazilganini anglatmaydi. Ochiq upstream Firebase konfiguratsiyasi asosidagi mahalliy moslashtirish bajarildi. Google yangi paket/imzoga token berishi va fon bildirishnomalari kelishi haqiqiy APK bilan tekshirilishi kerak; hozir buni tasdiqlab bo‘lmaydi.

## Hali o‘lchanmaganlar

Android SDK bilan to‘liq kompilyatsiya, resurs linklash va APK bajarilishi tekshirilmagan. Telefon ulanmagan: Redmi 9A/Android 11 dagi RAM, FPS, ANR/crash, batareya, 10 akkaunt bilan fon ishlashi va haqiqiy upload/download tezligi o‘lchanmagan. Keyingi, alohida ruxsat berilgan yig‘ishdan keyin shu qurilmada chat aylantirish, folder/arxiv/hidden almashish, audio tugashi, tez-tez cancel/retry va kesh tozalashni tekshirish kerak.

Hozirgi natija: topilgan takroriy hisoblash va indeks muammolari tuzatildi; bajarilgan yordamchi sinovlari o‘tdi. To‘liq Android yig‘ish hamda qurilma sinovi qolgan.

## Qo‘llash

`changes.patch` — barcha oldingi funksiyalar va ushbu tuzatishlar birga. Uni yuqoridagi toza upstream commitga qo‘llang. Oldingi patchlar ketma-ketligi allaqachon qo‘llangan bo‘lsa, `download_resume.patch` dan keyin `stability_audit.patch`, so‘ng `firebase_package.patch` ni qo‘llang. Ikkala yo‘lni birga qo‘llamang.

`verification/` ichida izolyatsiyalangan yordamchi sinovlari bor. Ular yonma-yon `Telegram/` manba katalogi va JDK kompilyator moduli bilan bajariladi; Android APK yaratmaydi.
