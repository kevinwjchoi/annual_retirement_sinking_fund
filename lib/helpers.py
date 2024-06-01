# lib/helpers.py

from models.account import Account
from models.transaction import Transaction
from datetime import datetime



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
            print(f'{account.name} has been updated')
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
    from cli import handle_transaction_menu
    name = input("enter account's name: ")
    account = Account.find_by_name(name)

    if account:
        print('\n')
        print(f'Name: {account.name}')
        print(f'Balance: {account.balance}')
        print(f'Taxed: {account.taxed}')
        print(f'Goal: {account.goal}')
        print('\n')
        handle_transaction_menu(account)
    else:
        print("This failed")
        


#Helpers for transactions tables 


def create_transaction(account):
    note = input("Enter transaction description note: ")
    amount = input("Enter transaction amount: ")
    valid_inputs = ["deposit", "withdrawal"]
    action = input("Is this a deposit or withdrawal? ")
    account_id = account.id
    timestamp = None
    while action.lower() not in valid_inputs:
        print("Invalid input, please enter either 'deposit' or 'withdrawal'.")
        action = input("Is this a deposit or withdrawal? ")
    try:
        transaction = Transaction.create(note, amount, action, account_id)
        print(f'You made a {transaction.action} of ${transaction.amount}.')
    except Exception as exc:
        print("Error creating transaction: ", exc)
    
def update_transaction(account):
    note = input("Enter transaction description note: ")
    amount = input("Enter transaction amount: ")
    valid_inputs = ["deposit", "withdrawal"]
    action = input("Is this a deposit or withdrawal? ")
    account_id = account.id
    while action.lower() not in valid_inputs:
        print("Invalid input, please enter either 'deposit' or 'withdrawal'.")
        action = input("Is this a deposit or withdrawal? ")
    try:
        transaction = Transaction.update(note, amount, action, account_id)
        print(f'You made a {transaction.action} of ${transaction.amount}.')
    except Exception as exc:
        print("Error updating transaction: ", exc)