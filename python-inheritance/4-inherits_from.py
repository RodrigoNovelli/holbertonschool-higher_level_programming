#!/usr/bin/python3
'''
In this module we are checking if the obj is
directly or indiretly a child form a class
'''


def inherits_from(obj, a_class):
    '''
    This function checks
    '''
    return isinstance(obj, a_class) and type(obj) is not a_class
