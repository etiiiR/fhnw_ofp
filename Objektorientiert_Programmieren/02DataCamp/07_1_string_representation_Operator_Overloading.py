class Customer():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

c1 = Customer("Ben", -1000)
print(c1)

class Customer2():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # Implentieren von __str__()
    # wird aufgerufen, wenn print(objekt) aufgerufen wird.

    def __str__(self):
        customer_string = """
        Customer: 
        name: {name} 
        balance: {balance}""".format(name = self.name, balance = self.balance)

        return customer_string

c2 = Customer2("Ben", -1000)
print(c2) # ruft __str__() Methode auf

class Customer3():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        # Beachte '...' um {name}
        return "Customer('{name}', '{balance}')".format(name = self.name, balance = self.balance)

c3 = Customer3("Ben", -1000)
print(c3) # Ruft __repr__() Methode auf
