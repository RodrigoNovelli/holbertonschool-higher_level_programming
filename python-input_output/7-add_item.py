#!/usr/bin/python3
'''
This module is to make a function that
adds the arguments passed to a list in pyhton
and then making a file to store it as a
json file.
'''


import sys
'''
command line args
'''
from 6-load_from_json_file import load_from_json_file
'''
converts from json
'''
from 5-save_to_json_file import save_to_json_file
'''
converts to json
'''

filename = "add_item.json"
try:
    content = load_from_json_file(filename)
except:
    content = []
for i in range(1, len(argv)):
    content.append(argv[i])
save_to_json_file(content, filename)
