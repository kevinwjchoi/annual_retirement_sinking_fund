# lib/cli.py

from helpers import (
    create_account,
    update_account,
    delete_account,
    list_accounts,
    search_account,
    create_transaction,
    update_transaction
)

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            handle_account_menu()
        elif choice == '2':
            ...
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
            list_accounts()
        elif choice == '2':
            search_account()
        elif choice == '3':
            create_account()
        elif choice == '4':
            update_account()
        elif choice == '5':
            delete_account()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def handle_transaction_menu(account):
    while True:
        transaction_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            create_transaction(account)
        elif choice == '2':
            update_transaction(account)
        elif choice == '3':
            ...
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    print("\n")
    print("Welcome to the Investment Contribution Tracker CLI!")
    print("What would you like to do?")
    print("1) Look at your account(s)?")
    print("2) Look at examples of different types of accounts?")
    print("3) Exit")

def account_menu():
    print("\n")
    print("Account Menu:")
    print("1) Show all accounts")
    print("2) Select account by name search")
    print("3) Create an account")
    print("4) Update an account")
    print("5) Delete an account")
    print("6) Back to Main Menu")

def transaction_menu():
    print("\n")
    print("What would you like to do?")
    print("1) Create transaction")  
    print("2) Update transaction")   
    print("3) Delete transaction")   
    print("4) Back to Account Menu")   


if __name__ == "__main__":
    main()