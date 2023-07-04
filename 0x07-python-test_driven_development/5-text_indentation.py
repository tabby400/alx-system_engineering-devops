#!/usr/bin/python3

# 5-text_indentation.py
"""explains on a function that is on text indentation."""


def text_indentation(text):
    """function that peints 2 lines after '.', '?', and ':'.

    Arguements:
        text(string): what text to be printed
    Raises:
        TypeError: when the text isnt a str
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    h = 0
    while h < len(text) and text[h] == ' ':
        h = h + 1

    while h < len(text):
        print(text[h], end="")

        if text[h] == "\n" or text[h] in ".?:":
            if text[h] in ".?:":
                print("\n")
            h = h + 1
            while h < len(text) and text[h] == ' ':
                h = h + 1
            continue
        h = h + 1
