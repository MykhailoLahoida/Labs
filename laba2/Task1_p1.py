"""
Create a class Rectangle with attributes length and width, each of which defaults to 1. Provide methods that calculate
the perimeter and the area of the rectangle. Also, provide setter and getter for the length and width attributes.
The setter should verify that length and width are each floating-point numbers larger than 0.0 and less than 20.0.
"""
class Rectangle:
    def __init__(self, length=1, width=1):
        if not isinstance(length, float) and not isinstance(width, float):
            raise TypeError("Length and width are floating-point numbers")
        elif not 0.0 < length < 20.0 and 0.0 < width < 20.0:
            raise ValueError("Length and width are floating-point numbers larger than 0.0 and less than 20.0")
        else:
            self.__length = length
            self.__width = width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

    @property
    def area(self):
        return self.length * self.width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, length):
        if not isinstance(length, float):
            raise TypeError("Length and width are floating-point numbers")
        elif not 0.0 < length < 20.0:
            raise ValueError("Length and width are floating-point numbers larger than 0.0 and less than 20.0")
        else:
            self.__length = length

    @width.setter
    def width(self, width):
        if not isinstance(width, float):
            raise TypeError("Length and width are floating-point numbers")
        elif not 0.0 < width < 20.0:
            raise ValueError("Length and width are floating-point numbers larger than 0.0 and less than 20.0")
        else:
            self.__width = width

if __name__ == "__main__":
    rect = Rectangle(5.0, 6.0)
    print('Sizes: ', rect.length, 'x', rect.width)
    print('Perimeter:', rect.perimeter)
    print('Area:', rect.area, '\n')
    rect.length = 5.0
    rect.width = 4.0
    print('Sizes: ', rect.length, 'x', rect.width)
    print('Perimeter:', rect.perimeter)
    print('Area:', rect.area, '\n')