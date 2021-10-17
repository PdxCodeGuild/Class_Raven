# Christerpher Hunter
# PDX Codeguild Lab 10: Dad Joke

from requests import get


class Dad_Joke:
    """Pull a dad joke from the Dad Joke API"""

    def __init__(self) -> None:

        self.dad_joke = dict()

    def get_joke(self):
        """Use request library to utilize an API"""

        self.dad_joke = get("https://icanhazdadjoke.com/application.json")

        return self.dad_joke


def main() -> None:
    """Execution and testing"""

    dad_bod = Dad_Joke()
    print(dad_bod.get_joke)
