import uuid
from enum import StrEnum

from Person import Person


class CreditCard(Person):

    # Getters and setters
    def __init__(self):
        super().__init__()
        self.__card_number = uuid.uuid4()
        self.__card_balance = 0
        self.__card_provider = CreditCardProvider
        self.__card_name = ""
        self.__pincode = 0

    @property
    def card_number(self):
        return self.__card_number

    @property
    def card_balance(self):
        return self.__card_balance

    @card_balance.setter
    def card_balance(self, card_balance):
        self.__card_balance = card_balance

    @property
    def credit_card_provider(self):
        return self.__card_provider

    @credit_card_provider.setter
    def credit_card_provider(self, card_provider):
        self.__card_provider = card_provider

    @property
    def card_name(self):
        return self.__card_name

    @card_name.setter
    def card_name(self, card_name):
        self.__card_name = card_name

    @property
    def pincode(self):
        return self.__pincode

    @pincode.setter
    def pincode(self, pincode):
        self.__pincode = pincode


class CreditCardProvider(StrEnum):
    KAPITAL_BANK = "Kapital Bank"
    NATIONAL_BANK_OF_UZBEKISTAN = "NBU Bank"
    INFIN_BANK = "Infin Bank"
    TBC_BANK = "TBC Bank"
