#!/usr/bin/python3
"""magicClass defining using bytecode provded"""


import math


class MagicClass:
    """reiterates its a circle."""

    def __init__(self, radius=0):
        """magicclass init

        Arguements:
            radius(int/float):magicClass radius.
        """

        self.__radius = 0

        if type(radius) is not float and type(radius) is not int:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius * self._radius * math.pi)

    def circumference(self):
        """gets circumference of magicClass."""

        return (2 * math.pi * self.__radius)
