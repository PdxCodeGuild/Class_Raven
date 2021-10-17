# Christerpher Hunter
# Lab 08: Pick6


from random import randint, seed


class Pick6:
    """Generate and pick winners at random"""

    def __init__(self, winning_ticket: list) -> None:

        self.balance = int()
        self.earnings = float()
        self.expenses = float()
        self.winning_ticket = winning_ticket
        self.user_ticket = list()
        self.__matches = int()

    def pick6(self) -> None:
        """Generate 6 random numbers"""

        # Generate the winning & user ticket of 6 numbers
        for _ in range(6):
            self.winning_ticket.append(randint(1, 99))
            seed(_)
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
        for i in range(6):
            if self.winning_ticket[i] == self.user_ticket[i]:
                self.__matches += 1

    def add_winnings(self) -> None:
        """Add the winning to the running balance"""

        # Calculate the amount of winnings to award and track winnings
        match self.__matches:
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

    def ROI(self) -> float:
        """Calculate ROI, earnings, and expenses"""

        roi = (self.earnings - self.expenses) / self.expenses

        return roi, self.earnings, self.expenses


def main() -> None:
    """Testing and execution"""

    winning_ticket = list()
    for _ in range(6):
        winning_ticket.append(randint(1, 99))


if __name__ == "__main__":
    main()
