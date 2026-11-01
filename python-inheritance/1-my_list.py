#!/usr/bin/python3
"""This module defines a MyList class that inherits from list."""


class MyList(list):
    """A list that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
