class Vector():
    def __init__(self, x, y):
        self.x, self.y = x, y

    def change_x(self, num):
        self.x += num

    def change_y(self, num):
        self.y += num

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

v1 = Vector(10,20)
print(v1.get_length())

v2 = Vector(20,30)
print(v2.get_length())
