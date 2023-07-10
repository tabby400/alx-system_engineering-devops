#!/usr/bin/python3


"""definition of an object being exactly an instance of
a specified class"""


def is_same_class(obj, a_class):
    """function that is used to see if an object is exactly
    an instance of a specified class.

    Arguements:
        obj: object to be looked at
        a_class: class to see if object is an instance of

    Returns:
        True if the object is exactly the instance of the class
        otherwise False
    """

    if type(obj) == a_class:
        return True

    return (False)  # is not an instance of the class
