[![Roadmap.sh Project](https://img.shields.io/badge/Project-Roadmap.sh-blue.svg)](https://roadmap.sh/projects/task-tracker)
# 🚀 Task CLI: Command Line Task Management

**Task CLI** is a simple, lightweight, and cross-platform command-line interface tool for managing your daily to-dos right from your terminal. Stop switching apps—track, update, and organize your tasks with simple commands\!

-----

## 🛠️ Installation

Because Task CLI is packaged using `setuptools`, installation is a breeze using `pip`.

### 1\. Clone the Repository

```bash
git clone https://github.com/JideMartins/task-cli.git
cd task-cli
```

### 2\. Activate Virtual Environment (Crucial Step‼️)

For best practice, always install CLI tools in a virtual environment. This step **must** be performed every time you open a new terminal session to run the `tsk` command.

```bash
# Create the environment
python -m venv .venv

# Run the activation script based on your operating system:
source .venv/bin/activate    # 🐧 For macOS and Linux
.\.venv\Scripts\activate     # 🪟 For Windows Command Prompt (cmd)
.\.venv\Scripts\Activate.ps1 # 🪟 For Windows PowerShell
```

> **Note:** After activation, your terminal prompt should start with `(.venv)`. This confirms that the system can now find the `tsk` executable.

### 3\. Install the Application

Install the package locally using `pip`. This makes the `tsk` command available *within the active virtual environment*.

```bash
pip install .
```

### 4\. Verify Installation

After installation, immediately test the command to ensure it's recognized.

```bash
tsk --help
```

  * **Expected Result:** The help documentation for the Task CLI is displayed.
  * **If you get an error like 'tsk' is not recognized:** This means you missed or failed the **Activation Step (Step 2)**. Please run the correct activation command for your OS and try again.

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


-----

## 🆘 Getting Help

The Task CLI application uses Python's `argparse` module, which includes robust, built-in help documentation accessible directly from the command line.

### 1\. General Help

To see a list of all available subcommands and a brief description of the tool, run the main command with the standard help flag:

```bash
tsk --help    # or task -h
```

### 2\. Subcommand Specific Help

To view the required arguments, flags, and options for any specific command (like `add`, `update`, or `mark`), run the subcommand followed by the help flag. This is essential for commands that use arguments like `ID` or status flags.

| Command | Action |
| :--- | :--- |
| **Add Help** | Displays the required `description` argument. |
| **Mark Help** | Displays the mutually exclusive flags (`-d` / `-i`) and the required `ID`. |
| **List Help** | Displays the optional `status` filter argument and available choices. |

```bash
# Example 1: Getting help for the 'mark' command
tsk mark --help
```

```bash
# Example 2: Getting help for the 'list' command
tsk list -h
```

-----

### 📝 Example Output for `tsk mark --help`

If a user runs the command above, they will see output similar to this:

```
usage: tsk mark [-h] [-d | -i] id

Mark task as 'done' or 'in-progress' Usage:-d, --done or -i, --inprog

positional arguments:
  id                    Task ID

options:
  -h, --help            show this help message and exit

mutually exclusive arguments:
  -d, --done            Marks task as done
  -i, --inprog          Marks task as in-progress
```