# lib/cli.py

from helpers import (
    create_account
)

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            handle_account_menu()
        elif choice == '2':
            handle_transaction_menu()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def handle_account_menu():
    while True:
        account_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            ...
        elif choice == '3':
            ...
        elif choice == '4':
            ...
        elif choice == '5':
            ...    
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    print("Welcome to the Investment Contribution Tracker CLI!")
    print("What would you like to do?")
    print("1) Look at your account(s)?")
    print("2) Look at your transaction(s)?")
    print("3) Exit")

def account_menu():
    print("Account Menu:")
    print("1) Create an account")
    print("2) Update an account")
    print("3) Delete an account")
    print("4) Show all accounts")
    print("5) Back to Main Menu")

def handle_transaction_menu():
    print("Transaction Menu:")
    print("1) Create transaction")  
    print("2) Update transaction")   
    print("3) Delete transaction")   
    print("4) Back to Main Menu")   


if __name__ == "__main__":
    main()