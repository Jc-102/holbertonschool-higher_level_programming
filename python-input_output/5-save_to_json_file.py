#!/usr/bin/python3
"""This module defines save_to_json_file, which saves an object as JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation.

    Args:
        my_obj: The object to save.
        filename (str): The path of the file to write.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
