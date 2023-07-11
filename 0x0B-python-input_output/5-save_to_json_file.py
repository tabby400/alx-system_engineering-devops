#!/usr/bin/python3

"""Definition of writing object to txt file using
JSON."""

import json


def save_to_json_file(my_obj, filename):
    """A function that is used to write an object in a
    text file by use of JSON."""

    with open(filename, "w") as fh:
        json.dump(my_obj, fh)
