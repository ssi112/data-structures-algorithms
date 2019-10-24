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

    NOTE
    display and _display_aux methods borrowed to provide a visual representation of tree
    https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
"""

import sys
import queue

class Huffman_Node(object):
    def __init__(self, left = None, right = None, frequency = None, element = None):
        self.left = left
        self.right = right
        self.frequency = frequency
        self.element = element

    def get_element_frequency(self):
        return (self.frequency, self.element)

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __str__(self): # printable representation
        return f"Node({self.get_element_frequency()})"

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

### # ### # ### # ### # ### # ### # ### # ### # ### # ### # ### # ### # ### # ### # ###
#                       NOT needed - can be ignored
    def _display_aux(self):
        """
        Returns list of strings, width, height, and horizontal coordinate of the root.
        """
        # No child.
        if self.right is None and self.left is None:
            line = '%s %s' % self.get_element_frequency() # self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s %s' % self.get_element_frequency() # self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s %s' % self.get_element_frequency() # self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s %s' % self.get_element_frequency() # self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
### # ### # ### # ### # ### # ### # ### # ### # ### # ### # ### # ### # ### # ### # ###

def frequency_count(sentence):
    """
    counts the occurrence of each letter in sentence
    calculates a relative frequency for each letter
    convert it to a sorted list of tuples [(frequency, letter)]
    returns False if var passed is not a string
    """
    char_count = {}
    if not isinstance(sentence, str):
        return False

    # create the counts for each letter
    for char in sentence:
        """
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        """
        if char_count.get(char):
            char_count[char] += 1
        else:
            char_count[char] = 1
    # convert to a list of tuples
    list_of_tuples = [(value, key) for key, value in char_count.items()]
    return list_of_tuples


def create_huffman_tree(frequencies):
    # check and return False if not valid input
    try:
        if not frequencies:
            msg  = "\nError: There is nothing to encode!"
            msg += "\nCheck your input and try again.\n"
            raise ValueError(msg)
    except ValueError as ve:
        print(ve)
        return False

    priority_queue = queue.PriorityQueue()

    if len(frequencies) == 1:
        # make a fake root node
        # left = None, right = None, frequency = None, element = None
        node = Huffman_Node(None, None, 0, None)
        priority_queue.put(node)

    # create a leaf node for each letter
    for value in frequencies:
        node = Huffman_Node(frequency = value[0], element = value[1])
        priority_queue.put(node)

    while priority_queue.qsize() > 1:
        # get the two highest priority items
        hp1 = priority_queue.get() # left
        hp2 = priority_queue.get() # right
        parent = Huffman_Node(hp1, hp2,  hp1.frequency + hp2.frequency)
        priority_queue.put(parent)

    tree = priority_queue.get()
    del priority_queue
    return tree


def encode_string(node, encoding_string = None, codes = None):
    """
    store the codes in a string
    left branch is 0, right branch is 1
    return False if tree (node) does not exist
    """
    if not node:
        return False

    if codes is None:
        codes = {}
    if encoding_string is None:
        encoding_string = ""
    if node.element:
        codes[node.element] = encoding_string
        #print("encode_string: encoding_string =>", encoding_string)
        #print("encode_string: node.element =>", node.element)
        # return
    encode_string(node.left, encoding_string + "0", codes)
    encode_string(node.right, encoding_string + "1", codes)
    return codes


def encode(codes, sentence):
    """
    join the codes together into one string
    """
    try:
        if not codes:
            msg  = "\nNo data available for encoding.\nDid you send a valid string?"
            raise ValueError(msg)
    except ValueError as ve:
        print(ve)
        return False

    output = "".join([codes[letter] for letter in sentence])
    return output


def decode_string(root, encoded_string):
    """
    Set current node to tree
    Set empty message variable
    Iterate through each char in data
    If the current_node is a leaf, concatenate char with message
    If current_node is not a leaf, traverse left or right depending on data
        if letter is 0 move left
        if letter is 1 move right
    Return message
    """
    try:
        if not root or not encoded_string:
            msg  = "\nERROR! Nothing to decode!"
            msg += "\nPlease check your data and try again!"
            raise ValueError(msg)
    except ValueError as ve:
        print(ve)
        return False

    node = root
    output = ""
    for char in encoded_string:
        if (node.left is None and node.right is None):
            # found a character (leaf) - add to output
            # then restart for next character
            output += node.element
            node = root;
        if char == '0':
            node = node.left
        else:
            node = node.right
    # capture final node element
    output += node.element
    return output


def test_case(some_string):
    print("\n>>>>> TEST <<<<<")
    print("~"*sys.getsizeof(some_string))
    print ("The size of the data is: {}".format(sys.getsizeof(some_string)))
    print ("The content of the data is: '{}'".format(some_string))

    # ----------------------------------------------------------------------- #
    # 1) set the frequency counts
    frequencies = frequency_count(some_string)
    print("\n-----frequencies-----")
    print("frequencies =>", frequencies)

    # ----------------------------------------------------------------------- #
    # 2) create the huffman tree
    tree = create_huffman_tree(frequencies)

    """
    # print if desired - can take up a lot of screen real estate
    if tree:
        print("\n...tree...")
        tree.display()
    """

    # ----------------------------------------------------------------------- #
    # 3) create a character to binary code mapping
    codes = {}
    codes = encode_string(tree, "", codes)
    print("\n-----codes-----")
    print(codes)

    # ----------------------------------------------------------------------- #
    # 4) create the encoded message
    encoded_string = encode(codes, some_string)
    print("\n-----encoded message-----")
    print(encoded_string)
    print("\n-----decoded_sentence-----")
    print(decode_string(tree, encoded_string))


def main():
    sentence = "The bird is the word."
    test_case(sentence)

    # will just return Falses on an empty string
    sentence = ""
    test_case(sentence)

    sentence = "A"
    test_case(sentence)

    sentence = "AAA"
    test_case(sentence)


if __name__ == "__main__":
    main()
