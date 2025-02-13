#!/usr/bin/python3
'''
This module is for making a function
that passes from json to python
'''


import json


def from_json_string(my_str):
    '''
    This function is for pass from json to
    python
    '''
    return (json.loads(my_str))
