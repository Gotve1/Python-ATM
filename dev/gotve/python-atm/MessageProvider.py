class MessageProvider():

    @classmethod
    def main_menu_message(cls):
        print(
            "Please choose one of available options \n"
            "1. Register a new credit card \n"
            "2. Deposit money \n"
            "3. Withdraw money \n"
            "4. View cards \n"
            "5. Delete a card \n"
            "6. Exit \n"
        )

    @classmethod
    def card_providers_message(cls):
        print(
            "Choose one of card providers \n"
            "1. Kapital Bank \n"
            "2. NBU Bank \n"
            "3. Infin Bank \n"
            "4. TBC Bank"
        )

    @classmethod
    def invalid_input_message(cls):
        print(
            "Cannot use letters or special characters, please try again."
        )

    @classmethod
    def select_card_by_index(cls):
        print("Select one of available cards")