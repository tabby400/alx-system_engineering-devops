#!/usr/bin/python3


"""Definition of a derived MyInt class from base int
class."""


class MyInt(int):

    """this is an  int class that changes the behaviour of
    operators  == and !=."""

    def __eq__(self, value):
        """changes the == operator with != behavior."""
        return (super().__ne__(value))

    def __ne__(self, value):
        """changes the != operator with == behavior."""
        return (super().__eq__(value))
