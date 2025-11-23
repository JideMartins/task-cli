import json
import os
from argparse import ArgumentParser
from datetime import datetime
from data_handler import dump_json, now

# 1. Create parser object
parser = ArgumentParser(description="CLI to track and manage your tasks")

# 2. Add Subparser Container
subparsers = parser.add_subparsers(
    dest="subcommand", required=True, help="Sub-command help"
)


# 3. Define 'add' subcommand
parsers_add = subparsers.add_parser("add", help="Adds task with description given")

# argument specific to 'add' subcommand
parsers_add.add_argument("description", type=str, help="Short description of task")


# 4. Define 'update' subcommand
parser_update = subparsers.add_parser(
    "update", help="Update task with ID and/or description"
)

# arguments specific to 'update' subcommand
parser_update.add_argument("id", type=str, help="Task ID")

parser_update.add_argument("description", type=str, help="Description update")

# 5. Define 'delete' subcommand
parser_delete = subparsers.add_parser("delete", help="Deletes task with known id")

parser_delete.add_argument("id", type=str, help="Task ID")


# 6. Define 'mark' subcommand
parser_mark = subparsers.add_parser(
    "mark",
    help="Mark task as 'done' or 'in-progress'",
    # argument_default="todo"
)

# Add mutually exclusive group for marking progress
mark_group = parser_mark.add_mutually_exclusive_group()

mark_group.add_argument(
    "-d",
    "--done",
    action="store_const",
    dest="progress",
    const="DONE",
    help="Marks task as done",
)

mark_group.add_argument(
    "-i",
    "--in-progress",
    action="store_const",
    dest="progress",
    const="IN-PROGRESS",
    help="Marks task as in-progress",
)
# marker ID
parser_mark.add_argument("id", type=str, help="Task ID")

# 7. Define 'list' subcommands
parser_list = subparsers.add_parser(
    "list", help="Lists tasks with optional return task progress filters"
)

parser_list.add_argument(
    "progress",
    nargs="?",
    default="ALL",
    choices=["ALL", "todo", "done", "in-progress"],
    type=str,
    help="Task progress (optional: todo, done or in-progress). Default shows all."
)

# parse arguments
args = parser.parse_args()




# Use commands
if args.subcommand == "add":
    # TODO: Use add function here and create or add to JSON file
    pass
elif args.subcommand == "update":
    # TODO: Use update function here and update JSON file
    pass
elif args.subcommand == "delete":
    # TODO: Delete and update JSON file
    pass
elif args.subcommand == "mark":
    # TODO: mark files according to options
    pass
elif args.subcommand == "list":
    # TODO: list files
    # TODO: handle logic for optional args
    pass

