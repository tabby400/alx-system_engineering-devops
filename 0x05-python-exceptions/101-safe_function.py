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
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
