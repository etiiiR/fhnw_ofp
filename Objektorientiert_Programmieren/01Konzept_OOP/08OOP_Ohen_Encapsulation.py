# ohne Encapsulation
class Auto():
    def __init__(self, maxspeed, color):
        self.maxspeed = maxspeed
        self.color = color

car1 = Auto(100, "red")
print(car1.maxspeed)
car1.maxspeed = 200
print(car1.maxspeed)

# Mit Encapsulation

class Auto1():
    def __init__(self, maxspeed, color):
        self.__maxspeed = maxspeed
        self.__color = color



