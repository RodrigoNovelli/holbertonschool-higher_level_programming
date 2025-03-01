#!/usr/bin/python3
"""
This is a mudle that defines a class
"""


class Square:
    """
    This is a class that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        a = position[0]
        b = position[1]
        if not isinstance(size, int):
            raise TypeError("")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif a < 0 or b < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        message = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple):
            raise TypeError(message)
        for i in value:
            if i is not isinstance(i, int) or i < 0:
                raise ValueError(message)
        else:
            self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
