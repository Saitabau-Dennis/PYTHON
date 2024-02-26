class Bank_Account:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            return "INSUFFICIENT BALANCE!!!!!"
        else:
            self.balance -= amount
            return self.balance

    def check_balance(self):
        print("Current balance:", self.balance)

    def customer_details(self):
        print(f"Customer name: {self.customer_name}")
        print("Account number:", self.account_number)
        print("Date of account opening:", self.date_of_opening)
        print("Balance:", self.balance)

def main():
    name = input("Enter your name: ")
    try:
        account_number = int(input("Enter your account number: "))
    except ValueError:
        print("Invalid account number. Please enter a number.")
        return
    date = input("Enter the date you opened your account (YYYY-MM-DD): ")
    try:
        initial_balance = float(input("Enter your initial balance: "))
    except ValueError:
        print("Invalid initial balance. Please enter a number.")
        return
    bank = Bank_Account(account_number, initial_balance, date, name)

    while True:
        print("\nMenu:")
        print("1. DEPOSIT")
        print("2. WITHDRAW")
        print("3. CHECK BALANCE")
        print("4. VIEW ACCOUNT DETAILS")
        print("5. EXIT")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice ==  1:
            try:
                amount = float(input("Enter the amount to deposit: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            bank.deposit(amount)
            print(f"Deposited {amount}. New balance: {bank.balance}")
        elif choice ==  2:
            try:
                amount = float(input("Enter the amount to withdraw: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            result = bank.withdraw(amount)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Withdrew {amount}. New balance: {result}")
        elif choice ==  3:
            bank.check_balance()
        elif choice ==  4:
            print("\nAccount Details:")
            bank.customer_details()
        elif choice ==  5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
