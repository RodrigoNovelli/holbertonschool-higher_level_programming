#!/usr/bin/python3
'''
Defines a fcuntion that prints a square
'''


def print_square(size):
    """

    Prints a square of '#' characters of a given size.


    Parameters:

    size (int): The size of the square to be printed.
    Must be a non-negative integer.


    Raises:

    TypeError: If size is not an integer or if size is negative.


    Example:

    print_square(3) will output:

    ###

    ###

    ###

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
