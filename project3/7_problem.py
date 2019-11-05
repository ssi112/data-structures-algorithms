
"""
7_problem.py

Implement an HTTPRouter like you would find in a typical web server using
the Trie data structure.

The purpose of an HTTP Router is to take a URL path like "/", "/about",
or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content
to return. In a dynamic web server, the content will often come from a
block of code called a handler.

"""


"""
A RouteTrieNode will be similar to our autocomplete TrieNode...
with one additional element, a handler.
"""
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = dict()
        self.handler = handler

    def insert(self, path, handler):
        # Insert the node as before
        for path_part in path:
            self.children[path_part]
        if handler:
            self.handler = handler
        else:
            self.handler = None


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        """
        Initialize the trie with a root node and a handler,
        this is the root path or home page node
        """
        self.root = RouteTrieNode()


    def insert(self, path, handler):
        """
        Similar to our previous example you will want to recursively
        add nodes. Make sure you assign the handler to only the leaf
        (deepest) node of this path
        """
        node = self.root
        for path_part in path:
            if path_part not in node.children:
                node.children[path_part] = RouteTrieNode()
            node = node.children[path_part]

    def find(self, path):
        """
        Starting at the root, navigate the Trie to find a match for
        this path. Return the handler for a match, or None for no match
        """
        if self.root is None:
            return None
        node = self.root
        for path_part in path:
            if path_part not in node.children:
                return None
            node = node.children[path_part]
        return node.handler



# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler):
        """
        Create a new RouteTrie for holding our routes. You could also
        add a handler for 404 page not found responses as well!
        """
        self.root = RouteTrieNode()
        self.handler = handler
        self.not_found = "HTTP 404 Page Not Found"

    def add_handler(self, path, handler):
        """
        Add a handler for a path. You will need to split the path and
        pass the parts as a list to the RouteTrie
        """
        node = self.root
        path_list = self.split_path(path)
        for path_part in path_list:
            if path_part not in node.children:
                # add the path if it doesn't exist
                node.insert(path_part)
            node = node.children[path_part]
        # at the end so can add the handler
        node.handler = handler


    def lookup(self, path):
        """
        Lookup path (by parts) and return the associated handler.
        You can return None if it's not found or return the "not found"
        handler if you added one.
        Bonus points if a path works with and without a trailing slash
        e.g. /about and /about/ both return the /about handler
        """
        if path == "/":
            return "got root!"

        node = self.root
        path_list = self.split_path(path)

        for path_part in path_list:
            if path_part not in node.children:
                return node.not_found
            node = node.children[path_part]
        return node.handler

    def split_path(self, path):
        """
        You need to split the path into parts for both the add_handler
        and lookup functions, so it should be placed in a function here
        """
        # if begins or ends with '/' they will be '' in the list
        path_list = path.split('/')
        # discard the empty strings
        if path_list[0] == '':
            path_list = path_list[1:]
        if path_list[-1] == '':
            path_list = path_list[:-1]
        print("path_list:", path_list)
        return path_list


# ----------------------------------------------------------------------
"""
Here are some test cases and expected outputs you can use to test your
implementation
"""

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route


# some lookups with the expected output

# should print 'root handler'
print(router.lookup("/"))

# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))

# should print 'about handler'
print(router.lookup("/home/about"))

# should print 'about handler' or None if you do not handle trailing slashes
print(router.lookup("/home/about/"))

# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))



