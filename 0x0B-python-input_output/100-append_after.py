#!/usr/bin/python3

"""Definition of a function that handle text insertion"""


def append_after(filename="", search_string="", new_string=""):
    """function that is used in insertion of a text after
    each line with specific string.

    Arguements:
        filename: nameof the file
        new_string(str): the string to be inserted
        search_string: the string to be searched for
    """

    txt = ""
    with open(filename) as fh:
        for txt_line in fh:
            txt = txt + txt_line
            if search_string in txt_line:
                txt = txt + new_string

    with open(filename, "w") as fw:
        fw.write(txt)
