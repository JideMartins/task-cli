from datetime import datetime


# Timestamp for now
def now():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


# # Add task
# def add_task(data):
#     des = input("Input new task: ")

#     data["ID"] += 1
#     data["description"] = des


# def update_task(data):
#     data["updatedAt"] = now()


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
    return data


print("=" * 50)
print(f"Your tasks\n{base_data()}")
