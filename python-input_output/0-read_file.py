#!/usr/bin/python3


"""
This module provides a function for reading and printing
the contents of a text file.
"""


def read_file(filename=""):

    """
    Reads a text file (UTF-8 encoding) and prints its contents to stdout.
    """

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
