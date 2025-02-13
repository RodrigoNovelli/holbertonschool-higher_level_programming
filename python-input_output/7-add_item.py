#!/usr/bin/python3
'''
This module is to make a function that
adds the arguments passed to a list in pyhton
and then making a file to store it as a
json file.
'''


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
try:
    content = load_from_json_file(filename)
except FileNotFoundError:
    content = []
for i in range(1, len(sys.argv)):
    content.append(sys.argv[i])
save_to_json_file(content, filename)
