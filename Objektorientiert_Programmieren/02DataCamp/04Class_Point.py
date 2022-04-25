# Write the class Point as outlined in the instructions
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return ((self.x ** 2 + self.y ** 2) ** 0.5)

    def reflect(self, axis):
        if axis == "x":
            self.y = self.y * -1
        elif axis == "y":
            self.x = self.x * -1
        else:
            print("error")


pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())