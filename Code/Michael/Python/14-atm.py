"""
PDX Code Guild Full Stack Bootcamp
->Lab 14
  Automated Teller Machine
Michael B

Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. 
Implement the initializer, as well as the following functions:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account


Version 2
Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. 
Add a new method print_transactions() to your class for printing out the list of transactions.
"""


class ATM:
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = float(balance)  # the balance of the account.
        self.interest_rate = float(interest_rate)  # interest rate is 10% by default.
        self.transactions = []  # list of transactions.

    def check_balance(self):  # returns the account balance.
        return self.balance

    def deposit(self, amount):  # deposits the given amount in the account.
        if amount > 0:
            self.balance += amount
            self.log_transaction(f"Deposited: {amount}")
            return True
        else:
            return False

    def check_withdrawal(
        self, amount
    ):  # returns true if the withdrawn amount won't put the account in the negative.
        if (
            self.balance - amount < 0 or amount < 0
        ):  # if the balance is less than the amount to withdraw.
            return False
        else:  # if the balance is greater than the amount to withdraw.
            return True

    def withdraw(self, amount):  # withdraws the amount from the account and returns it.
        self.balance -= amount
        self.log_transaction(f"Withdrew: {amount}")
        return amount

    def calc_interest(
        self,
    ):  # returns the amount of interest calculated on the account.
        self.balance += self.balance * self.interest_rate
        self.log_transaction(f"Interest added: {self.balance * self.interest_rate}")

    def print_transactions(self):  # prints out the list of transactions.
        for (
            transaction
        ) in self.transactions:  # for each transaction in the list of transactions.
            print(transaction)

    def log_transaction(
        self, transaction
    ):  # logs the transaction to the list of transactions.
        self.transactions.append(transaction)


if __name__ == "__main__":

    atm = ATM()  # create an instance of our class

    menu_options = {
        "1": "Balance",
        "2": "Deposit",
        "3": "Withdraw",
        "4": "Interest",
        "5": "Transactions",
        "6": "Exit",
    }

    while True:
        print()  # blank line
        for label, option in menu_options.items():  # print the menu options
            print(f"{label}. {option}")

        command = input(
            "\nEnter the number of the option you would like to perform\n> "
        )  # get the user's command
        command = menu_options.get(command)

        if command == "Balance":
            balance = atm.check_balance()  # call the check_balance() method
            print(f"Your balance is ${balance}")

        elif command == "Deposit":
            amount = float(input("How much would you like to deposit?\n> $ "))
            success = atm.deposit(amount)  # call the deposit(amount) method
            if not success:
                print("Deposit amount must be a positive number.")
            else:
                print(f"Deposited ${amount}")

        elif command == "Withdraw":
            amount = float(input("How much would you like to withdraw?\n> $"))
            success = atm.check_withdrawal(
                amount
            )  # call the check_withdrawal(amount) method

            if not success:
                print("Insufficient funds or negative number entered")
            else:
                atm.withdraw(amount)  # call the withdraw(amount) method
                print(f"Withdrew ${amount}")

        elif command == "Interest":
            before_interest = atm.check_balance()
            atm.calc_interest()  # call the calc_interest() method
            after_interest = atm.check_balance()
            amount = (
                after_interest - before_interest
            )  # calculate the amount of interest
            print(f"Accumulated ${amount} in interest")

        elif command == "Exit":  # exit the program
            print("Goodbye!")
            break

        elif command == "Transactions":
            atm.print_transactions()

        else:  # if the user enters an invalid command
            print("Command not recognized")
