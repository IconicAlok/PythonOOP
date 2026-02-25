# @Property = decorator used to defied a method as a property (it can be accessed like an attribute)
#             Benefits: Add aditional logic when read, write, delete attributes
#             Gives you getter, setter and deleter method

class Ractangle:
    def __init__(self, width, height):
        self._width = width      # with _width, width has been decleared as a proctated
        self._height = height    # with _ height, height has been decleared as a proctated

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be gratter than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height= new_height
        else:
            print("Height must be gratter than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")



def main():

    ractangle = Ractangle(3, 4)

    ractangle.width = 5
    ractangle.height = 6

    del ractangle.width
    del ractangle.height

    # print(ractangle.width)
    # print(ractangle.height)

if __name__ == "__main__":
    main()