"""
2_problem.py

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its
index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's
runtime complexity must be in the order of O(log n).

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
"""

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    # parition array if needed
    first_indx = 0
    mid_indx = len(input_list) // 2
    last_indx = len(input_list) - 1
    """
    print("first: {} mid: {} last: {}".format(first_indx, mid_indx, last_indx))
    print("first item in list: {}".format(input_list[first_indx]))
    print("middle item in list: {}".format(input_list[mid_indx]))
    print("last item in list: {}".format(input_list[last_indx]))
    """

    # before we embark on a search see if we already have target data
    if number == input_list[first_indx]:
        # found it in first position
        return first_indx

    if number == input_list[mid_indx]:
        # found it in middle position
        return mid_indx

    if number == input_list[last_indx]:
        # found it in last position
        return last_indx

    # partition the input list and do a binary search but first
    # find the index to partition the list
    indx = find_partition_index(input_list, first_indx, last_indx)
    #print("partition index is", indx)
    #print("input_list", input_list)

    if indx == -1:
        # could be a sorted list, let's try a binary search
        return binary_search(input_list, number, first_indx, last_indx)

    # search left partition
    if number >= input_list[first_indx] and number <= input_list[indx]:
        return binary_search(input_list, number, first_indx, indx)

    # search right partition
    if number >= input_list[indx + 1] and number <= input_list[last_indx]:
        return binary_search(input_list, number, indx + 1, last_indx)

    # if those don't work do a plain binary search on entire list
    # print("plain binary search " + str(input_list) + "..." + str(number))
    # at this point the number is likely not in the list, but check anyway
    return binary_search(input_list, number, first_indx, last_indx)


def find_partition_index(input_list, first, last):
    """
    Divide up the list by iteratively narrowing the
    partition to find the pivot point basically by
    checking if the portion is sorted
     - essentially a binary search) - O(log n)
    ------------------------------------------------------
    We can get stuck in this loop w/out below test in case
    where this is a sorted list the indx will calc the
    middle position and never change
    """
    indx = -1
    while indx != ((first + last) // 2):
        indx = (first + last) // 2
        if input_list[indx] > input_list[indx + 1]:
            break
        if input_list[indx] > input_list[first]:
            first = indx
        if input_list[last] > input_list[indx]:
            last = indx
    return indx


def binary_search(input_list, number, first, last):
    # cannot find it
    if first > last:
        return -1
    middle = (first + last) // 2
    if number == input_list[middle]:
        return middle
    elif number < input_list[middle]:
        # search on the left partition
        return binary_search(input_list, number, first, middle - 1)
    else:
        # search on the right partition
        return binary_search(input_list, number, middle + 1, last)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1, 2, 3, 4, 6, 7, 8, 9], 6])

test_function([[6, 7, 8, 9, 10, 11, 12, 13, 14], 10])

test_function([[12, 13, 14, 15, 16, 17, 18, 10, 11], 10])
test_function([[12, 13, 14, 15, 16, 17, 18, 10, 11], 13])
test_function([[16, 11, 12, 13, 14, 15], 11])
