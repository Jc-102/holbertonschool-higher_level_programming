#!/usr/bin/python3
"""This module defines matrix_divided, which divides a matrix by a number."""


def matrix_divided(matrix, div):
    """Return a new matrix with every element divided by div.

    Each result is rounded to 2 decimal places.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int or float): The number to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if the rows are not all the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        list of lists: The new matrix.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(msg)
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
