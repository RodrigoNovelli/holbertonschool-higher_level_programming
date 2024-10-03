#!/usr/bin/python3


"""
This module provides a function for appending a string to a text file.
"""


def append_write(filename="", text=""):

    """
    Writes a string to a text file (UTF-8 encoding) and returns the
    number of characters written.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        char = f.write(text)
    return (char)
