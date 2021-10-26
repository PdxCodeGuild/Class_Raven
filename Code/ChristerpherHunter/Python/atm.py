"""
Christerpher Hunter
Lab 14: ATM
Let's represent an ATM with a class containing two attributes: a balance
and an interest rate. A newly created account will default to a balance of
0 and an interest rate of 0.1%. Implement the initializer, as well as the
following functions:

- `check_balance()` returns the account balance
- `deposit(amount)` deposits the given amount in the account
- `check_withdrawal(amount)` returns true if the withdrawn amount won't put
     the account in the negative
- `withdraw(amount)` withdraws the amount from the account and returns it
- `calc_interest()` returns the amount of interest calculated on the account
"""

from colorama import Fore as F

R = F.RESET


class ATM:
    """Automated Teller Machine"""

    def __init__(self) -> None:

        self.__balance = 0
        self.__interest = 0.01
        self.transaction_num = int()
        self.user_input = str()

        print(f"\n{F.GREEN}Welcome to the ATM:{R} ")

    def menu(self) -> None:
        """Display the menu and act on the selections"""

        while self.user_input != 'q' or "":

            print("\nPlease enter from the following list:\n\
                1: Balance\n\
                2: Deposit\n\
                3: Withdraw\n\
                4: Interest\n\
                5: Exit")
            self.user_input = input()

            match self.user_input:
                case "1":
                    ATM.balance()
                case "2":
                    user_input = input("Deposit amount: ")
                    ATM.deposit(user_input)
                    ATM.transactions()
                case "3":
                    withdraw_amnt = float(input("Withdraw amount: "))
                    ATM.withdraw(withdraw_amnt)
                    ATM.transactions()
                case "4":
                    interest_chng = float(input("Interest rate: "))
                    interest_chng = interest_chng % 100
                    ATM.interest(interest_chng)
                case "5":
                    ATM.quit()
                case _:
                    print(f"{F.RED}INVALID INPUT: {self.user_input}{R}")
                    continue

    def balance(self) -> None:
        """Return the present balance"""

        print(f"\n{F.YELLOW}Balance:{R} {self.__balance}")

    def deposit(self, input: float) -> None:
        """Deposit doll hairs into the account balance"""

        self.transaction_num += 1
        self.__balance += input

    def withdraw(self, input: float) -> None:
        """Subtract monies from the account balance"""

        self.transaction_num += 1
        self.__balance -= input

    def interest(self, input: float) -> None:
        """Change the interest amount"""

        self.__interest = input

    def transactions(self) -> None:
        """Keep a log of all transctions"""

        with open("ATM_log.txt", "a") as f_write:
            f_write.write(f"Transaction number: {self.transaction_num}\n\
                           Balance: {self.__balance}\n\
                           Interest rate: {self.__interest}")

    def quit(self) -> None:
        """Exit the ATM menu"""

        print(f"{F.GREEN}Thanks you for choosing Hunter ATM's for your\
            business today!{R}")
        exit()
