#!/usr/bin/python3
'''
Defines a function htat adds two numbers
'''


def add_integer(a, b=98):
    """

    Adds two integers or floats and returns the result as an integer.


    Parameters:

    a (int, float): The first number to add. Must be an integer or float.

    b (int, float, optional): The second number to add. Defaults to 98.
    Must be an integer or float.


    Returns:

    int: The sum of a and b, both cast to integers.


    Raises:

    TypeError: If a or b is not an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
