from models.__init__ import CURSOR, CONN
from datetime import datetime

class Account:
    def __init__(self, account_id, name, balance=0.0, taxed=False, date_created=None, goal=None):
        self.account_id = account_id
        self.name = name
        self.balance = balance
        self.taxed = taxed
        self.date_created = date_created if date_created else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.goal = goal

    def __repr__(self):
        return (f"Account({self.account_id}, {self.name}, {self.balance}, {self.taxed}, "
                f"{self.date_created}, {self.goal})")


    
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

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Account instances """
        sql = """
            CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY,
            name TEXT,
            balance REAL,
            taxed INTEGER,
            date_created TEXT,
            goal REAL
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Account instances """
        sql = """
            DROP TABLE IF EXISTS accounts;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the account attributes or update if it exists """
        if self.account_id is None:
            sql = """
                INSERT INTO accounts (name, balance, taxed, date_created, goal)
                VALUES (?, ?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.balance, self.taxed, self.date_created, self.goal))
            CONN.commit()
            self.account_id = CURSOR.lastrowid
        else:
            self.update()
        type(self).all[self.account_id] = self

    @classmethod
    def create(cls, name, balance=0.0, taxed=False, goal=None):
        """ Initialize a new Account instance and save the object to the database """
        account = cls(None, name, balance, taxed, None, goal)
        account.save()
        return account
    
    def update(self):
        """Update the table row corresponding to the current Account instance."""
        sql = """
            UPDATE accounts
            SET name = ?, balance = ?, taxed = ?, date_created = ?, goal = ?
            WHERE account_id = ?
        """
        CURSOR.execute(sql, (self.name, self.balance, self.taxed, self.date_created, self.goal, self.account_id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Account instance,
        delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM accounts
            WHERE account_id = ?
        """
        CURSOR.execute(sql, (self.account_id,))
        CONN.commit()
        del type(self).all[self.account_id]
        self.account_id = None