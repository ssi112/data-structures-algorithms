
###### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
# Given your birthday and the current date, calculate your age in days.
# Compensate for lead days. Assume that the birthday and current date
# are correct dates and there is no time travle involved. Simply put,
# if you were bon 1 Jan 2012 and todays date is 2 Jan 2012 you are 1 day old.
###### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####

daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months = ["January", "February", "March", "April", "May",
"June", "July", "August", "September", "October", "November", "December"]

def isLeapYear(year):
    # returns True or False
    # https://en.wikipedia.org/wiki/Leap_year#Algorithm
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


# helpf functions
def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonths[month - 1]:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1, month1, and day1 is before
        year2, month2 and day2. Otherwise returns False
    """
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    # YOUR CODE HERE!
    days = 0
    leapYearCounted = False

    assert not dateIsBefore(year2, month2, day2, year1, month1, day1) == True

    # original code to test 1st date is less than 2nd
    # while ((year1 != year2) or (month1 != month2) or (day1 != day2)):

    # new code using helper function to test
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
        if (isLeapYear(year1) and month1 == 2):
            if not leapYearCounted:
                days += 1
                leapYearCounted = True
        else:
            leapYearCounted = False
    # print(year1, month1, day1)
    # print(days)
    return days


def testDaysBetweenDates():
    # test same day
    assert(daysBetweenDates(2017, 12, 30, 2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30,  2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30,  2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29, 2013, 6, 29)  == 365)
    # Second date must be equal to or occur after first date
    assert(daysBetweenDates(2012, 12, 8, 2012, 12, 7)  == Undefined)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")

# testDaysBetweenDates()

def test():
    test_cases = [((2012,9,30, 2012,10,30) ,30),
                  ((2012,1,1, 2013,1,1) ,366),
                  ((2012,9,1, 2012,9,4) ,3),
                  ((2013,1,1, 1999,12,31), "AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result == answer and answer != "AssertionError":
                print( "Test case passed!" )
            else:
                print( "Test with data:", args, "failed" )

        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args) )
            else:
                print( "Check your work! Test case {0} should not raise AssertionError!\n".format(args) )


def main():
    # print(isLeapYear(1932)) # true
    # print(isLeapYear(2012)) # true
    # print(isLeapYear(2100)) # false
    # print(isLeapYear(2064)) # true
    print( daysBetweenDates(2013,1,24, 2013,6,29) )
    print( daysBetweenDates(1912,12,12, 2012,12,12) )
    # print( daysBetweenDates(2013,1,24, 2012,12,20) )
    test()

if __name__ == '__main__':
    main()

