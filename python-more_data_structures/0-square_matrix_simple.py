#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        new_matrix = [row.copy() for row in matrix]
    for row in range(len(matrix)):
        for i in range(len(matrix[row])):
            new_matrix[row][i] = matrix[row][i] * matrix[row][i]
    return new_matrix
