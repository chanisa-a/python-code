def deposit(money):
    balance = 1000  # ยอดเงินเริ่มต้น
    print(f"ยอดเงินเริ่มต้น: {balance} บาท")

    try:
        amount = float(money)
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    except ValueError as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    else:
        balance += amount
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")


print("กรณีปกติ")
deposit(500)

print("\nกรณีจำนวนเงินติดลบ")
deposit(-200)

print("\nกรณีกรอกข้อมูลที่แปลงเป็นตัวเลขไม่ได้")
deposit("abc")