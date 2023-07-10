#!/usr/bin/python3

"""Definition on a function that checks if an object is an instance
of a class inherited directly or indirectly."""


def inherits_from(obj, a_class):
    """function that looks to see if an object is an inherited
    instance of a class.

    Arguemets:
        obj: object to be checked
        a_class: class to check object with
    Returns:
        True if object is instance of a class inherited otherwise
        False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    else:
        return (False)
