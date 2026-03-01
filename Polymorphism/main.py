# Polymorphism = Greek work that means to "have many form or faces"
#                Poly = many
#                Morphe = form

#                Two ways to achive ploymorphism
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Dock Typeing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
       pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


def main():

    shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni",15)]

    for shape in shapes:
        print(f"{shape.area()}cm²")

if __name__== "__main__":
    main()