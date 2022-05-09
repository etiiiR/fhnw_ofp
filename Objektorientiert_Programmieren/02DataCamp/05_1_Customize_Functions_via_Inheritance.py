class BankAccount():
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

class SavingsAccount(BankAccount):
    # Methode einer "Parent" Klasse modifizieren

    # Hinzufuegen eines Konstruktur speziell fuer SavingsAccount()
    def __init__(self, balance, interest_rate):
        # Zuerst "Parent" Konstruktur verwenden/erstellen
        BankAccount.__init__(self, balance)
        # Funktionalitaet hinzufuegen
        self.interest_rate = interest_rate

    # Eine weitere Methode hinzufuegen
    def compute_interest(self, n_periods = 1):
        return self.balance * ((1 + self.interest_rate) ** n_periods - 1)


# Neues Objekt erstellen
saving_acount1 = SavingsAccount(1000, 0.05)
print(saving_acount1.interest_rate)
print(saving_acount1.compute_interest(10))