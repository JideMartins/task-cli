from datetime import datetime
import json


# Timestamp for now
def now():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# JSON handling
def convert_json(json_string):
    data_dict = json.loads(json_string)
    return data_dict

# add  data
def base_data():
    data = {}
    id = 1

    task = {"description": "", "status": "todo", "createdAt": now(), "updatedAt": None}

    while True:
        task["description"] = input("input task: ")
        task["updatedAt"] = now()
        data[id] = task
        id += 1
        user_input = input("Would you like to addmore tasks? y/n: ")

        if user_input != "y":
            print("bye!")
            break
    

    # convert to json
    data_json = json.dumps(data, indent=4)
    return data_json


print("=" * 50)
print(f"Your tasks\n{base_data()}")
