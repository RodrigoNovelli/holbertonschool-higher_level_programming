#!/usr/bin/python3
"""
This is a module that defines a class
"""


class Rectangle:
    """
    This is a class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.print_symbol = "#"
        self.__width = width
        self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        return ("Rectangle({:d}, {:d})" .format(self.__width, self.__height))

    def __str__(self):
        rec = []
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            for i in range(self.__height):
                rec.append(str(self.print_symbol) * (self.__width))
            return "\n".join(rec)

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))
