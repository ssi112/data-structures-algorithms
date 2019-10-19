"""
1_lru_cache.py

For our first problem, the goal will be to design a data structure known as a
Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove
the least recently used entry when the cache memory reaches its limit.
For the current problem, consider both get and set operations as a use operation.

Your job is to ** use an appropriate data structure(s) to implement the cache **

    In case of a cache hit, your get() operation should return the appropriate value.
    In case of a cache miss, your get() should return -1.
    While putting an element in the cache, your put() / set() operation must insert the
    element. If the cache is full, you must write code that removes the least recently
    used entry first and then insert the element.

All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
Uses Pythons's OrderedDict as cache, which keeps track of the order that
entries are inserted. Deleting an entry and reinserting it will move it to the end.
If the value of a key is changed, the key position does not change.

Reference: https://docs.python.org/2/library/collections.html#collections.OrderedDict

Somewhat related implementation methodology (not in python)
https://www.geeksforgeeks.org/lru-cache-implementation/
"""

from collections import OrderedDict

class lru_cache(object):
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache.keys():
            """
            pop removes item and then re-inserting it moves it to the back
            which makes it the most recently used/accessed
            """
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def set(self, key, value):
        if key in self.cache:
            # reinsert the same key
            # why? could have a different value so pop the key, discard it
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                """
                Per documentaion: returns and removes a (key, value) pair.
                Pairs are returned in LIFO order if last is true (default)
                or FIFO order if false
                """
                self.cache.popitem(last = False)
            self.cache[key] = value


print("\ncreate new cache to hold maximum five entries...\n")
our_cache = lru_cache(5)

print("setting key, value pairs: (1,1), (2,2), (3,3) & (4,4)")
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print()
print("Returns 1 - our_cache.get(1):", our_cache.get(1))
print("Returns 2 - our_cache.get(2):", our_cache.get(2))
print("Returns -1 - our_cache.get(9):", our_cache.get(9))
print("  (because 9 is not present in the cache)")

print("\nSetting key, value pairs: (5, five), (6, six)")
our_cache.set(5, "five")
our_cache.set(6, "six")

# returns -1 because the cache reached it's capacity and 3 was the least
# recently used entry
print("\nour_cache.get(3):", our_cache.get(3))
print("Returned -1 because the cache reached it's capacity and 3 was the least recently used entry")
print("\nReturns 'five' - our_cache.get(5):", our_cache.get(5))
print("Returns 'six' - our_cache.get(6):", our_cache.get(6))
