#!/usr/bin/python3
with open("source.txt", "w") as file:
    file.write("Hola mi nombre\n")
    file.write("y esta linea tambien\n")

with open("source.txt", "r") as file:
    content = file.read()

with open("destination.txt", "w") as file:
    file.write(content)
