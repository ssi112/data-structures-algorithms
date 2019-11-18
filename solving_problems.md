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

OOPS! <br />
Doesn't handle input dates in same month <br />
Doesn't handle cases where month2 < month1, but year2 is > year1 <br />
Need to check for leap years <br />

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

Write small bits of code and _test_ them. Know what each part does and how it fits into solving the problem.

#### Step-wise Refinement
Below is a simple procedure that is _partially_ correct.
```
# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    # YOUR CODE HERE!
    days = 0
    while ((year1 != year2) or (month1 != month2) or (day1 != day2)):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    # print(year1, month1, day1)
    # print(days)
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

# output:
Test case passed!
Test case passed!
Test case passed!
```

**&checkmark; So far with the solution to the problem broken into three parts:**

1. Step One Pseudocode
2. Step Two Helper Function(s)
3. Step Three daysBetweenDates

**&#x261B; Write small bits of code and test so the problem is solved incrementally**

<hr /> 

This focused on solving the problem and how to get a working version of the days between dates, but left efficiency out of the equation. In the steps outlined above and repeated below we stopped at step 4) and put off efficiency. Efficiency being the amount of time it takes to run the program and the amount of space (memory) required. 

These are the problem solving steps used:

1. What are the inputs?
2. What are the outputs?
3. Work through some examples by hand
4. Try a simple mechanical solution
5. Don't optimize prematurely - keep it simple and correct!


**A correct working version is in tmp/daysBetweenDates.py**

---

## Problem Solving?

#### When there are many choices or states the complexity comes from making the right choices.

#### Example: route finding problem

**Problem Definition**

Initial State => s0

Actions (s) : => {a1, a2, a33, ...}

* A function that takes a state as input and returns a set of possible actions the agent can execute

Result (s, a) => s'

* Function that takes a state and action and delivers a new state as output

Goal Test (s) => True | False

* Function to take in a state and returns whether this state is a goal or not

Path Cost (si => si+1 => si+2) => cost value (n) where i = 0,1,... j = 1,2,...
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; aj &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; aj+1

* A function which takes a path, a sequence of state, actions, transitions and returns a number, which is the cost of that path.

Typically, the cost path is additive so the total cost of a path is just the sum of the individual steps. Implemented as a _step cost function_

Step Cost (s, a, s') => n

* Function that takes a state, action, and resulting state' of the action and returns a number that represents the _cost*_ of that action.

&nbsp;&nbsp;&nbsp;&nbsp;_*Cost can be number of miles, time (hours/minutes), dollars, etc._

**Route finding [video example](https://www.youtube.com/watch?time_continue=150&v=5lrkPKQwOFE&feature=emb_logo)**

#### Uniform Cost Search

**Uniform Cost search** - expands out equally in all directions, may expend additional effort getting to a fairly direct path to the goal.


**Greedy best-first search** - expands outward toward locations estimated as closer to the goal. If a direct path is available, expends much less effort than Uniform Cost; however, it does not consider any routes in which it may need to temporarily take a further away path in order to arrive at an overall shorter path.


**A* Search** - utilizes both of these - will try to optimize with both the shortest path and the goal in mind. We'll see how this works in the next video.






