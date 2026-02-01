class CardStorage:
    __card_storage = []

    @classmethod  # works like static methods in java
    def store_card(cls, card):
        cls.__card_storage.append(card)
        return cls.__card_storage

    @classmethod
    def __get_card_by_id(cls, index):
        return cls.__card_storage[index]

    @classmethod
    def length(cls):
        return cls.__card_storage.__len__()

    @classmethod
    def __get_all_cards(cls):
        return cls.__card_storage

    @classmethod
    def get_all_cards_by_name(cls):
        for card in cls.__get_all_cards():
            print(
                "Card number: ", card.get_card_number(), "\n",
                "Card balance: ", card.get_card_balance(), "\n",
                "Card provider: ", card.get_credit_card_provider(), "\n",
                "Card name: ", card.get_card_name(), "\n",
                "Card pincode: ", card.get_pincode(), "\n"
            )