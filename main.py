tasks = {"ID": 0, "description": "", "status": "todo", "createdAt": "", "updatedAt": ""}
base_tasks = {}
print("Get your tasks done!")


# Add task
def add_task(data):
    des = input("Input new task: ")

    data["ID"] += 1
    data["description"] = des


print(tasks)
num = 0
not_done = True
while not_done:
    add_task(tasks)
    base_tasks.update(tasks)
    
    user_input = input("Would you like to addmore tasks? y/n: ")
    if user_input.lower() == "y":
        continue
    else:
        not_done = False
        print("bye")

print("=" * 50)
print(f"Your tasks\n{base_tasks}")
