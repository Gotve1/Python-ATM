import uuid
from enum import StrEnum
from uuid import UUID

from Person import Person


class CreditCard(Person):
    __card_number: UUID
    __balance: int
    __card_provider: CreditCardProvider
    __card_name: str
    __pincode: int

    # Getters and setters
    def __init__(self):
        super().__init__()
        __card_number = uuid.uuid4()

    def get_card_number(self):
        return self.__card_number

    def set_card_balance(self, balance):
        __balance = balance

    def get_card_balance(self):
        return self.__balance

    def set_credit_card_provider(self, card_provider):
        __card_provider = card_provider

    def get_credit_card_provider(self):
        return self.__card_provider

    def set_card_name(self, card_name):
        __card_name = card_name

    def get_card_name(self):
        return self.__card_name

    def set_card_pincode(self, pincode):
        __pincode = pincode

    def get_pincode(self):
        return self.__pincode


class CreditCardProvider(StrEnum):
    KAPITAL_BANK = "Kapital Bank"
    NATIONAL_BANK_OF_UZBEKISTAN = "NBU Bank"
    INFIN_BANK = "Infin Bank"
    TBC_BANK = "TBC Bank"
