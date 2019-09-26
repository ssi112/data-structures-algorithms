"""
last_index.py

Problem statement

Given an array arr and a target element target, find the last index of occurence
of target in arr using recursion. If target is not present in arr, return -1.

For example:

    arr = [1, 2, 5, 5, 4] and target = 5, output = 3
    arr = [1, 2, 5, 5, 4] and target = 7, output = -1
"""

def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    TODO: complete this method to find the last index of target in arr
    """
    # we start looking from the last index
    return last_index_arr(arr, target, len(arr) - 1)


def last_index_arr(arr, target, index):
    if index < 0:
        return -1

    # check if target is found - searching backwards
    if arr[index] == target:
        return index

    # else make a recursive call to the rest of the array
    return last_index_arr(arr, target, index - 1)


def test_function(test_case):
    arr = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = last_index(arr, target)
    if output == solution:
        print("Pass")
    else:
        print("False")


arr = [1, 2, 5, 5, 4]
target = 5
solution = 3

test_case = [arr, target, solution]
test_function(test_case)

arr = [1, 2, 5, 5, 4]
target = 7
solution = -1

test_case = [arr, target, solution]
test_function(test_case)

arr = [91, 19, 3, 8, 9]
target = 91
solution = 0

test_case = [arr, target, solution]
test_function(test_case)

arr = [1, 1, 1, 1, 1, 1]
target = 1
solution = 5

test_case = [arr, target, solution]
test_function(test_case)
