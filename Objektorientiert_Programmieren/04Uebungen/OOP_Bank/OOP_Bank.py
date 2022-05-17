class Bank():
    def __init__(self, kunden, konten, kontonr):
        self.kunden = kunden
        self.konten = konten
        self.kontonr = kontonr
        self.saldo = 0

    def kontoeroeffnen(self, vorname, nachname):
        self.kunden = vorname + nachname

    def einzahlen(self, betrag):
        if betrag <= 0:
            print("Einzahlung fehlgeschalgen!")
            return
        self.saldo += betrag

    def auszahlen(self, betrag):
        if betrag <= self.saldo:
            print("Saldo zu klein!")
            return
        self.saldo -= betrag

    def kontostand(self):
        print("Aktuelles Guthaben von", self.kunden, ":", self.saldo)

    def ueberweisen(self, vonkonto, nachkonto, betrag):
        if betrag >= vonkonto.saldo:
            print("Ueberweisung fehlgeschlagen!")
            return
        vonkonto.saldo -= betrag
        vonkonto.kontostand()
        nachkonto.saldo += betrag
        nachkonto.kontostand()

# Objekt erstellen, das ein konto eroeffnet
ben = Bank("1512-1252", 1, "CH1512")
ben.kontoeroeffnen("Ben", "Tran")
print(ben.kunden)
print(ben.saldo)
ben.einzahlen(1000)
print(ben.saldo)


broke = Bank("1512-1553", 1, "CH1590")
broke.kontoeroeffnen("Broken", "Things")
broke.einzahlen(1000)
broke.ueberweisen(broke, ben, 10)