class Konto():
    def __init__(self, nummer, kontostand):
        if kontostand < 0:
            self.kontostand = 0
        self.kontostand = kontostand
        self.nummer = nummer

    def einzahlen(self, einzahlung):
        self.kontostand += einzahlung

    def auszahlen(self, auszahlung):
        self.kontostand -= auszahlung

k1 = Konto(10420941, 40000)

print(k1.kontostand)
k1.einzahlen(10000)
print(k1.kontostand)
k1.auszahlen(20000)
print(k1.kontostand)