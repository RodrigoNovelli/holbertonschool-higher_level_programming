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
            raise TypeError("{} must be an integer" .format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0" .format(name))
