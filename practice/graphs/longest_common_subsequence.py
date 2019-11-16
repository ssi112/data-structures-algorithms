"""
longest_common_subsequence.py

Dynamic Programming
Breaking a larger problem into a smaller set of subproblems, and
building up a complete result without having to repeat any subproblems.

The Matrix Rules
You can efficiently fill up this matrix one cell at a time.
Each grid cell only depends on the values in the grid cells
that are directly on top and to the left of it, or on the
diagonal/top-left. The rules are as follows:

    Start with a matrix that has one extra row and column of zeros.
    As you traverse your string:

        If there is a match, fill that grid cell with the value to the
        top-left of that cell plus one.

        If there is not a match, take the maximum value from either
        directly to the left or the top cell, and carry that value over
        to the non-match cell.

    After completely filling the matrix, the bottom-right cell will
    hold the non-normalized LCS value.

Reference longest_common_subsequence.odt for complete explanation
"""

def lcs(string_a, string_b):
    lookup_table = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]

    string_a = string_a.lower()
    string_b = string_b.lower()
    space = ' '

    for char_a_i, char_a in enumerate(string_a):
        for char_b_i, char_b in enumerate(string_b):
            if char_a == char_b:
                if char_a is not space:
                    lookup_table[char_a_i + 1][char_b_i + 1] = lookup_table[char_a_i][char_b_i] + 1
            else:
                lookup_table[char_a_i + 1][char_b_i + 1] = max(
                    lookup_table[char_a_i][char_b_i + 1],
                    lookup_table[char_a_i + 1][char_b_i])

    return lookup_table[-1][-1]


## >>>>> Test <<<<<
test_A1 = "WHO WEEKLY"
test_B1 = "HOW ONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATS IN SPACE TWO"
test_B2 = "DOGS PACE WHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 =', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 =', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')

test_A2 = "An apple a day keeps the doctor away"
test_B2 = "Never compare an apple to an orange"

lcs_val2 = lcs(test_A2, test_B2)
print('LCS val 2 =', lcs_val2)
print("string A2: {}, length: {:d}, {:05.3f}%".format(test_A2, len(test_A2), lcs_val2 / len(test_A2)))
print("string B2: {}, length: {:d}, {:05.3f}%".format(test_B2, len(test_B2), lcs_val2 / len(test_A2)))


