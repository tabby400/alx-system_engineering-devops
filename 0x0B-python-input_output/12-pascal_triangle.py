#!/usr/bin/python3

"""Explains more on a pascal triangle function."""


def pascal_triangle(n):
    """is a representation of new trianfle with n size

    Returns:
    a list of lists representing triangle.
    """

    if n <= 0:  # if is empty
        {
            return []
        }

    tri_list = [[1]]

    while len(tri_list) != n:
        cur_row = tri_list[-1]
        new_rw = [1]

        for p in range(len(cur_row) - 1):
            new_rw.append(cur_row[p] + cur_row[p + 1])
        new_rw.append(1)
        tri_list.append(new_rw)

    return (tri_list)
