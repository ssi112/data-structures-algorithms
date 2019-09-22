"""
    recursion2_reverse_string.py

Call Stack
There are limitations of recursion on a call stack.
Python limits the depth on recursion if you create a condition wherein a
very large call stack is used.
It will raise the error RecursionError: maximum recursion depth exceeded in comparison.

Some compiliers may turn them into an iterative loop to prevent using up the stack.
Python does not do this.
"""


"""
Reversing a String

Practice a problem that is frequently solved by recursion: Reversing a string.

Note that Python has a built-in function that you could use for this,
but the goal here is to avoid that and understand how it can be done using recursion instead.
"""
def reverse_string(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """
    if len(input) == 0:
        return ""
    else:
        first_char = input[0]
        the_rest = slice(1, None)
        sub_string = input[the_rest]
        reversed_substring = reverse_string(sub_string)
        return reversed_substring + first_char


def reverse_string_print(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """
    if len(input) == 0:
        return ""
    else:
        first_char = input[0]
        print("\nfirst_char", first_char)

        the_rest = slice(1, None)
        print("\nthe_rest", the_rest)

        sub_string = input[the_rest]
        print("\nsub_string", sub_string)

        reversed_substring = reverse_string(sub_string)
        print("\nreversed_substring", reversed_substring)

        return reversed_substring + first_char

sumstr = ""
print()
print("-"*55)
print("reverse_string({}) = [{}]\n".format(sumstr, reverse_string(sumstr)))

sumstr = "Esteban DeJesus"
print()
print("-"*55)
print("reverse_string({}) = [{}]\n".format(sumstr, reverse_string(sumstr)))

sumstr = "cba"
print("-"*55)
print("reverse_string_print({}) = [{}]\n".format(sumstr, reverse_string_print(sumstr)))
