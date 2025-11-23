[![Roadmap.sh Project](https://img.shields.io/badge/Project-Roadmap.sh-blue.svg)](https://roadmap.sh/projects/task-tracker)
# 🚀 Task CLI: Command Line Task Management

**Task CLI** is a simple, lightweight, and cross-platform command-line interface tool for managing your daily to-dos right from your terminal. Stop switching apps—track, update, and organize your tasks with simple commands\!



## 🛠️ Installation

Because Task CLI is packaged using `setuptools`, installation is a breeze using `pip`.

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/JideMartins/task-cli.git
    cd task-cli
    ```

2.  **Activate Environment (Recommended):**
    For best practice, always install CLI tools in a virtual environment.

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .\.venv\Scripts\activate   # On Windows
    ```

3.  **Install the Application:**
    Install the package locally using `pip`. This makes the `tsk` command available in your terminal.

    ```bash
    pip install .
    ```

-----

## 💡 Quick Start & Usage

Once installed, you can run the main command `tsk` followed by any subcommand.

### Core Commands

| Command | Description | Example |
| :--- | :--- | :--- |
| `tsk add` | Creates a new task. | `tsk add "Call the dentist"` |
| `tsk list` | Displays all tasks in a formatted table. | `tsk list` |
| `tsk update` | Modifies the description of an existing task. | `tsk update 5 "Call dentist at 2 PM"` |
| `tsk mark` | Changes the status of a task to `done` or `in-progress`. | `tsk mark -d 5` |
| `tsk delete` | Permanently removes a task. | `tsk delete 5` |

-----

## 📚 Detailed Command Reference

### 1\. Adding a Task (`tsk add`)

Adds a new task. It is automatically assigned the next available ID and given the status `todo`.

```bash
tsk add "Prepare the README documentation"
```

### 2\. Listing Tasks (`tsk list`)

Displays all tasks by default, using a clean table powered by the `tabulate` module.

| Option | Description | Example |
| :--- | :--- | :--- |
| **No Filter** | Lists all tasks. | `tsk list` |
| **Status Filter** | Filters tasks by a specific status. | `tsk list done` |

**Available Status Filters:** `todo`, `done`, `in-progress`

### 3\. Updating a Task (`tsk update`)

Requires the Task **ID** and the **new description**.

```bash
tsk update 10 "Refactor file_utils into storage module"
```

### 4\. Marking Status (`tsk mark`)

Uses mutually exclusive flags to change the task status.

| Flag | Status | Example |
| :--- | :--- | :--- |
| `-d`, `--done` | Marks task as `done`. | `tsk mark -d 10` |
| `-i`, `--inprog` | Marks task as `in-progress`. | `tsk mark -i 10` |

### 5\. Deleting a Task (`tsk delete`)

Permanently removes a task using its **ID**.

```bash
tsk delete 10
```

-----

## 💻 Project Structure

The Task CLI is organized into three distinct layers for maintainability and clarity:

  - **`cli.py`**: Handles command-line argument parsing using `argparse` and acts as the entry point (`tsk = cli:main`).
  - **`task_manager.py`**: Contains the core **business logic** (add, update, delete, set status).
  - **`file_utils.py`**: Manages data **persistence** (loading and dumping the `tasks.json` file).
  - **`table.py`**: Handles the clean, formatted display of tasks using the `tabulate` library.
