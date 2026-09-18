""""""
#โจทย์ 1 : เครื่องคำนวณอย่างปลอดภัย
#เขียนโปรแกรมรันตัวเลข 2 จำนวนและตัวดำเนินการ 1 ตัว ได้แก่ + - * / แล้วแสดงผลลัพธ์
#โปรแกรมต้องจัดการกรณีต่อไปนี้
 #ผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข #ValueError
 #ผู้ใช้เลือกตัวดำเนินการอื่นนอกเหหนือจาก + - * / raise ValueError
 #ผู้ใช้พยายามหารด้วยศูนย์ #ZeroDivisitionError
 #โปรแกรมต้องแสดง จบการทำงาน เสมอด้วย Finaiiy

#ตัวอย่างผลลัพธ์ที่คาดหวัง

#ตัวเลขที่ 1:
#ตัวเลขที่ 2:
#เครื่องหมาย (+,-,*,/): /

#ไม่สามารถหารด้วยศูนย์ได้
#จบการทำงาน

""""""

try:
    num1 = float(input("ตัวเลขที่1: "))
    num2 = float(input("ตังเลขที่2: "))
    opertor = input("เครื่องหมาย (+,-,*,/): ")

    if opertor == "+":
        result = num1 + num2
    elif opertor == "-":
        result = num1 - num2
    elif opertor == "*":
        result = num1 * num2
    elif opertor == "/":
        result = num1 / num2
    else:
        raise ValueError("เครื่องหมายไม่ถูกต้อง")

    print("ผลลัพธ์ =", result)

except ValueError as error:
    print("ValueError: ", error)

except ZeroDivisionError:
    print("ZeroDivisionError: ไม่สามารถหารด้วยศูนย์ได้")

finally:
    print("จบการทำงาน")

    