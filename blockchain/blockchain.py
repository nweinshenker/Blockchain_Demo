import hashlib
import random, uuid
import time

from flask import Flask


class Blockchain:
    """
        Definition of a block chain structure with list of
        transactions that correspond to the link of the chain
    """

    def __init__(self):
        self.transactions = []
        self.chain = []
        self.nodes = set()
        # Generate random number to be used as node_id
        self.node_id = str(uuid.uuid4()).replace('-', '')
        # Create genesis block
        self.create_block(0, '00')

    def generate_nonce(length=8):
        """
        Generate pseudorandom number.
        """
        return ''.join([str(random.randint(0, 9)) for i in range(length)])

    def create_block(self, nonce, previous_hash):
        """
        Builds a new block and uses the previous_hash from the corresponding old block
        as the new block's header
        :return: Returns a newly created block on the block chain
        """
        # Copy all the transactions from the previous node
        self.transactions = []
        self.chain[nonce] = '00'



    def create_hash(self, block):
        """
            Perform SHA-256 hashing algorithm on the following block to encrypt it
        :param blocks to hash
        :return: hashed block component
        """
        hash_block = hashlib.sha256(block).hexdigest()
        return self.chain[hash_block]


if __name__ == '__main__':
    block = Blockchain()



    # while True:
    #     action = input("Do you want to create a seperate hash block value"
    #                    "[Y]es or [N]o").upper()
    #     if action not in 'YN' or len(action) != 1:
    #         print("I'm not sure what {} command you enter: ".format(action))
    #     elif action == 'Y':
    #         print(str(block.compute_hash(block.node_id)))
    #     elif action == 'N':
    #         break
