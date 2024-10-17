#!/usr/bin/python3


"""
add_item.py

Este módulo permite añadir elementos a una lista
almacenada en un archivo JSON.

Uso:
    ./add_item.py elemento1 elemento2 ...
"""

from sys import argv
"""
Permitte utilizar argvs
"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
Carga un objeto de Python desde un archivo JSON.
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""
    Guarda un objeto de Python en un archivo JSON.
"""
filename = "add_item.json"
try:
    load_from_json_file(filename)
except ValueError:
    list = []
for i in range(1, len(argv)):
    list.append(argv[i])
save_to_json_file(list, filename)
