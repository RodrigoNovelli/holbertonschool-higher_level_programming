#!/usr/bin/python3


"""
This module provides a function for writing a string to a text file.
"""


def write_file(filename="", text=""):

    """
    Writes a string to a text file (UTF-8 encoding) and returns the
    number of characters written.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        char = f.write(text)
    return (char)
