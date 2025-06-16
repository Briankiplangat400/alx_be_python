import sys
from bank_account import BankAccount

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main-0.py <name> <amount> <operation>")
        sys.exit(1)

    name = sys.argv[1]
    amount = float(sys.argv[2])
    operation = sys.argv[3]

    # Always start with a balance of $250.00 as required
    account = BankAccount(name)

    if operation == "deposit":
        print(account.deposit(amount))
    elif operation == "withdraw":
        print(account.withdraw(amount))
    elif operation == "balance":
        print(account.display_balance())
    else:
        print("Invalid operation.")
