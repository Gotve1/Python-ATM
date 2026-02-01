class CardStorage:

    __card_storage = []

    def store_card(card):
        CardStorage.__card_storage__.append(card)
        return CardStorage.__card_storage__

    def get_card(index):
        print(CardStorage.__card_storage__[index])