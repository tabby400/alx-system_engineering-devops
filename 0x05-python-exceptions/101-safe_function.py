#!/usr/bin/python3

import sys  # prints in stderr


def safe_function(fct, *args):
    """function executes a function safely.

    Arguements:
    fct: the func to be executed
    args: the arguments

    Return:
    the result of func otherwise if there is
    an error None.
    """
    try:
        outcome = fct(*args)
        return outcome
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
