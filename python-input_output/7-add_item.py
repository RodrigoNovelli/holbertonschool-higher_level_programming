#!/usr/bin/python3
'''
This module is to make a function that
adds the arguments passed to a list in pyhton
and then making a file to store it as a
json file.
'''


import sys
from 6-load_from_json_file import load_from_json_file
from 5-save_to_json_file import save_to_json_file


filename = "add_item.json"
try:
    content = load_from_json_file(filename)
except:
    content = []
for i in range(1, len(argv)):
    content.append(argv[i])
save_to_json_file(content, filename)
