# update task
import json
from data_handler import convert_dictionary, dump_json, load_json, convert_json, now

# load data
data = convert_json(load_json("tasks.json"))


def add_task(description):
    """Adds a new task to the global task data structure.

    New task is assigned the next sequential integer ID, starting from 1.
    The status is set to 'todo' as default and timestamps are recorded.

    Args:
        description (str): A brief summary of the task to be added.

    Returns:
        str: The updated task data converted into a JSON formatted string.
    Side Effects:
        Modifies the global 'data' dictionary in memory.
        The caller is expected to save the returned JSON string to the task file.
    """
    # if dictionary is empty, start at 1
    if not data:
        new_id = 1
    else:
        # Get highest existing key and add 1
        data_keys = map(int, data.keys())
        new_id = max(data_keys) + 1
    data[str(new_id)] = {
        "description": "",
        "status": "todo",
        "createdAt": now(),
        "updatedAt": now(),
    }
    data[str(new_id)]["description"] = description

    # convert to json
    data_json = json.dumps(data, indent=4)
    print(f"Task added successfully (ID: {new_id})")
    return data_json


def update_task(id, description):
    """
    The function first checks if the specified task ID exists. If the ID is found, it updates the task's description and then serializes the entire data structure into a JSON string. If the ID is not found, the function prints an error message and returns the current, unchanged JSON data.

    Args:
        id (str): The string ID of the task to update (e.g., "1", "10").
        description (str): The new description for the task.

    Returns:
        str: updated task data converted into a JSON formatted string if
             successful, or the original JSON string if the task ID is not found.
    Side Effects:
        Modifies the global 'data' dictionary in memory if successful.
    """

    if id not in data:
        print(f"Error: Task with ID '{id}' not found")
        return json.dumps(data, indent=4)  # return current JSON string

    # If ID exists, proceed with update
    data[id]["description"] = description

    # update timestamp
    data[id]["updatedAt"] = now()

    # convert modified dictionary to json
    data_json = json.dumps(data, indent=4)
    print(f"Task Updated! (ID: {id})")

    return data_json


def delete_task(id):
    """Deletes a task from the global data structure based on its ID.

    The function checks if the specified task ID exists in the data. If found,
    the task is removed. If the ID is not found, an error message is printed
    and the existing data is returned.

    Args:
        id (str): String ID of the task to be deleted (eg "1", "5").

    Returns:
        str: The updated task data converted into a JSON formatted string.
             If the task was not found, the original JSON string is returned.

    Side Effects:
        Modifies the global 'data' dictionary in memory if a task is deleted.
    """
    if id not in data:
        print(f"Error: Task with ID '{id}' not found")
        return json.dumps(data, indent=4)  # return current JSON string

    data.pop(str(id))

    # convert to json and return
    data_json = json.dumps(data, indent=4)
    print(f"Task Deleted! (ID: {id})")

    return data_json


def set_status(id, status):
    """Sets the status of an existing task to a specified value.

    Args:
        id (str): The string ID of the task to update.
        status (str): The desired status

    Returns:
        The updated task data as a JSON formatted string,
             or the original JSON string if the task ID is not found.

    Side Effects:
        Modifies the global 'data' dictionary in memory if a task is deleted.
    """
    if id not in data:
        print(f"Error: Task with ID '{id}' not found")
        return json.dumps(data, indent=4)

    data[id]["status"] = status
    data[id]["updatedAt"] = now()

    data_json = json.dumps(data, indent=4)
    print(f"Task status set to {status} (ID: {id})")

    return data_json


def list_tasks(status_filter="ALL"):
    """
    Lists tasks, optionally filtered by status (todo, done, in-progress).

    Args:
        status_filter (str): The status to filter by, or "ALL" to list everything.
    """
    if not data:
        print("There are no tasks to display:")
        print("   run add [description] to create new task")
        return

    tasks_shown = 0

    for id, task_details in data.items():
        task_status = task_details.get("status")

        # Filtering Logic: Only proceed if the task matches the filter or if filter is "ALL"
        if status_filter == "ALL" or task_status == status_filter:

            # --- START of Display Block  ---
            print(f"Task ID: {id}")
            if status_filter != "ALL":
                print(f"--- Filter: {status_filter.upper()} ---")

            # Iterate over task_details dictionary
            # This loop ONLY runs if the task passed the filter check
            for key, value in task_details.items():
                print(f"  {key:<12}: {value}")

            print("-" * 40)
            tasks_shown += 1
            # --- END of Display Block ---

    if tasks_shown == 0 and status_filter != "ALL":
        print(f"No tasks found with status: {status_filter}")
