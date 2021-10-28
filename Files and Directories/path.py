# We will work with the module 'pathlib' that lets us create classes where we can create objects to work with files and directories
# example:
from pathlib import Path # we are calling 'Path' from the pathlip module
# there are two ways to do this: Absolute path and Relative path
# Absolute path is taking a path through your file system, like this: c:\Program\Microsoft
# for this example we will work with Relative path:
path = Path("ecommerce") # we are calling the 'ecommerce' directory
print(path.exists()) # we are checking if the directory exists through a boolean value
# *directories won't be detected if if the file is in the same folder as the directory
#this will create or remove a path:
path = Path("email")
#print(path.mkdir()) # this will make a directory and then print "None"
#print(path.rmdir()) # this will remove the directory, still outputs 'None'

path = Path() # this is set to the current directory
for file in path.glob('*'): # 'glob' is for searching through files and directories
    print(file) # this will search for all directories in the current path
for file in path.glob('*.*'):
    print(file) # this will search for all files in the current path
for file in path.glob('*.py'):
    print(file) # this will search for all .py files in the current path
