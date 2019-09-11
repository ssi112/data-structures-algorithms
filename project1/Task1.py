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
    global texts
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)


def readCalls():
    global calls
    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)


def uniqueListTest():
    """
        appends unique telephone numbers to list using an
        if not in logic

        returns the count of unique numbers
    """
    uniqueTeleNumbers = []
    # calls
    for callDetail in calls:
        # calling tele number
        if callDetail[0] not in uniqueTeleNumbers:
            uniqueTeleNumbers.append(callDetail[0])
        # receiving tele number
        if callDetail[1] not in uniqueTeleNumbers:
            uniqueTeleNumbers.append(callDetail[1])
    # texts
    for textDetail in texts:
        # sending text tele number
        if textDetail[0] not in uniqueTeleNumbers:
            uniqueTeleNumbers.append(textDetail[0])
        # receiving text tele number
        if textDetail[1] not in uniqueTeleNumbers:
            uniqueTeleNumbers.append(textDetail[1])
    return len(uniqueTeleNumbers)


def uniqueSetTest():
    """
        appends unique telephone numbers to list using
        a set and the add method

        returns the count of unique numbers
    """
    unique = set()
    for callDetail in calls:
        # calling tele number
        unique.add(callDetail[0])
        # receiving tele number
        unique.add(callDetail[1])
    for textDetail in texts:
        # sending text tele number
        unique.add(textDetail[0])
        # receiving text tele number
        unique.add(textDetail[1])
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

    time_start = time.process_time()
    print("There are {} different telephone numbers in the records.".format(uniqueSetTest()))
    set_elapsed_time = time.process_time() - time_start


if __name__ == '__main__':
    main()
