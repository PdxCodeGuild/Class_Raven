# Christerpher Hunter
# Lab 08: Pick6


from random import randint
from time import time
from colorama import Fore as F

R = F.RESET


class Pick6:
    """Generate and pick winners at random"""

    def __init__(self, winning_ticket: list) -> None:

        self.balance = int()
        self.earnings = float()
        self.expenses = float()
        self.winning_ticket = winning_ticket
        self.user_ticket = list()
        self.matches, self.temp_matches = int(), int()

    def pick6(self) -> None:
        """Generate 6 random numbers"""

        # Generate the user ticket of 6 numbers
        self.user_ticket = list()
        for _ in range(6):

            self.user_ticket.append(randint(1, 99))

    def purchase(self) -> None:
        """Take in balance and subtract the ticket cost"""

        # Subtract $2 from the balance and return balance
        self.balance += -2

        # Keep track of expenses
        self.expenses += 2

    def matched(self) -> None:
        """Compare the user number to the winning numbers"""

        # Find the number of matches
        self.temp_matches = 0
        for i in range(6):
            if self.winning_ticket[i] == self.user_ticket[i]:
                self.matches += 1
                self.temp_matches += 1

    def add_winnings(self) -> None:
        """Add the winning to the running balance"""

        # Calculate the amount of winnings to award and track winnings
        match self.temp_matches:
            case 1:
                self.balance += 4
                self.earnings += 4
            case 2:
                self.balance += 7
                self.earnings += 7
            case 3:
                self.balance += 100
                self.earnings += 100
            case 4:
                self.balance += 50_000
                self.earnings += 50_000
            case 5:
                self.balance += 1_000_000
                self.earnings += 1_000_000
            case 6:
                self.balance += 25_000_000
                self.earnings += 25_000_000
            case _:
                self.balance += 0
                self.earnings += 0

    def ROI(self) -> list:
        """Calculate ROI, earnings, and expenses"""

        self.balance -= self.expenses
        roi = ((self.earnings - self.expenses) / self.expenses) * 100

        return roi, self.earnings, self.expenses, self.balance


def main() -> None:
    """Testing and execution"""

    winning_ticket = list()
    for _ in range(6):
        winning_ticket.append(randint(1, 99))
    print(f"Winning Numbers: {winning_ticket}")

    game = Pick6(winning_ticket)
    begin_time = time()
    for _ in range(100_000):
        game.pick6()
        game.purchase()
        game.matched()
        game.add_winnings()

    end_time = time()

    print(f"\n\nROI: {F.YELLOW}{game.ROI()[0]:,.2f}{R}%\n\
Earnings: ${F.GREEN}{game.ROI()[1]:,.2f}{R}\n\
Expenses: ${F.GREEN}{game.ROI()[2]:,.2f}{R}\n\
Balance: ${F.GREEN}{game.ROI()[3]:,.2f}{R}\n")

    print(f"Run time: {F.RED}{end_time - begin_time:.6f}{R} secs")
    print(f"Number of matches: {F.CYAN}{game.matches:,}{R}")


if __name__ == "__main__":
    main()
