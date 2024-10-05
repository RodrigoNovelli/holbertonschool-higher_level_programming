#!/usr/bin/python3
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
filename = "add_item.json"
try:
    load_from_json_file(filename)
except:
    list = []
for i in range(1, len(argv)):
    list.append(argv[i])
save_to_json_file(list, filename)
