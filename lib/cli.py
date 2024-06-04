# lib/cli.py

from helpers import (
    create_account,
    update_account,
    delete_account,
    list_accounts,
    search_account,
    create_transaction,
    update_transaction,
    show_transactions,
    show_all_transactions,
    delete_transaction
    
)

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            handle_account_menu()
        elif choice == '2':
            account_examples()
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
            show_all_transactions()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def handle_transaction_menu(account):
    while True:
        transaction_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            show_transactions(account)
        elif choice == '2':
            create_transaction(account)
        elif choice == '3':
            update_transaction(account)
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
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
    print("Enter a number that corresponds to the menu")
    print("1) Show all accounts")
    print("2) Select account by name search")
    print("3) Create an account")
    print("4) Update an account")
    print("5) Delete an account")
    print("6) Show all accounts' transactions") 
    print("7) Back to Main Menu")

def transaction_menu():
    print("\n")
    print("What would you like to do?")
    print("Enter a number that corresponds to the menu")
    print("1) Show transactions")
    print("2) Create transaction")  
    print("3) Update transaction")   
    print("4) Delete transaction")   
    print("5) Back to Account Menu")   

def account_examples():
    print("\n")
    print("---- Example Accounts ----")
    print("Health Savings Account (HSA)")
    print("Brokerage Account")
    print("High Yield Savings Account")
    print("401k")



if __name__ == "__main__":
    main()