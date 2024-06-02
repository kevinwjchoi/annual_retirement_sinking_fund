from models.__init__ import CURSOR, CONN
from datetime import datetime
from models.account import Account

class Transaction:
    all ={}
    
    def __init__(self, id, note, amount, action, timestamp, account_id):
        self.id = id
        self.note = note
        self.amount = amount
        self.action = action
        self.timestamp = timestamp or datetime.now().isoformat()
        self.account_id = account_id

    # def __repr__(self):
    #     return (f"Transaction({self.transaction_id}, {self.a
    # mount}, "
    #             f"{self.action}, {self.timestamp}) , {self.account_id}")
    
    @property
    def note(self):
        return self._note
    
    @note.setter
    def note(self, note):
        if isinstance(note, str) and len(note):
            self._note = note 
        else: 
            raise ValueError(
                "note must be a non-empty string"
            )

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount
        # if isinstance(amount, int):
        #     self._amount = amount
        # else:
        #     raise ValueError(
        #         "Amount must be a whole integer"
        #     )

    @property
    def action(self):
        return self._action
    
    @action.setter
    def action(self, action):
        if isinstance(action, str):
            self._action = action
        else:
            raise ValueError(
                "Transaction type must be a non-empty string"
            )
    
    @property 
    def timestamp(self):
        return self._timestamp
    
    @timestamp.setter
    def timestamp(self, timestamp):
        if isinstance(timestamp, str):
            self._timestamp = timestamp
        else:
            raise ValueError("Timestamp must be a string")
    
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
            note TEXT,
            amount REAL,
            action TEXT,
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
                INSERT INTO transactions (note, amount, action, timestamp, account_id)
                VALUES (?, ?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.note, self.amount, self.action, self.timestamp, self.account_id))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            self.update()
        type(self).all[self.id] = self
        self.update_account_balance()


    @classmethod
    def create(cls, note, amount, action, account_id):
        """ Initialize a new Transaction instance and save the object to the database """
        transaction = cls(None, note, amount, action, None, account_id)
        transaction.save()
        return transaction

    def update(self):
        """Update the table row corresponding to the current Transaction instance."""
        sql = """
            UPDATE transactions
            SET note = ?, amount = ?, action = ?, timestamp = ?, account_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.note, self.amount, self.action, self.timestamp, self.account_id, self.id))
        CONN.commit()
        self.update_account_balance()


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
        self.update_account_balance()


    @classmethod
    def instance_from_db(cls, row):
        """Return an Transaction object having the attribute values from the table row."""
        transaction = cls.all.get(row[0])
        if transaction:
            transaction.note = row[1]
            transaction.amount = row[2]
            transaction.action = row[3]
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
    def find_by_note(cls, note):
        """Return a Transaction object corresponding to first table row matching specified note"""
        sql = """
            SELECT *
            FROM transactions
            WHERE note is ?
        """

        row = CURSOR.execute(sql, (note,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def update_account_balance(self):
        account = Account.find_by_id(self.account_id)
        if account:
            calculate_and_update_balance(account)