#!/usr/bin/python3

"""this defines a lockedclass with no object or class attribute"""


class LockedClass:

    """
    lockedclass is uesd to prevent the user from creating new instance of
    attributes except for the attributr first name
    """

    __slots__ = ["first_name"]
