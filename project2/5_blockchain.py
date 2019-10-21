"""
5_blockchain.py

build a link list to store basic blockchain data
the data in this example is just a random integer
"""

import hashlib
import datetime
import random

class Block(object):
    def __init__(self, data, previous_hash, previous_block):
        self.timestamp = datetime.datetime.now()
        self.data = data
        # this is a cryptographic hash of the previous block
        # helps prevent modification of data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous_block = previous_block

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) +
                    str(self.data) +
                    str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    @property
    def get_previous_hash(self):
        return self.previous_hash

    @property
    def get_hash(self):
        return self.hash

    def __repr__(self):
        the_block = ("\nBlock Attributes:" +
                     "\n   timestamp: " + str(self.timestamp) +
                     "\n   data: " + str(self.data) +
                     "\n   previous hash: " + str(self.previous_hash) +
                     "\n   hash: " + str(self.hash))
        return the_block


class Chain(object):
    def __init__(self, tail = None):
        self.tail = tail
        self.size = 0

    def get_size(self):
        return self.size

    def append(self, data):
        if data is None or data == "":
            return False

        if self.tail is None:
            self.tail = big_bang_block() # initialize
            self.size += 1
            return True

        new_block = create_new_block(data, self.tail)
        self.tail = new_block
        self.size += 1
        return True


def big_bang_block():
    """
    initial block in the chain
    data and previous hash are arbitrary
    """
    return Block( "1) the singularity", 0, None )


def create_new_block(data, previous_block):
    """
    helper function to creat a new block
    """
    some_data = str(data)
    last_hash = 0 if previous_block is None else previous_block.hash
    return Block(some_data, last_hash, previous_block)


def main():
    chain_link = Chain()
    # initialize the first block
    chain_link.append(big_bang_block())
    # add some more blocks for fun
    chain_link.append(random.randint(1, 9999))
    chain_link.append(random.randint(1, 9999))
    chain_link.append(random.randint(1, 9999))
    chain_link.append(random.randint(1, 9999))
    trap = chain_link.append("")
    if not trap:
        print("Uh oh, that didn't work. Try again, please!")

    print("\n-----Block Chain (link list test)-----")
    i = chain_link.get_size()
    print("\nLength of chain =", i)
    print("Going backwards through the blockchain")
    node = chain_link.tail

    while node:
        print("\nBlock #{} Attributes:".format(i))
        print("-----------------------" +
              "\n   timestamp: " + str(node.timestamp) +
              "\n   data: " + str(node.data) +
              "\n   previous hash: " + str(node.previous_hash) +
              "\n   hash: " + str(node.hash )
              )
        i -= 1
        node = node.previous_block


if __name__ == "__main__":
    main()
