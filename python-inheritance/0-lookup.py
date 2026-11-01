#!/usr/bin/python3
"""This module defines a function that lists an object's attributes."""


def lookup(obj):
    """Return the list of available attributes and methods of obj.

    Args:
        obj: The object to inspect.

    Returns:
        list: The names of the attributes and methods of obj.
    """
    return dir(obj)
