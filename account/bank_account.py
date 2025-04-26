from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Email is invalid!")
        return
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
        print("Invalid input. Please enter a number for the user.")
        return

    print("Account Type:")
    print("1. Savings Account")
    print("2. Students Account")
    print("3. Current Account")
    try:
        account_choice = int(input("Enter your choice (1, 2, 3): "))
        amount_str = input("Enter initial deposit: ")
        amount = float(amount_str)
        if amount < 0:
            print("Initial deposit cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Please enter a number for the account choice and deposit amount.")
        return

    try:
        if account_choice == 1:
            account = SavingsAccount(initial_balance=amount, name=user.name, email=user.email)
        elif account_choice == 2:
            account = StudentAccount(initial_balance=amount, name=user.name, email=user.email)
        elif account_choice == 3:
            account = CurrentAccount(initial_balance=amount, name=user.name, email=user.email)
        else:
            print("Invalid account choice.")
            return
        user.add_account(account)
        print(f"{account.get_account_type()} added!\n")
    except ValueError as e:
        print(f"Error creating account: {e}")

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
        print("Invalid input. Please enter a number for the user.")
        return

    if not user.accounts:
        print(f"{user.name} has no accounts.")
        return

    print("Select account to deposit into:")
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")
    try:
        acc_idx = int(input("Select account: ")) - 1
        if 0 <= acc_idx < len(user.accounts):
            amount_str = input("Enter amount to deposit: ")
            amount = float(amount_str)
            if amount <= 0:
                print("Deposit amount must be positive.")
                return
            user.accounts[acc_idx].deposit(amount)
            print("Deposit successful.\n")
        else:
            print("Invalid account selection.")
            return
    except ValueError as e:
        print(f"Invalid input: {e}")

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
        print("Invalid input. Please enter a number for the user.")
        return

    if not user.accounts:
        print(f"{user.name} has no accounts.")
        return

    print("Select account to withdraw from:")
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")
    try:
        acc_idx = int(input("Select account: ")) - 1
        if 0 <= acc_idx < len(user.accounts):
            amount_str = input("Enter amount to withdraw: ")
            amount = float(amount_str)
            if amount <= 0:
                print("Withdrawal amount must be positive.")
                return
            try:
                user.accounts[acc_idx].withdraw(amount)
                print("Withdrawal successful.\n")
            except ValueError as e:
                print(f"Withdrawal error: {e}")
        else:
            print("Invalid account selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number for the account and amount.")

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
        print("Invalid input. Please enter a number for the user.")
        return

    if not user.accounts:
        print(f"{user.name} has no accounts.")
        return

    print("Select account to view transactions:")
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")
    try:
        acc_idx = int(input("Select account: ")) - 1
        if 0 <= acc_idx < len(user.accounts):
            account = user.accounts[acc_idx]
            print(f"\n{account.get_account_type()} - Balance: Rs. {account.get_balance()}")
            transactions = account.get_transaction_history()
            if transactions:
                print("Transaction History:")
                for tx in transactions:
                    print(tx)
            else:
                print("No transaction history for this account.")
        else:
            print("Invalid account selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number for the account.")

def main():
    while True:
        print("\nBank Management System")
        print("1. Create User")
        print("2. List Users")
        print("3. Create Account")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. View Transactions")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            list_users()
        elif choice == '3':
            create_account()
        elif choice == '4':
            deposit_money()
        elif choice == '5':
            withdraw_money()
        elif choice == '6':
            view_transactions()
        elif choice == '7':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

