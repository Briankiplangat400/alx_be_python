import sys
from bank_account import BankAccount

if len(sys.argv) != 4:
    print("Usage: python main-0.py <owner> <amount> <operation>")
    sys.exit(1)

owner = sys.argv[1]
amount = float(sys.argv[2])
operation = sys.argv[3].lower()

account = BankAccount(owner)

if operation == "deposit":
    deposited = account.deposit(amount)
    if deposited > 0:
        print(f"Deposited: ${deposited:.1f}")
    else:
        print("Deposit failed.")
elif operation == "withdraw":
    withdrawn = account.withdraw(amount)
    if withdrawn is not None:
        print(f"Withdrawn: ${withdrawn:.1f}")
    else:
        print("Insufficient balance.")
elif operation == "balance":
    print(account.display_balance())
else:
    print("Invalid operation. Use 'deposit', 'withdraw', or 'balance'.")
