#!/usr/bin/python3
""" Pascal's triangle """


def pascal_triangle(n):
    """
        Function that returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    pas_trngl = []
    if n <= 0:
        return pas_trngl

    pas_trngl.append([1])
    for i in range(1, n):
        row_trngl = [1]
        for j in range(1, i):
            row_trngl.append(pas_trngl[i - 1][j - 1] + pas_trngl[i - 1][j])
        row_trngl.append(1)
        pas_trngl.append(row_trngl)

    return pas_trngl
