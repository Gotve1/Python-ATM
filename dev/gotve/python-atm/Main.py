from ATM import ATM
from CardStorage import CardStorage
from CreditCard import CreditCardProvider, CreditCard


def main():
    ATM()

def pre_init():
    blank_card = (
        CreditCard()
        .set_age(18)
        .set_firstname("John")
        .set_lastname("Doe")
        .set_credit_card_provider(CreditCardProvider.KAPITAL_BANK)
        .set_card_name("Blank Card")
        .set_card_pincode(1234)
        .set_card_balance(100)
    )
    CardStorage.store_card(blank_card)

if __name__ == "__main__":
    pre_init()
    while True:
        main()
