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
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name 
        else: 
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        if isinstance(amount, float):
            self._amount = amount
        else:
            raise ValueError(
                "Amount must be a float"
            )

    @property
    def transaction_type(self):
        return self._transaction_type
    
    @transaction_type.setter
    def transaction_type(self, transaction_type):
        if isinstance(transaction_type, str):
            self._transaction_type = transaction_type
        else:
            raise ValueError(
                "Transaction type must be a non-empty string"
            )
    
    @property 
    def timestamp(self):
        return self._timestamp
    
    @timestamp.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp
    
    @property
    def account_id(self):
        return self._account_id
    
    @account_id.setter  
    def account_id(self, account_id):
        self._account_id = account_id
    

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Transaction instances """
        sql = """
            CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            name TEXT,
            amount REAL,
            transaction_type TEXT,
            timestamp TEXT,
            account_id INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Transaction instances """
        sql = """
            DROP TABLE IF EXISTS transaction;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the transaction attributes or update if it exists """
        if self.id is None:
            sql = """
                INSERT INTO transactions (name, amount, transaction_type, timestamp, account_id)
                VALUES (?, ?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.amount, self.transaction_type, self.timestamp, self.account_id))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            self.update()
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, amount, transaction_type):
        """ Initialize a new Account instance and save the object to the database """
        account = cls(None, name, amount, transaction_type, None, None)
        account.save()
        return account

    def update(self):
        """Update the table row corresponding to the current Account instance."""
        sql = """
            UPDATE transactions
            SET name = ?, amount = ?, transaction_type = ?, timestamp = ?, account_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.amount, self.transaction_type, self.timestamp, self.account_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Transaction instance,
        delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM transactions
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

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
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Transaction object per row in the table"""
        sql = """
            SELECT *
            FROM transactions
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Transaction object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM transaction
            WHERE id = ?
        """
    
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Transaction object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM transactions
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None