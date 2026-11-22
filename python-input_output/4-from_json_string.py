#!/usr/bin/python3
"""This module defines from_json_string, which converts JSON to an object."""
import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string.

    Returns:
        The Python data structure.
    """
    return json.loads(my_str)
