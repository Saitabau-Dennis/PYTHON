class BankAccount:
    def __init__(self, account_number, date_of_opening, customer_name, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

    def main_menu():
        print("\nATM Menu, choose an option")
        print("\n1 - Create Account")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - View Balance")
        print("5 - Exit")

        while True:
            try:
                choice = int(input("Please enter a number: "))
            except ValueError:
                print("This is not a number")
            else:
                if choice ==  1:
                    account_number = input("Enter your account number: ")
                    date_of_opening = input("Enter the date of opening (YYYY-MM-DD): ")
                    customer_name = input("Enter your name: ")
                    my_account = BankAccount(account_number, date_of_opening, customer_name)
                    print("Account created successfully.")
                elif choice ==  2:
                    deposit_amount = float(input("Enter the amount you want to deposit: "))
                    print(f"You deposited: {my_account.deposit(deposit_amount)}")
                elif choice ==  3:
                    withdraw_amount = float(input("Enter the amount you want to withdraw: "))
                    print(my_account.withdraw(withdraw_amount))
                elif choice ==  4:
                    my_account.check_balance()
                elif choice ==  5:
                    break
                else:
                    print("Not a valid number")


                BankAccount.main_menu()
