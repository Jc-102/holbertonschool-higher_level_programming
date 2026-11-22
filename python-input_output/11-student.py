#!/usr/bin/python3
"""This module defines a Student class that can be saved and reloaded."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student.

        Args:
            attrs (list): If a list of strings, only these attributes
                          are returned. Otherwise, all are returned.
        """
        if isinstance(attrs, list) and \
                all(isinstance(attr, str) for attr in attrs):
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student with those in json.

        Args:
            json (dict): Attribute names and their new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
