# Christerpher Hunter
# Lab 09: Blackjack Advice


class Blackjacked:
    """Take in 3 card and advise to Hit or Stay"""

    def __init__(self, card_1: str, card_2: str, card_3: str) -> None:
        """Internal variables"""

        self.__card_1 = card_1.upper()
        self.__card_2 = card_2.upper()
        self.__card_3 = card_3.upper()
        self.probability = float()
        self.advice = str()
        self.total = int()

    def grade_cards(self) -> None:
        """Assign value to the given cards"""

        for card in [self.__card_3, self.__card_2, self.__card_1]:

            match card:
                case 'A':
                    if self.total >= 11:
                        self.total += 1
                    else:
                        self.total += 11
                case 'K' | 'J' | 'Q' | '10':
                    self.total += 10
                case '9':
                    self.total += 9
                case '8':
                    self.total += 8
                case '7':
                    self.total += 7
                case '6':
                    self.total += 6
                case '5':
                    self.total += 5
                case '4':
                    self.total += 4
                case '3':
                    self.total += 3
                case '2':
                    self.total += 2
                case '1':
                    self.total += 1
                case 'A':
                    self.total += 0
                case _:
                    print("Invalid input")
                    exit()

    def probability(self) -> None:
        """Determine the probability"""

    def adviced(self) -> None:
        """Make an informed decision"""

        if self.total > 21 and self.__card_2 == 'A':
            self.total -= 10

        match self.total:
            case 21:
                self.advice = "Blackjack!"
            case 20:
                self.advice = "Stay"
            case 19:
                self.advice = "Stay"
            case 18:
                self.advice = "Stay"
            case 17:
                self.advice = "Stay"
            case 16:
                self.advice = "Stay"
            case 15:
                self.advice = "Stay"
            case 14:
                self.advice = "Hit"
            case 13:
                self.advice = "Hit"
            case 12:
                self.advice = "Hit"
            case 11:
                self.advice = "Hit"
            case 10:
                self.advice = "Hit"
            case 9:
                self.advice = "Hit"
            case 8:
                self.advice = "Hit"
            case 7:
                self.advice = "Hit"
            case 6:
                self.advice = "Hit"
            case 5:
                self.advice = "Hit"
            case 4:
                self.advice = "Hit"
            case _:
                self.advice = "Bust!"

        print(f"{self.total} {self.advice}")


def main() -> None:
    """Execution and Testing"""

    card_1 = input("\nPlease enter your first card: ")
    card_2 = input("Please enter your second card: ")
    card_3 = input("Please enter your third card: ")

    game = Blackjacked(card_1, card_2, card_3)

    game.grade_cards()
    game.adviced()


if __name__ == "__main__":
    main()
