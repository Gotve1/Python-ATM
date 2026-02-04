# Python ATM

Python ATM is a small interactive command-line project that implements fundamental ATM-like operations for learning and demonstration purposes. It provides a simple in-memory model of credit cards, basic validation, and an interactive menu to register cards, deposit and withdraw money, list cards, and delete cards.

---
## Requirements

- Python 3.11+ recommended
  - Reason: `StrEnum` (used for `CreditCardProvider`) is available from Python 3.11+
- No external dependencies — purely standard library usage
---
## Quick start

1. Ensure you have Python 3.11+ installed.
2. Run the application:
   - cd into the folder containing `Main.py` (e.g. `dev/gotve/python-atm/`) and run:
     ```
     python Main.py
     ```
3. Follow the interactive menu.

Note: `pre_init()` seeds one card (John Doe) with pincode `1234` and balance `100` so you can test deposit/withdraw immediately.

---

## Features (implemented in the codebase)

- Interactive CLI menu (see `ATM.py` / `MessageProvider.py`)
  - 1. Register a new credit card
  - 2. Deposit money
  - 3. Withdraw money
  - 4. View cards
  - 5. Delete a card
  - 6. Exit
- Register new credit card
  - Collects first name, last name and age (age validated: must be 18 or older)
  - Lets user choose a card provider from an enum of providers (Kapital, NBU, Infin, TBC)
  - Lets user name the card and set a numeric PIN code
  - Created card is stored in in-memory storage
- Card model
  - `CreditCard` extends `Person` and stores a UUID card number, balance, provider, card name and pincode
  - Card numbers are generated with `uuid.uuid4()`
- In-memory card storage (`CardStorage`)
  - Stores cards in a class-level list (`__card_storage`)
  - Methods to store, list, lookup by index, delete, deposit and withdraw
- Deposit
  - Select a card by index, enter a positive amount, updates the balance
  - Guard against negative or non-numeric amounts (raises/handles `NegativeAmountOfMoney`)
- Withdraw
  - Select a card by index, verify PIN, enter amount to withdraw; updates balance
  - Basic insufficient-funds check (prints "Not enough money" when balance <= 0)
- Delete a card
  - Select a card and verify PIN before deletion
- Basic error handling classes:
  - `InvalidAgeException`
  - `NegativeAmountOfMoney`
- Message text separated into `MessageProvider` for easy CLI messages
- Example data seeding: `Main.py`'s `pre_init()` creates a sample card (John Doe with balance 100 and pincode `1234`) so the app has at least one card on first run

---

## How it works (high-level)

1. `Main.py` calls `pre_init()` to seed an example card, then enters a loop that creates an `ATM()` instance.
2. `ATM.__init__()` displays the main menu and routes user choice to the corresponding handler.
3. Each handler interacts with `CardStorage`, `CreditCard`, and `MessageProvider` to implement the selected operation.
4. All cards are kept in memory for the duration of execution (no persistence to disk).

---

## Files of interest

- `dev/gotve/python-atm/Main.py` — entry point and pre-initialization
- `dev/gotve/python-atm/ATM.py` — main CLI menu and handlers (register, deposit, withdraw, view, delete)
- `dev/gotve/python-atm/CreditCard.py` — `CreditCard` class and `CreditCardProvider` enum
- `dev/gotve/python-atm/Person.py` — simple `Person` base class
- `dev/gotve/python-atm/CardStorage.py` — in-memory card repository and operations
- `dev/gotve/python-atm/MessageProvider.py` — CLI text & prompts
- `dev/gotve/python-atm/InvalidAgeException.py` and `NegativeAmountOfMoney.py` — small exception classes
