"""
Christerpher Hunter
Lab 17: Trivia API

Send a request that will return a list of 10 true/false computer questions.
Ask the user each question, ask them for their answer, and keep track of
the score. At the end show them how many they got correct/incorrect.
"""

from requests import get, Session
from json import loads
from html import unescape


class Trivia:
    """Reach out to the Trivia API"""

    def __init__(self) -> None:

        self.url = \
            "https://opentdb.com/api.php?amount=10&category=18&type=boolean"

    def touch_api(self) -> object:
        """Get the information from the API"""

        with Session():
            self.url = get(self.url)

        return self.url

    def fix_text(self) -> dict:
        """Format the incoming information"""

        self. url = self.touch_api()

        ques_01 = unescape(loads(self.url.text)["results"][0]["question"])
        ques_02 = unescape(loads(self.url.text)["results"][1]["question"])
        ques_03 = unescape(loads(self.url.text)["results"][2]["question"])
        ques_04 = unescape(loads(self.url.text)["results"][3]["question"])
        ques_05 = unescape(loads(self.url.text)["results"][4]["question"])
        ques_06 = unescape(loads(self.url.text)["results"][5]["question"])
        ques_07 = unescape(loads(self.url.text)["results"][6]["question"])
        ques_08 = unescape(loads(self.url.text)["results"][7]["question"])
        ques_09 = unescape(loads(self.url.text)["results"][8]["question"])
        ques_10 = unescape(loads(self.url.text)["results"][9]["question"])

        return {
            1: ques_01,
            2: ques_02,
            3: ques_03,
            4: ques_04,
            5: ques_05,
            6: ques_06,
            7: ques_07,
            8: ques_08,
            9: ques_09,
            10: ques_10,
        }


def main() -> None:

    api = Trivia()

    holding = api.fix_text()
    for key in holding:
        print(f"\n{holding[key]}\n")


if __name__ == "__main__":
    main()
