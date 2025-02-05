#!/usr/bin/python3
'''
In this module we create a class  with two
methods
'''


class BaseGeometry:
    '''
    A method area that raise an exception
    and another that validates
    '''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{name} must be an integer")
        if value <= 0:
            raise ValueError("{name} must be greater than 0")
