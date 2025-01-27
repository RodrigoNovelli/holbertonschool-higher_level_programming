#!/usr/bin/python3
'''
Dfines a dunction that divides a matrix
'''


def matrix_divided(matrix, div):
    """

    Divides all elements of a matrix by a given divisor and rounds the result to 2 decimal places.


    Parameters:

    matrix (list of list of int/float): A matrix (list of lists) containing integers or floats.

    div (int, float): The divisor by which to divide each element of the matrix.


    Returns:

    list of list of float: A new matrix with each element divided by div and rounded to 2 decimal places.


    Raises:

    TypeError: If matrix is not a list of lists of integers/floats, or if div is not a number.

    ZeroDivisionError: If div is zero.

    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
