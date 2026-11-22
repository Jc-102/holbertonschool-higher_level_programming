#!/usr/bin/python3
"""This module defines text_indentation, which splits text into lines."""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    Spaces at the beginning and at the end of each printed line
    are removed.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    lines = [line.strip(" ") for line in result.split("\n")]
    print("\n".join(lines), end="")
