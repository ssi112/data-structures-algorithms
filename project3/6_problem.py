"""
6_problem.py

In this problem, we will look for smallest and largest integer from a list of
unsorted integers. The code should run in O(n) time. Do not use Python's
built-in functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""

def find_min_max(input_list):
    min = 0
    max = 0

    if len(input_list) == 0:
        return (False, False)
    if len(input_list) == 1:
        min = input_list[0]
        max = input_list[0]
        return (min, max)

    # initialize min and max with first two elements
    if input_list[0] < input_list[1]:
        min = input_list[0]
        max = input_list[1]
    else:
        min = input_list[1]
        max = input_list[0]
    # walk the rest of the list and update min/max as needed
    # could use enumerate but value is not needed
    # plus the index begins at zero anyway
    # and we need to skip the first two elements
    for indx in range(len(input_list[2:])+2):
        if input_list[indx] > max:
            max = input_list[indx]
        elif input_list[indx] < min:
            min = input_list[indx]
        indx += 1
    return (min, max)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == find_min_max(l)) else "Fail")

print("Pass" if ((False, False) == find_min_max([])) else "Fail")
print("Pass" if ((99, 99) == find_min_max([99])) else "Fail")
print("Pass" if ((-2, 2) == find_min_max([0,0,-1,-1,0,-2,1,0,2,1])) else "Fail")
print("Pass" if ((99, 99) == find_min_max([99,99])) else "Fail")


