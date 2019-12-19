
import hashlib;
import random, uuid
import time;

from flask import Flask

class Blockchain:
    """
        Definition of a block chain structure with list of
        transactions that correspond to the link of the chain
    """
    def __init__(self):
        self.current_transactions = []      # list of transactions that are happening within the block
        self.chain = []         # actual chain of blocks
        self.nodes = set()      # a set containing node_urls
        self.node_id = str(uuid.uuid4()).replace('-','')

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def generate_nonce(length=8):
        """Generate pseudorandom number."""
        return ''.join([str(random.randint(0, 9)) for i in range(length)])

    def create_hash(self, block):
        """
            Perform SHA-256 hashing algorithm on the following block to encrypt it
        :param block to hash
        :return: hashed block component
        """
        hash_block = hashlib.sha256(block).hexdigest()
        return self.chain[hash_block]



    # def create_node(self, nonce, previous_hash, index):
    #     self.nonce = generatenonce(8)


if __name__ == 'main':