import json

# JSON fayldan talabalar ma'lumotlarini o'qib, eng yaxshi va eng past baholi talabani hamda o'rtacha bahoni topib ekranga chiqaruvchi dastur yozish.

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

grades = [s['grade'] for s in students]
average = sum(grades) / len(grades)

best = max(students, key=lambda x: x['grade'])
worst = min(students, key=lambda x: x['grade'])

print(f"Eng yaxshi talaba: {best['name']} - {best['grade']}")
print(f"Eng past baho: {worst['name']} - {worst['grade']}")
print(f"O'rtacha baho: {average}")