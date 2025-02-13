#!/usr/bin/python3
'''
This module is used to create a function
that writes a line in a file
'''


def write_file(filename="", text=""):
    '''
    This function creates a file and
    writes it
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        char = file.write(text)
        return char
