#!/usr/bin/python3

"""adding all of the args to a python list and saving them
to a file."""

import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        elements = load_from_json_file("add_item.json")
    except FileNotFoundError:  # if file exists
        elements = []
    elememts.extend(sys.argv[1:])  # cmd args got except script name
    save_to_json_file(elements, "add_item.json")
