class BalanceError(Exception):
    pass

class Customer():
    def __init__(self, name, balance):
        if balance < 0:
            raise BalanceError("Balance has to be a positive integer")
        else:
            self.name, self.balance = name, balance

try:
    c1 = Customer("Ben", -10)
except BalanceError:
    c1 = Customer("Ben", 10)

c2 = Customer("ben", -10)