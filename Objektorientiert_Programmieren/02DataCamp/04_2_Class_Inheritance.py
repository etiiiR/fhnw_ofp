class BankAccount():
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

class SavingsAccount(BankAccount):
    pass

saving_account1 = SavingsAccount(1000)
print(saving_account1.balance)

saving_account1.withdraw(200)
print(saving_account1.balance)

print(isinstance(saving_account1, SavingsAccount))
print(isinstance(saving_account1, BankAccount))

# Unterschied bei:
bank_account1 = BankAccount(200)

print(isinstance(bank_account1, SavingsAccount))
# Warum False?: False weil das Objekt bank_account1 durch die Klasse BankAccount() erstellt wurde

print(isinstance(bank_account1, BankAccount))
