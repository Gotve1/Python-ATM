from ATM import ATM
from CardStorage import CardStorage
from CreditCard import CreditCardProvider, CreditCard


def main():
    ATM()

def pre_init():

    blank_card = CreditCard()
    blank_card.age = 18
    blank_card.firstname = 'John'
    blank_card.lastname = 'Doe'
    blank_card.card_balance = 100
    blank_card.credit_card_provider = CreditCardProvider.KAPITAL_BANK
    blank_card.card_name = "John's card"
    blank_card.pincode = 1234

    CardStorage.store_card(blank_card)

if __name__ == "__main__":
    pre_init()
    while True:
        main()
