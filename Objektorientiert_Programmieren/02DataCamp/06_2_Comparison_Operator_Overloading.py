class Customer():
    def __init__(self, id, name):
        self.id = id
        self.name = name


    # Wird aufgerufen, wenn Verlgeichsoperator == verwendet wird
    def __eq__(self, other): # Operator ==
        print("__eq__() wird aufgerufen")
        return (self.id == other.id) and (self.name == other.name)

    def __ne__(self, other): # Operator !=
        pass

    def __ge__(self, other): # Operator >=
        pass

    def __le__(self, other): # Operator <=
        pass

    def __gt__(self, other): # Operator >
        pass

    def __lt__(self, other): # Operator <
        pass


c1 = Customer(1,"Ben")
c2 = Customer(1,"Ben")

print(c1 == c2)



