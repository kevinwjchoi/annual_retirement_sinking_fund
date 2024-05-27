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
