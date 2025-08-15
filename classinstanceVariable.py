# classinstanceVariable

# Class variable คือ ด้วนมาท่าทางานภายใน class ส่วนอื่นสามารถเข้าถึงฆ์อมูลส่วนนี้ใต้เลย (static attribute)
# ส่วนอื่นสามารถเข้าถึงข้อมูลส่วนนี้ได้เลย (static attribute)
# โดยไม่จำเป็นต้องสร้าง 0bject ขึ้นมา

# instance Variable คือ ตัวแปรที่agภายใน object
# สามารถเข้าถึงข้อมูลส่วนนี้โดยต้องสร้าง Object ขึ้นมา


class Employee:
    #class variable
    _minSaloary = 1200
    _maxSalary = 5000
    _companyName = 'บริษัท XYX จำกัด'
    def __init__(self, name, salary, department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self.__department = department

    def _showData(self):
        print('ชื่อพนักงาน = {}'+self.__name)
        print('เงินเดือน = {}'+self.__salary)
        print('แผนก = {}'+self.__department)


emp1 = Employee('พรอนงค์', 50000, 'วิชาการ')
# print('เงินเดือนขั้นต่ำ = ' +str(Employee._minSalary))
print(Employee._companyName)