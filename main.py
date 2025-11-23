from datetime import datetime
import json
import os

from data_handler import dump_json, now




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
