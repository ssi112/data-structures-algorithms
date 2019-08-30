# How to Solve Problems

### Lesson 5 Practice Problem Notes

**Given your birthday and the current date, calculate your age in days. Compensate for lead days. Assume that the birthday and current date are correct dates and there is no time travle involved. Simply put, if you were bon 1 Jan 2012 and todays date is 2 Jan 2012 you are 1 day old.** 

**First, make certain we understand the problem!**  

**STEPS**

1. What are the inputs?
2. What are the outputs?
3. Work through some examples by hand
4. Try a simple mechanical solution
5. Don't optimize prematurely - keep it simple and correct!


------
- What are the inputs, if any?
- What are the outputs, if any?
- What is the relationship between the inputs and the desired outputs?   
------

- **Inputs: birthday and current date**
- **Outputs: age in days**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input -> | Procedure | -> Output


**Input assumption:**

* Dates could be any date
* Second date must be after first date (i.e., no time travel)
* Gregorian calendar (began 15 Oct 1582)

_How are the inputs represented?_

While there are various ways to handle dates for this problem they will be treated as individual component parts of a date.

def daysBetweenDates(year1, month1, day1, year2, month2, day2):

------
- **What are the outputs?**

Return a number giving the number of days between the first date and the second date.

Output assumption:

* Second date is the same or after the first date

------
**Solve the Problem!**

Work up some examples for test cases:
```
#test same day
assert(daysBetweenDates(2017, 12, 30, 2017, 12, 30) == 0)
#test adjacent days
assert(daysBetweenDates(2017, 12, 30,  2017, 12, 31) == 1)
#test new year
assert(daysBetweenDates(2017, 12, 30,  2018, 1,  1)  == 2)
# test full year difference
assert(daysBetweenDates(2012, 6, 29, 2013, 6, 29)  == 365)
# Second date must be equal to or occur after first date
assert(daysBetweenDates(2012, 12, 8, 2012, 12, 7)  == Undefined)
```

**Consider how a human would systematically solve the problem**

Work through an example to solve the problem.

 - 2013 Jan 24 to 2013 June 29 (easy)
    - Use a calendar and count the number of days between the two dates.
 - 2013 Jan 24 to 2024 June 29 (harder)
 
Write down an algorithm in psuedo code to layout the idea of how we might solve it.
First pass
```
days = number of days in month1 - day1
month = month + 1
while month1 < month 2
	days = days + number of days in month1
	month1 = month1 + 1
days = days + day2
while year 1 < year 2
	days = days + days in year1
```

OOPS!
Doesn't handle input dates in same month
Doesn't handle cases where month2 < month1, but year2 is > year1
Need to check for leap years

Is there a simpler method?

A Simple Mechanical Solution!
```
days = 0
while date1 is before date 2:
	date1 = day after date1
	days = days + 1
return days
```

For the above a procedure is needed to figure out the next day (day after date1)



