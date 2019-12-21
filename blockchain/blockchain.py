

import hashlib
import json
import random, uuid
from datetime import date

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

    def create_block(self, nonce, previous_hash):
        """
        Builds a new block and uses the previous_hash from the corresponding old block
        as the new block's header
        :return: Returns a newly created block on the block chain
        """
        # Copy all the transactions from the previous node
        block = {'block_number': len(self.chain) + 1,
                'timestamp': date.today(),
                'transactions': self.transactions,
                'nonce': nonce,
                'previous_hash': previous_hash
                }

        self.transactions = []  # reset the following block node
        self.chain.append(block)
        return block





    def create_hash(self, block):
        """
            Perform SHA-256 hashing algorithm on the following block to encrypt it
        :param blocks to hash
        :return: hashed block component
        """
        hash_block = hashlib.sha256(block).hexdigest()
        return self.chain[hash_block]


def generate_nonce(length=8):
    """
    Generate pseudorandom number.
    """
    return ''.join([str(random.randint(0, 9)) for i in range(length)])


if __name__ == '__main__':


    """
        Tested the functionality of generating a random nonce
    """
    # block = Blockchain()
    # print(f"The initial block transactions " + str(block.transactions))
    # list = []
    # while True:
    #     nonce = generate_nonce()
    #     if nonce not in list:
    #         list.append(nonce)
    #         print(nonce)
    #     else:
    #         print("This is not a valid nonce")
    #         break

    # y = json.dumps(block, indent=4, sort_keys=True)
    # print(f"The following object has the json dump of" + y)


