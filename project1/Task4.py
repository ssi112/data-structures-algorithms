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
import csv
import time

# raw data read from files
texts = list()
calls = list()

# sets of calling and texting numbers
receivingCallNumber = set()
sendingTxtNumber = set()
receivingTxtNumber = set()

# combines the three sets into one list
allNumbersToCheck = list()

# list of calling numbers
callingList = list()

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


def buildSets():
    global receivingCallNumber
    global sendingTxtNumber
    global receivingTxtNumber
    global allNumbersToCheck

    for callDetail in calls:
        # receiving tele number
        receivingCallNumber.add( str(callDetail[1]) )
    for textDetail in texts:
        # sending text tele number
        sendingTxtNumber.add( str(textDetail[0]) )
        # receiving text tele number
        receivingTxtNumber.add( str(textDetail[1]) )
    # make one unique list of numbers to check
    x = receivingCallNumber.union(sendingTxtNumber)
    y = x.union(receivingTxtNumber)
    allNumbersToCheck = sorted(y)
    # print("len of allNumbersToCheck =", len(allNumbersToCheck))


def uniqueCallNumbers():
    """
        appends unique calling telephone numbers to
        a set using the add method then
        converts the unique numbers to a list
    """
    global callingList
    unique = set()
    for callDetail in calls:
        # calling tele number
        unique.add( str(callDetail[0]) )
    callingList = sorted(unique)
    return


# Cannot iterate over a list and update it in place
# indexes change after an item is removed - DOH!!!
# https://stackoverflow.com/questions/52941953/python-delete-from-list-while-iterating
def outGoingCallsOnly():
    global allNumbersToCheck

    outgoingNumbers = list()

    for callingNumber in callingList:
        if callingNumber not in allNumbersToCheck:
            outgoingNumbers.append(callingNumber)
    # print("length of outgoingNumbers =", len(outgoingNumbers))
    return outgoingNumbers

def main():
    """
        unique list of calling tele numbers
            not in receiving call list
            not in sending text list
            not in receiving text list
    """
    readTexts()
    readCalls()

    buildSets()

    print("="*55)
    print("receivingCallNumber len: ", len(receivingCallNumber))
    #for val in sorted(receivingCallNumber):
    #    print(val)

    print("="*55)
    print("sendingTxtNumber len: ", len(sendingTxtNumber))
    #for val in sorted(sendingTxtNumber):
    #    print(val)

    print("="*55)
    print("receivingTxtNumber len: ", len(receivingTxtNumber))
    #for val in sorted(receivingTxtNumber):
    #    print(val)

    # creates list of numbers making outgoing calls
    uniqueCallNumbers()
    print("="*55)
    print("callingList len: ", len(callingList))

    outgoingNumbers = outGoingCallsOnly()
    print("outgoingNumbers len (after): ", len(outgoingNumbers))
    print("\nThese numbers could be telemarketers: ")
    for val in outgoingNumbers:
        print(val)
    return 0


if __name__ == '__main__':
    main()
