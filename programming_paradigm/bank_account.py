class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return amount  # Do NOT print here
        return 0

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return None

    def display_balance(self):
        return f"Current Balance: ${self.balance:.2f}"
