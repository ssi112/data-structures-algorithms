"""
priority_queue_test02.py

some tests for priority_queue.py

TESTING 1, 2, 3
see https://repl.it/@ssi112/PriorityQueue for similar testing

"""
import sys
from priority_queue import *


# ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

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


def create_priority_queue(frequencies):
    priority_queue = PriorityQueue()
    # create a leaf node for each letter
    for inx, (letter, frequency) in enumerate(frequencies):
        # add it to the queue
        priority_queue.enqueue(letter, frequency)
    """ TEST THIS LATER
    while priority_queue.qsize() > 1:
        # get the two highest nodes
        left, right = priority_queue.get(), priority_queue.get()
        print("left - left[1]", left, left[1])
        print("right - right[1]", right, right[1])
        # add the two nodes to the tree
        node = huffman_node(left, right)
        # add the new node to the queue
        priority_queue.put(((left[1] + right[1]), node))
    """
    return priority_queue


sentence = "The bird is the word"

print("~"*sys.getsizeof(sentence))
print ("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
print ("The content of the data is: '{}'\n".format(sentence))

frequencies = frequency_count(sentence)

print("\nindex letter frequency")
print("------------------------")
for inx, (letter, frequency) in enumerate(frequencies):
    #print("  {0:02d}    '{1}'      {2:6.3f}".format(inx, frequency, letter))
    print("  {0:02d}    '{1}'      {2:6.3f}".format(inx, letter, frequency))

pq = create_priority_queue(frequencies)

print()
print("Is queue empty?", pq.isEmpty())
print("What is the size of queue?", pq.size())
hpi = pq.front()
print("Highest priority item is {} at priority {}".format( hpi.element, hpi.priority) )

print()
print("\n.....current priority queue.....")
print(pq)

print("\n...about to remove highest priority item...")
hpi = pq.dequeue()
print("Removed highest priority item {} at priority {}".format( hpi.element, hpi.priority))

print()
print("What is the size of queue?", pq.size())
print("\n.....current priority queue.....")
print(pq)

