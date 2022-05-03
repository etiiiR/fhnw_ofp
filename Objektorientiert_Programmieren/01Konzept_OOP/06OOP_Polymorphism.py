# Polymorphismus, die Methode capital wird 2x in der For Schlaufe aufgerufen und
# gibt zwei Werte aus.

class Switzerland():
    def capital(self):
        print("Bern is the capital of Switzerland")


class Germany():
    def capital(self):
        print("Berlin is the capital of Germany")

swiss = Switzerland()
german = Germany()

for x in [swiss, german]:
    x.capital()