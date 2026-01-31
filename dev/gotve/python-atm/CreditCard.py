import uuid
from enum import StrEnum


class CreditCard:

    def __init__(self):
        self.__card_number = uuid.uuid4()

    def get_card_number(self):
        return self.__card_number

    def set_card_balance(self, balance):
        self.__balance = balance

    def get_card_balance(self):
        return self.__balance

    def set_credit_card_provider(self, card_provider):
        self.__card_provider = card_provider

    def get_credit_card_provider(self):
        return self.__card_provider


class CreditCardProvider(StrEnum):
    KAPITAL_BANK = "Kapital Bank"
    NATIONAL_BANK_OF_UZBEKISTAN = "NBU Bank"
    INFIN_BANK = "Infin Bank"
    TBC_BANK = "TBC Bank"
