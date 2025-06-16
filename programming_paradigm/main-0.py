import sys
from bank_account import BankAccount

if __name__ == "__main__":
    account = BankAccount("John Doe", 500)

    if len(sys.argv) > 1:
        action = sys.argv[1].lower()
        if action == "deposit" and len(sys.argv) == 3:
            amount = float(sys.argv[2])
            account.deposit(amount)
        elif action == "withdraw" and len(sys.argv) == 3:
            amount = float(sys.argv[2])
            account.withdraw(amount)
    
    account.display_balance()
