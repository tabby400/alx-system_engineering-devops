#!/usr/bin/python3


"""Definition of a file that handles appending in a
text file"""


def append_write(filename="", text=""):

    """Function used in appending a string at the end
        of a UTF -8 file.
    Arguements:
        filename : file in which we are appending to
        text: string to append to the file
    Returns:
        the characters appended to the file
    """

    with open(filename, "a", encoding="utf-8") as fh:
        return (fh.write(text))  # a to append
