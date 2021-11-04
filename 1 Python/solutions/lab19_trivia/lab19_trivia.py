import requests
import html
from question_options import difficulties, types, categories 

class Trivia:
    def __init__(self):
        self.questions = self.fetch_questions()
        self.options = {
            'difficulties': difficulties,
            'types': types,
            'categories': categories
        }
        self.score = 0
        self.current_question = 0

    def fetch_questions(self, total_questions=10, category=18, question_type='boolean'):
        url = f"https://opentdb.com/api.php?amount={total_questions}&category={category}&type={question_type}"
        response = requests.get(url)

        results = response.json()['results']

        # if not results:
        #     "ERROR"
        questions = []
        for datum in results:
            question = {
                'text': html.unescape(datum['question']),
                'correct_answer': datum['correct_answer'],
                'incorrect_answers': datum['incorrect_answers'][0] if datum['type'] == 'boolean' else datum['incorrect_answers'], # ternary
                'category': datum['category'],
                'type': datum['type'],
                'user_answer': None,
                'was_answered_correctly': False
            }
            questions.append(question)
        return questions
        
    def answer_is_correct(self, question, answer_attempt):
        '''Return a boolean indicating if the answer_attempt is the correct_answer'''
        if question['type'] == 'boolean':
            return question['correct_answer'] == answer_attempt

    @property
    def total_questions(self):
        return len(self.questions)

    def __str__(self):
        return f'Question {self.current_question + 1} of {len(self.questions)}'


if __name__ == '__main__':
    def get_custom_settings():
        choices = {
            '1': 'Default settings',
            '2': 'Custom settings'
        }

        # print("Choose settings:")
        # for label, choice in choices.items():
        #     print(f"{label}. {choice}")

    def v1():
        while True:
            game = Trivia()

            print("Welcome to Trivia!\n")

            for question in game.questions:
                print(game)
                print(question['text'])
                game.current_question += 1

                answer = input("True or False: ")
                print()

                if game.answer_is_correct(question, answer):
                    game.score += 1
                    question['was_answered_correctly'] = True

            
            message = f'You got {game.score} out of {game.total_questions} correct!'
            if game.score < 4:
                message += '\nBetter luck next time!'
            elif game.score < 7:
                message += '\nGood work.'
            elif game.score <= 10:
                message += '\nWell done!'

            print(message)


            show_results = input("Do you want to see your results? y/n: ")
            if show_results == 'y':
                for question in game.questions:
                    symbol = "x" if question['was_answered_correctly'] == True else "+"
                    print(f"{symbol} - {question['text']}")
            


            again = input("Do you want to play again? y/n: ")
            if again == 'y':
                print("Okay, let's play again!")

            elif again == 'n':
                print("Goodbye")
                break

    def v2():
        pass


v1()