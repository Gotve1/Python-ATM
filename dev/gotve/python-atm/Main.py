from ATM import ATM
from CardStorage import CardStorage
from CreditCard import CreditCardProvider

def main():
    blank_card = lambda CreditCard : (
        blank_card.set_age(18),
        blank_card.set_credit_card_provider(CreditCardProvider.KAPITAL_BANK),
        blank_card.set_card_name("Blank Card"),
        blank_card.set_card_pincode(2008)
    )
    CardStorage.store_card(blank_card)
    ATM()


if __name__ == "__main__":
    while True:
        main()
