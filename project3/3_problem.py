"""
3_problem.py

Rearrange Array Elements so as to form two numbers such that their sum
is maximum. Return these two numbers. You can assume that all array
elements are in the range [0, 9].

The number of digits in both the numbers cannot differ by more than 1.
You're not allowed to use any sorting function that Python provides and
the expected time complexity is O(nlog(n)).

Example: [1, 2, 3, 4, 5]

The expected answer would be [531, 42].
Another expected answer can be [542, 31].

In scenarios such as these when there are more than one possible answers,
return any one.
"""

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their
    sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    first = 0
    mid = len(input_list) // 2
    last = len(input_list) - 1
    maximum = sum(input_list)

    list1 = input_list[:mid]
    list2 = input_list[mid:]
    list1 = merge_sort(list1)
    list2 = merge_sort(list2)

    result = [int("".join([str(item) for item in list1]))]
    result.append(int("".join([str(item) for item in list2])))
    return result


"""
Divide and Conquer Algorithm: O(n log n)
Divide array into smaller arrays until each small array has one
position and then merge these small arrays into bigger ones until
one single array exist that is sorted
"""
def merge_sort(input_list):
    """
    helper function for the merge & sort
    """
    input_list = merge_sort_recur(input_list)
    return input_list


def merge_sort_recur(input_list):
    """
    transforms a larger list into successively smaller lists
    """
    length = len(input_list)
    if (length == 1):
        return input_list
    # split the list in half
    mid = len(input_list) // 2
    left = input_list[0:mid]
    right = input_list[mid:]
    # recursively split the list then merge and sort it
    return merge(merge_sort_recur(right), merge_sort_recur(left), False)


def merge(left, right, ascending = True):
    """
    merge and sort the smaller list back into bigger ones until
    we have the original list in sorted format
    """
    result = []
    index_left = 0
    index_right = 0
    # iterate and compare left to right
    # add left or right item depending on which is smaller
    while index_left < len(left) and index_right < len(right):
        if ascending:
            # ascending sort
            if left[index_left] < right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1
        # descending sort
        else:
            if left[index_left] > right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

    # add any remaining items from the left array
    while index_left < len(left):
        result.append(left[index_left])
        index_left += 1

    # add any remaining items form the right array
    while index_right < len(right):
        result.append(right[index_right])
        index_right += 1

    # merged and sorted array
    return result


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [21, 543]])
test_case = [[4, 6, 2, 5, 9, 8], [642, 985]]
test_function(test_case)

print(rearrange_digits([1, 2, 3, 4, 5]))
print(rearrange_digits([4, 6, 2, 5, 9, 8]))
print(rearrange_digits([0, 2, 4, 6, 8]))
print(rearrange_digits([11, 9, 3, 9]))
