#!/usr/bin/python3
'''
Making a function thar returns a list of attributes
'''


def lookup(obj):
    '''
    This function creates a list, and then uses dir method to
    put the attributes in it
    '''
    return dir(obj)
