class Parent:
    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c

    def get_c(self):
        return self.__c

    def _f(self):
        print("Parent f")

    def callfunktion(self):
        return self._f()

class Child(Parent):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.__c = c
        self.__d = d

    def _f(self):
        print("Child f")




#
c1 = Child(1,2,3,4)
p1 = Parent(1,2,3)

p1.callfunktion()
c1.callfunktion()