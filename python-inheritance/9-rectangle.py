#!/usr/bin/python3


"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width=0, height=0):

        """
        Initializes a Rectangle object.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}" .format(self.__width, self.__height))
