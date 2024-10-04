#!/usr/bin/python3
"""
0x00. Pascal's Triangle
"""


def pascal_triangle(n):
    """A function that returns a list of lists of integers representing the
    Pascal's triangle of n."""
    if n <= 0:
        return []
    triangle = [[1] + [0] * (n - 1) for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]
    triangle = list(map(lambda row: list(filter(lambda x: x != 0, row)),
                    triangle))
    return triangle
