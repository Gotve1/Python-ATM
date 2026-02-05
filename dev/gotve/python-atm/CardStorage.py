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
    def get_card_by_index(cls, index):
        return cls.__card_storage[index]

    @classmethod
    def get_all_cards(cls):
        return cls.__card_storage

    @classmethod
    def get_card_pincode(cls, index):
        selected_card = cls.get_card_by_index(index)
        return selected_card.pincode

    @classmethod
    def delete_card(cls, index):
        cls.__card_storage.pop(index)

    @classmethod
    def deposit_money(cls, card_index, amound_of_money):
        try:
            selected_card = cls.get_card_by_index(card_index)
            selected_card.card_balance = amound_of_money
        except IndexError:
            print("Selected wrong card, operation terminated.")

    @classmethod
    def withdraw(cls, card_index, amount_of_money):
        selected_card = cls.get_card_by_index(card_index)
        current_balance = selected_card.card_balance

        if current_balance <= 0 or current_balance < amount_of_money:
            print("Not enough money")
            return
        if amount_of_money < 0:
            print("Withdraw number cannot be negative")
            return
        else:
            selected_card.card_balance = current_balance - amount_of_money
            print("Withdraw succeed \n")

    @classmethod
    def print_all_cards(cls):
        for index, card in enumerate(cls.get_all_cards()):
            print(
                f"Index: {index} \n"
                f"Card number: {card.card_number} \n"
                f"Card owner: {card.firstname} {card.lastname} \n"
                f"Money: {card.card_balance} \n"
                f"Card provider: {card.credit_card_provider} \n"
                f"Card name: {card.card_name} \n"
                f"Card pincode: {card.pincode} \n"
            )
