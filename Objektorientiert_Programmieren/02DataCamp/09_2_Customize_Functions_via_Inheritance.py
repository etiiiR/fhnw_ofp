class BankAccount():
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

class CheckingAccount(BankAccount):
    # Zur vorhandenem Balance von "Parent" Klasse BankAccount() fuegen wir "limit" hinzu
    def __init__(self, balance, limit):
        BankAccount.__init__(self, balance)
        self.limit = limit

    # Zur Klasse fuegen wir noch deposit() Methode hinzu.
    def deposit(self, amount):
        self.balance += amount

    # Hier bearbeiten wir die withdraw() Methode von BankAccount() und ergaenzen diese
    # mit einer gebuehr.
    def withdraw(self, amount, fee=0):
        # Wenn Gebuehr kleinr gleich limit ist
        if fee <= self.limit:
            # dann wir das Geld mit gebuehr abgezogen
            BankAccount.withdraw(self, amount - fee)
            # Wenn ueber der limit geld entnommen wird,
        else:
            # Dann wird das Geld mit limit abgezogen
            BankAccount.withdraw(self, amount + self.limit)

check_account1 = CheckingAccount(1000, 25)

check_account1.withdraw(25, 100)
print(check_account1.balance)


# Polymorphismus
# Objekt wird durch CheckingAccount() erstellt
check_account2 = CheckingAccount(1000, 25)
check_account2.withdraw(200)

# Objekt wird durch BankAccount() erstellt
bank_account1 = BankAccount(1000)
bank_account1.withdraw(200)