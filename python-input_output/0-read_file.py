#!/usr/bin/python3
'''
In this module we are opening and reading a file
'''
import sys


def read_file(filename=""):
    '''
    This function opens and prints the content
    of a file
    '''
    with open(filename, 'r') as file:
        read = file.read()
        print(read)
