
###### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
# Given your birthday and the current date, calculate your age in days.
# Compensate for lead days. Assume that the birthday and current date
# are correct dates and there is no time travle involved. Simply put,
# if you were bon 1 Jan 2012 and todays date is 2 Jan 2012 you are 1 day old.
###### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = ["January", "February", "March", "April", "May",
"June", "July", "August", "September", "October", "November", "December"]

def isLeapYear(year):
    # returns True or False
    # https://en.wikipedia.org/wiki/Leap_year#Algorithm
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

print(isLeapYear(1932)) # true
print(isLeapYear(2012)) # true
print(isLeapYear(2100)) # false
print(isLeapYear(2064)) # true

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    """
    Calculates the number of days between two dates.
    """
    return 0

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
