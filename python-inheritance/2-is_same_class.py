#!/usr/bin/python3
'''
This module has a function that checks if
the object is an instance of a class
'''


def is_same_class(obj, a_class):
    '''
    Function that checks if obj is a sub class of a_class
    '''
    return type(obj) is a_class
