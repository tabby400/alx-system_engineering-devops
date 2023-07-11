#!/usr/bin/python3

"""Definition of a function that writes a string
to a text file"""


def write_file(filename="", text=""):
    """function that is used to write a string to a
    UTF8 file
    Arguements:
        filename(str): name of file to write to
        text: text to be written in the file
    Returns:
    the no of chatacters written in the file
    """

    with open(filename, "w", encoding="utf-8") as fh:
        return fh.write(text)  # with closes file automatically
