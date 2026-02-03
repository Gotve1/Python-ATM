from ATM import ATM
from CardStorage import CardStorage
from CreditCard import CreditCardProvider, CreditCard


def main():
    ATM()


if __name__ == "__main__":
    blank_card = (
        CreditCard()
        .set_age(18)
        .set_firstname("John")
        .set_lastname("Doe")
        .set_credit_card_provider(CreditCardProvider.KAPITAL_BANK)
        .set_card_name("Blank Card")
        .set_card_pincode(2008)
    )
    CardStorage.store_card(blank_card)
    while True:
        main()
