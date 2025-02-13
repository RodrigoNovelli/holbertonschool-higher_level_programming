#!/usr/bin/python3
'''
This module is for making a file that
will be written by a translate of an
object from python to json
'''


import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as file:
        data = json.dumps(my_obj)
        file.write(data)
