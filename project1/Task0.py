"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
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


def main():
    """
    TASK 0:
    What is the first record of texts and what is the last record of calls?
    Print messages:
    "First record of texts, <incoming number> texts <answering number> at time <time>"
    "Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
    """
    readTexts()
    readCalls()
    # print("length of texts is {}".format(len(texts)))
    # print("length of calls is {}".format(len(calls)))

    textSplit = []
    callsSplit = []

    textSplit = texts[0][0].split(',') # split first line of texts
    callsSplit = calls[len(calls)-1][0].split(',') # split last line of calls

    # print(textSplit)
    # print(callsSplit)

    print("First record of texts, {} texts {} at time {}".format(textSplit[0], textSplit[1], textSplit[2]))
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(callsSplit[0], callsSplit[1], callsSplit[2], callsSplit[3] ))


if __name__ == '__main__':
    main()
