"""
    recursion1_simple.py

Call Stack
There are limitations of recursion on a call stack.
Python limits the depth on recursion if you create a condition wherein a
very large call stack is used.
It will raise the error RecursionError: maximum recursion depth exceeded in comparison.

Some compiliers may turn them into an iterative loop to prevent using up the stack.
Python does not do this.
"""

def power_of_2(n):
    """
    The base case. This is where you catch edge cases that don't fit the problem (2∗2𝑛−1).
    Since we aren't considering any 𝑛<0 valid, 2∗2𝑛−1 can't be used when 𝑛 is 0.
    This section of the code returns the solution to 2^0 without using 2∗2𝑛−1.
    """
    if n == 0:
        return 1
    """
    This code is where it breaks the problem down into smaller instances.
    Calling itself to calculate 2𝑛−1
    """
    return 2 * power_of_2(n - 1)


def sum_integers(n):
    if n == 1:
        return 1
    return n + sum_integers(n - 1)


# sometime iterative solutions are more readable and hence less prone to bugs
def sum_array_iter(array):
    result = 0
    for x in array:
        result += x
    return result




def factorial(n):
    """
    A factorial function is a mathematical function that multiplies a given number, 𝑛,
    and all of the whole numbers from 𝑛 down to 1

        4! = 4∗3∗2∗1 = 24

        we can say that for any input 𝑛

        𝑛! = 𝑛∗(𝑛−1)∗(𝑛−2)...1

    For Python: factorial(n) = n * factorial(n - 1)

    Calculate n!
        Args:
           n(int): factorial to be computed
        Returns:
           n!
    """
    if n == 0:
        return 1    # by definition of 0!
    return n * (factorial(n - 1))


sumnum = 5
print()
print("-"*55)
print("power_of_2({}) = {}".format(sumnum, power_of_2(sumnum)))

sumnum = 3
print()
print("-"*55)
print("sum_integers({}) = {}".format(sumnum, sum_integers(sumnum)))

arr = [1, 2, 3, 4, 5, 6]
print()
print("-"*55)
print("sum_array_iter({}) = {}\n".format(arr, sum_array_iter(arr)))

sumnum = 4
print()
print("-"*55)
print("factorial({}) = {}\n".format(sumnum, factorial(sumnum)))
