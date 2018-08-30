from collections import OrderedDict

from utility.printable import Printable


class Transaction(Printable):
    """A transaction that can be added to a block.

    Attributes:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :signature: The signature of the transaction.
        :amount: The coin amount.
    """
    def __init__(self, sender, recipient, signature, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    def to_ordered_dict(self):
        return OrderedDict([
            ('sender', self.sender), 
            ('recipient', self.recipient), 
            ('amount', self.amount)])
