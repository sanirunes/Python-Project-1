from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Email is invalid!")
        return  # Prevent adding the user if the email is invalid
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    if not users:
        print("No users created yet.")
        return
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")

def create_account():
    if not users:
        print("No users available to create an account for. Please create a user first.")
        return
    list_users()
    try:
        idx = int(input("Select user number: ")) - 1
        if 0 <= idx < len(users):
            user = users[idx]
        else:
            print("Invalid user selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    print("Account Type:")
    print("1. Savings Account")
    print("2. Students Account")
    print("3. Current Account")
    try:
        account_choice = int(input("Enter your choice (1, 2, 3): "))
        amount = float(input("Enter initial deposit: "))
        if amount < 0:
            print("Initial deposit cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if account_choice == 1:
        account = SavingsAccount(amount)
    elif account_choice == 2:
        account = StudentAccount(amount)
    elif account_choice == 3:
        account = CurrentAccount(amount)
    else:
        print("Invalid choice!")
        return

    user.add_account(account)
    print(f"{account.get_account_type()} added!\n")

def deposit_money():
    if not users:
        print("No users available.")
        return
    list_users()
    try:
        idx = int(input("Select user: ")) - 1
        if 0 <= idx < len(users):
            user = users[idx]
        else:
            print("Invalid user selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if not user.accounts:
        print(f"{user.name} has no accounts.")
        return

    print("Select account to deposit into:")
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    try:
        acc_idx = int(input("Select account: ")) - 1
        if 0 <= acc_idx < len(user.accounts):
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Deposit amount must be positive.")
                return
            user.accounts[acc_idx].deposit(amount)
        else:
            print("Invalid account selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")

def withdraw_money():
    if not users:
        print("No users available.")
        return
    list_users()
    try:
        idx = int(input("Select user: ")) - 1
        if 0 <= idx < len(users):
            user = users[idx]
        else:
            print("Invalid user selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if not user.accounts:
        print(f"{user.name} has no accounts.")
        return

    print("Select account to withdraw from:")
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    try:
        acc_idx = int(input("Select account: ")) - 1
        if 0 <= acc_idx < len(user.accounts):
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
                return
            try:
                user.accounts[acc_idx].withdraw(amount)
                print("Withdrawal successful.\n")
            except ValueError as e:
                print(f"Error: {e}\n")
        else:
            print("Invalid account selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_transactions():
    if not users:
        print("No users available.")
        return
    list_users()
    try:
        idx = int(input("Select user: ")) - 1
        if 0 <= idx < len(users):
            user = users[idx]
        else:
            print("Invalid user selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if not user.accounts:
        print(f"{user.name} has no accounts.")
        return

    for i, acc in enumerate(user.accounts):
        print(f"\n{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")
        transactions = acc.get_transaction_history()
        if transactions:
            print("Transaction History:")
            for tx in transactions:
                print(tx)
        else:
            print("No transaction history for this account.")
