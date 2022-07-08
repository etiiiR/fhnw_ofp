class Parent():
    def __init__(self, vorname, nachname):
        self._vorname = vorname
        self.__nachname = nachname

    G_FORCE = 9.81


    def get_nachname(self):
        return self.__nachname

    def methode_hi(self):
        return "Hi " + self._vorname

class Child(Parent):
    def __init__(self,vorname, nachname, age=0):
        Parent.__init__(self, vorname, nachname)
        self.age = age

    def methode_hi(self):
        return "Hiiuuuuuu" + str(self.age)

parent1 = Parent("Cedric", "Kuenz")
parent2 = Parent("Ben", "Tran")
parent2.G_FORCE = 6.1
print(parent1.G_FORCE)
print(parent2.G_FORCE)
print(parent1.get_nachname())

