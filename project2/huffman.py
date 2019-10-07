"""
huffman.py

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

sentence = "The bird is the word"


class huffman_node(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def get_children(self):
        return((self.left, self.right))

    def __lt__(self, other):
        return self.node < other.node

    def __eq__(self, other):
        return self.node == other.node

    def __gt__(self, other):
        return self.node > other.node


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
    list_of_tuples = [(key, value) for key, value in char_count.items()]
    # sort the list by the letter x[1] then return it
    return list_of_tuples
    #return sorted(list_of_tuples, key = lambda x: x[1])


ALTERNATE SOLUTION THAT MAY WORK
5 USES A DICTIONARY
https://stackoverflow.com/questions/11587044/how-can-i-create-a-tree-for-huffman-encoding-and-decoding

MAYBE => https://gist.github.com/quakehead/58553

https://gist.github.com/socksy/d652e24286ad43471461

https://gist.github.com/matthewlevy97/2d7a0ce3f8f2466bb7355d2a02cbeed8

https://gist.github.com/zjor/5218818

def create_huffman_tree(frequencies):
    priority_queue = queue.PriorityQueue()
    # create a leaf node for each letter
    for value in frequencies:
    # for inx, (letter, frequency) in enumerate(frequencies):
        # add it to the queue
        priority_queue.put(value)
        #priority_queue.put((inx, frequency, letter))
        # print("value", value)
    while priority_queue.qsize() > 1:
        # get the two highest nodes
        left, right = priority_queue.get(), priority_queue.get()
        print("left - left[1]", left, left[1])
        print("right - right[1]", right, right[1])
        # add the two nodes to the tree
        node = huffman_node(left, right)
        # add the new node to the queue
        priority_queue.put(((left[1] + right[1]), node))
    # return the root node of the tree
    return priority_queue.get()


# assigning a code value to each symbol
def walk_tree(node, prefix="", code={}):
    if isinstance(node[1].left[1], huffman_node):
        walk_tree(node[1].left,prefix+"0", code)
    else:
        code[node[1].left[1]]=prefix+"0"
    if isinstance(node[1].right[1],huffman_node):
        walk_tree(node[1].right,prefix+"1", code)
    else:
        code[node[1].right[1]]=prefix+"1"
    return(code)


print("~"*sys.getsizeof(sentence))
print ("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
print ("The content of the data is: '{}'\n".format(sentence))

frequencies = frequency_count(sentence)

print("\nindex letter frequency")
print("------------------------")
for inx, (letter, frequency) in enumerate(frequencies):
    #print("  {0:02d}    '{1}'      {2:6.3f}".format(inx, frequency, letter))
    print("  {0:02d}    '{1}'      {2:6.3f}".format(inx, letter, frequency))

print(frequencies)

"""
"""
tree = create_huffman_tree(frequencies)

"""
code = walk_tree(tree)
for i in sorted(frequencies, reverse=True):
    print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])
"""
