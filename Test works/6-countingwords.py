#!/usr/bin/python3
with open("words.txt", "w") as file:
    file.write("This is a new file and have 9 words")

def count_words(filename):
    with open(filename, "r") as file:
        content = file.read()
        words =  content.split()
        return len(words)
word_count = count_words("words.txt")
print(f"The file 'words.txt' contains {word_count} words.")