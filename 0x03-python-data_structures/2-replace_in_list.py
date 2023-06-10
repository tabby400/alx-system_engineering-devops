#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element  # to be replaced
    return (my_list)
