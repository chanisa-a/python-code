import random

#refactor != debug

def test_random():
    # สุ่มตัวเลขระหว่าง 1 - 10 เก็บไว้ในตัวแปรชื่อ random_number
    random_number = random.randint(1, 10)
    
    # รับค่าการทายเลขจากผู้ใช้ เก็บไว้ในตัวแปรชื่อ guess_number
    guess_number = input("What is your guess number?:")

    if random_number == guess_number:
        print("Congratulation")

    elif random_number < guess_number:
        print("Too much")

    elif random_number > guess_number:
        print("Too low")

    print(random_number)

test_random()