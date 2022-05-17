class Math():

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def pr():
        return "run!"

print(Math.add5(5))
print(Math.pr())

# Static => Methode aendert sich nicht! (Sie tun was aber aendern nichts)
# Bsp: Den Wert x um 5 erhoehen.
