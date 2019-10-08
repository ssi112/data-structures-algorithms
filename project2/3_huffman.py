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

https://stackoverflow.com/questions/11587044/how-can-i-create-a-tree-for-huffman-encoding-and-decoding

"""

import sys
# from priority_queue import *
import queue

class Huffman_Node(object):
    def __init__(self, left = None, right = None, node = None):
        self.left = left
        self.right = right
        self.node = node

    def __lt__(self, other):
        return 0

    def set_element_frequency(self, element, frequency):
        self.element = element
        self.frequency = frequency

    def get_element_frequency(self):
        return ((self.inx, self.element, self.frequency))

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None


# ################################# ################################# ###### #
# MIGHT WANT TO REVISE SOME OF THIS
# https://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree
# See 9 Simple implementation of BST in Python
#
#       eliminate calling add then calling _add
#       can do it once with recursion
#       same with print
# ################################# ################################# ###### #
class Huffman_Tree(object):
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, inx, element, frequency):
        if self.root == None:
            self.root = Huffman_Node(None, None, inx, element, frequency)
            #print("add root", None, None, inx, element, frequency)
        else:
            self._add(inx, element, frequency, self.root)

    def _add(self, inx, element, frequency, node):
        if(inx < node.inx):
            if(node.left != None):
                self._add(inx, element, frequency, node.left)
                #print("add node.left", None, None, inx, element, frequency)
            else:
                node.left = Huffman_Node(None, None, inx, element, frequency)
        else:
            if(node.right != None):
                self._add(inx, element, frequency, node.right)
                #print("add node.right", None, None, inx, element, frequency)
            else:
                node.right = Huffman_Node(None, None, inx, element, frequency)

    def print_tree(self):
        if(self.root != None):
            self._print_tree(self.root)

    def _print_tree(self, node):
        if(node != None):
            self._print_tree(node.left)
            print(node.get_element_frequency())
            self._print_tree(node.right)

    def printInorder(self, node):
        if(node != None):
            self.printInorder(node.left)
            print(node.get_element_frequency())
            self.printInorder(node.right)


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
        # add it to the queue
        priority_queue.put(value)

    while priority_queue.qsize() > 1:
        # get the two highest priority items
        hp1 = priority_queue.get() # left
        hp2 = priority_queue.get() # right
        node = Huffman_Node(hp1, hp2)

        print("hp1[0] - hp1[1]", hp1[0], hp1[1])
        print("hp2[0] - hp2[1]", hp2[0], hp2[1])
        print(hp1[0] + hp2[0])
        priority_queue.put( (hp1[0] + hp2[0], node) )
        # print(hp1, hp2)


        # tree.add(0, hp1.element+hp2.element, hp1.priority+hp2.priority)
        # tree.add(0, hp2.element, hp2.priority)
        # add new priority, new element  to the queue
    return priority_queue.get()


sentence = "The bird is the word"

print("~"*sys.getsizeof(sentence))
print ("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
print ("The content of the data is: '{}'\n".format(sentence))

frequencies = frequency_count(sentence)

print(frequencies)

print("\nindex frequency letter")
print("------------------------")
for inx, (frequency, letter) in enumerate(frequencies):
    print("  {0:02d}    {1:6.3f}      '{2}'".format(inx, frequency, letter))


"""
"""

node = create_huffman_tree(frequencies)

print("\n...node...")
print(node)
print("\n")

print("#"*55)
tree.printInorder(tree.get_root())
print("#"*55)
# tree.print_tree()


"""
code = walk_tree(tree)
for i in sorted(frequencies, reverse=True):
    print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])
"""
