#!/usr/bin/python3

"""Definition of aobject string to JSON rep"""

import json


def to_json_string(my_obj):
    """function is used to return the JSON representation of
    an object (string)."""
    return (json.dumps(my_obj))  # encoding python object to JSON str
