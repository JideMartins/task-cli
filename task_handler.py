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
    try:
        data[str(id)]["description"] = description
        # convert to json
        data_json = json.dumps(data, indent=4)
        print(f"Task Updated!(ID: {id})")
    except:
        print("Please enter appropriate ID and description")
    
    return data_json


# def update_task(data_json):
#     print(data_json)
#     data_dict = convert_json(data_json)

#     id = input("what is the id number: ")
#     if str(id) not in data_dict.keys():
#         print("id not found")
#         print(data_dict)

#     else:
#         u_input = input(
#             "what would you like to update?\nt for task\ns for status: "
#         ).lower()
#         if u_input == "t":
#             data_dict[id]["description"] = input("update task: ")
#         elif u_input == "d":
#             data_dict[id]["status"] = input(
#                 "update status(done, in-progress, todeeeo): "
#             )
#         else:
#             print("Command not found")

#     # convert to json
#     return convert_dictionary(data_dict)


def delete_task(data_json):
    print(data_json)
    data_dict = convert_json(data_json)

    id = input("Enter id: ")
    try:
        data_dict.pop(str(id))
    except KeyError:
        print("id not found")

    # convert to json
    return convert_dictionary(data_dict)






# print("=" * 50)
# print(f"Your tasks\n{base_data()}")
# print(update_task(base_data()))


# print(delete_task(base_data()))
