#!/usr/bin/python3
""" Module to rotate a matrix """


def rotate_2d_matrix(matrix):
    """ Function that given an n x n 2D matrix,
        rotate it 90 degrees clockwise
    """

    aux = [row[:] for row in matrix]
    aux.reverse()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[j][i] = aux[i][j]
