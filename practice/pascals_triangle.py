"""
Problem Statement

Find and return the nth row of Pascal's triangle in the form a list. n is 0-based.

For exmaple, if n = 4, then output = [1, 4, 6, 4, 1].

To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html

"""

# once again they are not attempting to teach anything in this course:
# Pascal's Triangle
#     https://spiderlabweb.com/python-program-print-pascals-triangle/


def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    if n == 0:
        return [1]
    current_row = [1]
    for i in range(1, n + 1):
        previous_row = current_row
        current_row = [1]
        for j in range(1, i):
            next_number = previous_row[j] + previous_row[j - 1]
            current_row.append(next_number)
        current_row.append(1)
    return current_row


# factorial
def fact(n):
    res=1
    for c in range(1, n + 1):
        res = res * c
    return res


def pascal_triangle_fact(rows):
    for i in range(0, rows):
        for j in range(1, rows-i):
            print("  ", end="")
        for k in range(0, i+1):
            coff = int(fact(i) / (fact(k) * fact(i - k)))
            print("  ", coff, end="")
        print()


def pascal_triangle(rows):
    for i in range(0, rows):
        coff = 1
        for j in range(1, rows - i):
            print("  ", end="")
        for k in range(0, i+1):
            print("  ", coff, end="")
            coff = int(coff * (i - k) / (k + 1))
        print()


def main():
    rows = int(input("Enter the number of rows : "))
    pascal_triangle_fact(rows)

    # without using the factorial function
    rows = int(input("Enter the number of rows : "))
    pascal_triangle(rows)

    rows = int(input("Enter the number of rows : "))
    print("Udacity's lack of teaching solution", nth_row_pascal(rows - 1))

if __name__ == '__main__':
    main()
