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
    if not os.path.exists(json_file):
        with open(json_file, "w"):
            pass
    with open(json_file) as f:
        json_string = f.read()
    return json_string


def dump_json(json_file, data_json):
    with open(json_file, "w") as j_file:
        j_file.write(data_json)
        print("saved succesfully")

# Timestamp for now
def now():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")