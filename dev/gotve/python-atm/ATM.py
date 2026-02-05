import sys

from CardStorage import CardStorage
from CreditCard import CreditCard, CreditCardProvider
from InvalidAgeException import InvalidAgeException
from NegativeAmountOfMoney import NegativeAmountOfMoney
from MessageProvider import MessageProvider


class ATM:

    def __init__(self):
        self.show_main_message()
        self.user_input_handler()

    def show_main_message(self):
        MessageProvider.main_menu_message()

    def user_input_handler(self):
        match input():
            case '1':
                self.register_a_new_credit_card()
            case '2':
                self.deposit()
            case '3':
                self.withdraw()
            case '4':
                CardStorage.print_all_cards()
            case '5':
                self.delete_a_card()
            case '6':
                sys.exit()
            case _:  # used as "default" block like in java
                print("Invalid option \n")

    def register_a_new_credit_card(self):
        credit_card = CreditCard()
        print("Enter your first name")
        credit_card.firstname(input())

        print("Enter your last name")
        credit_card.lastname(input())

        try:
            print("Enter your age")
            person_age = input()

            try:
                self.validate_age(person_age)
            except InvalidAgeException:
                return

            credit_card.age(int(person_age))
        except ValueError:
            print("You cannot input letters in your age, please try again. \n")
            return

        MessageProvider.card_providers_message()

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
                    print("Invalid provider1")
                    MessageProvider.card_providers_message()

        print("Name your card")
        credit_card.set_card_name(input())

        print("Add a pincode to your card (numbers only)")
        while True:
            try:
                input_pincode = int(input())
                credit_card.set_card_pincode(input_pincode)
                break
            except ValueError:
                MessageProvider.invalid_input_message()

        print("Your card has been created successfully!\n")
        CardStorage.store_card(credit_card)

    def deposit(self):
        if not CardStorage.get_card_storage():
            print("No cards available \n")
            return
        else:
            while True:
                CardStorage.print_all_cards()
                MessageProvider.select_card_by_index()

                try:
                    card_index = int(input())
                except ValueError:
                    print("Cannot use letters as an index.\n")
                    break

                print("How much money do you want to deposit")

                try:
                    amount_of_money = int(input())

                    if amount_of_money <= 0:
                        raise NegativeAmountOfMoney

                    selected_card = CardStorage.get_card_by_index(card_index)
                    new_balance = selected_card.get_card_balance() + amount_of_money
                except ValueError:
                    print("Cannot use letters as amount of money.\n")
                    break
                except NegativeAmountOfMoney:
                    print("Cannot deposit a negative amount of money")
                    break

                CardStorage.deposit_money(card_index, new_balance)
                print("Operation succeed! \n")
                break

    def withdraw(self):
        while True:
            CardStorage.print_all_cards()
            MessageProvider.select_card_by_index()

            try:
                input_card = int(input())
            except ValueError:
                MessageProvider.invalid_input_message()
                break

            print("Enter the pincode")
            try:
                pincode_input = int(input())

                if pincode_input == CardStorage.get_card_pincode(input_card):
                    print("Pincode correct")
                else:
                    print("Invalid pincode, please try again")
                    break
            except ValueError:
                MessageProvider.invalid_input_message()
                return

            print("Choose amount of money to withdraw")
            try:
                withdraw_amount = int(input())
            except ValueError:
                MessageProvider.invalid_input_message()
                return

            CardStorage.withdraw(input_card, withdraw_amount)
            return

    def delete_a_card(self):
        CardStorage.print_all_cards()
        MessageProvider.select_card_by_index()

        while True:
            try:
                selected_card = int(input())
            except ValueError:
                MessageProvider.invalid_input_message()
                break

            print("Enter a password")
            try:
                pincode_input = int(input())
            except ValueError:
                MessageProvider.invalid_input_message()
                break

            if pincode_input == CardStorage.get_card_pincode(selected_card):
                CardStorage.delete_card(selected_card)
                break


    def validate_age(self, age):
        if int(age) < 18:
            print("You are too young to own a credit card \n")
            raise InvalidAgeException
