# Importing necessary modules
from bankaccount_class import Bank_Account
import csv

# Function to save account information to a file
def save_accounts_to_file(bank_information, accounts):
    with open(bank_information, mode='w', newline='') as f:
        writer = csv.writer(f)
        # Loop through accounts and write each account's data to the file
        for account in accounts:
            writer.writerow(account.to_csv_string().split(','))

# Function to load accounts from a file
def load_accounts_from_file(bank_information):
    accounts = []
    with open(bank_information, mode='r') as f:
        reader = csv.reader(f)
        # Loop through each row in the file and create Bank_Account objects
        for row in reader:
            account_number, name, balance = row
            balance = float(balance)
            account = Bank_Account(account_number, name, balance)
            accounts.append(account)
    return accounts

# Function to get user choice from predefined options
def get_choice():
    choice_options= {
     '1': 1,
        'create': 1,
        'new': 1,
        '2': 2,
        'view': 2,
        'existing': 2,
        '3': 3,
        'quit': 3,
        'exit': 3,   
    }
    
    while True:
        user_input = input("Enter Your Choice: ").lower()
        choice = choice_options.get(user_input)
        if choice is not None:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Main function where the program execution starts
def main():
    # Load existing accounts from a file
    accounts = load_accounts_from_file("accounts.csv")
        
    while True:
        print("Options")
        print("1: Create a new account: ")
        print("2: View Existing Account: ")
        print("3: Quit")        
        choice = get_choice()

        if choice == 1:
            # Get user input to create a new account
            account = input("Enter account number: ")
            name = input("Enter account holder's name: ")
            balance = float(input("Enter initial balance: "))
            
            # Create a new Bank_Account object and add it to the list of accounts
            new_account = Bank_Account(account, name, balance)
            accounts.append(new_account)
            print("Account Created Successfully")
            
        elif choice == 2:
            # Get user input to view an existing account
            account = input("Enter Your Account Number: ")
            for acc in accounts:
                if acc.account == account:
                    print("Account Holder:\t", acc.name)
                    print("Balance:\t", acc.get_balance())
                    What_to_do = (input("Do you want to Deposit or Withdraw from this account or Exit ")).lower()
                    if What_to_do == "deposit":                                  
                         deposit_amount = float(input("Enter the amount to deposit: $ "))
                         acc.deposit(deposit_amount)
                    elif What_to_do == "withdraw":
                        withdrawal_amount = float(input("Enter the amount to withdraw: $ "))
                        acc.withdraw(withdrawal_amount)
                        print("Updated balance: $ ", acc.get_balance())
                        break
                    else:
                        break
            else:
                print("Account not found.")

        elif choice == 3:
            # Save the updated accounts to the file and exit the program
            save_accounts_to_file("accounts.csv", accounts)
            break

        else:
            print("Invalid choice. Please try again.")

# Check if the script is being run directly
if __name__ == "__main__":
    main()
