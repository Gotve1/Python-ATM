import uuid
from enum import StrEnum

from Person import Person


class CreditCard(Person):

    # Getters and setters
    def __init__(self):
        super().__init__()
        self.__card_number = uuid.uuid4()
        self.__balance = 0

    def get_card_number(self):
        return self.__card_number

    def set_card_balance(self, balance):
        self.__balance = balance
        return self

    def get_card_balance(self):
        return self.__balance

    def set_credit_card_provider(self, card_provider):
        self.__card_provider = card_provider
        return self

    def get_credit_card_provider(self):
        return self.__card_provider

    def set_card_name(self, card_name):
        self.__card_name = card_name
        return self

    def get_card_name(self):
        return self.__card_name

    def set_card_pincode(self, pincode):
        self.__pincode = pincode
        return self

    def get_pincode(self):
        return self.__pincode


class CreditCardProvider(StrEnum):
    KAPITAL_BANK = "Kapital Bank"
    NATIONAL_BANK_OF_UZBEKISTAN = "NBU Bank"
    INFIN_BANK = "Infin Bank"
    TBC_BANK = "TBC Bank"
