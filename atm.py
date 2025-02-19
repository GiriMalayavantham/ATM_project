class ATM:
    def __init__(self):
        self.__balance = 0
        self.__pin = "1234"
        self.transactions = []  # Store transaction history
        self.authenticate()

    def authenticate(self):
        """Authenticate user with a PIN (3 attempts allowed)."""
        for attempt in range(3):
            entered_pin = input("Enter your ATM PIN: ")
            if entered_pin == self.__pin:
                print("Authentication successful!\n")
                return
            else:
                print(f"Incorrect PIN. {2 - attempt} attempts remaining.")
        print("Too many failed attempts. Exiting.")
        exit()

    def change_pin(self):
        """Allows the user to change their PIN securely."""
        current_pin = input("Enter current PIN: ")
        if current_pin == self.__pin:
            new_pin = input("Enter new PIN: ")
            confirm_pin = input("Confirm new PIN: ")
            if new_pin == confirm_pin:
                self.__pin = new_pin
                print("PIN changed successfully!")
            else:
                print("Error: PIN confirmation does not match.")
        else:
            print("Error: Incorrect current PIN.")

    def check_balance(self):
        print(f"Your current balance is: ₹{self.__balance:.2f}")

    def deposit(self):
        """Deposit money after validation."""
        try:
            amount = float(input("Enter deposit amount: ₹"))
            if amount > 0:
                self.__balance += amount
                self.transactions.append(f"Deposited ₹{amount:.2f}")
                print(f"₹{amount:.2f} deposited successfully!")
            else:
                print("Error: Deposit amount must be greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    def withdraw(self):
        """Withdraw money after checking the balance."""
        try:
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount <= 0:
                print("Error: Withdrawal amount must be greater than 0.")
            elif amount > self.__balance:
                print("Error: Insufficient balance.")
            else:
                self.__balance -= amount
                self.transactions.append(f"Withdraw ₹{amount:.2f}")
                print(f"₹{amount:.2f} withdrawn successfully!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    def show_transactions(self):
        """Display transaction history."""
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("\nTransaction History:")
            for transaction in self.transactions:
                print(transaction)

    def menu(self):
        """Display the ATM menu and process user choices."""
        while True:
            print("\n=== ATM MENU ===")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Show Transactions")
            print("5. Change PIN")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.show_transactions()
            elif choice == "5":
                self.change_pin()
            elif choice == "6":
                print("Thank you for using the ATM!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.menu()
