"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import time

texts = list()
calls = list()

"""
Read file into texts and calls.
"""
def readTexts():
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f, delimiter='\n')
        for line in reader:
            texts.append(line)


def readCalls():
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f, delimiter='\n')
        for line in reader:
            calls.append(line)



"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

