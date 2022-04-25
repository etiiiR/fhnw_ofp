from datetime import datetime

class Employee:
    def __init__(self, name, salary = 0):
        self.name = name
        if salary > 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid Salary")
        self.hire_date = datetime.today()

emp1 = Employee("Ben", -10)
print(emp1.name, emp1.salary, emp1.hire_date)