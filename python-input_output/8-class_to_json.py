#!/usr/bin/python3
"""This module defines class_to_json, which describes an object as a dict."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: The object's attributes.
    """
    return obj.__dict__
