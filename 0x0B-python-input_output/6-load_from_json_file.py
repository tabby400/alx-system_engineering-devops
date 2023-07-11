#!/usr/bin/python3

"""Definition of creating object from JSON file."""

import json


def load_from_json_file(filename):
    """function used in creating an object from
    a JSON file"""

    with open(filename) as fh:
        return (json.load(fh))
