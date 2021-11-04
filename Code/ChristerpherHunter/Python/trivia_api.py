"""
Christerpher Hunter
Lab 19: Trivia API

Send a request that will return a list of 10 true/false computer questions.
Ask the user each question, ask them for their answer, and keep track of
the score. At the end show them how many they got correct/incorrect.
"""

from requests import get, Session
from json import loads
from html import unescape
from colorama import Fore as F

R = F.RESET


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
            10: ques_10
        }

    def user_answers(self) -> list:
        """Store the user answers"""

        usr_answers = []
        truthy = []
        holding = self.fix_text()

        print(f"\n{F.YELLOW}Please answer True or False:{R} ")
        for i in holding:
            print(f"\n{F.YELLOW}Question:{R} {i}")
            usr_answers.append(input(f"{holding[i]}: "))
            match usr_answers[i - 1].lower():
                case "true":
                    truthy.append(1)
                case "false":
                    truthy.append(0)
                case _:
                    print(f"{F.RED}INVALID INPUT{R}")

        return truthy

    def get_results(self) -> dict:
        """Get the answers to the quiz"""

        ans_01 = loads(self.url.text)["results"][0]["correct_answer"]
        ans_02 = loads(self.url.text)["results"][1]["correct_answer"]
        ans_03 = loads(self.url.text)["results"][2]["correct_answer"]
        ans_04 = loads(self.url.text)["results"][3]["correct_answer"]
        ans_05 = loads(self.url.text)["results"][4]["correct_answer"]
        ans_06 = loads(self.url.text)["results"][5]["correct_answer"]
        ans_07 = loads(self.url.text)["results"][6]["correct_answer"]
        ans_08 = loads(self.url.text)["results"][7]["correct_answer"]
        ans_09 = loads(self.url.text)["results"][8]["correct_answer"]
        ans_10 = loads(self.url.text)["results"][9]["correct_answer"]

        return {
            1: ans_01,
            2: ans_02,
            3: ans_03,
            4: ans_04,
            5: ans_05,
            6: ans_06,
            7: ans_07,
            8: ans_08,
            9: ans_09,
            10: ans_10
        }

    def get_answers(self) -> list:
        """Store correct answers to be manipulated later"""

        hiding = self.get_results()
        correct_answer = []
        ansy = []

        for i in hiding:
            correct_answer.append(hiding[i])
            match correct_answer[i - 1].lower():
                case "true":
                    ansy.append(1)
                case "false":
                    ansy.append(0)
                case _:
                    print(f"{F.RED}UNEXPECTED INPUT{R}")

        return ansy

    def publish_findings(self) -> int:
        """Publish the quiz results"""

        truthy = self.user_answers()
        ansy = self.get_answers()
        correct = int() + sum(truthy[i] == ansy[i] for i in range(len(truthy)))

        return correct


def main() -> None:

    api = Trivia()

    holding = api.publish_findings()
    print(f"\nYou know {F.CYAN}{holding}{R} correct answers "
          f"of {F.RED}10{R}.\n")


if __name__ == "__main__":
    main()
