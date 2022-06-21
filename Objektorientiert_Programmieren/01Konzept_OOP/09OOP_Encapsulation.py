class Zahlung():
	def __init__(self, betrag):
		self.endbetrag = betrag + betrag * 0.05

buch1 = Zahlung(10)
print(buch1.endbetrag)


buch1.endbetrag = 0
print(buch1.endbetrag)

class Zahlung():
	def __init__(self, betrag):
		self._endbetrag = betrag + betrag * 0.05
# Durch _ vor der Variabel, koennen wir nun diese als nicht-oeffentlich markieren

buch2 = Zahlung(10)
print(buch2._endbetrag)


buch2._endbetrag = 0
print(buch2._endbetrag)

class Zahlung():
	def __init__(self, betrag):
		self.__endbetrag = betrag + betrag * 0.05
# Durch __ vor der Variabel, koennen wir nun diese als Privat deklarieren

buch3 = Zahlung(10)
#print(buch3.__endbetrag)


class Zahlung():
	def __init__(self, betrag):
		self.__endbetrag = betrag + betrag * 0.05

	# Definieren eine Methode, die uns erlaubt, den endbetrag zu sehen.

	def get_endbetrag(self):
		return self.__endbetrag

buch4 = Zahlung(10)
print(buch4.get_endbetrag())

class Zahlung():
	def __init__(self, betrag):
		self.__endbetrag = betrag + betrag * 0.05

	def get_endbetrag(self):
		return self.__endbetrag

# Hier erstellen wir eine Methode, die die Variabel veraendern kann.
	def set_endbetrag(self, rabatt):
		self.__endbetrag = self.__endbetrag - (self.__endbetrag * (rabatt/100))

buch5 = Zahlung(10)
buch5.set_endbetrag(10)
print(buch5.get_endbetrag())

class Zahlung():
	def __init__(self, betrag):
		self.__endbetrag = betrag + betrag * 0.05

	def get_endbetrag(self):
		return self.__endbetrag

	def set_endbetrag(self, rabatt):
		self.__endbetrag = self.__endbetrag - self.__rabatt_rechner(rabatt)

# Hier erstellen wir eine entkapselte Methode um den Rabatt Betrag zu berechnen
	def __rabatt_rechner(self, rabatt):
		return self.__endbetrag * (rabatt/100)

buch6 = Zahlung(10)
buch6.set_endbetrag(10)
print(buch6.get_endbetrag())