class A():
    def polyfunc(self, num):
        print(num)

class B(A):
    def polyfunc(self, num):
        print(num**2)

objekt_A = A()
objekt_B = B()

objekt_A.polyfunc(10)
objekt_B.polyfunc(10)



class Auto():

    def wheels(self):
        print(4)

    def verwendung(self):
        print("transport")

class Bus():

    def wheels(self):
        print(8)

    def verwendung(self):
        print("Public Transport")

bus = Bus()
auto = Auto()
    
for fahrzeug in (bus, auto):
    fahrzeug.wheels()
    fahrzeug.verwendung()






auto1 = Auto(4, "transport")



