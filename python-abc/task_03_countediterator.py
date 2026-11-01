#!/usr/bin/python3
"""This module defines CountedIterator, an iterator that counts items."""


class CountedIterator:
    """An iterator that keeps track of how many items were fetched."""

    def __init__(self, iterable):
        """Initialize the iterator and set the counter to 0."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items fetched so far."""
        return self.count

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self):
        """Return the next item and increment the counter.

        Raises:
            StopIteration: When there are no more items.
        """
        item = next(self.iterator)
        self.count += 1
        return item
