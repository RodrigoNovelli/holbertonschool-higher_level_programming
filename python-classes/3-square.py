#!/usr/bin/python3
"""
This is a mudle that defines a class
"""

class Square:
    '''
    This is a class that defines a square
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            
    def area(self):
        return (self.__size * self.__siz)