"""
Double Linked List: has the following methods:
    appending - add to beginning of list
    prepending - add item at end of list
    finding (search) a node for a value
    pop - remove item from beginning of list
    remove - find item that matches value and remove first occurrence
    insert - a new node into specified position in the list
    convert to regular Python list
    print nodes in natural order
    print nodes in reverse natual order

linked list fundamentals: https://www.pythoncentral.io/singly-linked-list-insert-node/

Add new node to beginning of list. This keeps coding simple and allows it to act like
a stack: last item added is at top of stack/beginning of list. If a tail node is kept
then can append new node at end of list without having to loop through the list to
find the end.
"""
class Node(object):
    """
    Node class for linked list. Contains data and pointers to the next and
    previous node.
    """
    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def setData(self, value):
        self.data = value

    def getNextNode(self):
        return self.next

    def setNextNode(self, value):
        self.next = value

    def getPreviousNode(self):
        return self.previous

    def setPreviousNode(self, value):
        self.previous = value


class DoublyLinkedList(object):
    """
    Each node is connected to the next node and to the previous node in the list.
    Making it possible to go forward and backward through the list and we can
    either prepend or append data by maintaining a head and tail pointers.

    Contains a size attribute to easily find how many items are contained in the
    list without have to loop through the list and count them.
    """
    def __init__(self, head = None, tail = None):
        self.head = None
        self.tail = None
        self.size = 0

    def getSize(self):
        return self.size

    def appendNode(self, value):
        if self.head is None:   # empty list
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

    def prependNode(self, value):
        if self.head is None:   # empty list
            newNode = Node(value)
            self.head = newNode
            self.tail = self.head
            self.size += 1
            return True

        # tail does not change since we add at start of list
        newNode = Node(value)
        newNode.next = self.head # point new node to head
        self.head.previous = newNode
        self.head = newNode # point the head to the start of list again
        self.size += 1
        return True

    def findNode(self, value):
        """
        Search the linked list for a node with the requested value and return the node.
        Random access is not possible. Must traverse the linked list from the
        beginning to get to a particular node. Worst case is O(n) and assumes the
        list is not sorted.
        """
        search_node = self.head
        while search_node:
            if search_node.getData() == value:
                return search_node
            search_node = search_node.getNextNode()
        return False # either list is empty or we hit the end of the list

    def pop(self):
        """
        Find the first node's value and remove it from the list.
        Then return the first value.
        """
        if self.head is None:
            return None

        node = self.head
        # get head's next list item and make it the new head
        self.head = self.head.getNextNode()
        self.head.previous = None
        self.size -= 1
        return node.data   # removed data value

    def removeNode(self, value):
        """
        Find the first element in list that matches value and remove it.
        Returns True if found and removed else False.
        Example:
            Linked list: H-->3-->4-->5
            Remove 4: H-->3-->5
        """
        if self.head is None:
            return None     # empty list

        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.getData() == value:
                # if found link the previous node's next to current's next
                # effectively skips or jumps around the node to remove
                if previous_node:
                    previous_node.setNextNode(current_node.getNextNode())
                    # -----------------------------------------------------
                    current_node.getNextNode().setPreviousNode(current_node.getPreviousNode())
                else:
                    # this is if the first (head) node is to be removed
                    self.head = current_node.getNextNode()
                    # -----------------------------------------------------
                    current_node.getNextNode().setPreviousNode(self.head)
                self.size -= 1
                return True
            # proceed to the next node
            previous_node = current_node
            current_node = current_node.getNextNode()
        # element not found in list
        return False

    def insert(self, value, pos):
        """
        Insert value at pos position in the list. If pos is larger than
        the length of the list, append to the end of the list. If pos = 0
        then add it to the beginning of the list
        """
        if pos == 0:
            self.prependNode(value)
            return True

        # CHECK THIS ==>> https://stackabuse.com/doubly-linked-list-with-python-examples/
        # as this uses position it inserts the new node BEFORE the item
        # that is already in the specified posiition
        position = 0
        selectedNode = self.head
        while selectedNode.getNextNode() and position <= pos:
            if (pos - 1) == position:
                newNode = Node(value)

                # Set the next reference of the newly inserted node to
                # the selected node (inserted before)
                newNode.next = selectedNode

                # Set the previous reference of the newly inserted node
                # to the previous reference of the selected
                newNode.previous = selectedNode.getPreviousNode()

                # Set the next reference of the node previous to the selected
                # node, to the newly added node
                selectedNode.previous.next = newNode

                # set the previous reference of the selected node to the
                # newly inserted node
                selectedNode.previous = newNode
                self.size += 1
                return True
            position += 1
            selectedNode = selectedNode.getNextNode()
        # executed when the while condition becomes false
        else:
            self.appendNode(value)
        return True

    def to_list(self):
        converted = []
        node = self.head
        while node:
            converted.append(node.getData())
            node = node.getNextNode()
        return converted

    def printNodes(self):
        current = self.head
        while current:
            print(current.data)
            current = current.getNextNode()

    def printNodesReverse(self):
        current = self.tail
        while current:
            print(current.getData())
            current = current.getPreviousNode()


# <<< ***** TEST ***** >>> #
myList = DoublyLinkedList()
print("Appending nodes")
print("Successfully appended?", myList.appendNode(5))
print("Successfully appended?", myList.appendNode(15))
print("Successfully appended?", myList.appendNode(25))
print("Printing nodes...")
myList.printNodes()
print("Size = {}".format(myList.getSize()))

print("\nPrepending nodes")
print("Sccessfully prepended?", myList.prependNode(11))
print("Successfully prepended?", myList.prependNode(3))
print("Printing nodes...")
myList.printNodes()
print("Size = {}".format(myList.getSize()))

print("Searching for 99...")
nodeFindIt = myList.findNode(99)
if nodeFindIt == False:
    print("\tNot found")
else:
    print(nodeFindIt)

print("Searching for 3, updating to 33 if found...")
nodeFindIt = myList.findNode(3)
if nodeFindIt == False:
    print("\tNot found")
else:
    print(nodeFindIt)
    nodeFindIt.setData(33)
print("-"*55)
myList.printNodes()

print("-"*55)
print("Pop Test - remove first node value if not empty list...")
myList.pop()
myList.printNodes()
print("Size = {}".format(myList.getSize()))

print("-"*55)
print("Attempting to remove node value 99...")
print(myList.removeNode(99))
print("Attempting to remove node value 15...")
print(myList.removeNode(15))
myList.printNodes()
print("Size = {}".format(myList.getSize()))

print("-"*55)
print("Attempting to insert value 99 in position 2...")
print(myList.insert(99, 2))
myList.printNodes()
print("Attempting to insert value 13 in position 0...")
print(myList.insert(13, 0))
myList.printNodes()
print("Attempting to insert value 101 in position 100...")
print(myList.insert(101, 100))

print("-"*55)
print("Current List...")
myList.printNodes()
print("Size = {}".format(myList.getSize()))

print("-"*55)
print("Current List Reversed...")
myList.printNodesReverse()

print("Convert to list: ", myList.to_list())

# convert a list to doubly linked list
convertList = ['a', 'b', 0, 'ska', [0,9,9]]
newList = DoublyLinkedList()
for val in convertList:
    newList.appendNode(val)
print("-"*55)
print("New List...")
newList.printNodes()
newList.printNodesReverse()

