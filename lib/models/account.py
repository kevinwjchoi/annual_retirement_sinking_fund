from models.__init__ import CURSOR, CONN
from datetime import datetime

class Account:
    all ={}
    
    def __init__(self, account_id, name, balance=0.0, taxed=False, date_created=None, goal=None):
        self.account_id = account_id
        self.name = name
        self.balance = balance
        self.taxed = taxed
        self.date_created = date_created if date_created else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.goal = goal

    # def __repr__(self):
    #     return (f"Account({self.account_id}, {self.name}, {self.balance}, {self.taxed}, "
    #             f"{self.date_created}, {self.goal})")

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = balance

    @property
    def taxed(self):
        return self._taxed

    @taxed.setter
    def taxed(self, taxed):
        if taxed not in [0, 1]:
            raise ValueError("Taxed must be 0 (False) or 1 (True)")
        self._taxed = int(taxed)

    @property
    def date_created(self):
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        self._date_created = date_created

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, goal):
        if goal is not None and goal < 0:
            raise ValueError("Goal cannot be negative")
        self._goal = goal



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
    

    @classmethod
    def instance_from_db(cls, row):
        """Return an Account object having the attribute values from the table row."""
        account = cls.all.get(row[0])
        if account:
            account.name = row[1]
            account.balance = row[2]
            account.taxed = bool(row[3])
            account.date_created = row[4]
            account.goal = row[5]
        else:
            account = cls(row[0], row[1], row[2], bool(row[3]), row[4], row[5])
            cls.all[account.account_id] = account
        return account
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Department object per row in the table"""
        sql = """
            SELECT *
            FROM accounts
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Account object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM accounts
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Account object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM accounts
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def transactions(self):
        """Return list of transaction of the department"""
        from models.transaction import Transaction
        sql = """
            SELECT * FROM transactions
            WHERE account_id = ?
        """
        CURSOR.execute(sql, (self.id),)

        rows = CURSOR.fetchall()
        return[
            Transaction.instance_from_db(row) for row in rows
        ]