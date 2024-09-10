#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix) -1):
        for x in range (0, len(matrix[i] -1)):
            if x == len(matrix[i] -1):
                print("{:d}" .format(matrix[i][x]))
            else:
                print("{:d}" .format(matrix[i][x]), end=" ")

            