#!/usr/bin/python3


"""
This module provides a function that converts a Python object
into its JSON string representation.
"""


import json


def to_json_string(my_obj):

    """
    Converts a Python object to a JSON string.
    """

    return (json.dumps(my_obj))
