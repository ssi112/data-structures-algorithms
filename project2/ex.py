"""
ex.py

Locally save and call this file ex.py ##
Code to demonstrate the use of some of the OS modules in python
"""
import os

pwd = os.getcwd()
print(pwd)

# Let us print the files in the directory in which you are running this script
print(os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py ends with py?", "./ex.py".endswith(".py"))

print( os.path.isdir("testdir") )

os.chdir("testdir")
print("-"*25)
print(os.listdir("."))

os.chdir("..")

suffix = ".c"
path = os.getcwd()

print("cwd =", path)

for dirs in os.listdir("."):
    if os.path.isdir(dirs):
        print("-"*25)
        print(dirs)

print("="*50)
"""
for dirs in os.listdir("."):
    if os.path.isdir(dirs):
        directories.append(dirs)
    if os.path.isfile(dirs):
        if dirs.endswith(suffix):
            files.append(dirs)

--------------------------------------------------------------------------------
https://stackoverflow.com/questions/23468294/python-recursive-directory-reading-without-os-walk
--------------------------------------------------------------------------------
"""
def walkfn(dirname):
    for dirs in os.listdir("."):
        if os.path.isfile(dirs):
            if dirs.endswith(suffix):
                print(dirs)
        else:
            for name in os.listdir(dirname):
                path = os.path.join(dirname, name)
                if os.path.isdir(path):
                    print("name = '{}'".format(name))
                    os.chdir(path)
                    walkfn(path)

cwd = os.getcwd()
walkfn(cwd)

print("="*50)


# This is to get the directory that the program
# is currently running in.
dir_path = os.path.dirname(os.path.realpath(__file__))

"""
for root, dirs, files in os.walk(dir_path):
    for file in files:
        # change the extension from '.mp3' to
        # the one of your choice.
        if file.endswith(suffix):
            print(root+'/'+str(file))
"""

from pathlib import Path

package_dir = os.path.dirname(os.path.abspath(__file__))
print(package_dir)
