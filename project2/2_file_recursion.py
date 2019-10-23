"""
2_file_recursion.py

For this problem, the goal is to write code for finding all files under a directory
(and all directories beneath it) that end with ".c"

Here is an example of a test directory listing listing:

    ./testdir
    ./testdir/subdir1
    ./testdir/subdir1/a.c
    ./testdir/subdir1/a.h
    ./testdir/subdir2
    ./testdir/subdir2/.gitkeep
    ./testdir/subdir3
    ./testdir/subdir3/subsubdir1
    ./testdir/subdir3/subsubdir1/b.c
    ./testdir/subdir3/subsubdir1/b.h
    ./testdir/subdir4
    ./testdir/subdir4/.gitkeep
    ./testdir/subdir5
    ./testdir/subdir5/a.c
    ./testdir/subdir5/a.h
    ./testdir/t1.c
    ./testdir/t1.h

Python's os module will be useful—in particular, you may want to use the
following resources:

  os.path.isdir(path)

  os.path.isfile(path)

  os.listdir(directory)

  os.path.join(...)

Note: os.walk() is a handy Python method which can achieve this task very easily.
However, for this problem you are NOT allowed to use os.walk().
"""
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    paths = []
    try:
        if not suffix:
            msg  = "\nPlease provide a valid suffix of the file name."
            msg += "\n   Example '*.txt' \n"
            raise ValueError(msg)
        if not os.path.exists(path):
            msg = "\nInvalid path given."
            raise ValueError(msg)
    except ValueError as err_msg:
        print(err_msg)
        return False

    for dirs in os.listdir(path):
        pathalogic = os.path.join(path, dirs)
        if os.path.isfile(pathalogic):
            if pathalogic.endswith(suffix):
                # print(pathalogic)
                paths.append(pathalogic)
        if os.path.isdir(pathalogic):
            # print("dirs = '{}' - {}".format(dirs, pathalogic))
            os.chdir(pathalogic)
            # adds specified list elements to the end of the current list
            # if not done the final 'return paths' yields an empty list
            paths.extend(find_files(suffix, pathalogic))
    return paths

def relative_path(suffix_files):
    global slash
    relative_paths = []
    for file_names in suffix_files:
        # print(file_names)
        # testdir is test directory
        # so relative path looks something like '/testdir/sub_dir/file_name'
        pos = file_names.find('testdir')
        if '/' in file_names:
            slash = '/'
        else:
            slash = '\\'
        # print(".{}{}".format(slash, file_names[pos:]))
        relative_paths.append("." + slash + file_names[pos:])
    return relative_paths

def check_paths(list_of_paths, slash):
    str1 = "./testdir/subdir1/a.c"
    str2 = "./testdir/subdir3/subsubdir1/b.c"
    str3 = "./testdir/subdir5/a.c"
    str4 = "./testdir/t1.c"

    if slash == '\\':
        str1 = str1.replace('/', slash)
        str2 = str2.replace('/', slash)
        str3 = str3.replace('/', slash)
        str4 = str4.replace('/', slash)

    count = 0
    if str1 in list_of_paths:
        count += 1
    if str2 in list_of_paths:
        count += 1
    if str3 in list_of_paths:
        count += 1
    if str4 in list_of_paths:
        count += 1
    if count == 4:
        return True
    return False


slash = '/'

# ----------------------------------------------------------------------
print("\nTest 1: Checking list of paths...")
suffix = ".c"
path = os.getcwd()
relative_paths = []

suffix_files = find_files(suffix, path)

# go back to where we started
if os.path.exists(path):
    os.chdir(path)

if suffix_files is not False and path is not False:
    print("-"*55)
    print("Showing relative paths...\n")
    relative_paths = relative_path(suffix_files)
    for rel in relative_paths:
        print(rel)

print("Pass, yay!" if (check_paths(relative_paths, slash)) else "Fail, uh oh!")

# ----------------------------------------------------------------------
print("\nTest 2: Checking list of paths...")
suffix = ""
path = os.getcwd()
relative_paths = []

suffix_files = find_files(suffix, path)

# go back to where we started
if os.path.exists(path):
    os.chdir(path)

if suffix_files is not False and path is not False:
    print("-"*55)
    print("Showing relative paths...\n")
    relative_paths = relative_path(suffix_files)
    for rel in relative_paths:
        print(rel)

print("Pass, yay!" if (check_paths(relative_paths, slash)) else "Fail, uh oh!")

# ----------------------------------------------------------------------
print("\nTest 3: Checking list of paths...")
suffix = "*.c"
path = 909 #os.getcwd()
relative_paths = []

suffix_files = find_files(suffix, path)

# go back to where we started
if os.path.exists(path):
    os.chdir(path)

if suffix_files is not False and path is not False:
    print("-"*55)
    print("Showing relative paths...\n")
    relative_paths = relative_path(suffix_files)
    for rel in relative_paths:
        print(rel)

print("Pass, yay!" if (check_paths(relative_paths, slash)) else "Fail, uh oh!")



