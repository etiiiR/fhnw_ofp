class Auto():
    def __init__(self):
        pass

    def distance(self, xdelta, ydelta):
        return xdelta + ydelta

    def distance2(self, xdelta, ydelta):
        return Flugzeug.distance(self, xdelta, ydelta)

class Flugzeug():
    def __init__(self):
        pass

    def distance(self, xdelta, ydelta):
        return (xdelta**2 + ydelta**2) ** 0.5

auto_flieg = Auto()

print(auto_flieg.distance(10,20))

print(auto_flieg.distance2(10,20))


