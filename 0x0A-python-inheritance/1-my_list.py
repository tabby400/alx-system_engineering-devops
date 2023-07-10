#!/usr/bin/python3


"""Explains more on creating a class through inheritance
of a base class list"""


class MyList(list):  # the mylist is inherirting from list

    """MyList class is the derived one and list is base class"""

    def print_sorted(self):
        """The list is printed sorted in ascending order"""

        newone = self[:]
        newone.sort()

        print("{}".format(newone))
