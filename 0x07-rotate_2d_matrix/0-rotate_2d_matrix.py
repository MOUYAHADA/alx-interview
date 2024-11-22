#!/usr/bin/python3
"""module for rotate_2d_matrix_function"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix"""
    transposed = [
        [matrix[x][i] for x in range(len(matrix))]
        for i in range(len(matrix[0]))
    ]

    matrix.clear()

    for row in transposed:
        matrix.append(row[::-1])
