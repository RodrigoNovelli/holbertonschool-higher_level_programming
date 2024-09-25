#!/usr/bin/python3

"""
Module is a_class
"""

def is_same_class(obj, a_class):

    """
    is_same_class
    Check if the object is exactly an instance of the specified class.

    This function returns True if the object is an instance of the specified 
    class and False otherwise. It does not consider inheritance, meaning 
    it will only return True if the object is created from the exact class 
    provided.
    """

    return (type(obj) is a_class)