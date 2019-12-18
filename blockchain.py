
class Block:

    def __int__(self, nonce, time_stamp, index, previous_hash, hash):
        self.nonce = nonce
        self.time_stamp = time_stamp
        self.index = index
        self.previous_hash = previous_hash
        self.hash = hash


    def calculate_hash(self):
