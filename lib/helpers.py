# lib/helpers.py

from models.account import Account
# from models.transaction import Transaction
# from datetime import datetime

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
    for account in accounts:
        print(account)

        