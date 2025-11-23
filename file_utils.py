from datetime import datetime
import json
import os


# JSON string handling
def convert_json(json_string):
    """
    Parses a JSON formatted string and converts it into a Python dictionary.

    This function acts as a wrapper around json.loads().

    Args:
        json_string (str): A string containing valid JSON data.

    Returns:
        dict: The Python dictionary equivalent of the input JSON string.
    """
    data_dict = json.loads(json_string)
    return data_dict


def convert_dictionary(data_dict):
    """
    Serializes a Python dictionary into a formatted JSON string.

    This function acts as a wrapper around json.dumps() and uses an indent of 4.

    Args:
        data_dict (dict): The Python dictionary to be converted.

    Returns:
        str: A JSON formatted string representation of the dictionary.
    """
    data_json = json.dumps(data_dict, indent=4)
    return data_json


# JSON File handling
def load_json(json_file):
    """Loads JSON data from a file and returns a dictionary or an empty dictionary"""
    if not os.path.exists(json_file):
        # create file if it doesn't exist
        with open(json_file, "w"):
            pass
    with open(json_file) as f:
        # read file and remove whitespaces
        json_string = f.read().strip()

    # if string is empty, return a valid JSON string for an empty object
    if not json_string:
        return "{}"

    return json_string


def dump_json(json_file, data_json):
    """
    Writes a JSON formatted string directly to a specified file.

    Args:
        json_file (str): The path to the file to be overwritten.
        data_json (str): The JSON formatted string data to write.
    """
    with open(json_file, "w") as f:
        f.write(data_json)


# Timestamp for now
def now():
    """
    Generates the current timestamp in 'DD/MM/YYYY HH:MM:SS' format.

    Returns:
        str: The formatted current date and time.
    """
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
