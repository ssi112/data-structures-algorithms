"""
binary_tree_state.py

Reference:
https://www.geeksforgeeks.org/binary-search-tree-data-structure/#basic
"""

## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
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


## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
# define a binary tree
class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root


## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
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


## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
# pre-order traversal using a stack, tracking state
# implement DFS with a stack, where we also track whether we've already
# visited the left or right child of the node.
class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s


def pre_order_with_stack(tree, debug_mode = False):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0
    while(node):
        if debug_mode:
            print(f"""
            loop count: {count}
            current node: {node}
            stack:
            {stack}
            """)
        count += 1
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    if debug_mode:
            print(f"""
            loop count: {count}
            current node: {node}
            stack:
            {stack}
            """)
    return visit_order


## ### ### ### ### ### ### ### ### ### ### ### ### ### ###
# root, left, right
def pre_order_recursion(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            # visit
            visit_order.append(node.get_value())
            # traverse left
            traverse(node.get_left_child())
            # traverse right
            traverse(node.get_right_child())

    traverse(root)
    return visit_order

## ### ### ### ### ### ### ### ### ### ### ### ### ### ###
# left, root. right
def in_order_recursion(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            # traverse left
            traverse(node.get_left_child())
            # visit
            visit_order.append(node.get_value())
            # traverse right
            traverse(node.get_right_child())

    traverse(root)
    return visit_order


## ### ### ### ### ### ### ### ### ### ### ### ### ### ###
# left, right, root
def post_order_recursion(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            # traverse left
            traverse(node.get_left_child())
            # traverse right
            traverse(node.get_right_child())
            # visit
            visit_order.append(node.get_value())


    traverse(root)
    return visit_order


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

# check pre-order traversal
pre_order_with_stack(tree, debug_mode=True)

print("\n*** pre_order_recursion ***")
print(pre_order_recursion(tree))

print("\n*** in_order_recursion ***")
print(in_order_recursion(tree))

print("\n*** post_order_recursion ***")
print(post_order_recursion(tree))

