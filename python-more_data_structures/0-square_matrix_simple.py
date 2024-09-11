#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(0, len(matrix)):
        new_list = []
        for x in range(len(matrix[i])):
            new_list.append(matrix[i][x] * matrix[i][x])
        new_matrix.append(new_list)
    return (new_matrix)
