
from models.__init__ import CONN, CURSOR
from models.account import Account
# from models.transaction import Transaction


def reset_database():
    # Transaction.drop_table()
    Account.drop_table()
    Account.create_table()
    # Transaction.create_table()



breakpoint()
