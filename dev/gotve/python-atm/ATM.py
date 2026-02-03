import sys

from CardStorage import CardStorage
from CreditCard import CreditCard, CreditCardProvider
from InvalidAgeException import InvalidAgeException


class ATM:

    def __init__(self):
        self.show_main_message()
        self.user_input_handler()

    def show_main_message(self):
        print(
            "Please choose one of available options \n"
            "1. Register a new credit card \n"
            "2. Deposit money \n"
            "3. Withdraw money \n"
            "4. View cards \n"
            "5. Delete a card \n"
            "6. Exit \n"
        )

    def user_input_handler(self):
        match input():
            case '1':
                self.register_a_new_credit_card()
            case '2':
                self.deposit()
            case '3':
                # self.withdraw()
                print("")
            case '4':
                CardStorage.print_all_cards()
            case '5':
                print("you choosed option 5")
            case '6':
                sys.exit()
            case _:  # used as "default" block in java
                print("Invalid option")

    def register_a_new_credit_card(self):
        credit_card = CreditCard()
        print("Enter your first name")
        credit_card.set_firstname(input())

        print("Enter your last name")
        credit_card.set_lastname(input())

        try:
            print("Enter your age")
            person_age = input()

            try:
                self.validate_age(person_age)
            except InvalidAgeException:
                return

            credit_card.set_age(int(person_age))
        except ValueError:
            print("You cannot input letters in your age, please try again. \n")
            return

        print(
            "Choose one of card providers \n"
            "1. Kapital Bank \n"
            "2. NBU Bank \n"
            "3. Infin Bank \n"
            "4. TBC Bank"
        )
        while True:
            match input():
                case '1':
                    credit_card.set_credit_card_provider(CreditCardProvider.KAPITAL_BANK)
                    break
                case '2':
                    credit_card.set_credit_card_provider(CreditCardProvider.NATIONAL_BANK_OF_UZBEKISTAN)
                    break
                case '3':
                    credit_card.set_credit_card_provider(CreditCardProvider.INFIN_BANK)
                    break
                case '4':
                    credit_card.set_credit_card_provider(CreditCardProvider.TBC_BANK)
                    break
                case _:
                    print(
                        "Invalid bank provider select one of available card providers: \n"
                        "1. Kapital Bank \n"
                        "2. NBU Bank \n"
                        "3. Infin Bank \n"
                        "4. TBC Bank"
                    )

        print("Name your card")
        credit_card.set_card_name(input())

        print("Add a pincode to your card (numbers only)")
        while True:
            try:
                input_pincode = int(input())
                credit_card.set_card_pincode(input_pincode)
                break
            except ValueError:
                print(
                    "Cannot use letters or special characters in pincode \n"
                    "Please try again"
                )

        print("Your card has been created successfully!\n")
        CardStorage.store_card(credit_card)

    def deposit(self):
        if not CardStorage.get_card_storage():
            print("No cards available \n")
            return
        else:
            while True:
                CardStorage.print_all_cards()
                print("Select a card to make a deposit (by index)")

                try:
                    card_index = int(input())
                except ValueError:
                    print("Cannot use letters as an index.\n")
                    break

                print("How much money do you want to deposit")

                try:
                    amount_of_money = int(input())
                except ValueError:
                    print("Cannot use letters as amount of money.\n")
                    break

                CardStorage.deposit_money(card_index, amount_of_money)
                print("Operation succeed! \n")

    # def withdraw(self):

    def validate_age(self, age):
        if int(age) < 18:
            print("You are too young to own a credit card \n")
            raise InvalidAgeException
