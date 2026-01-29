import uuid


class CreditCard:

    def __init__(self):
        self.__card_number = uuid.uuid4()

    def get_card_number(self):
        return self.__card_number