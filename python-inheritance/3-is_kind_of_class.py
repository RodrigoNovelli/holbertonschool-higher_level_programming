#!/usr/bin/python3


"""
Function that checks if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):

    """
    Check if the object is an instance of the specified class
    or an instance of a class that inherited from it.
    """

    return (isinstance(obj, a_class))
