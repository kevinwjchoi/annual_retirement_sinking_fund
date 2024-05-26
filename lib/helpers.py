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