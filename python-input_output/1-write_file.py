#!/usr/bin/python3
"""This module defines write_file, which writes a string to a file."""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return the number of characters written.

    The file is created if it doesn't exist and overwritten if it does.

    Args:
        filename (str): The path of the file to write.
        text (str): The text to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
