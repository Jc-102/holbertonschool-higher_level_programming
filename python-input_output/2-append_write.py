#!/usr/bin/python3
"""This module defines append_write, which appends a string to a file."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return the number of characters added.

    The file is created if it doesn't exist.

    Args:
        filename (str): The path of the file to append to.
        text (str): The text to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
