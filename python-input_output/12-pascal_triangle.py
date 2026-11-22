#!/usr/bin/python3
"""This module defines pascal_triangle, which builds Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): The number of rows.

    Returns:
        list: The triangle, or an empty list if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(n - 1):
        prev = triangle[-1]
        row = [1]
        for i in range(len(prev) - 1):
            row.append(prev[i] + prev[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
