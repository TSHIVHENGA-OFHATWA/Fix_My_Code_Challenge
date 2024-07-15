#!/usr/bin/python3

class Square:
    """Class representing a square"""

    def __init__(self, *args, **kwargs):
        """Initialize the square with given attributes"""
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)

    def area_of_my_square(self):
        """Calculate the area of the square"""
        return self.width * self.width

    def perimeter_of_my_square(self):
        """Calculate the perimeter of the square"""
        return self.width * 4

    def __str__(self):
        """String representation of the square"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
