"""
3_huffman.py

Here is one type of pseudocode for this coding schema:

    1) Take a string and determine the relevant frequencies of the characters
    2) Build and sort a list of tuples from lowest to highest frequencies
    3) Build the Huffman Tree by assigning a binary code to each letter, using shorter
       codes for the more frequent letters
       (This is the heart of the Huffman algorithm.)
    4) Trim the Huffman Tree (remove the frequencies from the previously built tree)
    5) Encode the text into its compressed form
    6) Decode the text from its compressed form

"""

import sys
import queue

class Huffman_Node(object):
    def __init__(self, left = None, right = None, frequency = None, element = None):
        self.left = left
        self.right = right
        self.frequency = frequency
        self.element = element

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency


def frequency_count(sentence):
    """
    counts the occurrence of each letter in sentence
    calculates a relative frequency for each letter
    convert it to a sorted list of tuples [(frequency, letter)]
    """
    char_count = {}
    # create the counts for each letter
    for char in sentence:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # sum of all values
    sum_a_thon = sum(char_count.values())
    # convert counts to a relative frequency
    list_of_tuples = []
    for key in char_count:
        char_count[key] = round(char_count[key] / sum_a_thon * 100, 3)
    # convert to a list of tuples
    list_of_tuples = [(value, key) for key, value in char_count.items()]
    # sort the list by the letter x[1] then return it
    return list_of_tuples


def create_huffman_tree(frequencies):
    priority_queue = queue.PriorityQueue()

    # create a leaf node for each letter
    for value in frequencies:
        # this does not work
        # node = Huffman_Node(None, None, value[0], value[1])

        # this doesn't work either
        # add it to the queue
        # priority_queue.put(value)
        node = Huffman_Node()
        #priority_queue.put(value, value[0], value[1])
        priority_queue.put(node, value[0], value[1])

    while priority_queue.qsize() > 1:

        # get the two highest priority items
        hp1 = priority_queue.get() # left
        hp2 = priority_queue.get() # right
        print("-----------------FUBAR--------------------------")
        print("hp1[0] - hp1[1]", hp1[0], hp1[1])
        print("hp2[0] - hp2[1]", hp2[0], hp2[1])
        print(hp1[0] + hp2[0])
        print(hp1, hp2)
        print("-----------------FUBAR--------------------------")

        node = Huffman_Node(hp1, hp2, hp1[0] + hp2[0])

        priority_queue.put(node)
    return priority_queue.get()


sentence = "The bird is the word"

print("~"*sys.getsizeof(sentence))
print ("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
print ("The content of the data is: '{}'\n".format(sentence))

frequencies = frequency_count(sentence)

print(frequencies)

"""
print("\nindex frequency letter")
print("------------------------")
for inx, (frequency, letter) in enumerate(frequencies):
    print("  {0:02d}    {1:6.3f}      '{2}'".format(inx, frequency, letter))
"""

node = create_huffman_tree(frequencies)

print("\n...node...")
print(node)
print("\n")

print("#"*55)
tree.printInorder(tree.get_root())
print("#"*55)
# tree.print_tree()

