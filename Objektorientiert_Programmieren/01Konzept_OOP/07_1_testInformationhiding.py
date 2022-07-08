class Parent:
    def __init__(self, a, b, c):
        self.a = a
        self._b = b
        self.__c = c

    def get_c(self):
        return self.__c

class Child(Parent):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.__c = c
        self.__d = d

c1 = Child(1,2,3,4)

print(c1.c)

print(dir(c1))
