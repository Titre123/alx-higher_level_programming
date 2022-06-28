#!/usr/bin/python3
"""
Module matrix_divided
Divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    '''
    This function divide element of a matrix
    '''
    length = []
    len_row = []
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for i in matrix:
        for j in i:
            if isinstance(i, list) is False or type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")
        len_row.append(len(i))
        for k in len_row:
            length.append(k == len_row[0])
            if not all(length):
                raise TypeError("Each row of the matrix must \
                    have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]

    return new_matrix
