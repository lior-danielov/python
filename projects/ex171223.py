import math
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

radius = float(input("please enter radius: "))
area2 = Circle(radius)
print(area2.area())
