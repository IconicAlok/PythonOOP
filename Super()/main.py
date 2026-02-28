# super() = Function used in a child class to call methods from a parents class (superclass)
#           Allow you to extend the functionality of the inherited methods


class Shape():
    def __init__(self,color, is_filled):
        self.color = color
        self.is_filled = is_filled

    #method overriding
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()     # calling superclass describe() method : extending describe(self) method functionality
        print(f"It is a circle area of {3.14 * self.radius * self.radius}cm^2")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square area of {self.width * self.width}cm^2")

class Triangle(Shape):
    def __init__(self, color, is_filled, width, heigth):
        super().__init__(color, is_filled)
        self.width = width
        self.height = heigth

    def describe(self):
        super().describe()
        print(f"It is a triangle area of {self.width * self.height / 2}cm^2")

def main():
    circle = Circle(color="red", is_filled=True, radius=5)      #use keyword argument
    square = Square(color="blue",is_filled=False, width=6)
    triangle = Triangle(color="yellow",is_filled=True,width=7,heigth=8)

    triangle.describe()

if __name__=="__main__":
    main()