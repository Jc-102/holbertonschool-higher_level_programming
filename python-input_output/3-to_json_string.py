#!/usr/bin/python3
"""This module defines to_json_string, which converts an object to JSON."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string.

    Args:
        my_obj: The object to convert.

    Returns:
        str: The JSON string.
    """
    return json.dumps(my_obj)
