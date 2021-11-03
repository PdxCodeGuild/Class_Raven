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

        self.__balance = float()
        self.__interest = 0.01
        self.user_input = str()
        self.filename = "ATM_log.txt"

        print(f"\n{F.GREEN}Welcome to the ATM:{R} ")

    def balance(self) -> None:
        """Return the present balance"""

        try:
            with open(self.filename, "r", encoding="UTF-8") as f_read:
                line = [line for line in f_read.readlines() for i in line if i.isdigit()]
                print(line)
        except FileNotFoundError:
            print(f"{F.RED}NO PREVIOUS INPUT{R}")

        print(f"\n{F.YELLOW}Balance:{R} {self.__balance:.2f}")

    def deposit(self, input: float) -> None:
        """Deposit doll hairs into the account balance"""

        self.__balance += input if (input > 0) else\
            (print(f"{F.RED}INVALID INPUT{R}"), self.quit())

        with open(self.filename, "a") as f_write:
            f_write.write(f"\nuser deposited $ {input:.2f}")
            # f"{self.__interest:.2f}\n")

    def withdraw(self, input: float) -> None:
        """Subtract monies from the account balance"""

        temp_balance = self.__balance - input
        self.__balance -= input if input < self.__balance else 0

        if temp_balance < 0:
            print("INSUFFICIENT FUNDS")
        else:
            with open(self.filename, "a") as f_write:
                f_write.write(f"user withdrew ${input}\n")

    def interest(self, input: float) -> None:
        """Change the interest amount"""

        self.__interest = input if (input < 1 and input > 0) else\
            (print(f"{F.RED}INVALID INPUT{R}"), self.quit())

        interest_amount = self.__balance * self.__interest
        print(f"{F.YELLOW}The interest accrued is: ${interest_amount:.2f}{R}")

    def quit(self) -> None:
        """Exit the ATM menu"""

        print(f"{F.GREEN}Thanks you for choosing Hunter ATM's for your"
              f"business today!{R}\n")
        exit()

    def menu(self) -> None:
        """Display the menu and act on the selections"""

        while self.user_input != 'q' or "":

            print("\nPlease enter from the following list: \n"
                  "1: Balance\n"
                  "2: Deposit\n"
                  "3: Withdraw\n"
                  "4: Interest\n"
                  "5: Transactions\n"
                  "6: Exit")
            self.user_input = input()

            match self.user_input:
                case "1":
                    self.balance()
                case "2":
                    user_input = float(input("Deposit amount: "))
                    self.deposit(int(user_input))
                case "3":
                    withdraw_amnt = float(input("Withdraw amount: "))
                    self.withdraw(withdraw_amnt)
                case "4":
                    interest_chng = float(input("Interest rate: "))
                    interest_chng = interest_chng % 100
                    self.interest(interest_chng)
                case "5":
                    try:
                        with open(self.filename, "r") as f_read:
                            print(f"\n{f_read.read()}")
                    except FileNotFoundError:
                        print(f"{F.RED}NO TRANSACTIONS MADE YET{R}")
                case "6":
                    self.quit()
                case _:
                    print(f"{F.RED}INVALID INPUT: {self.user_input}{R}")
                    continue


def main() -> None:

    atm = ATM()
    atm.menu()


if __name__ == "__main__":
    main()
