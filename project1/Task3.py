"""
iterate through the list of calls
check if areaCode "080" is in the list
if "080" then add to new dict if it doesn't already exist in that dict
Results in a dict of all 080 code numbers
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


def calls_area_code(area_code, tele_count_calls):
    """
        builds a dictionary of telephone numbers as key and a list of
        the number of times called from a specific area code plus the
        number or count of times it called to same area code
        tele_count_calls = {'tele_number': [tot_cnt_calls, cnt_calls_080]}

        also, builds a set of the area codes called then finally returns
        the sorted list
    """
    codes_called = set()    # unique list of codes called

    for callDetail in calls:
        if (callDetail[0].find(area_code, 1, 4) != -1):
            # add new item to dict if calling # does not exist
            if callDetail[0] not in tele_count_calls:
                tele_count_calls[callDetail[0]]= [1, 0]
                # is receiving call in same area code
                if (callDetail[1].find(area_code, 1, 4) != -1):
                    tele_count_calls[callDetail[0]][1] = 1
            # otherwise increase the call count
            else:
                tele_count_calls[callDetail[0]][0] += 1
                # is receiving call in same area code
                if (callDetail[1].find(area_code, 1, 4) != -1):
                    tele_count_calls[callDetail[0]][1] += 1
            """
            Fixed-line number - enclosed within brackets so check for opening bracket
            Telemarkets numbers - always start with 140 and area code is also 140
            Mobile number - always start with 9, 8 or 7 and the area code is up to 4 digits.
                We can fetch it directly like num[0:4].
            Then create unique list of area codes called
            """
            check_code = callDetail[1][0:4]
            if check_code[0:3] == "140":  # Telemarketers
                codes_called.add("140")
            if check_code[0] == "(":    # fixed line number
                codes_called.add(check_code[1:4])
            if check_code[0] in ['7','8','9']:
                codes_called.add(check_code[0:4])
            # codes_called.add( callDetail[1][1:4] ) # original method
    return sorted(codes_called)


def main():
    """
    TASK 3:
    (080) is the area code for fixed line telephones in Bangalore.
    Fixed line numbers include parentheses, so Bangalore numbers
    have the form (080)xxxxxxx.)

    Part A: Find all of the area codes and mobile prefixes called by people
    in Bangalore.
     - Fixed lines start with an area code enclosed in brackets. The area
       codes vary in length but always begin with 0.
     - Mobile numbers have no parentheses, but have a space in the middle
       of the number to help readability. The prefix of a mobile number
       is its first four digits, and they always start with 7, 8 or 9.
     - Telemarketers' numbers have no parentheses or space, but they start
       with the area code 140.

    Print the answer as part of a message:
    "The numbers called by people in Bangalore have codes:"
     <list of codes>
    The list of codes should be print out one per line in lexicographic order with no duplicates.

    Part B: What percentage of calls from fixed lines in Bangalore are made
    to fixed lines also in Bangalore? In other words, of all the calls made
    from a number starting with "(080)", what percentage of these calls
    were made to a number also starting with "(080)"?

    Print the answer as a part of a message::
    "<percentage> percent of calls from fixed lines in Bangalore are calls
    to other fixed lines in Bangalore."
    The percentage should have 2 decimal digits
    """
    readCalls()

    time_start = time.process_time()

    tele_count_calls = dict()
    sorted_codes_called = []

    sorted_codes_called = calls_area_code("080", tele_count_calls)

    print("\n")
    print("="*53)
    print("The numbers called by people in Bangalore have codes:")
    for val in sorted_codes_called:
        print(val)
    print("*"*55)
    print("length of sorted_codes_called: {0:05d}".format(len(sorted_codes_called)))

    sum_cnt_calls = 0
    sum_cnt_same_area_code = 0

    for key, value in tele_count_calls.items():
        #print(key, value)
        sum_cnt_calls += value[0]
        sum_cnt_same_area_code += value[1]
    print("\n")
    print("sum_cnt_calls={:,} | sum_cnt_same_area_code={:,}".format(sum_cnt_calls, sum_cnt_same_area_code) )
    print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(sum_cnt_same_area_code / sum_cnt_calls * 100))

    elapsed_time = time.process_time() - time_start
    print("\nElapsed time {:4.8f}".format(elapsed_time))

    return 0


if __name__ == '__main__':
    main()
