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
    def get_card_pincode(cls, index):
        selected_card = cls.get_card_by_index(index)
        return selected_card.get_pincode()

    @classmethod
    def delete_card(cls, index):
        cls.__card_storage.pop(index)

    @classmethod
    def deposit_money(cls, card_index, amound_of_money):
        try:
            selected_card = cls.get_card_by_index(card_index)
            CreditCard.set_card_balance(selected_card, amound_of_money)
        except IndexError:
            print("Selected wrong card, operation terminated.")

    @classmethod
    def withdraw(cls, card_index, amount_of_money):
        selected_card = cls.get_card_by_index(card_index)
        current_balance = selected_card.get_card_balance()

        if current_balance <= 0:
            print("Not enough money")
        else:
            selected_card.set_card_balance(current_balance - amount_of_money)
            print("Withdraw succeed \n")

    @classmethod
    def print_all_cards(cls):
        for index, card in enumerate(cls.get_all_cards()):
            print(
                f"Index: {index} \n"
                f"Card number: {card.get_card_number()} \n",
                f"Card owner: {card.firstname} {card.lastname} \n",
                f"Money: {card.get_card_balance()} \n"
            )
