import math


class Shape:
    #create

    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def display_info(self):
        print(f"The shape is good: {self.color} shape.")

class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        super().area()
        return math.pi*self.radius**2

    def display_info(self):
        print(f"the circle shape color is:{self.color}\nthe radius is {self.radius}\narea is: {self.area()}. ")

class Ractangle(Shape):

    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        super().area()
        return self.length * self.width

    def display_info(self):
        print(f"color is: {self.color}\nlength is:{self.length}\nwidth is: {self.width}\nArea is: {self.area()}.")


circle1 = Ractangle("blue", 5, 4)
circle1.display_info()


