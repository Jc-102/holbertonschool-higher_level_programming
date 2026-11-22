#!/usr/bin/python3
"""This module defines read_file, which prints a text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print it to stdout.

    Args:
        filename (str): The path of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
