#!/usr/bin/python3


"""
This is a module that defines a class
"""


class BaseGeometry:

    """
    This is an empty class
    """
    def area(self):

        """
        Method to calculate area
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        Method to validate if a number is an interger
        """

        if not isinstance(value, int):
            raise TypeError("name must be an integer")
        elif value <= 0:
            raise ValueError("name must be greater than 0")
