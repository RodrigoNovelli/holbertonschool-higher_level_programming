#!/usr/bin/python3
'''
In this module we create a subclass that is
based on rectangle
'''


Rectangle = __import__('9-rectangle').rectangle


class Square(Rectangle):
    '''
    Square is a class that inherits all theattributes
    from rectangle
    '''
    def __init__(self, size):
        super().__init__(size, size)
        slef.integer_validator('size', size)
        self.__size = size

    def area(slef):
        slelf.__size ** 2

    return area(self)
