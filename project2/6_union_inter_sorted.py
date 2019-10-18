"""
6x_union_inter.py

You will take in two linked lists and return a linked list that is composed
of either the union or intersection, respectively.

Your task for this problem is to fill out the union and intersection functions.

The union of two sets A and B is the set of elements which are in A, in B, or
in both A and B.

The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects
that are members of both the sets A and B.

--------------------------------------------------------------------------------
Option to create list(s) in ascending or descendin sorted order.

*** NOT required for this particular task.***

Also, this link has code for merging two sorted lists - not implemented here,
though, just for future information
--------------------------------------------------------------------------------
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

    # append nodes in the order received
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    # -------------------------------------------------------------------------
    # NOT REQUIRED - makes it easier to eyeball results
    # Solution for inserting by sorted order:
    # https://stackoverflow.com/questions/19217647/sorted-linked-list-in-python
    # append nodes in ascending order
    def asc_ordered_list(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        if temp.value > value:
            new_node.next = temp
            self.head = new_node
            return

        while temp.next:
            if temp.next.value > value:
                break
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # append nodes in descending order
    def desc_ordered_list(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        if value > temp.value:
            new_node.next = temp
            self.head = new_node
            return

        while temp.next:
             if temp.value > value and temp.next.value < value:
                 break
             temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

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
    current = llist_1.head
    while current:
        e = current.get_value()
        if not ll_union.in_list(e):
            ll_union.asc_ordered_list(e) #ll_union.append(e)
        if llist_2.in_list(e):
            if not ll_union.in_list(e):
                ll_union.asc_ordered_list(e) #ll_union.append(e)
        current = current.next
    # search in the llist_2
    current = llist_2.head
    while current:
        e = current.get_value()
        if not ll_union.in_list(e):
            ll_union.asc_ordered_list(e) #ll_union.append(e)
        if llist_1.in_list(e):
            if not ll_union.in_list(e):
                ll_union.asc_ordered_list(e) #ll_union.append(e)
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
            ll_intersect.asc_ordered_list(e) #ll_intersect.append(e)
        current = current.next
    if ll_intersect.size():
        return ll_intersect
    return None


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


print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))


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

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))


