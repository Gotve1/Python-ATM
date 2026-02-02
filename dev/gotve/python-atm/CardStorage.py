class CardStorage:
    __card_storage = []

    @classmethod
    def get_card_storage(cls):
        return cls.__card_storage

    @classmethod  # works like static methods in java
    def store_card(cls, card):
        cls.__card_storage.append(card)
        return cls.__card_storage

    @classmethod
    def get_card_by_id(cls, index):
        return cls.__card_storage[index]

    @classmethod
    def get_all_cards(cls):
        return cls.__card_storage

    @classmethod
    def length(cls):
        return cls.__card_storage.__len__()

    @classmethod
    def print_all_cards(cls):
        for card in cls.get_all_cards():
            print(
                f"Card number: {card.get_card_number()} \n",
                f"Card owner: {card.get_firstname(), card.get_lastname()} \n",
                f"Card balance: {card.get_card_balance()} \n",
                f"Card provider: {card.get_credit_card_provider()} \n",
                f"Card name: {card.get_card_name()} \n"
            )