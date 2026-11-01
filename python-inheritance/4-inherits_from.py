#!/usr/bin/python3
"""This module defines a function that checks for subclass instances."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj inherits (directly or indirectly) from a_class,
              but is not exactly an instance of a_class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
