#!/usr/bin/python3


"""
This module provides a function that converts JSON string
representation into Pyhton object
"""


import json


def from_json_string(my_str):

    """
    Converts a JSON string into a Python object
    """

    return (json.loads(my_str))
