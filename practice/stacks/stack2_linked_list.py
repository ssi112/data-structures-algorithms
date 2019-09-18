"""
Implement a stack using a linked list. The top of the stack is the beginning
of the list, so items are added or removed from the head of the list.

If we pop or push an element with this stack, there's no traversal.
We simply add or remove the item from the head of the linked list,
and update the head reference. So with our linked list implementaion,
pop and push have a time complexity of O(1).
"""

class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self, head = None, num_elements = 0):
        self.head = None
        self.num_elements = 0

    def push(self, data):
        """
        The method will need to have a parameter for the value that you want to push
        You'll then need to create a new Node object with this value and link it to the list
        Remember that we want to add new items at the head of the stack, not the tail!
        Once you've added the new node, you'll want to increment num_elements
        """
        new_node = Node(data)
        # stack is empty
        if self.head is None:
            self.head = new_node
        # add new node to head/top of stack
        else:
            # existing item at top of stack becomes new node's next
            new_node.next = self.head
            # now pt head to top of stack
            self.head = new_node

        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return (True if self.num_elements == 0 else False)

    def pop(self):
        """
        Check if the stack is empty and, if it is, return None
        Get the value from the head node and put it in a local variable
        Move the head so that it refers to the next item in the list
        Return the value we got earlier
        """
        if self.is_empty():
            return None
        popped = self.head.data
        # move head pointer to next node (this removes item from stack)
        self.head = self.head.next
        self.num_elements -= 1
        return popped

# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")
