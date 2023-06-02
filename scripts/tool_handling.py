from sys import exit
import os
from scripts.tool_running import run

def return_list_from_file(file_name):
    """Return a list from a file"""

    try:
        with open(file_name, "r") as file:
            return [line.strip() for line in file if line.strip() != ""] # make sure we only get the raw data
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        exit(1)


def return_dict_from_file(file_name):
    """Return a dict from a file"""

    try:
        with open(file_name, "r") as file:
            return {line.split(":")[0].strip(): line.split(":")[1].strip() for line in file if line.strip() != ""} # make sure we only get the raw data
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        exit(1)


def write_dict_to_file(file_name, dict):
    """Write a dict to a file"""

    try:
        with open(file_name, "w") as file:
            for key, value in dict.items():
                file.write(f"{key}:{value}\n")
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        exit(1)


# check if a supported python version is running or not for shutil (python 3.3+)
try:
    from shutil import which
except ImportError:
    print("Missing module: shutil (probably unsupported Python version)")
    exit(1)

def find_tool(tool_name):
    """Find the tool in the PATH, return 0 if not found"""

    tool_path = which(tool_name)

    if tool_path is None:
        return 0

    return str(tool_path) # not sure if we have to turn it into a string but we are being safe


def update_tool_list():
    """Update the tool list"""
    tools = return_list_from_file("data/preset/tool_list.txt")

    found_tools = {}
    for tool in tools:
        path = find_tool(tool)
        if path != 0:
            found_tools[tool] = path

    return found_tools

def get_tool_list(update=False):
    """Return the tool list or update"""

    if not os.path.isfile("data/generated/tool_paths.txt") or update:
        tools = update_tool_list()
        write_dict_to_file("data/generated/tool_paths.txt", tools)
        # print("Tool list updated")
        return tools

    return return_dict_from_file("data/generated/tool_paths.txt")
       
def run_tool(name, target, options=None):
    """call the running function from tool_running"""

    tools = return_dict_from_file("data/generated/tool_paths.txt")
    name_list = list(tools.keys())
    if name in name_list:
        return run(name, target, options)
    
    print(f"{name} not in name_list")
