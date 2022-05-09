class Employee:
    def __init__(self):
        self.name = None
        self.salary = None

    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary

    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return (self.salary / 12)

emp1 = Employee()
emp1.set_name("Ben")
emp1.set_salary(10000)
print(emp1.name, emp1.salary, emp1.monthly_salary())
emp1.give_raise(2000)
print(emp1.name, emp1.salary, emp1.monthly_salary())
