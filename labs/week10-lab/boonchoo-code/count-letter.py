# เขียนโปรแกรม
# 1.รับค่าข้อความจากผู้ใช้ เป็นตัวแปร string ชื่อ text
# 2.รับค่าอักขระที่ต้องการนับในข้อความ text 
# 3.ดำเนินการนับอักขระตามที่ผู้ใช้ต้องการ และแสดงผลออกทางหน้าจอ

# ตัวอย่างหน้าจอ
# Input your text: Boonchoo Jitnupong
# Which character do you want to count: o
# 5 letters 'o' found in Boonchoo Jitnupong

print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = 'Hello World'
for letter in text:
    if letter == 'l':
        count += 1
print(f"{count} letters 'l' found in '{text}'")

# =========================================================

text = input("Input your text: ")
character = input("Which character do you want to count: ")

count = 0

for letter in text:
    if letter == character:
        count += 1

print(f"{count} letters '{character}' found in '{text}'")

# =========================================================

