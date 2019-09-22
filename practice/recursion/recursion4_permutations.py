"""
    recursion4_permutations.py

The number of permutations on a set of n elements is given by  n!.
For example, there are 2! = 2*1 = 2 permutations of {1, 2}, namely {1, 2} and {2, 1},
and 3! = 3*2*1 = 6 permutations of {1, 2, 3},
namely {1, 2, 3}, {1, 3, 2}, {3, 1, 2}, {3, 2, 1}, {2, 3, 1} and {2, 1, 3}

*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
in the last example, kept shifting last number to the left until it was
at the beginning of the list then repeated
*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***

https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/

In mathematics, permutation is the act of arranging the members of a set into a
sequence or order, or, if the set is already ordered, rearranging (reordering)
its elements—a process called permuting.

https://www.andlearning.org/permutation-combination-formulas/
https://en.wikipedia.org/wiki/Permutation
"""

import copy

def permutation(lst):
    """
    Return a list of permutations

    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]

    Args:
      lst(list): list of items to be permuted

    Returns:
      list of permutation with each permuted item being represented by a list

    ----------------------------------------------------------------------------
    The idea is to one by one extract all elements, place them at first position
    and recur for remaining list.
    ----------------------------------------------------------------------------
    """
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then only one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]

       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]

       # Generating all permutations where m is first element
       for p in permutation(remLst):
           l.append([m] + p)
    return l

# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e

print ("Pass" if  (check_output(permutation([]), [])) else "Fail")
print ("Pass" if  (check_output(permutation([0]), [[0]])) else "Fail")
print ("Pass" if  (check_output(permutation([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print ("Pass" if  (check_output(permutation([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")


# -----------------------------------------------------------------------------
# UDACITY Solution
def permute(l):
    """
    Return a list of permutations

    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]

    Args:
      l(list): list of items to be permuted

    Returns:
      list of permutation with each permuted item be represented by a list
    """
    perm = []
    if len(l) == 0:
        perm.append([])
    else:
        first_element = l[0]
        after_first = slice(1, None)
        sub_permutes = permute(l[after_first])
        for p in sub_permutes:
            for j in range(0, len(p) + 1):
                r = copy.deepcopy(p)
                r.insert(j, first_element)
                perm.append(r)
    return perm
# -----------------------------------------------------------------------------

# Python program to print all permutations with
# duplicates allowed

def toString(List):
    return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.

def permute(a, l, r):
    if l==r:
        print(toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack

# Driver program to test the above function
print("\nPermuting a string using backtrack")
print("Reference: https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/")
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)

# -----------------------------------------------------------------------------
# UDACITY Solution
# Solution
def permutations(string):
    return return_permutations(string, 0)

def return_permutations(string, index):
    # Base Case
    if index >= len(string):
        return [""]

    small_output = return_permutations(string, index + 1)

    output = list()
    current_char = string[index]

    # iterate over each permutation string received thus far
    # and place the current character at between different indices of the string
    for permutation in small_output:
        for index in range(len(small_output[0]) + 1):
            new_permutation = permutation[0: index] + current_char + permutation[index:]
            output.append(new_permutation)
    return output
# -----------------------------------------------------------------------------
