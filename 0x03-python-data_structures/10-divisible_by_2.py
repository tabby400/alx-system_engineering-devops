#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divisible_by_two = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:  # divisible by 2
            divisible_by_two.append(True)
        else:
            divisible_by_two.append(False)

    return (divisible_by_two)
