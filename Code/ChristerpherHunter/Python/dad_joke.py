# Christerpher Hunter
# PDX Codeguild Lab 10: Dad Joke

from requests import get
from random import randint


class Dad_Joke:
    """Pull a dad joke from the Dad Joke API"""

    def __init__(self) -> None:

        self.data = dict()
        self.search_data = dict()
        self.url = "https://icanhazdadjoke.com"
        self.header = {"accept": "application/json"}

    def get_joke(self):
        """Use request library to utilize an API"""

        self.data = get(self.url, headers=self.header).json()

        return self.data

    def search_joke(self, search_term):
        """Search the Dad Joke API for jokes"""

        search_results = list()
        self.search_data = get(f"{self.url}/search?term={search_term}",
                               headers=self.header).json()

        search_results = self.search_data['results'][randint(1, "total jokes")]['joke']

        return search_results


def main() -> None:
    """Execution and testing"""

    dad_joke = Dad_Joke()

    data = dad_joke.get_joke()

    search_data = dad_joke.search_joke("bee")

    print(f"\n{data.get('joke')}\n")

    print(f"\n{search_data}\n")


if __name__ == "__main__":
    main()
