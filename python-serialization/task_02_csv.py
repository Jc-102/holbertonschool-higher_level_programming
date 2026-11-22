#!/usr/bin/python3
"""This module converts a CSV file into a JSON file."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Read a CSV file and write its rows to data.json.

    Args:
        csv_filename (str): The path of the input CSV file.

    Returns:
        bool: True if the conversion worked, False otherwise.
    """
    try:
        with open(csv_filename, newline="", encoding="utf-8") as csv_file:
            data = list(csv.DictReader(csv_file))
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)
        return True
    except Exception:
        return False
