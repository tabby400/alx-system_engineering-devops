#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """function div element by ek=lement in two lists.

    Arguements:
    my_list_1: one of the lists
    my_list_2: the other list
    list_length: the elemnts to divide

    Returns:
    list_length which is new list with divs
    """

    div_new = []
    for p in range(0, list_length):
        # no of elements
        try:
            quotient = my_list_1[p] / my_list_2[p]
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            div_new.append(quotient)
    return (div_new)
