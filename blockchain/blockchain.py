import hashlib
import json
import random
import uuid
from datetime import date


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

    def proof_of_work(self, block):

    def create_hash(self, block):
        """
            Perform SHA-256 hashing algorithm on the following block to encrypt it
        :return: hashed block component
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


def generate_nonce(length=8):
    """
    Generate pseudorandom number.
    """
    return ''.join([str(random.randint(0, 9)) for i in range(length)])


if __name__ == '__main__':
    block_chain1 = Blockchain()
    block_chain2 = Blockchain()

    # New blocks to test difference hash functions on the block
    new_block1 = block_chain1.create_block(generate_nonce(), block_chain1.chain[0])
    new_block2 = block_chain2.create_block(generate_nonce(), block_chain2.chain[0])

    hash1 = block_chain1.create_hash(json.dumps(new_block1, indent=4, sort_keys=True, default=str))
    print(f"The first hash value corresponds to {hash1}")

    hash2 = block_chain1.create_hash(json.dumps(new_block2, indent=4, sort_keys=True, default=str))
    print(f"The first hash value corresponds to {hash2}")
    # hash1 = block_chain1.create_hash(new_block1)
    # hash2 = block_chain2.create_hash(new_block2)
    # print(hash1)
    # print(hash2)

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
