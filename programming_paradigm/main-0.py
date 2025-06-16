import sys
from bank_account import BankAccount

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main-0.py <name> <amount> <operation>")
        sys.exit(1)

    name = sys.argv[1]
    operation = sys.argv[-1].lower()

    # Initialize account with default $250.00
    account = BankAccount(name)

    if operation == "deposit" or operation == "withdraw":
        amount = float(sys.argv[2])

        if operation == "deposit":
            print(account.deposit(amount))
        elif operation == "withdraw":
            print(account.withdraw(amount))

    elif operation == "balance":
        print(account.display_balance())

    else:
        print("Invalid operation.")
