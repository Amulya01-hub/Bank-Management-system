import datetime
class BankAccount:
    def __init__(self, account_number, name, account_type, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = initial_balance
        self.transactions = []
        self.add_transaction("Account opened", initial_balance)
    def add_transaction(self, description, amount):
        transaction = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": description,
            "amount": amount,
            "balance": self.balance
        }
        self.transactions.append(transaction)
    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return False
        self.balance += amount
        self.add_transaction("Deposit", amount)
        print(f"Deposited ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
        return True
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        self.balance -= amount
        self.add_transaction("Withdrawal", -amount)
        print(f"Withdrew ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
        return True
    def check_balance(self):
        print(f"Current balance: ₹{self.balance:.2f}")
        return self.balance
    def get_transaction_history(self):
        return self.transactions
    def display_account_info(self):
        print("\n" + "="*50)
        print("Account Information".center(50))
        print("="*50)
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: ₹{self.balance:.2f}")
        print("="*50)
class BankManagementSystem:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1000
    def create_account(self):
        print("\n" + "="*50)
        print("Create New Account".center(50))
        print("="*50)
        name = input("Enter customer name: ")
        print("\nSelect account type:")
        print("1. Savings Account")
        print("2. Current Account")
        account_type_choice = input("Enter choice (1-2): ")
        if account_type_choice == "1":
            account_type = "Savings"
        elif account_type_choice == "2":
            account_type = "Current"
        else:
            print("Invalid choice. Defaulting to Savings Account.")
            account_type = "Savings"
        initial_balance = 0
        while True:
            try:
                initial_deposit = float(input("Enter initial deposit amount (minimum ₹500 for Savings): ₹"))
                if account_type == "Savings" and initial_deposit < 500:
                    print("Savings account requires minimum ₹500 deposit.")
                    continue
                if initial_deposit < 0:
                    print("Amount cannot be negative.")
                    continue
                initial_balance = initial_deposit
                break
            except ValueError:
                print("Please enter a valid amount.")
        account_number = self.next_account_number
        self.next_account_number += 1
        new_account = BankAccount(account_number, name, account_type, initial_balance)
        self.accounts[account_number] = new_account
        print("\nAccount created successfully!")
        print(f"Your account number is: {account_number}")
        print(f"Account Holder: {name}")
        print(f"Account Type: {account_type}")
        print(f"Initial Balance: ₹{initial_balance:.2f}")
    def access_account(self):
        try:
            account_number = int(input("Enter your account number: "))
        except ValueError:
            print("Invalid account number. Please enter numbers only.")
            return None
        if account_number not in self.accounts:
            print("Account not found.")
            return None
        return self.accounts[account_number]
    def run(self):
        print("\n" + "#"*50)
        print("BANK MANAGEMENT SYSTEM".center(50))
        print("#"*50)
        while True:
            print("\nMain Menu:")
            print("1. Create New Account")
            print("2. Access Existing Account")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")
            if choice == "1":
                self.create_account()
            elif choice == "2":
                account = self.access_account()
                if account:
                    self.account_menu(account)
            elif choice == "3":
                print("\nThank you for using our Bank Management System!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    def account_menu(self, account):
        while True:
            account.display_account_info()
            print("\nAccount Menu:")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            print("4. View Transaction History")
            print("5. Return to Main Menu") 
            choice = input("Enter your choice (1-5): ") 
            if choice == "1":
                try:
                    amount = float(input("Enter deposit amount: ₹"))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid amount entered.")
            elif choice == "2":
                try:
                    amount = float(input("Enter withdrawal amount: ₹"))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid amount entered.")
            elif choice == "3":
                account.check_balance()
            elif choice == "4":
                transactions = account.get_transaction_history()
                print("\n" + "="*70)
                print("TRANSACTION HISTORY".center(70))
                print("="*70)
                print(f"{'Date':<20}{'Description':<20}{'Amount':<15}{'Balance':<15}")
                print("-"*70)
                for t in transactions:
                    print(f"{t['date']:<20}{t['description']:<20}₹{t['amount']:<14.2f}₹{t['balance']:<14.2f}")
                print("="*70)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a number between 1-5.")
bank_system = BankManagementSystem()
bank_system.run()