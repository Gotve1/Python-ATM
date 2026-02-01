from CreditCard import CreditCard

class CardStorage:

    __card_storage = []

    @classmethod # works like static methods in java
    def store_card(cls, card):
        cls.__card_storage.append(card)
        return CardStorage.__card_storage

    @classmethod
    def get_card(index):
        print(CardStorage.__card_storage[index])