from account.transaction import Transaction
from account.user import User

class BankAccount:
    def __init__(self, name="John", email="john@gmail.com", initial_balance=0):
        # Validate initial balance
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            print("Invalid initial balance!")
            self.balance = 0  # Default to 0 if invalid
        else:
            self.balance = initial_balance
        
        self.transactions_history = []
        self.account_type = "Generic"
        self.user = User(name, email)

    def deposit(self, amount):
        # Validate deposit amount
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Deposit amount is invalid!")
            return

        self.balance += amount
        # Add transaction to history with updated balance
        self.transactions_history.append(Transaction(amount, "deposit", self.balance))

    def withdraw(self, amount):
        # Validate withdrawal amount
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount is invalid!")
            return

        # Check for sufficient balance before withdrawing
        if self.balance < amount:
            print("Insufficient Balance!")
            return

        self.balance -= amount
        # Add transaction to history with updated balance
        self.transactions_history.append(Transaction(amount, "withdraw", self.balance))

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions_history

    def get_account_type(self):
        return self.account_type

    def get_user(self):
        return self.user


class SavingsAccount(BankAccount):
    MIN_BALANCE = 100

    def withdraw(self, amount):
        # Ensure there's enough balance considering the minimum balance requirement
        if self.balance - amount < self.MIN_BALANCE:
            print(f"A minimum balance of {self.MIN_BALANCE} is required to withdraw!")
            return
        super().withdraw(amount)

    def get_account_type(self):
        return "Savings account"


class CurrentAccount(BankAccount):
    def get_account_type(self):
        return "Current account"


class StudentAccount(BankAccount):
    MIN_BALANCE = 100

    def withdraw(self, amount):
        # Ensure there's enough balance considering the minimum balance requirement
        if self.balance - amount < self.MIN_BALANCE:
            print(f"A minimum balance of {self.MIN_BALANCE} is required to withdraw from a Student account!")
            return
        super().withdraw(amount)

    def get_account_type(self):
        return "Student account"
