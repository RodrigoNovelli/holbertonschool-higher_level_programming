#!/usr/bin/python3


"""
Este script carga una lista desde un archivo JSON, agrega nuevos elementos
pasados como argumentos de la línea de comandos y guarda la lista de nuevo
en el archivo JSON.
"""

from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
filename = "add_item.json"
try:
    load_from_json_file(filename)
except ValueError:
    list = []
for i in range(1, len(argv)):
    list.append(argv[i])
save_to_json_file(list, filename)
