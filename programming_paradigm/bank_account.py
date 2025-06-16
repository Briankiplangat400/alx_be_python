class BankAccount:
    def __init__(self, name, balance=250.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount:.1f}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        elif amount > 0:
            self.balance -= amount
            return f"Withdrew: ${amount:.1f}"
        else:
            return "Invalid withdrawal amount."

    def display_balance(self):
        return f"Current Balance: ${self.balance:.2f}"
