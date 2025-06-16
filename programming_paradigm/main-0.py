import sys
from bank_account import BankAccount

if len(sys.argv) != 4:
    print("Usage: python main-0.py <account_holder> <initial_balance> <transaction_type>")
    sys.exit(1)

name = sys.argv[1]
try:
    balance = float(sys.argv[2])
except ValueError:
    print("Initial balance must be a number.")
    sys.exit(1)

transaction = sys.argv[3].lower()

account = BankAccount(name, balance)

if transaction == "deposit":
    account.deposit(100)
elif transaction == "withdraw":
    account.withdraw(50)
else:
    print("Invalid transaction type. Use 'deposit' or 'withdraw'.")

account.display_balance()
