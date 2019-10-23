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
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # removed per reviewer's comments for additional test
        # default to 5 if zero or not an integer
        # self.capacity = capacity if capacity is not 0 and isinstance(capacity, int) else 5
        self.cache = OrderedDict()

    @property
    def get_capacity(self):
        return self.capacity

    def get(self, key):
        if key in self.cache.keys():
            """
            In Python 3 cache.keys() is O(1). In 2 it is O(n).
            pop removes item and then re-inserting it moves it to the back
            which makes it the most recently used/accessed
            """
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def set(self, key, value):
        try:
            if self.get_capacity <= 0:
                msg  = "\nError: Cannot have cache capacity of zero or less."
                msg += "\nCache capacity is " + str(self.get_capacity)
                msg += "\nCannot perform set operation on 0 or less sized cache!\n"
                raise ValueError(msg)
        except ValueError as ve:
            print(ve)
            return False
        if key in self.cache:
            # reinsert the same key
            # why? could have a different value so pop the key, discard it
            self.cache.pop(key)
            self.cache[key] = value
            return True
        else:
            if len(self.cache) >= self.capacity:
                """
                Per documentaion: returns and removes a (key, value) pair.
                Pairs are returned in LIFO order if last is true (default)
                or FIFO order if false
                """
                self.cache.popitem(last = False)
            self.cache[key] = value
        return True


print("\ncreate new cache to hold maximum five entries...\n")
our_cache = lru_cache(5)
print("Capacity of cache is ", our_cache.capacity)

print("setting key, value pairs: (1,1), (2,2), (3,3) & (4,4)")
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print("\nTest #1...")
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

# create new cache with different size
our_new_cache = lru_cache(2)
our_new_cache.set(1, 1)
our_new_cache.set(2, 2)
our_new_cache.set(1, 10)
print("\nTest #2...")
print("our_new_cache (should return 10):", our_new_cache.get(1))
print("our_new_cache (should return 2):", our_new_cache.get(2))

# create another cache with size 0
another_new_cache = lru_cache(-100)
print("\nTest #3...")
print("Capacity of cache is ", another_new_cache.capacity)

# should raise an exception
another_new_cache.set(1, 1)

print("another_new_cache (should return -1):", another_new_cache.get(1))


