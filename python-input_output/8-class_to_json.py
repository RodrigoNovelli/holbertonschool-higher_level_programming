#!/usr/bin/python3
'''
A function that passes a class to json
'''


def class_to_json(obj):
    '''
    this function will return a class
    in json format
    '''
    return __dict__(obj)
