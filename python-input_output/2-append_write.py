#!/usr/bin/python3
'''
This module is used to create a function
athat writes a file adding text
'''


def append_write(filename="", text=""):
    '''
    This function opens a file and adds the
    content
    '''
    with open(filename, 'w', encoding="utf-8") as file:
        char = file.write(text)
        return char
