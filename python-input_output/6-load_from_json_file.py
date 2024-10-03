#!/usr/bin/python3


"""
This module provides a function to save a Python
object to a file in JSON format.
"""


import json


def load_from_json_file(filename):

    """
    Writes a Python object to a text file, using a JSON representation.
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return (json.load(f))
