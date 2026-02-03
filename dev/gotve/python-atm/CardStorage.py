from CreditCard import CreditCard


class CardStorage(CreditCard):
    __card_storage = []

    @classmethod
    def get_card_storage(cls):
        return cls.__card_storage

    @classmethod  # works like static methods in java
    def store_card(cls, card):
        cls.__card_storage.append(card)
        return cls.__card_storage

    @classmethod
    def get_card_by_index(cls, index):
        return cls.__card_storage[index]

    @classmethod
    def get_all_cards(cls):
        return cls.__card_storage

    @classmethod
    def deposit_money(cls, card_index, amound_of_money):
        try:
            selected_card = cls.get_card_by_index(card_index)
            CreditCard.set_card_balance(selected_card, amound_of_money)
        except IndexError:
            print("Selected wrong card, operation terminated.")

    @classmethod
    def withdraw(cls, card_index, amount_of_money):
        CreditCard.get_card_balance(card_index) - amount_of_money

        if CreditCard.get_card_balance(card_index) - amount_of_money <= 0:
            print("Not enough money try lower amount")

    @classmethod
    def print_all_cards(cls):
        for index, card in enumerate(cls.get_all_cards()):
            print(
                f"Index: {index} \n"
                f"Card number: {card.get_card_number()} \n",
                f"Card owner: {card.get_firstname(), card.get_lastname()} \n",
            )
