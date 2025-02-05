#!/usr/bin/pyhton3
'''
Making a function thar returns a list of attributes
'''


def lookup(obj):
    list_att = []
    list_att = dir(obj)
    return list_att