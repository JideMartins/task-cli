from argparse import ArgumentParser
from task_manager import (
    add_task,
    delete_task,
    list_tasks,
    set_status,
    update_task,
)
from file_utils import dump_json

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
    help="Mark task as 'done' or 'in-progress' Usage:-d, --done or -i, --inprog",
    # argument_default="todo"
)

# Add mutually exclusive group for marking progress
mark_group = parser_mark.add_mutually_exclusive_group()

mark_group.add_argument(
    "-d",
    "--done",
    action="store_const",
    dest="status",
    const="done",
    help="Marks task as done",
)

mark_group.add_argument(
    "-i",
    "--inprog",
    action="store_const",
    dest="status",
    const="in-progress",
    help="Marks task as in-progress",
)
# mark ID
parser_mark.add_argument("id", type=str, help="Task ID")

# 7. Define 'list' subcommands
parser_list = subparsers.add_parser(
    "list", help="Lists tasks with optional return task progress filters"
)

parser_list.add_argument(
    "status",
    nargs="?",
    default="ALL",
    choices=["ALL", "todo", "done", "in-progress"],
    type=str,
    help="Task status (optional: todo, done or in-progress). Default shows all.",
)



# defining main
def main():
    # parse arguments
    args = parser.parse_args()

    # Use commands
    if args.subcommand == "add":
        data_json = add_task(args.description)
        dump_json("tasks.json", data_json)

    elif args.subcommand == "update":
        data_json = update_task(args.id, args.description)
        dump_json("tasks.json", data_json)

    elif args.subcommand == "delete":
        data_json = delete_task(args.id)
        dump_json("tasks.json", data_json)

    elif args.subcommand == "mark":
        data_json = set_status(args.id, args.status)
        dump_json("tasks.json", data_json)

    elif args.subcommand == "list":
        list_tasks(args.status)


if __name__ == "__main__":
    main()
