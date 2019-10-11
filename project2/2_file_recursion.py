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

suffix = ".c"
path = os.getcwd()
suffix_files = find_files(suffix, path)

# go back to where we started
os.chdir(path)

print("~"*55)
for file_names in suffix_files:
    # print(file_names)
    # testdir is test directory
    # so relative path looks something like '/testdir/sub_dir/file_name'
    pos = file_names.find('testdir')
    if '/' in file_names:
        slash = '/'
    else:
        slash = '\\'
    print(".{}{}".format(slash, file_names[pos:]))
    """

    print( [pos for pos, char in enumerate(file_names) if char == slash] )
    """


