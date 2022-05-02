class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


class Manager(Employee):
    # Add a constructor
    def __init__(self, name, salary=50000, project=None):
        # Call the parent's constructor
        Employee.__init__(self, name, salary)
        # Assign project attribute
        self.project = project

    # Add a given_raise method
    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        Employee.give_raise(self, new_amount)

    def display(self):
        print("Manager ", self.name)

# Create Object
mngr = Manager("Ashta Dunbar", 78500)

# Give Raise + 1000
mngr.give_raise(1000)
print(mngr.salary)

mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)