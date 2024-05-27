# lib/helpers.py

from models.account import Account
from models.transaction import Transaction
from datetime import datetime

def create_account():
    name = input("Enter name of the investment: ")
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
        account = Account.create(name, taxed, goal)
        print(f'Created {account.name} account')
    except Exception as exc:
        print("Error creating account: ", exc)

def update_account(): 
    id_ = input("Enter the account's id: ")
    if account := Account.find_by_id(id_):
        try: 
            name = input("Enter new account name: ")
            account.name = name 
            taxed = input("Is it taxed?\n 0) No or 1) Yes: ")
            account.taxed = taxed 
            goal = input("Enter new account goal: ")
            account.goal = goal 

            account.update()
            print(f'{account} has been updated')
        except Exception as exc:
            print("Error updating account: ", exc)
    else: 
        print(f'Account {id_} not found')

def delete_account():
    id_ = input("Enter account's id: ")
    if account := Account.find_by_id(id_): 
        account.delete()
        print(f'Account {id_} deleted')
    else: 
        print(f'Account {id_} not found')