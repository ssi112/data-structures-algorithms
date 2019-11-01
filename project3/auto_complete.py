"""
auto_complete.py
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
        #print("suffix=", suffix)
        for s in suffix:
            if s in node.children:
                node = node.children[s]
                #for key, val in node.children.items():
                #    result.append(key)
            else:
                return result
        self.find_letters(node, list(suffix), result)
        return result

    def find_letters(self, node, letters, result):
        if node.is_word:
            result.append(letters[:])
            #print("result.append(self.letters)", result)
        for key, next_node in node.children.items():
            letters.append(key)
            self.find_letters(next_node, letters, result)
            # pop last item in list
            letters.pop(-1)


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


wordList = ["ant", "anthology", "antagonist", "antonym",
            "fun", "function", "factory", "tensorflow",
            "trie", "trigger", "trigonometry", "tripod"
           ]

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

