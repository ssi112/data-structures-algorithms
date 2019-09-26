"""
tower_of_hanoi.py

Problem Statement

The Tower of Hanoi is a puzzle where we have three rods and n disks. The three rods are:

    1. source
    2. destination
    3. auxiliary

Initally, all the n disks are present on the source rod. The final objective of the puzzle is
to move all disks from the source rod to the destination rod using the auxiliary rod.
However, there are some rules according to which this has to be done:

    1. Only one disk can be moved at a time.
    2. A disk can be moved only if it is on the top of a rod.
    3. No disk can be placed on the top of a smaller disk.

You will be given the number of disks num_disks as the input parameter.

For example, if you have num_disks = 3, then the disks should be moved as follows:

    1. move disk from source to auxiliary
    2. move disk from source to destination
    3. move disk from auxiliary to destination

You must print these steps as follows:

    S A
    S D
    A D

Where S = source, D = destination, A = auxiliary


Wikipedia has nice animation showing the solution:
https://en.wikipedia.org/wiki/Tower_of_Hanoi

Also, the friendly geeks describe an algorithm too:
https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

"""

def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination
    """
    move(num_disks, 'S', 'D', 'A')

def move(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    move(n-  1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod", from_rod, "to rod", to_rod)
    move(n - 1, aux_rod, to_rod, from_rod)

# Driver code
n = 4
tower_of_Hanoi(n)
