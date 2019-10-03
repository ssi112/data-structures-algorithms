"""
lru_cache.py

Borrowed from:
    https://gist.github.com/reterVision/5018901#file-lru-py-L12

"""

from datetime import datetime
from time import sleep

class LRUCacheItem(object):
    """Data structure of items stored in cache"""
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.timestamp = datetime.now()


class LRUCache(object):
    """A sample class that implements LRU algorithm"""

    def __init__(self, length, delta=None):
        self.length = length
        self.delta = delta
        self.hash = {}
        self.item_list = []

    def insertItem(self, item):
        """Insert new items to cache"""

        if item.key in self.hash:
            # Move the existing item to the head of item_list.
            item_index = self.item_list.index(item)
            self.item_list[:] = self.item_list[:item_index] + self.item_list[item_index+1:]
            self.item_list.insert(0, item)
        else:
            # Remove the last item if the length of cache exceeds the upper bound.
            if len(self.item_list) > self.length:
                self.removeItem(self.item_list[-1])

            # If this is a new item, just append it to
            # the front of item_list.
            self.hash[item.key] = item
            self.item_list.insert(0, item)

    def removeItem(self, item):
        """Remove those invalid items"""

        del self.hash[item.key]
        del self.item_list[self.item_list.index(item)]

    def validateItem(self):
        """Check if the items are still valid."""

        def _outdated_items():
            now = datetime.now()
            for item in self.item_list:
                time_delta = now - item.timestamp
                if time_delta.seconds > self.delta:
                    yield item
        map(lambda x: self.removeItem(x), _outdated_items())

    def print_cache(self, cache):
        for i, item in enumerate(cache.item_list):
            print ("index: {0} "
                   "key: {1} "
                   "item: {2} "
                   "timestamp: {3}".format(i,
                                           item.key,
                                           item.item,
                                           item.timestamp))

one = LRUCacheItem(1, 'one')
two = LRUCacheItem(2, 'two')
three = LRUCacheItem(3, 'three')

print("Initial cache items.")
cache = LRUCache(length=3, delta=5)
cache.insertItem(one)
cache.insertItem(two)
cache.insertItem(three)
cache.print_cache(cache)
print("#" * 20)

print("Insert a existing item: {0}.".format(one.key))
cache.insertItem(one)
cache.print_cache(cache)
print("#" * 20)

print("Insert another existing item: {0}.".format(two.key))
cache.insertItem(two)
cache.print_cache(cache)
print("#" * 20)

print("Validate items after a period of time")
sleep(6)
cache.validateItem()
cache.print_cache(cache)
print("#" * 20)
