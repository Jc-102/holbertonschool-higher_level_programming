#!/usr/bin/python3
"""This module defines print_square, which prints a square of #."""


def print_square(size):
    """Print a square of size x size with the # character.

    Args:
        size (int): The length of each side of the square.

    Raises:
        TypeError: If size is not an integer (including negative floats).
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
