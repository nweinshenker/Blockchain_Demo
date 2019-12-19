
import hashlib;
import random
import time;

from flask import Flask

class Blockchain:
    """
        Definition of a block chain structure with list of
        transactions that correspond to the link of the chain
    """
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = []

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def generate_nonce(length=8):
        """Generate pseudorandom number."""
        return ''.join([str(random.randint(0, 9)) for i in range(length)])

    def create_hash(self, node):
        """

        :param node:
        :return:
        """



    # def create_node(self, nonce, previous_hash, index):
    #     self.nonce = generatenonce(8)


def main():

    b = Blockchain({}, {}, {} , 00000000000000)

if __name__ == 'main':
    main()