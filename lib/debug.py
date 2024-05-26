
# from models.__init__ import CONN, CURSOR
# from models.sinking_fund import SinkingFund
# from models.transaction import Transaction
# import ipdb

# def reset_database():
#     Transaction.drop_table()
#     SinkingFund.drop_table()
#     SinkingFund.create_table()
#     Transaction.create_table()

#     #creating seed data 
#     savings_account = SinkingFund.create("Savings Account")
#     Transaction.create("name", "type", savings_account.id)

# reset_database()
# ipdb.set_trace()