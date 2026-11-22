#!/usr/bin/python3
"""This module defines load_from_json_file, which loads an object from JSON."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): The path of the JSON file.

    Returns:
        The Python object represented in the file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
