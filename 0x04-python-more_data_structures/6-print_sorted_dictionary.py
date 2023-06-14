#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    for p in sorted(a_dictionary.keys()):
        print("{}: {}".format(p, a_dictionary[p]))
