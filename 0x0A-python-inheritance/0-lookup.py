#!/usr/bin/python3


"""Explains more on a function that lists all the
available attributes and methods of an object."""


def lookup(obj):
    """function which is able to return a list of an
    objects attributes and methods"""

    return (dir(obj))  # dir function returns a sorted list
