from setuptools import setup

setup(
    name="task-cli",
    version="0.1.0",
    py_modules=["cli", "file_utils", "task_manager"],
    install_requires=[],
    entry_points={"console_scripts": ["tsk = cli:main"]},
)
