"""
1_problem.py

Find the square root of the integer without using any Python library.
You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196
whose floor value is 5.

The expected time complexity is O(log(n))

Reference:
https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method


"""

def sqrt(number):
    """
    Calculate the floored square root of a number
    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root

    Babylonian Method: described on Wikipedia link above
    """

    # if n is negative then bail out
    try:
        if number < 0:
            msg = "\nSquare root of a negative number is undefined.\n"
            raise ValueError(msg)
    except ValueError as err_msg:
        print(err_msg)
        return False

    # take care of the easy cases
    if number == 0 or number == 1:
        return number

    # num is initial value to begin with and divided by a factor
    # some guess work/experimenting here, if you divide the number in half
    # this can fail on square root of 9 and other small numbers.
    #
    # *** otherwise helps reduce the number of iterations ***
    # *** performs slightly better than binary method on large numbers ***
    if number < 9:
        num = number // 1.5
    if 9 <= number <= 15:
        num = number
    else:
        num = number // 2

    # initially this is 1
    # as num decreases this increases until the difference
    # between the two is less then the estimate_error
    incremental = 1

    # making this number too small increases iterations
    estimate_error = 1 # 0.01

    # not needed: used to see the effect of tweaking above variables
    iterations = 0

    while (num - incremental > estimate_error):
        num = (num + incremental) / 2
        incremental = number / num
        iterations += 1
        # here for testing, can watch the function converge to answer
        # print("num={} one={}".format(num, incremental))

    #print("sqrt({})={}. Number of iterations is {}".format(number, num//1, iterations))

    # floor: integer division gets rid of digits to the right of decimal pt
    return num // 1


print("-"*70)
print ("Pass sqrt(9) = 3"     if (3 == sqrt(9))       else "Fail sqrt(9)")
print ("Pass sqrt(0) = 0"     if (0 == sqrt(0))       else "Fail sqrt(0)")
print ("Pass sqrt(16) = 4"    if (4 == sqrt(16))      else "Fail sqrt(16)")
print ("Pass sqrt(1) = 1"     if (1 == sqrt(1))       else "Fail sqrt(1)")
print ("Pass sqrt(27) = 5"    if (5 == sqrt(27))      else "Fail sqrt(27)")
print ("Pass sqrt(-11) = False"  if (False == sqrt(-11)) else "Fail sqrt(-11)")
print ("Pass sqrt(576) = 24"  if (24 == sqrt(576))    else "Fail sqrt(576)")
print ("Pass sqrt(6241) = 79" if (79 == sqrt(6241))   else "Fail sqrt(6241)")
print ("Pass sqrt(5) = 2"     if (2 == sqrt(5))       else "Fail sqrt(5)")
print ("Pass sqrt(3) = 1"     if (1 == sqrt(3))       else "Fail sqrt(3)")
print ("Pass sqrt(3) = 1250"  if (1250 == sqrt(1562500)) else "Fail sqrt(1562500)")
print("-"*70)


