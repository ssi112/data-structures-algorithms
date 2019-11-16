"""
knapsack.py

Code Below:
https://codereview.stackexchange.com/questions/20569/dynamic-programming-knapsack-solution

Also Reference:
https://rosettacode.org/wiki/Knapsack_Problem/Python
"""

import sys

def knapsack(items, maxweight):
    # Create an (N+1) by (W+1) 2-d list to contain the running values
    # which are to be filled by the dynamic programming routine.
    #
    # There are N+1 rows because we need to account for the possibility
    # of choosing from 0 up to and including N possible items.
    # There are W+1 columns because we need to account for possible
    # "running capacities" from 0 up to and including the maximum weight W.
    bestvalues = [[0] * (maxweight + 1)
                  for i in range(len(items) + 1)]

    # Enumerate through the items and fill in the best-value table
    for i, (value, weight) in enumerate(items):
        # Increment i, because the first row (0) is the case where no items
        # are chosen, and is already initialized as 0, so we're skipping it
        i += 1
        for capacity in range(maxweight + 1):
            # Handle the case where the weight of the current item is greater
            # than the "running capacity" - we can't add it to the knapsack
            if weight > capacity:
                bestvalues[i][capacity] = bestvalues[i - 1][capacity]
            else:
                # Otherwise, we must choose between two possible candidate values:
                # 1) the value of "running capacity" as it stands with the last item
                #    that was computed; if this is larger, then we skip the current item
                # 2) the value of the current item plus the value of a previously computed
                #    set of items, constrained by the amount of capacity that would be left
                #    in the knapsack (running capacity - item's weight)
                candidate1 = bestvalues[i - 1][capacity]
                candidate2 = bestvalues[i - 1][capacity - weight] + value

                # Just take the maximum of the two candidates; by doing this, we are
                # in effect "setting in stone" the best value so far for a particular
                # prefix of the items, and for a particular "prefix" of knapsack capacities
                bestvalues[i][capacity] = max(candidate1, candidate2)

    # Reconstruction
    # Iterate through the values table, and check
    # to see which of the two candidates were chosen. We can do this by simply
    # checking if the value is the same as the value of the previous row. If so, then
    # we say that the item was not included in the knapsack (this is how we arbitrarily
    # break ties) and simply move the pointer to the previous row. Otherwise, we add
    # the item to the reconstruction list and subtract the item's weight from the
    # remaining capacity of the knapsack. Once we reach row 0, we're done
    reconstruction = []
    N = len(items)
    W = maxweight
    while N > 0:
        # bestvalues[N][W] is the best sum of values for any
        # subsequence of the first N items, whose weights sum
        # to no more than W.
        if bestvalues[N][W] != bestvalues[N - 1][W]:
            reconstruction.append(items[N - 1])
            W -= items[N - 1][1]
        N -= 1

    # Reverse the reconstruction list, so that it is presented
    # in the order that it was given
    reconstruction.reverse()

    # Return the best value, and the reconstruction list
    return bestvalues[len(items)][maxweight], reconstruction

"""
>>>>>   O R I G I N A L   C O D E   <<<<<
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: knapsack.py [file]')
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    maxweight = int(lines[0])
    items = [map(int, line.split()) for line in lines[1:]]

    bestvalue, reconstruction = knapsack(items, maxweight)

    print('Best possible value: {0}'.format(bestvalue))
    print('Items:')
    for value, weight in reconstruction:
        print('V: {0}, W: {1}'.format(value, weight))
"""


"""
# Some test values
# items [value, weight]
maxweight = 165
items = [
            [92, 23],
            [57, 31],
            [49, 29],
            [68, 44],
            [60, 53],
            [43, 38],
            [67, 63],
            [84, 85],
            [87, 89],
            [72, 82]
        ]

maxweight = 15
items = [ [7,10], [8,9], [6,5] ]
"""

maxweight = 25
items = [ [2,10], [10,29], [7,5], [3,5], [1,5], [12,24] ]

bestvalue, reconstruction = knapsack(items, maxweight)

print('Best possible value: {0}'.format(bestvalue))
print('Items:')
for value, weight in reconstruction:
    print('V: {0}, W: {1}'.format(value, weight))


