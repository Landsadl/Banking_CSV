class Bank_Account():
    # Constructor to initialize the Bank_Account object with account number, account holder's name, and balance
    def __init__(self, account, name, balance):
        self.account = account
        self.name = name
        self.balance = balance

    # Method to deposit a specified amount into the account
    def deposit(self, amount):
        self.balance += amount

    # Method to withdraw a specified amount from the account, with a check for insufficient funds
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("NSF")  # NSF stands for "Non-Sufficient Funds"

    # Method to retrieve the current balance of the account
    def get_balance(self):
        return self.balance

    # Method to convert the account information into a CSV-formatted string
    def to_csv_string(self):
        return f"{self.account},{self.name},{self.balance}"
