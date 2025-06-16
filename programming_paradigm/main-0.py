import sys
from bank_account import BankAccount

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main-0.py <name> <amount> <action>")
        sys.exit(1)

    name = sys.argv[1]
    amount = sys.argv[2]
    action = sys.argv[3].lower()

    account = BankAccount(name)

    if action == "deposit":
        account.deposit(amount)
    elif action == "withdraw":
        account.withdraw(amount)
    else:
        print("Invalid action. Use 'deposit' or 'withdraw'.")

    account.display_balance()
