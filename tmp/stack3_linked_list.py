"""
Implement a stack using a linked list. The bottom of the stack is the beginning
of the list, so items are added or removed from the TAIL of the list.
"""
class Node(object):
    def __init__(self, value, previous = None):
        self.value = value
        self.previous = None

class Stack:
    def __init__(self):
         # TODO: Initialize the Stack
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
         # TODO: Check the size of the Stack
        return self.size

    def push(self, value):
         # TODO: Push item onto Stack
        if self.head is None: # empty list
            newNode = Node(value)
            self.head = newNode
            self.tail = self.head
            self.size += 1
            return True
        # head does not change since we add at end of list
        self.tail.next = Node(value) # tail next points to new node
        self.tail.next.previous = self.tail # point new node prev back to tail
        self.tail = self.tail.next # point the tail to the end of list again
        self.size += 1
        return True

    def pop(self):
         # TODO: Pop item off of the Stack
        """
        Check if the stack is empty and, if it is, return None
        Get the value from the tail node and put it in a local variable
        Move the tail so that it refers to the previous item in the list
        Return the value we got earlier
        """
        if self.size == 0:
            return None
        popped = self.tail.value
        # move tail pointer to previous node (this removes item from stack)
        self.tail = self.tail.previous
        self.size -= 1
        return popped

MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.head.value)
print (MyStack.tail.previous.value)
print (MyStack.tail.value)

print("Popped!", MyStack.pop())
print("Popped!", MyStack.pop())

print("current size =", MyStack.size)


print("Popped!", MyStack.pop())

print("current size =", MyStack.size)

