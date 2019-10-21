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

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next


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

    def in_list(self, value):
        """
        Search the linked list for the given value and return True if found,
        False if not found. Traverses the linked list from beginning to end.
        Worst case searches entire list: O(n), Assumes list is not sorted.
        """
        search_node = self.head
        while search_node:
            if search_node.get_value() == value:
                return True # found the value in the list
            search_node = search_node.get_next_node()
        return False # either list is empty or we hit the end of the list


# ------------------------------------
def union(llist_1, llist_2):
    ll_union = LinkedList()
    # search through the first list
    current = llist_1.head
    while current:
        e = current.get_value()
        if not ll_union.in_list(e):
            ll_union.append(e)
        current = current.next
    # search in the llist_2
    current = llist_2.head
    while current:
        e = current.get_value()
        if not ll_union.in_list(e):
            ll_union.append(e)
        current = current.next
    if ll_union.size():
        return ll_union
    return None


# ------------------------------------
def intersection(llist_1, llist_2):
    ll_intersect = LinkedList()
    current = llist_1.head
    while current:
        e = current.get_value()
        if llist_2.in_list(e) and not ll_intersect.in_list(e):
            ll_intersect.append(e)
        current = current.next
    if ll_intersect.size():
        return ll_intersect
    return None


# ======================================================================
def test_ui(element_1, element_2, llu, lli):
    # test against Python's set methods
    set1 = set(element_1)
    set2 = set(element_2)

    set_union = set1.union(set2)
    set_intersect = set1.intersection(set2)

    # compare the link list union (llu) against set_union
    if llu and set_union:
        current = llu.head
        for element in set_union:
            if not llu.in_list(element):
                return False
    # compare the link list intersect (lli) against set_intersect
    if lli and set_intersect:
        current = lli.head
        for element in set_intersect:
            if not lli.in_list(element):
                return False
    return True


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

ll_union = union(linked_list_1, linked_list_2)
ll_intersect = intersection(linked_list_1, linked_list_2)
print("\nTest Case 1")
print("    union", ll_union)
print("intersect", ll_intersect)

print("\nChecking against Python's union and intersection with sets...", end=" ")
print("Pass, yay!" if (test_ui(element_1, element_2, ll_union, ll_intersect)) else "Fail, uh oh!")

#-----------------------------------------------------------------------
# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

ll_union = union(linked_list_3, linked_list_4)
ll_intersect = intersection(linked_list_3, linked_list_4)
print("\nTest Case 2")
print("    union", ll_union)
print("intersect", ll_intersect)

print("\nChecking against Python's union and intersection with sets...", end=" ")
print("Pass, yay!" if (test_ui(element_1, element_2, ll_union, ll_intersect)) else "Fail, uh oh!")

#-----------------------------------------------------------------------
# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [2, 4, 6, 8, 10]
element_2 = [1,3,5,7,9,11,13]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

ll_union = union(linked_list_5, linked_list_6)
ll_intersect = intersection(linked_list_5, linked_list_6)
print("\nTest Case 3")
print("    union", ll_union)
print("intersect", ll_intersect)

print("\nChecking against Python's union and intersection with sets...", end=" ")
print("Pass, yay!" if (test_ui(element_1, element_2, ll_union, ll_intersect)) else "Fail, uh oh!")

#-----------------------------------------------------------------------
# Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

ll_union = union(linked_list_7, linked_list_8)
ll_intersect = intersection(linked_list_7, linked_list_8)
print("\nTest Case 4")
print("    union", ll_union)
print("intersect", ll_intersect)

print("\nChecking against Python's union and intersection with sets...", end=" ")
print("Pass, yay!" if (test_ui(element_1, element_2, ll_union, ll_intersect)) else "Fail, uh oh!")
