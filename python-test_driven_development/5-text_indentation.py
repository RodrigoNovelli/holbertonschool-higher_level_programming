#!/usr/bin/python3
'''
This fuction changes the identation to a given char
'''


def text_indentation(text):
    """

    Prints a text with two new lines after each
    of these characters: '.', '?', and ':'.


    Parameters:

    text (str): The text to be processed. Must be a string.


    Raises:

    TypeError: If text is not a string.


    Example:

    text_indentation("Hello. How are you? I am fine: thank you.") will output:

    Hello.


    How are you?


    I am fine: thank you.

    """
    if not isinstance(text, str):
        raise TypeError('Text must be a string')
    counter = 0
    while counter < len(text) and text[counter] == ' ':
        counter += 1

    while counter < len(text):
        print(text[counter], end="")
        if text[counter] == "\n" or text[counter] in ".?:":
            if text[counter] in ".?:":
                print("\n")
            counter += 1
            while counter < len(text) and text[counter] == ' ':
                counter += 1
            continue
        counter += 1
