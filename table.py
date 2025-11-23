# To represent in tabular format
from tabulate import tabulate
from task_manager import data


def make_table(status_filter="ALL"):
    """
    Lists tasks in tabular format, optionally filtered by status (todo, done, in-progress).

    Args:
        status_filter (str): The status to filter by, or "ALL" to list everything.
    """
    if not data:
        print("There are no tasks to display.")
        print("   run add [description] to create new task")
        return

    # Define headers once
    headers = ["ID", "Status", "Description", "Created At", "Updated At"]
    table_data = [] # List to hold rows of data
    tasks_shown = 0

    # 2. Add a title specific to the filter
    if status_filter != "ALL":
        print(f"\n--- FILTERED TASKS: {status_filter.upper()} ---")
    else:
        print("\n--- ALL TASKS ---")

    for id, task_details in data.items():
        task_status = task_details.get("status")

        # Filtering Logic
        if status_filter == "ALL" or task_status == status_filter:
            
            # 3. Collect the data for the current row
            row = [
                id,
                task_details["status"],
                task_details["description"],
                task_details["createdAt"],
                task_details["updatedAt"]
            ]
            table_data.append(row)
            tasks_shown += 1

    # 4. Generate and print the table
    if tasks_shown > 0:
        table_output = tabulate(
            table_data, 
            headers=headers, 
            tablefmt="fancy_grid"
        )
        print(table_output)
    
    # 5. Handle the case where no tasks matched the filter
    elif tasks_shown == 0 and status_filter != "ALL":
        print(f"No tasks found with status: {status_filter}")