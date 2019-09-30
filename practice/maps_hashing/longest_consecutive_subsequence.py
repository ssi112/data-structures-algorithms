"""
longest_consecutive_subsequence.py

Problem Statement

Given list of integers that contain numbers in random order, write a program to
find the longest possible sub sequence of consecutive numbers in the array.
Return this subsequence in sorted order. The solution must take O(n) time

For e.g. given the list 5, 4, 7, 10, 1, 3, 55, 2, the output should be 1, 2, 3, 4, 5
"""
def longest_consecutive_subsequence(input_list):
    element_dict = dict()

    for index, element in enumerate(input_list):
        element_dict[element] = index

    # print(element_dict)

    max_length = -1
    starts_at = len(input_list)

    for index, element in enumerate(input_list):
        current_starts = index
        element_dict[element] = -1

        current_count = 1

        # check upwards
        current = element + 1

        while current in element_dict and element_dict[current] > 0:
            current_count += 1
            element_dict[current] = -1
            current = current + 1

        # check downwards
        current = element - 1
        while current in element_dict and element_dict[current] > 0:
            current_starts = element_dict[current]
            current_count += 1
            element_dict[current] = -1
            current = current - 1

        if current_count >= max_length:
            if current_count == max_length and current_starts > starts_at:
                continue
            starts_at = current_starts
            max_length = current_count

    start_element = input_list[starts_at]
    return [element for element in range(start_element, start_element + max_length)]


"""
--------------------------------------------------------------------------------------
https://www.geeksforgeeks.org/longest-consecutive-subsequence/

Given an array of integers, find the length of the longest sub-sequence such that
elements in the subsequence are consecutive integers, the consecutive numbers can
be in any order.

Return this subsequence in sorted order.

The solution must take O(n) time

For e.g. given the list 5, 4, 7, 10, 1, 3, 55, 2, the output should be 1, 2, 3, 4, 5

One Solution is to first sort the array and find the longest subarray with consecutive
elements. Time complexity of this solution is O(nLogn).

We can solve this problem in O(n) time using an Efficient Solution.

The idea is to use Hashing. We first insert all elements in a Set.
Then check all the possible starts of consecutive subsequences.

Below is the complete algorithm.

    Create an empty hash.
    Insert all array elements to hash.
    Do following for every element arr[i]
    Check if this element is the starting point of a subsequence.
        To check this, we simply look for arr[i] – 1 in the hash, if not found,
        then this is the first element in subsequence.
    If this element is the first element, then count number of elements in the
        consecutive starting with this element. Iterate from arr[i] + 1 till
        the last element that can be found.
    If the count is more than the previous longest subsequence found, then update this.
"""
def length_longest_consecutive_subsequence(input_list):
    s = set()
    n = len(input_list)
    ans = 0
    out_list = []

    # Hash all the array elements
    for ele in input_list:
        s.add(ele)

    # check each possible sequence from the start
    # then update optimal length
    for i in range(n):

        # if current element is the starting element of a sequence
        if (input_list[i] - 1) not in s:
            # Then check for next elements in the sequence
            j = input_list[i]
            while(j in s):
                j += 1
                out_list.append(j - 1)

            # update optimal length if this length is more
            ans = max(ans, j - input_list[i])
    return ans


test = [5, 4, 7, 10, 1, 3, 55, 2]
# s/be [1, 2, 3, 4, 5]
print("\n-----------------------------------------------------------------------")
print("test: {} = {}".format(test, length_longest_consecutive_subsequence(test)))
print("test: {} = {}".format(test, longest_consecutive_subsequence(test)))

test = [2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6 ]
# s/be [8, 9, 10, 11, 12]
print("\n-----------------------------------------------------------------------")
print("test: {} = {}".format(test, length_longest_consecutive_subsequence(test)))
print("test: {} = {}".format(test, longest_consecutive_subsequence(test)))

test = [0, 1, 2, 3, 4]
# s/be [0, 1, 2, 3, 4]
print("\n-----------------------------------------------------------------------")
print("test: {} = {}".format(test, length_longest_consecutive_subsequence(test)))
print("test: {} = {}".format(test, longest_consecutive_subsequence(test)))


