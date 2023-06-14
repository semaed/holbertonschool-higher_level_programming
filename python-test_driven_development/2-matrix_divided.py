#!/usr/bin/python3
"""Function to divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix: List of lists of integers or floats to divide.
        div: The number to divide each element of the matrix by.
    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal
         places.
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   if each row of the matrix does not have the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
