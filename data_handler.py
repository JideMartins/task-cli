from datetime import datetime
import json
import os


# JSON string handling
def convert_json(json_string):
    data_dict = json.loads(json_string)
    return data_dict


def convert_dictionary(data_dict):
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
    with open(json_file, "w") as f:
        f.write(data_json)


# Timestamp for now
def now():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
