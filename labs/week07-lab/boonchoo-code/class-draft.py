class ClassName: # แนวทางการแก้ปัญหาหนึ่งเรื่อง

    # constructor method
    # การกำหนดข้อมูลที่จำเป็นต้องใช้ในการแก้ปัญหานั้นๆ
    def __init__(self, parameters):
        # Constructor method
        self.attribute = value

    # method การกระทำ วิธีการในการแก้ปัญหา
    def method_name1(self):
        # Instance method
        return something

    def method_name2(self):
        # statement ของการกระทำ

myObj = ClassName(parameters)
print(myObj.attribute)
resultFromMethod = myObj.method_name()

# เราออกแบบโปรแกรม ของเราใน class
# เขียนโปรแกรมเพื่อแก้ปัญหา ต้องมีข้อมูล (data), การกระทำ (method)
 
class ClassName: # แนวทางการแก้ปัญหาหนึ่งเรื่อง/ตรายาง/template/แม่พิมพ์
    # constructor method
    # การกำหนดข้อที่จำเป็นต้องใช้ในการแก้ไขปัญหานั้นๆ
    def __init__(self, parameters):
        self.attridute = parameters

    # method การกระทำ วิธีในการแก้ปัญหา
    def method_name1(self):
        # Instance method
        return something

    def method_name2(self):
        # statement ของการกระทำ

# การสร้างวัตถุจาก class ==> การนำแนวทางในการแก้ปัญหาที่ออกแบบไว้มาใช้ การปั้มภาพจากแม่แบบหรือจากตรายาง
myObj = ClassName(parameters)

# การ print ข้อมูลที่ใช้ของวัตถุจาก class
print(myObj.attribute)

# การใช้งาน method ในวัตถุของคลาส
resultFromMethod = myObj.method_name1()
myObj.method_name2()
