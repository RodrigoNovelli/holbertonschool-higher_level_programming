#!/usr/bin/python3
'''
This module is used to create a function that
makes a file in json format
'''


import json


def to_json_string(my_obj):
    '''
    This function translate a obj to
    json format
    '''
    return (json.dumps(my_obj))
