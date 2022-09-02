#!/usr/bin/python3
""" Program that solves the N queens problem """
import sys


def nqueens(n, i, a, b, c, d):
    """ Solution to N queens problem """
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from nqueens(n, i+1, a+[j], b+[i+j], c+[i-j], d+[[i, j]])
    else:
        yield d


if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if num < 4:
        print("N must be at least 4")
        sys.exit(1)

    for solution in nqueens(num, 0, [], [], [], []):
        print(solution)
