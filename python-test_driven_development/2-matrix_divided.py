#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    Args:
        matrix: List of lists of ints/floats.
        div: number to divide by.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_rows = []
    new_matrix = []

    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(msg_type)
        len_rows.append(len(row))
        if len(len_rows) > 1 and len_rows[-1] != len_rows[-2]:
            raise TypeError("Each row of the matrix must have the same size")
        
        new_row = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(msg_type)
            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)

    return new_matrix