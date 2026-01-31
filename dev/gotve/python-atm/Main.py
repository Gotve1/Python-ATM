import sys

from Person import Person
from CreditCard import CreditCard, CreditCardProvider


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
            register_a_new_credit_card()
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
        case _:  # used as "default" block in java
            print("Invalid option")


def register_a_new_credit_card():
    person = Person()
    print("Enter your first name")
    person.set_firstname(input())

    print("Enter your last name")
    person.set_lastname(input())

    try:
        print("Enter your age")
        person_age = input()
        person.set_age(int(person_age))
    except ValueError:
        print("You cannot input letters in your age, please try again. \n")

    print(
        "Choose one of card providers \n"
        "1. Kapital Bank \n"
        "2. NBU Bank \n"
        "3. Infin Bank \n"
        "4, TBC Bank \n"
    )
    credit_card = CreditCard()
    match input():
        case '1':
            credit_card.set_credit_card_provider(CreditCardProvider.KAPITAL_BANK)
        case '2':
            credit_card.set_credit_card_provider(CreditCardProvider.NATIONAL_BANK_OF_UZBEKISTAN)
        case '3':
            credit_card.set_credit_card_provider(CreditCardProvider.INFIN_BANK)
        case '4':
            credit_card.set_credit_card_provider(CreditCardProvider.TBC_BANK)
        case _:
            print("Invalid bank provider")


if __name__ == "__main__":
    while True:
        main()
