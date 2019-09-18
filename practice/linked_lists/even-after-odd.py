"""
Problem Statement

Given a linked list with integer data, arrange the elements in such a
manner that all nodes with even numbers are placed after odd numbers.
Do not create any new nodes and avoid using any other data structure.
The relative order of even and odd elements must not change.

Example:
    linked list = 1 2 3 4 5 6
    output = 1 3 5 2 4 6

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    if head is None:
        return head

    even = None
    odd = None
    even_tail = None
    head_tail = None

    while head:
        next_node = head.next
        if head.data % 2 == 0:
            if even is None:
                even = head
                even_tail = even
            else:
                even_tail.next = head
                even_tail = even_tail.next
        else:
            if odd is None:
                odd = head
                odd_tail = odd
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next
        head.next = None
        head = next_node

    if odd is None:
        return even
    odd_tail.next = even
    return odd

def main():
    arr = [1, 2, 3, 4, 5, 6]
    head = create_linked_list(arr)
    print("Before even-odd: ")
    print_linked_list(head)

    print("\nAfter even-odd: ")
    even_odd = even_after_odd(head)
    print_linked_list(head)


if __name__ == '__main__':
    main()
