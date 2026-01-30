import sys

from Person import Person
from CreditCard import CreditCard

def main():
    print(
        "Please choose one of available options \n"
        "1. Register a new credit card \n"
        "2. Withdraw money \n"
        "3. Deposit money \n"
        "4. View my cards \n"
        "5. Delete a card \n"
        "6. Exit \n"
    )
    user_input_handler()


def user_input_handler():
    match input():
        case '1':
            print("you choosed option 1")
        case '2':
            print("you choosed option 2")
        case '3':
            print("you choosed option 3")
        case '4':
            print("you choosed option 4")
        case '5':
            print("you choosed option 5")
        case '6':
            sys.exit()
        case _:
            print("Invalid option")


if __name__ == "__main__":
    while True:
        main()
