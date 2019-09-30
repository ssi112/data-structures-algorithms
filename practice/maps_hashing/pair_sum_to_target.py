"""
pair_sum_to_target.py

Problem statement

Given an input_list and a target, return the indices of pair of integers in the
list that sum to the target. The best solution takes O(n) time.
You can assume that the list does not have any duplicates.

For e.g. input_list = [1, 5, 9, 7] and target = 8, the answer would be [0, 3]
"""

def pair_sum_to_zero(in_list, target):
    # TODO: Write pair sum to zero function

    first_index = 0
    last_index = len(in_list) - 1

    while first_index < last_index:
        pair_sum = in_list[first_index] + in_list[last_index]
        if pair_sum < target:
            first_index += 1
        elif pair_sum > target:
            last_index -= 1
        else:
            # below is the actual values
            # in_list[first_index], in_list[last_index]
            return [first_index, last_index]
    return [None, None]


input_list = [1, 5, 9, 7]
print(pair_sum_to_zero(input_list, 8)) # [0, 3]

input_list = [10, 5, 9, 8, 12, 1, 16, 6]
print(pair_sum_to_zero(input_list, 16)) # [0, 7]

input_list = [0, 1, 2, 3, -4]
print(pair_sum_to_zero(input_list, -4)) # [0, 4]

input_list = [0, 1, 2, 3, -4, 77, 101, -3, 11, 81]
print(pair_sum_to_zero(input_list, -11)) # [None, None]

