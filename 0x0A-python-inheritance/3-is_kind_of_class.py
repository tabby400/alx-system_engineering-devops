#!/usr/bin/python3

"""Explains if an object is an instance of or instance of a class
that inherited from a specific class."""


def is_kind_of_class(obj, a_class):
    """Function used to see if an object is an instance of
    or instance of an object inherited from a specified class.

    Arguement:
        obj: object to be checked
        a_class: class to check with the object
    Returns:
        True if object is instance of or instance of class inherited
        from a specified class otherwise false
    """

    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
