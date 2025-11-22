tasks = {}

print("Get your tasks done!")


print(tasks)
num = 0
is_done = True
while is_done:
    task = input("Input new task: ")
    num += 1
    tasks[f"00{num}"] = task
    user_input = input("Would you like to addmore tasks? y/n: ")
    if user_input.lower() == "y":
        continue
    else:
        is_done = False
        print("bye")

print("=" * 50)
print(f"Your tasks\n{tasks}")
