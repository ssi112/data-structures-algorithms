"""
4_problem.py

Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2,
sort the array in a single traversal. You're not allowed
to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal.
For example if you traverse the array twice, that would still
be an O(n) solution but it will not count as single traversal.

Algorithm:
procedure three_way_part012(A : array of values, mid : value):
    i ← 0
    j ← 0
    n ← size of A - 1

    while j ≤ n:
        if A[j] < mid:
            swap A[i] and A[j]
            i ← i + 1
            j ← j + 1
        else if A[j] > mid:
            swap A[j] and A[n]
            n ← n - 1
        else:
            j ← j + 1
Reference:
https://en.wikipedia.org/wiki/Dutch_national_flag_problem
"""

def three_way_part012(input_list):
    low = 0
    mid = 0
    high = len(input_list) - 1
    # for a different type of list
    # middle value could be passed in for comparision
    mid_value = 1
    while mid <= high:
        if input_list[mid] < mid_value:
            # swap input_list[low] & input_list[mid]
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] > mid_value:
            # swap input_list[mid] & input_list[high]
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1
        else:
            mid += 1
    return input_list


def test_function(test_case):
    sorted_array = three_way_part012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)

test_case = [2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 2, 1]
test_function(test_case)

