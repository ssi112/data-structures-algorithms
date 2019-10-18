"""
6x_union_inter.py

You will take in two linked lists and return a linked list that is composed
of either the union or intersection, respectively.

Your task for this problem is to fill out the union and intersection functions.

The union of two sets A and B is the set of elements which are in A, in B, or
in both A and B.

The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects
that are members of both the sets A and B.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None


    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)


    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size


def union(llist_1, llist_2):
    # Your Solution Here
    print(llist_1)
    print(llist_2)
    return "union - stub test"


def intersection(llist_1, llist_2):
    # Your Solution Here
    print(llist_1)
    print(llist_2)
    return "intersection - stub test"

#-----------------------------------------------------------------------
# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

# ------------------------------------
print("\nTest 1 with Python's set methods...\n")
set1 = set()
set2 = set()

set1.update(element_1)
set2.update(element_2)

set_union = set1.union(set2)
set_intersect = set1.intersection(set2)


def union_test(e1, e2):
    # test the union logic
    e3 = []
    for e in e1:
        if e not in e3:
            e3.append(e)
        if e in e2:
            if e not in e3:
                e3.append(e)
    for e in e2:
        if e not in e3:
            e3.append(e)
        if e in e1:
            if e not in e3:
                e3.append(e)
    return sorted(e3)


def intersection_test(e1, e2):
    # test the intersection logic
    e3 = []
    for e in e1:
        if e in e2 and e not in e3:
            e3.append(e)
    return sorted(e3)


print("       Test 1: Python's set union check:", sorted(set_union))
print("Test 1: Python's set intersection check:", sorted(set_intersect))
print("                      union_test result:", union_test(element_1, element_2))
print("               intersection_test result:", intersection_test(element_1, element_2))

#print(union(linked_list_1, linked_list_2))
#print(intersection(linked_list_1, linked_list_2))


#-----------------------------------------------------------------------
print("\nTest 2 with Python's set methods...\n")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

# ------------------------------------
# test with Python's set methods
set1.clear()
set2.clear()

set1.update(element_1)
set2.update(element_2)

set_union = set1.union(set2)
set_intersect = set1.intersection(set2)

print("       Test 2: Python's set union check:", sorted(set_union))
print("Test 2: Python's set intersection check:", sorted(set_intersect))
print("                      union_test result:", union_test(element_1, element_2))
print("               intersection_test result:", intersection_test(element_1, element_2))

#print(union(linked_list_3, linked_list_4))
#print(intersection(linked_list_3, linked_list_4))


