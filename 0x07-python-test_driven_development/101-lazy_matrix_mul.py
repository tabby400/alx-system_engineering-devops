#!/usr/bin/python3
"""explains a matrix multiplication using module NumPy."""

import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    """'the multiplication of two matrices is returned.

    Arguements:
        m_a(list of lists with floats/ints): first matrix.
        m_b(list of lists with floats/ints): second matrix.
    """

    return npy.matmul(m_a, m_b)
