class BankAccount:
    # MODIFY to initialize a number attribute
    def __init__(self, balance=0, number=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount

        # Define __eq__ that returns True if the number attributes are equal

    def __eq__(self, other):
        return (self.number == other.number) and (type(self) == type(other))

    # Create accounts and compare them


acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)
