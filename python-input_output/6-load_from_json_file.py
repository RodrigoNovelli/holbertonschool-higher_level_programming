#!/usr/bin/python3
'''
This module is for creating an object from
a file that is .json
'''


import json


def load_from_json_file(filename):
    '''
    This function is for oppening a file, read it,
    and then making an object in python
    '''
    with open(filename, 'r') as json_file:
        data = json_file.read()
        return (json.loads(data))
