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
        super().__init__(size, size)
        self.__size = size

        def __str__(self):
            return ("[Square] {:d}/{:d}" .format(self.__size))
