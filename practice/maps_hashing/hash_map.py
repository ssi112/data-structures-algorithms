"""
hash_map.py

hash functions map data of any size to a fixed and unique value for storing

Refer to Jupyter Notebook HashMap.ipynb for further explanation of key
concepts used. Though this source duplicates the code it does not have
the full explanations.
"""


"""
For a given string, say abcd, a simple hash function can be sum of
corresponding ASCII values multiplied by a prime number and raised to a power.

Note: use ord(character) to determine ASCII value of a particular character
e.g. ord('a') will return 97

Similarly, we can treat abcde as
𝑎∗𝑝4 + 𝑏∗𝑝3 + 𝑐∗𝑝2 + 𝑑∗𝑝1 + 𝑒∗𝑝0

Here, we replace each character with its corresponding ASCII value.

This hash function is one of the most popular functions used for strings.
We use prime numbers because the provide a good distribution.
The most common prime numbers used for this function are 31 and 37.

We can get a corresponding integer value for each string key and store it in an array.
"""
def hash_function(string):
    hash_code = 0
    exp = len(string) - 1
    prime = 37
    for character in string:
        hash_code += (ord(character) * (prime ** exp))
        # print(character, exp, (prime**exp))
        exp -= 1
    return hash_code

hash_code_1 = hash_function("abcd")
print("hash code for 'abcd' is", hash_code_1)
hash_code_1 = hash_function("dcba")
print("hash code for 'dcba' is", hash_code_1)
hash_code_1 = hash_function("bcda")
print("hash code for 'bcda' is", hash_code_1)


"""
Linked list is used to handle collisions that might occur

Closed Addressing or Separate Chaining
Use the same bucket to store multiple objects. The bucket in this case will
store a linked list of key-value pairs. Every bucket has it's own separate
chain of linked list nodes.
"""
class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


"""
Get a corresponding integer value for each string key and store it in an array

The array used for this purpose is called a bucket array.
It is not a special array. We simply choose to give a special name to arrays
for this purpose. Each entry in this bucket array is called a bucket and the
index in which we store a bucket is called bucket index.

Also note the hash code method is different than the above in that the exponent
to raise the prime number begins at one instead of ending at zero.

Finally, it uses compression to create array values of reasonable size.
If we have an array of size 10, we can be sure that modulo of any number with 10
will be less than 10, allowing it to fit into our bucket array.

!!! Using compression increases likelhood of COLLISIONS !!!

https://www.geeksforgeeks.org/hashing-set-2-separate-chaining/

"""
class HashMap:
    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        self.load_factor = 0.7

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)
        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at
        # the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1

        # check for load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()

    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def get_bucket_index(self, key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            # compress the hash_code
            hash_code = hash_code % num_buckets
            current_coefficient *= self.p
            # compress the coefficient
            current_coefficient = current_coefficient % num_buckets
        return hash_code % num_buckets # one last compression

    def size(self):
        return self.num_entries

    # see notes in HashMap.ipynb, but the bucket array size changes
    # which results in a different compression so the index will change
    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]

        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                # we can use our put() method to rehash
                self.put(key, value)
                head = head.next

    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]
        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next


hash_map = HashMap()
hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)
hash_map.put("abcd", 9)
hash_map.put("dcba", 13)

print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("abcd: {}".format(hash_map.get("abcd")))
print("dcba: {}".format(hash_map.get("dcba")))
print("size: {}".format(hash_map.size()))

hash_map.delete("one")

print(hash_map.get("one"))
print(hash_map.size())

