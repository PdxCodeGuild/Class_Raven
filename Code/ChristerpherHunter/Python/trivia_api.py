"""
Christerpher Hunter
Lab 17: Trivia API

Send a request that will return a list of 10 true/false computer questions.
Ask the user each question, ask them for their answer, and keep track of
the score. At the end show them how many they got correct/incorrect.
"""

from requests import get, Session


class Trivia:
    """Reach out to the Trivia API"""

    def __init__(self) -> None:

        self.url = "https://opentdb.com/api.php?amount=10&category=18&type=boolean"

    def touch_api(self) -> str:
        """Get the information from the API"""

        with Session():
            self.url = get(self.url)

        print(self.url.status_code)


def main() -> None:

    api = Trivia()

    api.touch_api()


if __name__ == "__main__":
    main()
