"""
binary_tree.py

Reference:
https://www.geeksforgeeks.org/binary-search-tree-data-structure/#basic

"""

## define a node class
class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    # assumes this will replace any existing node if it's already assigned
    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    """
    str() is used for creating output for end user while repr() is mainly used for
    debugging and development. repr’s goal is to be unambiguous and str’s is to be readable
    """
    def __repr__(self): # printable representation
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


# define a binary tree
class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root


# define a stack to keep track of the tree nodes
# take advantage of Pythons list methods (LIFO) to push and pop
class Stack():
    def __init__(self):
        self.list = list()

    def push(self,value):
        self.list.append(value)

    def pop(self):
        return self.list.pop() # remove & return last value in list

    def top(self):
        if len(self.list) > 0:
            return self.list[-1] # end of list (LIFO)
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        else:
            return "<stack is empty>"


## ### ### ### ### ### ### ### ### ### ### ### ### ### ###
## Initial Check
## ### ### ### ### ### ### ### ### ### ### ### ### ### ###
node0 = Node()
print(f"""node0:
  value: {node0.value}
  left: {node0.left}
  right: {node0.right}
""")

node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")

print("adding left and right children")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"""
node 0: {node0.value}
  node 0 left child: {node0.left.value}
  node 0 right child: {node0.right.value}
""")

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")

## ### ### ### ### ### ### ### ### ### ### ### ### ### ###
## Depth First Search (DFS) - Pre-order Traversal Check
## ### ### ### ### ### ### ### ### ### ### ### ### ### ###
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

## ### ### ### ### ### ### ### ### ### ### ### ### ### ###
## Stack Check
## ### ### ### ### ### ### ### ### ### ### ### ### ### ###
"""
stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("cherry")
stack.push("dates")
print(stack.pop()) # remove 'dates'
print("\n")
print(stack)
"""

## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
# Depth first, pre-order traversal
# pre-order traversal of the tree would visit the nodes in this order:
#
# apple, banana, dates, cherry
#
# Notice how we're retracing our steps.
# It's like we are hiking on a trail, and trying to retrace our steps on the way back.
# This is an indication that we should use a stack.
## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

visit_order = list()
stack = Stack()

# start at the root node, visit it and then add it to the stack
node = tree.get_root()
visit_order.append(node.get_value())
stack.push(node)

print(f"""
===========================
visit_order {visit_order}
stack:
{stack}
""")

# check if apple has a left child
print(f"{node} has left child? {node.has_left_child()}")

# since apple has a left child (banana)
# we'll visit banana and add it to the stack
if( node.has_left_child()):
    node = node.get_left_child()
    print(f"visit {node}")
    visit_order.append(node.get_value())
    stack.push(node)

print(f"""
===========================
visit_order {visit_order}
stack:
{stack}
""")

# check if banana has a left child
print(f"{node} has left child? {node.has_left_child()}")

# since banana has a left child "dates"
# we'll visit "dates" and add it to the stack
if( node.has_left_child()):
    node = node.get_left_child()
    print(f"visit {node}")
    visit_order.append(node.get_value())
    stack.push(node)

print(f"""
visit_order {visit_order}
stack:
{stack}
""")

# check if "dates" has a left child
print(f"{node} has left child? {node.has_left_child()}")


# since dates doesn't have a left child, we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")


# since "dates" is a leaf node (has no children), we can start to retrace our steps
# in other words, we can pop it off the stack.
print(stack.pop())


stack


# now we'll set the node to the new top of the stack, which is banana
node = stack.top()
print(node)


# we already checked for banana's left child, so we'll check for its right child
print(f"{node} has right child? {node.has_right_child()}")


# banana doesn't have a right child, so we're also done tracking it.
# so we can pop banana off the stack
print(f"pop {stack.pop()} off stack")
print(f"""
stack
{stack}
""")


# now we'll track the new top of the stack, which is apple
node = stack.top()
print(node)


# we've already checked if apple has a left child; we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")


# since it has a right child (cherry),
# we'll visit cherry and add it to the stack.
if node.has_right_child():
    node = node.get_right_child()
    print(f"visit {node}")
    visit_order.append(node.get_value())
    stack.push(node)

print(f"""
visit_order {visit_order}
stack
{stack}
""")


# Now we'll check if cherry has a left child
print(f"{node} has left child? {node.has_left_child()}")

# it doesn't, so we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")


# since cherry has neither left nor right child nodes,
# we are done tracking it, and can pop it off the stack

print(f"pop {stack.pop()} off the stack")

print(f"""
visit_order {visit_order}
stack
{stack}
""")


# now we're back to apple at the top of the stack.
# since we've already checked apple's left and right child nodes,
# we can pop apple off the stack

print(f"pop {stack.pop()} off stack")
print(f"pre-order traversal visited nodes in this order: {visit_order}")


print(f"""stack
{stack}""")


