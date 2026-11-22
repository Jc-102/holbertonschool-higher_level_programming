#!/usr/bin/python3
"""This module defines CustomObject, which can be saved with pickle."""
import pickle


class CustomObject:
    """A custom object that can be serialized and deserialized."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject.

        Args:
            name (str): The name.
            age (int): The age.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize this object with pickle and save it to filename.

        Args:
            filename (str): The path of the output file.

        Returns:
            None. Also returns None if the file cannot be written.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load a CustomObject from a pickle file.

        Args:
            filename (str): The path of the input file.

        Returns:
            CustomObject: The loaded object, or None if the file is
            missing or malformed.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
        except Exception:
            return None
        if not isinstance(obj, cls):
            return None
        return obj
