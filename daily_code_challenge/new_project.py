#!/usr/bin/python3.6

from sys import argv
import shutil

project_name = argv[1]
folder_to_copy = "./projects/skeleton/"

try:
    shutil.copytree(folder_to_copy, project_name)
except shutil.Error as error:
    print(f"Error: {error.strerror}")

# TODO: rename the NAME to project_name
