#!/usr/bin/python3
"""Basic serialization module: save a dictionary to JSON and load it back."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to JSON and save it to a file.

    The file is replaced if it already exists.

    Args:
        data (dict): The data to serialize.
        filename (str): The path of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a JSON file and return its data as a dictionary.

    Args:
        filename (str): The path of the input JSON file.

    Returns:
        dict: The deserialized data.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
