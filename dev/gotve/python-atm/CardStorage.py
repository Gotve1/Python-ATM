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
    def get_card_by_id(cls, index):
        return cls.__card_storage[index]

    @classmethod
    def get_all_cards(cls):
        return cls.__card_storage

    @classmethod
    def deposit_money(cls, card_id, amound_of_money):
        try:
            selected_card = cls.get_card_by_id(card_id)
            CreditCard.set_card_balance(selected_card, amound_of_money)
        except IndexError:
            print("Selected wrong card, operation terminated.")


    @classmethod
    def print_all_cards(cls):
        for index, card in enumerate(cls.get_all_cards()):
            print(
                f"Index: {index} \n"
                f"Card number: {card.get_card_number()} \n",
                f"Card owner: {card.get_firstname(), card.get_lastname()} \n",
                f"Card balance: {card.get_card_balance()} \n",
                f"Card provider: {card.get_credit_card_provider()} \n",
                f"Card name: {card.get_card_name()} \n"
            )