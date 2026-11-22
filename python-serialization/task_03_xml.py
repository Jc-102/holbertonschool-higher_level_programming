#!/usr/bin/python3
"""This module serializes a dictionary to XML and deserializes it back."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML and save it to filename.

    Each key becomes a child element of <data>, and each value
    is stored as that element's text.

    Args:
        dictionary (dict): The data to serialize.
        filename (str): The path of the output XML file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    if hasattr(ET, "indent"):
        ET.indent(tree, space="    ")
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """Read an XML file and return its data as a dictionary.

    Values are returned as strings, because XML stores everything
    as text.

    Args:
        filename (str): The path of the input XML file.

    Returns:
        dict: The deserialized data, or None if the file can't be read.
    """
    try:
        root = ET.parse(filename).getroot()
    except (FileNotFoundError, ET.ParseError):
        return None
    return {child.tag: child.text or "" for child in root}
