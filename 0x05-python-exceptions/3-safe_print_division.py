#!/usr/bin/python3

def safe_print_division(a, b):
    """function divides two ints and gets result.

    Returns:
        result of the division of a by b
    """

    try:
        quotient = a / b
    except (ZeroDivisionError, TypeError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return (quotient)
