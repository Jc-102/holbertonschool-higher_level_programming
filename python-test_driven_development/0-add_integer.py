#!/usr/bin/python3
"""This module defines add_integer, a function that adds 2 integers."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Floats are cast to integers before the addition.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or a float.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
