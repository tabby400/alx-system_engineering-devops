#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    a_dictionary.pop(key, None)  # none is default if key isnt
    return (a_dictionary)
