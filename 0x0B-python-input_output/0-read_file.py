#!/usr/bin/python3


"""Definition of a file that reads a text file"""


def read_file(filename=""):
    """function used to read text file UTF8 and prints
    to stdout"""

    with open(filename, encoding="utf-8") as fh:
        print(fh.read(), end="")  # with closes file automatically
