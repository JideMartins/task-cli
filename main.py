import json
import os
from argparse import ArgumentParser
from datetime import datetime
from data_handler import dump_json, now

# 1. Create parser object
parser = ArgumentParser(description="CLI to track and manage your tasks")

# 2. Add Subparser Container
subparsers = parser.add_subparsers(
    dest="subcommand",
    required=True,
    help="Sub-command help"
)


# 3. Define 'add' subcommand
parsers_add = subparsers.add_parser(
    "add",
    help="Adds task with description given"
)

# argument specific to 'add' subcommand
parsers_add.add_argument(
    "description",
    type=str,
    help="Short description of task"
)


# 4. Define 'update' subcommand
parser_update = subparsers.add_parser(
    "update",
    help="Update task with ID and/or description"
)

# arguments specific to 'update' subcommand
parser_update.add_argument(
    "id",
    type=str,
    help="Task ID"
)

parser_update.add_argument(
    "description",
    type=str,
    help="Description update"
)

# 5. Define 'delete' subcommand
parser_delete = subparsers.add_parser(
    "delete",
    help="Deletes task with known id"
)

parser_delete.add_argument(
    "id",
    type=str,
    help="Task ID"
)



























# add  data
def base_data():
    data = {}
    id = 0

    while True:
        id += 1
        data[id] = {
            "description": "",
            "status": "todo",
            "createdAt": now(),
            "updatedAt": None,
        }
        data[id]["description"] = input("input task: ")
        data[id]["updatedAt"] = now()
        user_input = input("Would you like to addmore tasks? y/n: ")
        if user_input != "y":
            print("bye!")
            break

    # convert to json
    data_json = json.dumps(data, indent=4)
    return data_json


# print("=" * 50)
# print(f"Your tasks\n{base_data()}")
# print(update_task(base_data()))


# print(delete_task(base_data()))
dump_json("tasks.json", base_data())
