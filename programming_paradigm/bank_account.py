class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += float(amount)
        print(f"Deposited: ${float(amount):.1f}")

    def withdraw(self, amount):
        amount = float(amount)
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.1f}")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
