"""
5x_blockchain.py

A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to
the other blocks in the chain. Each block contains a cryptographic hash
of the previous block, a timestamp, and transaction data.

For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time
when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

Some related info on blockchains
https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b
http://adilmoujahid.com/posts/2018/03/intro-blockchain-bitcoin-python/

https://www.tutorialspoint.com/python_blockchain/python_blockchain_introduction.htm
https://ecomunsing.com/build-your-own-blockchain

"""

import hashlib
import datetime
import random


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        # this is a cryptographic hash of the previous block
        # helps prevent modification of data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        """
        encrypt the data
        """
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) +
                    str(self.data) +
                    str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        the_block = ("\nBlock Attributes:" +
                     "\n   timestamp: " + str(self.timestamp) +
                     "\n   data: " + str(self.data) +
                     "\n   previous hash: " + str(self.previous_hash) +
                     "\n   hash: " + str(self.hash))
        return the_block


def big_bang_block():
    """
    initial block in the chain
    data and previous hash are arbitrary
    """
    return Block( datetime.datetime.now(), "1) the singularity", 0 )


def create_new_block(data, previous_block):
    t_stamp = datetime.datetime.now()
    some_data = str( data )
    last_hash = previous_block.hash
    return Block(t_stamp, some_data, last_hash)


# build a link list to store blockchain data

# we'll start with a list for simplicity
blockchain = []

def main():
    # create the initial block to begin the chain
    blockchain.append( big_bang_block() )

    # pass initial block as the previous block and create new block
    another_block = create_new_block(random.randint(1, 9999), blockchain[0])
    blockchain.append(another_block)

    # add a some more test blocks
    another_block = create_new_block(random.randint(1, 9999), another_block)
    blockchain.append(another_block)

    another_block = create_new_block(random.randint(1, 9999), another_block)
    blockchain.append(another_block)

    another_block = create_new_block(random.randint(1, 9999), another_block)
    blockchain.append(another_block)

    another_block = create_new_block(random.randint(1, 9999), another_block)
    blockchain.append(another_block)

    print("\n---block chain---")
    print("length of chain =", len(blockchain))
    for block_heads in blockchain:
        print(block_heads)
    print()


if __name__ == "__main__":
    main()
