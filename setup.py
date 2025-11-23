from setuptools import setup

setup(
    name="task-cli",
    version="1.3.3",
    py_modules=["cli", "file_utils", "task_manager", "table"],
    install_requires=[],
    entry_points={"console_scripts": ["tsk = cli:main"]},
)
