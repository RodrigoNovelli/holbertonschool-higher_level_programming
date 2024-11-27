#!/usr/bin/python3
with open("example.txt", "w") as file:
        file.write("Hello, world!\n")
        file.write("Welcome to file I/O in Python.\n")

# Reading from the file
with open("example.txt", "r") as file:
    print("Contents of 'example.txt':")
    for line in file:
        print(line, end="")