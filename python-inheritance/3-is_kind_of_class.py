#!/usr/bin/python3
"""This module defines a function that checks class or inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or inherits from it.
    """
    return isinstance(obj, a_class)
