"""
queue_linked_list.py

Time Complexity
When we use enqueue, we simply create a new node and add it to the tail of the list.
And when we dequeue an item, we simply get the value from the head of the list and then
shift the head variable so that it refers to the next node over.

Both of these operations happen in constant time—that is, they have a time-complexity of O(1).
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return repr(self.value)

class Stack:
    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

class Queue:
    def __init__(self):
        """
        head attribute to keep track of the first node in the linked list
        tail attribute to keep track of the last node in the linked list
        num_elements attribute to keep track of how many items are in the stack
        """
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        """
        Adds a new item to the back of the queue. Since we're using a linked list,
        this is equivalent to creating a new node and adding it to the tail (append).

        If the queue is empty, then both the head and tail should refer to the new node
        (because when there's only one node, this node is both the head and the tail)
        Otherwise (if the queue has items), add the new node to the tail
        Be sure to shift the tail reference so that it refers to the new node
        (because it is the new tail)
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            # add value to the next attribute of the tail (append)
            self.tail.next = new_node
            # shift the tail (i.e., the back of the queue)
            self.tail = self.tail.next
        self.num_elements += 1

    def dequeue(self):
        """
        If the queue is empty, it should simply return None else
        Get the value from the front of the queue (head of the linked list)
        Shift the head over so that it refers to the next node
        Update the num_elements attribute
        Return the value that was dequeued
        """
        if self.is_empty():
            return None
        value = self.head.value     # copy the value to a local variable
        self.head = self.head.next  # shift the head (front of the queue)
        self.num_elements -= 1
        return value

    def size(self):
        # returns the current size of the stack
        return self.num_elements

    def is_empty(self):
        # returns True if the stack is empty and False otherwise
        return self.num_elements == 0

    def __repr__(self):
        return '<%s (%s:%s) %s>' % (self.__class__.__name__, self.head, self.tail,  self.num_elements)


def reverse_queue(queue):
    """
    Reverese the input queue
    Args:
       queue(queue),str2(string): Queue to be reversed
    Returns:
       queue: Reveresed queue
    """

    # You can use an auxiliary stack to reverse the elements of your Queue.
    # Basically, you will stack every element of your Queue until it becomes empty.
    # Then you pop each element of your stack and enqueue it until your stack is empty.
    aux_stack = Stack()
    while not queue.is_empty():
        aux_stack.push(queue.dequeue())

    while not aux_stack.is_empty():
        queue.enqueue(aux_stack.pop())
    return queue

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q)

r = reverse_queue(q)
print(r)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")

print(q)
