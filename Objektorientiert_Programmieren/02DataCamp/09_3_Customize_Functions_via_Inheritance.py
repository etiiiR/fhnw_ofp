class Employee():
    def __init__(self, name, salary = 30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

class Manager():
    def display(self):
        print("Manager", self.name)

    def __init__(self, name, salary = 50000, project = None):
        Employee.__init__(self, name, salary)
        self.project = project

    def give_raise(self, amount, bonus = 1.05):
        Employee.give_raise(self, amount * bonus)

mngr1 = Manager("Ben", 60000)
mngr1.give_raise(1000)
print(mngr1.salary)

mngr2 = Manager("Tran", 60000)
mngr2.give_raise(1000, 1.03)
print(mngr2.salary)
