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


def single_longest_call():
    """
        breaks out the call list and finds the one call with the
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


def longest_time_on_phone(tele_call_total):
    call_duration = 0
    tele_number_max = ''
    for tele_number, total_duration in tele_call_total.items():
        if total_duration > call_duration:
            call_duration = total_duration
            tele_number_max = tele_number
    # print(tele_number_max, call_duration)
    return tele_number_max, call_duration


def sum_call_times():
    """
        builds a dictionary of telephone numbers as key and
        total call duration as value
        tele_call_total = {'tele_number': total_duration}
    """
    tele_call_total = dict()

    for callDetail in calls:
        for call in callDetail:
            callSplit = call.split(',')
            # add new item to dict if calling # does not exist
            if callSplit[0] not in tele_call_total:
                tele_call_total[callSplit[0]] = int(callSplit[3])
            # otherwise sum the duration
            else:
                tele_call_total[callSplit[0]] += int(callSplit[3])

            # add new item to dict if receiving # does not exist
            if callSplit[1] not in tele_call_total:
                tele_call_total[callSplit[1]] = int(callSplit[3])
            else:
                tele_call_total[callSplit[1]] += int(callSplit[3])
    # find number with longest calling duration
    return longest_time_on_phone(tele_call_total)


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

    """
    # NOT USED - misunderstood requirements
    longest_call = ()
    longest_call = single_longest_call()

    print("\n{} spent the single longest time, {:,} seconds, on the phone during September 2016."
        .format(longest_call[1], longest_call[0] ))
    """

    time_start = time.process_time()

    most_time = ()
    most_time = sum_call_times()

    print("\n{} spent the longest time, {:,} seconds, on the phone during September 2016."
        .format(most_time[0], most_time[1] ))

    elapsed_time = time.process_time() - time_start
    # print("\nElapsed time {:4.8f}".format(elapsed_time))

    #print(single_longest_call())


if __name__ == '__main__':
    main()

