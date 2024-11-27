#!/usr/bin/python3
# Function to count occurrences of a word in a file
def count_word_in_file(filename, word):
    try:
        with open(filename, "r") as file:
            content = file.read()
            # Convert content to lowercase and search for the word
            content_lower = content.lower()
            word_lower = word.lower()
            word_count = content_lower.count(word_lower)
        return word_count
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        return 0

# Main program
filename = input("Enter the filename: ")
word_to_search = input("Enter the word to search for: ")

word_count = count_word_in_file(filename, word_to_search)

if word_count >= 0:
    print(f"The word '{word_to_search}' occurs {word_count} times in the file '{filename}'.")
