#!/usr/bin/python3
'''
Making a class with a public method
'''


class BaseGeometry:
    '''
    Class with an only method that raises a error
    '''
    def area(self):
        raise Exception("area() is not implemented")
