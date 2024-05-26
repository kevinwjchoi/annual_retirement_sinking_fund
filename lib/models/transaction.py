from models.__init__ import CURSOR, CONN
from lib.models.account import Account

class Transaction:
    
    def __init__(self, transaction_id, account_id, amount, transaction_type, timestamp):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = timestamp

    def __repr__(self):
        return (f"Transaction({self.transaction_id}, {self.account_id}, {self.amount}, "
                f"{self.transaction_type}, {self.timestamp})")