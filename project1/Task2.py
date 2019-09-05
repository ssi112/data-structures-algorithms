"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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

def LongestCall():
    """
        breaks out the call list and finds the call with the
        longest duration
    """
    call_duration = 0
    receiving_tele_number = ''
    calling_tele_number = ''

    for callDetail in calls:
        for call in callDetail:
            callSplit = call.split(',')
            if int(callSplit[3]) > call_duration:
                call_duration = int(callSplit[3])
                receiving_tele_number = callSplit[1]
                calling_tele_number = callSplit[0]
    return call_duration, receiving_tele_number, calling_tele_number

def main():
    """
    TASK 2: Which telephone number spent the longest time on the phone
    during the period? Don't forget that time spent answering a call is
    also time spent on the phone.
    Print a message:
    "<telephone number> spent the longest time, <total time> seconds, on the phone during
    September 2016.".
    """
    readCalls()

    time_start = time.process_time()

    longest_call = ()
    longest_call = LongestCall()

    print("\n{} spent the longest time, {} seconds, on the phone during September 2016."
        .format(longest_call[1], longest_call[0] ))

    elapsed_time = time.process_time() - time_start
    #print("\nElapsed time {:4.8f}".format(elapsed_time))


if __name__ == '__main__':
    main()

