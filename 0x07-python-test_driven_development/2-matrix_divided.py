#!/usr/bin/python3

# 2-matrix_divided.py
"""explains on a function that involves matrix division."""


def matrix_divided(matrix, div):
    """function that is used to divide all the elements in a matrix.

    Arguements:
        matrix(list): list of lists of floats and integers
        div(float/int): what is called the divisor
    Raises:
        TypeError: when the div is not a float or integer
        TypeError: when the rows are not of the same size
        TypeError: when the matrix contains non numbers
        ZeroDivisionError: when the div is 0.
    Return:
        Matrix with the division result
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(item, int) or isinstance(item, float))
                    for item in [value for row in matrix for value in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda p: round(p / div, 2), row)) for row in matrix])
    # round to two dp
