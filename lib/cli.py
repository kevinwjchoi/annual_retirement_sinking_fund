# lib/cli.py

from helpers import (
    exit_program,
    helper_1
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


def main_menu():
    print("Welcome to the Investment Contribution Tracker CLI!")
    print("What would you like to do?")
    print("1) Look at your account(s)?")
    print("2) Look at your transaction(s)?")
    print("3) Exit")

def handle_account_menu():
    ...

def handle_transaction_menu():
    ...        

if __name__ == "__main__":
    main()