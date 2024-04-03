import os
import shutil

path = 'deleteable.txt'

try:
    #os.rmdir(path) to delete an empty directory
    #shitil.rmtree(path) to delete a directory with all the files
    os.remove(path)
except FileNotFoundError as e:
    print(e)
    print("That file was not found")
except PermissionError as e:
    print(e)
    print(" You do not have permisions to delete that")

