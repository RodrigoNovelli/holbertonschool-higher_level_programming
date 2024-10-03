#!/usr/bin/python3


"""
This module provides a function to save a Python
object to a file in JSON format.
"""


import json


def save_to_json_file(my_obj, filename):

    """
    Writes a Python object to a text file, using a JSON representation.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
