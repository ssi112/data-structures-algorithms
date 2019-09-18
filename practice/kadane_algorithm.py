"""
Problem Statement

You have been given an array containg numbers.
Find and return the largest sum in a contiguous subarray within the input array.

Example 1:
    arr= [1, 2, 3, -4, 6]
    The largest sum is 8, which is the sum of all elements of the array.

Example 2:
    arr = [1, 2, -5, -4, 1, 6]
    The largest sum is 7, which is the sum of the last two elements of the array.
"""

# they apparently are not teaching much of anything in this course:
# Kadane’s Algorithm:
#     https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

import sys
def maxSubArraySum(a, size):
    max_so_far = -sys.maxsize - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    size = len(arr)
    max_so_far = -sys.maxsize - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + arr[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

# Driver function to check the above function
# a = [1, 2, -5, -4, 1, 6]
# a = [1, 2, 3, -4, 6]
a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print("Maximum contiguous sum is", maxSubArraySum(a,len(a)))

print("Maximum contiguous sum is", max_sum_subarray(a))


