#!/usr/bin/python3
"""This module defines a Square class with a private size."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the square.
        """
        self.__size = size
