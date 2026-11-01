#!/usr/bin/python3
"""This module defines VerboseList, a list that prints its changes."""


class VerboseList(list):
    """A list that prints a message when items are added or removed."""

    def append(self, item):
        """Add item to the end of the list and notify."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Add all items from iterable to the list and notify."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Notify, then remove the first occurrence of item."""
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Notify, then remove and return the item at index."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
