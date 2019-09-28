"""
bst_delete.py

binary search tree with delete function
    refer to '04 binary_search_tree_solution.ipynb' for explanation

insert: using a loop and with recursion
search: using a loop to find specific value
minimum value stored in tree
maximum value stored in tree
"""
from collections import deque

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
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


### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
# used to keep track of nodes in the print (__repr__) method
class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self,value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
# define a binary tree
class Tree(object):
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1 # traverse left
        else: #new_node > node
            return 1  # traverse right

    def insert_with_loop(self, new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return
        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node's value
                node.set_value(new_node.get_value())
                break # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break #inserted node, so stop looping
            else: #comparison == 1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break # inserted node, so stop looping

    def insert_with_recursion(self, value):
        if self.get_root() == None:
            self.set_root(value)
            return
        #otherwise, use recursion to insert the node
        self.insert_recursively(self.get_root(), Node(value))

    def insert_recursively(self, node, new_node):
        comparison = self.compare(node, new_node)
        if comparison == 0:
            # equal
            node.set_value(new_node.get_value())
        elif comparison == -1:
            # traverse left
            if node.has_left_child():
                self.insert_recursively(node.get_left_child(), new_node)
            else:
                node.set_left_child(new_node)
        else: #comparison == 1
            # traverse right
            if node.has_right_child():
                self.insert_recursively(node.get_right_child(), new_node)
            else:
                node.set_right_child(new_node)

    def search(self, value):
        """
        returns true if a node containing that value exists in the tree,
        otherwise false
        """
        node = self.get_root()
        s_node = Node(value)
        while(True):
            comparison = self.compare(node, s_node)
            if comparison == 0:
                return True
            elif comparison == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False

    def min_value_node(self, root):
        """
        Given a non-empty binary search tree, return the node
        with minimum key value found in that tree. Note that the
        entire tree does not need to be searched
        """
        current = root #self.get_root()
        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left
        return current

    def max_value_node(self, root):
        """
        Similar to min_value_node method, traverse the right side of
        the tree to find the maximum value that is stored
        """
        current = root #self.get_root()
        while (current.right is not None):
            current = current.right
        return current

    def delete_node(self, root, value):
        """
        Given a binary search tree and a key, this function recursively
        deletes the key and returns the new root
        https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
        """
        if root is None:
            return root

        # If the value to be deleted is smaller than the root's
        # value then it lies in left subtree
        if value < root.get_value():
            root.left = self.delete_node(root.left, value)

        # If the value to be deleted is greater than the root's value
        # then it lies in right subtree
        elif(value > root.get_value()):
            root.right = self.delete_node(root.right, value)

        # If value is same as root's value, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.min_value_node(root.right)

            # Copy the inorder successor's content to this node
            # root.value = temp.get_value()
            root.set_value(temp.get_value())

            # Delete the inorder successor
            root.right = self.delete_node(root.right, temp.get_value())

        return root


    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level
        return s


### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
# run some tests

tree = Tree()
tree.insert_with_loop(5)
tree.insert_with_loop(6)
tree.insert_with_loop(4)
tree.insert_with_loop(2)
tree.insert_with_loop(5) # attempt to insert duplicate
tree.insert_with_loop(3)
print("\n==============")
print(tree)

tree = Tree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(2)
tree.insert_with_recursion(5) # attempt to insert duplicate
tree.insert_with_recursion(3)
print("\n==============")
print(tree)

print(f"""
search for 8: {tree.search(8)}
search for 2: {tree.search(2)}
search for 3: {tree.search(3)}
""")

root = tree.get_root()
print("Minimum value stored in BST is", tree.min_value_node(root) )
print("Maximum value stored in BST is", tree.max_value_node(root) )

print("Deleting value 8 - root is", tree.delete_node(root, 8) )
print("Deleting value 3 - root is", tree.delete_node(root, 3) )
print(tree)

llist = [44,17,88,32,28,65,97,54,82,29,76,80,78]
tree = Tree()
for item in llist:
    tree.insert_with_recursion(item)

print(tree)

root = tree.get_root()
print("Deleting value 32 - root is", tree.delete_node(root, 32) )
print("Deleting value 65 - root is", tree.delete_node(root, 65) )
print(tree)

