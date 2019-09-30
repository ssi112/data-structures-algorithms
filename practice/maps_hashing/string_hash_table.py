"""
string_hash_table.py

Write your own hash table and hash function that uses string keys.
Your table will store strings in buckets by their first two letters,
according to the formula below:

Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter

You can assume that the string will have at least two letters, and the first two
characters are uppercase letters (ASCII values from 65 to 90). You can use the
Python function ord() to get the ASCII value of a letter, and chr() to get the
letter associated with an ASCII value.

You'll create a HashTable class, methods to store and lookup values, and a
helper function to calculate a hash value given a string.

You cannot use a Python dictionary—only lists!

And remember to store lists at each bucket, and not just the string itself.
For example, you can store "UDACITY" at index 8568
as ["UDACITY"].
"""


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """TODO: Input a string that's stored in
        the table."""
        hashed = self.calculate_hash_value(string)
        if hashed: # != -1:
            if self.table[hashed] != None:
                self.table[hashed].append(string)
            else:
                self.table[hashed] = [string]

    def lookup(self, string):
        """TODO: Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hashed = self.calculate_hash_value(string)
        if hashed: # != -1:
            if self.table[hashed] != None:
                if string in self.table[hashed]:
                    return hashed
        return -1

    def calculate_hash_value(self, string):
        """TODO: Helper function to calulate a
        hash value from a string."""
        return ord(string[0]) * 100 + ord(string[1])



hashish = HashTable()
print("hashish value (UDACITY) =", hashish.calculate_hash_value("UDACITY"))

print("hashish lookup (UDACITY) =", hashish.lookup("UDACITY"))

hashish.store("UDACITY")
print("hashish lookup (UDACITY) =", hashish.lookup("UDACITY"))

print("hashish lookup (UDACIOUS) =", hashish.lookup("UDACIOUS"))

hashish.store("Esteban")
print("hashish lookup (Esteban) =", hashish.lookup("Esteban"))
hashish.store("ESTEBAN")
print("hashish lookup (ESTEBAN) =", hashish.lookup("ESTEBAN"))

