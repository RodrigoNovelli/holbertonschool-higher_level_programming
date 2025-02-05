#!/usr/bin/python3
'''
In this module we create a subclass that is
based on rectangle
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Square is a class that inherits all theattributes
    from rectangle
    '''
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
