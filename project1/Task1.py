"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import time

texts = list()
calls = list()

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


def uniqueListTest():
    """
        appends unique telephone numbers to list using an
        if not in logic

        returns the count of unique numbers
    """
    uniqueTeleNumbers = []
    # calls
    for callDetail in calls:
        for call in callDetail:
            callSplit = call.split(',')
            # calling tele number
            if callSplit[0] not in uniqueTeleNumbers:
                uniqueTeleNumbers.append(callSplit[0])
            # receiving tele number
            if callSplit[1] not in uniqueTeleNumbers:
                uniqueTeleNumbers.append(callSplit[1])
    # texts
    for textDetail in texts:
        for text in textDetail:
            textSplit = text.split(',')
            # sending text tele number
            if textSplit[0] not in uniqueTeleNumbers:
                uniqueTeleNumbers.append(textSplit[0])
            # receiving text tele number
            if textSplit[1] not in uniqueTeleNumbers:
                uniqueTeleNumbers.append(textSplit[1])
    return len(uniqueTeleNumbers)


def uniqueSetTest():
    """
        appends unique telephone numbers to list using
        a set and the add method

        returns the count of unique numbers
    """
    unique = set()
    for callDetail in calls:
        for call in callDetail:
            callSplit = call.split(',')
            # calling tele number
            unique.add(callSplit[0])
            # receiving tele number
            unique.add(callSplit[1])
    for textDetail in texts:
        for text in textDetail:
            textSplit = text.split(',')
            # sending text tele number
            unique.add(textSplit[0])
            # receiving text tele number
            unique.add(textSplit[1])
    return len(unique)


def main():
    """
    TASK 1:
    How many different telephone numbers are there in the records?
    Print a message:
    "There are <count> different telephone numbers in the records."
    """
    readTexts()
    readCalls()

    # info on process time
    # https://docs.python.org/3/library/time.html#time.process_time
    time_start = time.process_time()
    print("LIST:There are {} different telephone numbers in the records.".format(uniqueListTest()))
    list_elapsed_time = time.process_time() - time_start
    print("Elapsed time {:4.8f}".format(list_elapsed_time))

    # try using a python set
    # yields the same results as using the if not in statement
    # which is faster ???
    time_start = time.process_time()
    print("SET:There are {} different telephone numbers in the records.".format(uniqueSetTest()))
    set_elapsed_time = time.process_time() - time_start
    print("Elapsed time {:4.8f}".format(set_elapsed_time))

    if list_elapsed_time > set_elapsed_time:
        print("It took the list method {:4.8f} seconds longer.".format(list_elapsed_time - set_elapsed_time))
    else:
        print("It took the set method {:4.8f} seconds longer.".format(set_elapsed_time - list_elapsed_time))

if __name__ == '__main__':
    main()
