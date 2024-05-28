from models.__init__ import CURSOR, CONN
from lib.models.account import Account

class Transaction:
    
    def __init__(self, id, name, amount, transaction_type, timestamp, account_id):
        self.id = id
        self.name = name
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = timestamp
        self.account_id = account_id

    # def __repr__(self):
    #     return (f"Transaction({self.transaction_id}, {self.amount}, "
    #             f"{self.transaction_type}, {self.timestamp}) , {self.account_id}")
    

    @classmethod
    def instance_from_db(cls, row):
        """Return an Transaction object having the attribute values from the table row."""
        transaction = cls.all.get(row[0])
        if transaction:
            transaction.name = row[1]
            transaction.amount = row[2]
            transaction.transaction_type = row[3]
            transaction.timestamp = row[4]
            transaction.account_id = row[5]


        else:
            transaction = cls(row[0], row[1], row[2], row[3], row[4], row[5])
            cls.all[transaction.id] = transaction
        return transaction
    