# lib/helpers.py

from models.account import Account
from models.transaction import Transaction
# from datetime import datetime


#Helpers for accounts tables
def create_account():
    name = input("Enter name of the investment: ")
    balance = 0.0
    taxed = None
    goal = None
    while taxed not in [0, 1]:
        taxed = int(input("Is it taxed?\n 0) No or 1) Yes: "))
        if taxed not in [0, 1]:
            print("Invalid input. Please enter:\n 0) No or 1) Yes")
    while goal is None:
        try:
            goal = int(input("Enter the goal amount as an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer for the goal amount.")
    try:
        account = Account.create(name, balance, taxed, goal)
        print(f'Created {account.name} account')
    except Exception as exc:
        print("Error creating account: ", exc)

def update_account(): 
    name = input("Enter the account's name: ")
    if account := Account.find_by_name(name):
        try: 
            name = input("Enter new account name: ")
            account.name = name 
            taxed = int(input("Is it taxed?\n 0) No or 1) Yes: "))
            account.taxed = taxed 
            goal = int(input("Enter new account goal: "))
            account.goal = goal 

            account.update()
            print(f'{account} has been updated')
        except Exception as exc:
            print("Error updating account: ", exc)
    else: 
        print(f'Account {name} not found')

def delete_account():
    name = input("Enter account's name: ")
    if account := Account.find_by_name(name): 
        account.delete()
        print(f'Account {name} deleted')
    else: 
        print(f'Account {name} not found')

def list_accounts():
    accounts = Account.get_all()
    print('\n')
    print('List of accounts:')
    for account in accounts:
        print(f'Name: ' + account.name)
    print('\n')

def search_account():
    name = input("enter account's name: ")
    if account := Account.find_by_name(name): 
        print('\n')
        print(f'Name:  {account.name}')
        print(f'Balance: {account.balance}')
        print(f'Goal: {account.goal}')
        print('\n')


#Helpers for transactions tables 

def create_transaction():
    name = input("Enter transaction name: ")
    amount = input("Enter transaction amount: ")
    valid_inputs = ["deposit", "withdrawal"]
    transaction_type = input("Is this a deposit or withdrawal?")
    while transaction_type.lower() not in valid_inputs:
        print("Invalid input, please enter either 'deposit' or 'withdrawal'.")
        transaction_type = input("Is this a deposit or withdrawal? ")
    try:
        transaction = Transaction.create(name, amount, transaction_type)
        print(f'Created {transaction.name} transaction')
    except Exception as exc:
        print("Error creating transaction: ", exc)
    
