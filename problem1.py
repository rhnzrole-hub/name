# Berilgan matndagi unli va undosh harflarni sanab, natijani dict ko'rinishida qaytaruvchi funksiya yozish.

def count_vowels_and_consonants(text: str) -> dict:
    v_a_c = {}
    v_a_c['unli'] = 0
    v_a_c['undosh'] = 0
    unlilar = "aeiouAEIOU"
    undoshlar = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for i in text:
        if i in unlilar:
            v_a_c['unli'] += 1
        elif i in undoshlar:
            v_a_c['undosh'] += 1
    return v_a_c

print(count_vowels_and_consonants("Salom Dunyo!"))