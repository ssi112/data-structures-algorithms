"""
huffman.py
"""

import sys

sentence = "The bird is the word"

def frequency_count(sentence):
    char_freq = {}
    for char in sentence:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return sorted(char_freq.items(), key=lambda x: x[1])

print("~"*sys.getsizeof(sentence))
print ("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
print ("The content of the data is: '{}'\n".format(sentence))

listofTuples = frequency_count(sentence)

# listofTuples = sorted(fq.items() ,  key=lambda x: x[1])

print(listofTuples)

"""
for elem in listofTuples:
    print(elem[0], " :: ", elem[1])
"""

print("\nindex letter frequency")
print("------------------------")
for i, (letter, frequency) in enumerate(listofTuples):
    print("  {0:02d}    '{1}'      {2}".format(i, letter, frequency))

