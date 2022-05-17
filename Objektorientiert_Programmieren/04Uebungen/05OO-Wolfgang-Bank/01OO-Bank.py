class Konto():

    Buchungs_verlauf = []

    def __init__(self, kennung, saldo):
        self.kennung = kennung
        self.saldo = saldo


    def kontostand(self):
        print(self.kennung, "hat ein Guthaben von:", self.saldo, ".-")

    def bareinzahlung(self, betrag):
        if betrag <= 0:
            print("Einzahlung fehlgeschalgen!")
            return
        self.betrag = betrag
        self.saldo += betrag

        print(self.kennung, "hat folgenden betrag eingezahlt:", self.betrag, ".-")
        print(self.kennung, "hat ein Guthaben von:", self.saldo, ".-")

        Konto.Buchungs_verlauf.append([self.kennung, "hat", self.betrag, "eingezahlt"])

    def kontouebertrag(self, kennung, betrag):
        if betrag > self.saldo:
            print("Saldo zu klein")
        elif betrag <= 0:
            print("Kontouebertrag nicht moeglich!")
            return

        self.betrag = betrag

        kennung.saldo += self.betrag
        self.saldo -= self.betrag

        print(self.kennung, "hat", self.betrag, ".- auf das Konto von", kennung.kennung, "uebertragen.")

        self.kontostand()
        kennung.kontostand()

class Jugendkonto(Konto):
    def __init__(self, kennung, saldo):
        Konto.__init__(self, kennung, saldo)


class Privatkonto(Konto):
    def __init__(self, kennung, saldo):
        Konto.__init__(self, kennung, saldo)

    def kontouebertrag(self, kennung, betrag, gebuehr=0.05):
        geld_betrag = betrag + betrag * gebuehr
        if geld_betrag > self.saldo:
            print("Saldo zu klein")
        elif geld_betrag <= 0:
            print("Kontouebertrag nicht moeglich!")
            return

        self.geld_betrag = geld_betrag
        self.betrag = betrag

        kennung.saldo += self.betrag
        self.saldo -= self.geld_betrag

        print(self.kennung, "hat", self.betrag, ".- auf das Konto von", kennung.kennung, "uebertragen.")

        self.kontostand()
        kennung.kontostand()

class Sparkonto(Konto):
    def __init__(self, kennung, saldo):
        Konto.__init__(self, kennung, saldo)

ben = Privatkonto("Ben", 200)
ben.kontostand()
ben.bareinzahlung(100)
print(ben.Buchungs_verlauf)

gabu = Privatkonto("Gabu", 100)
gabu.kontostand()
gabu.kontouebertrag(ben, 10)
