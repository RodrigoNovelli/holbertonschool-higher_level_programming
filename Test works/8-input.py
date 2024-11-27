#!/usr/bin/python3
# Function to count occurrences of a word in a file
def count_word_in_file(filename, word):
    try:
        # Open the file in read mode
        with open(filename, 'r', encoding='utf-8') as file:
            # Read the content of the file
            content = file.read()
        
        # Convert content to lowercase for case-insensitive comparison
        content_lower = content.lower()
        word_lower = word.lower()
        
        # Count occurrences of the word
        word_count = content_lower.count(word_lower)
        
        return word_count

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Step 1: Prompt the user for a filename and a word to search for
filename = input("Enter the filename: ")
word_to_search = input("Enter the word to search for: ")

# Step 2: Count occurrences of the word in the file
count = count_word_in_file(filename, word_to_search)

# Step 3: Display the result
if count >= 0:
    print(f"The word '{word_to_search}' occurs {count} times in the file '{filename}'.")
