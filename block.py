from time import time

from printable import Printable

class Block(Printable):
    def __init__(self, index, previous_hash, transactions, proof, time=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time() if time is None else time
        self.transactions = transactions
        self.proof = proof