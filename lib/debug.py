
from models.__init__ import CONN, CURSOR
from models.account import Account
from models.transaction import Transaction



def reset_database():
    Transaction.drop_table()
    Account.drop_table()
    Account.create_table()
    Transaction.create_table()


    #Seed Data
    brokerage = Account.create("Brokerage",0.0, 1, 6000)
    transaction1 = Transaction.create("First deposit", 100.0, "deposit", 1)

reset_database()



