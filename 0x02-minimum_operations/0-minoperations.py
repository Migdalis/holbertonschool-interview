#!/usr/bin/python3
""" Module to calculate the minimum operations """


def minOperations(n):
    """
        Method that calculates the fewest number of operations needed
        to result in exactly n H characters in the file.
        Returns an integer
        If n is impossible to achieve, return 0
    """
    min = 0
    div = 2
    while n > 1:
        if not (n % div):
            min += div
            n = n / div
            div = 2
        else:
            div += 1
    return min
