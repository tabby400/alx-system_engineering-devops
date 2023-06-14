#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squarevalue = []
    for row in matrix:
        squarevalue.append([p**2 for p in row])
    return (squarevalue)
