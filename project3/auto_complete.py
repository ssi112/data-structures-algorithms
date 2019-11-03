"""
auto_complete.py

With a functioning Trie, add the ability to list suffixes to implement our
autocomplete feature. To do that, we need to implement a new function on the
TrieNode object that will return all complete word suffixes that exist below
it in the trie.

For example, if our Trie contains the words ["fun", "function", "factory"]
and we ask for suffixes from the f node, we would expect to receive
["un", "unction", "actory"] back from node.suffixes().

"""

from collections import defaultdict

class TrieNode:
    def __init__(self, word = None):
        ## Initialize this node in the Trie
        self.children = defaultdict(TrieNode) #dict()
        self.is_word = False
        self.word = word

    def insert(self, word):
        ## Add a child node in this Trie
        for char in word:
            self = self.children[char]
        self.is_word = True
        self.word = word

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        result = []
        node = self
        for s in suffix:
            if s in node.children:
                node = node.children[s]
            else:
                return result
        self.find_letters(node, suffix, result)
        return result

    def find_letters(self, node, letters, result):
        """
        create a list to store words
        for every item in children (letter => node)
        base case => if node is a leaf append word to list of words
        else => list of words += recursive call to collect letters in
        suffix as suffix += letter
        return list of words
        """
        for key, next_node in node.children.items():
            if next_node.is_word:
                result.append(letters+key)
            self.find_letters(next_node, letters+key, result)

    """
    ORIGINAL METHOD
    def find_letters(self, node, letters, result):
        if node.is_word:
            result.append(node.word) #(letters[:]) #(node.word)
            #print("result.append(self.letters)", result)
        for key, next_node in node.children.items():
            letters.append(key)
            self.find_letters(next_node, letters, result)
            # pop last item in list
            letters.pop(-1)
    """

    def find_word(self, word):
        ## Find the Trie node that represents this prefix
        if self is None:
            return None
        node = self
        for char in word:
            if char not in node.children:
                return (False, False)
            node = node.children[char]
        return (node.is_word, node.word)


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        if self.root is None:
            return None
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        node.word = word

    def find_word(self, prefix):
        ## Find the Trie node that represents this prefix
        if self.root is None:
            return None
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return (node.is_word, node.word)

    def find_words(self, suffix):
        if self.root is None:
            return None
        if suffix == '':
            return None
        node = self.root
        return node.suffixes(suffix)


wordList = ["ant", "anthology", "antagonist", "antonym",
            "fun", "function", "factory", "tensorflow",
            "trie", "trigger", "trigonometry", "tripod",
            "perfunctory", "zagnut", "zanzibar", "dredd",
            "persnickety"
           ]

# ----------------------------------------------------------------------
# test by calling it directly on the node class
root = TrieNode()
for word in wordList:
    root.insert(word)

print(root.suffixes('f'))   # 'fun', 'function', 'factory'

prefix_node = root.suffixes('f')

if prefix_node:
    for prefixes in prefix_node:
        print(''.join(prefixes))
else:
    print("not found")


# ----------------------------------------------------------------------
# test by calling the trie class
print("~"*70)

test_trie = Trie()
for word in wordList:
    test_trie.insert(word)

auto_words = test_trie.find_words('t')
print(auto_words)

if auto_words:
    print('\n'.join(auto_words))
else:
    print("not found")

