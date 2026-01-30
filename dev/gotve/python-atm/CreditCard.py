import uuid


class CreditCard:

    def __init__(self):
        self.__card_number = uuid.uuid4()

    def get_card_number(self):
        return self.__card_number

    def set_card_balance(self, balance):
        self.__balance = balance

    def get_card_balance(self):
        return self.__balance
