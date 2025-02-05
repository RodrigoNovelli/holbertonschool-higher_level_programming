#!/usr/bin/python3
'''
In this module we create a subclass and a fucntion
that prints the objects sorted
'''

class MyList(list):
    '''
    A function that prints the list in ascending order
    '''
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
