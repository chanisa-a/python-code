# รับค่า password จากผู้ใช้
# password นั้นแข็งแรงหรือไม่
# password นั้นจะแข็งแรง ถ้าประกอบไปด้วยตัวเลข ตัวอักษร มี '@' 1 ตัว ยาวมากกว่า 8 ตัว

password = input("Please input your password: ")

is_long_enough = len(password) > 8
has_letter = any(char.isalpha() for char in password)
has_digit = any(char.isdigit() for char in password)
has_one_at = password.count("@") == 1

if is_long_enough and has_letter and has_digit and has_one_at:
    print("Your password is strong!")
else:
    print("Your password is not strong!")

