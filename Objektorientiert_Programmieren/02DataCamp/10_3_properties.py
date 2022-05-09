# Control Attribute access

class Employee():
    def __init__(self, name, new_salary):
        self._salary = new_salary

    # Eigenschafts - Decorator
    @property #@property verwenden um Variabel einzuschraenken
    def salary(self):
        # Underline sehr wichtig!
        return self._salary

    @salary.setter #attribute.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Invalid salary")
        # Ganz wichtig ist das underline zeichen! _
        self._salary = new_salary

emp = Employee("Ben Tran", 50000)
# Zugreifen auf Salary Eigenschaft
emp.salary = 60000
print(emp.salary)


