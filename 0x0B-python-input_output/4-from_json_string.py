#!/usr/bin/python3

"""Deinition of decoding from JSON to python
object."""

import json


def from_json_string(my_str):
    """function that is used to decode the JSON string to python
    object."""
    return json.loads(my_str)  # from JSON to python object
