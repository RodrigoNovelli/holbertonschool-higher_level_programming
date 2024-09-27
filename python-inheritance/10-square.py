#!/usr/bin/python3


"""
This module defines Square, a class that inherits from Rectangule.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """
    Square class that inherits from BaseGeometry.
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        self.area(self)
