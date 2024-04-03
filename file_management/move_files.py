import os

source = "moved.txt"

destination = "folder\\moved.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" We moved it")
except FileNotFoundError as e:
    print(e)
    print(source+" was not found")
