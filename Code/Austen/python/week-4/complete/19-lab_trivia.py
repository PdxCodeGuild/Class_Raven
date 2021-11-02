import json
import requests
import html
import random
# *Prompt the user for each of api parameter.
amount = input(
    'Welcome to trivia night!\n  How many questions would you like?\n')
url = f'https://opentdb.com/api.php?amount={amount}'
topics = categories = [
    {'parameter': 'any', 'name': 'Any Category'},
    {'parameter': '9', 'name': 'General Knowledge'},
    {'parameter': '10', 'name': 'Entertainment: Books'},
    {'parameter': '11', 'name': 'Entertainment: Film'},
    {'parameter': '12', 'name': 'Entertainment: Music'},
    {'parameter': '13', 'name': 'Entertainment: Musicals &amp; Theatres'},
    {'parameter': '14', 'name': 'Entertainment: Television'},
    {'parameter': '15', 'name': 'Entertainment: Video Games'},
    {'parameter': '16', 'name': 'Entertainment: Board Games'},
    {'parameter': '17', 'name': 'Science &amp; Nature'},
    {'parameter': '18', 'name': 'Science: Computers'},
    {'parameter': '19', 'name': 'Science: Mathematics'},
    {'parameter': '20', 'name': 'Mythology'},
    {'parameter': '21', 'name': 'Sports'},
    {'parameter': '22', 'name': 'Geography'},
    {'parameter': '23', 'name': 'History'},
    {'parameter': '24', 'name': 'Politics'},
    {'parameter': '25', 'name': 'Art'},
    {'parameter': '26', 'name': 'Celebrities'},
    {'parameter': '27', 'name': 'Animals'},
    {'parameter': '28', 'name': 'Vehicles'},
    {'parameter': '29', 'name': 'Entertainment: Comics'},
    {'parameter': '30', 'name': 'Science: Gadgets'},
    {'parameter': '31', 'name': 'Entertainment: Japanese Anime &amp; Manga'},
    {'parameter': '32', 'name': 'Entertainment: Cartoon &amp; Animations'}
]
print('What topic would you like?')
for topic in topics:
  topic_id = topic['parameter']
  topic = html.unescape(topic['name'])
  print(f'#{topic_id} - {topic}')
topic = input('enter the topic number or any: ')
url += f'&category={topic}'
query = 'Easy, Medium, or Hard questions?'
print(query)
difficulty = input('enter easy, medium, hard or any: ').lower()
url += f'&difficulty={difficulty}'
query = 'Boolean (true/false) or multiple choice questions?'
print(query)
qtype = input('enter boolean, multiple, or any: ')
url += f'&type={qtype}'
# *Include them in the request to get the list of questions.
response = requests.get(url)
content = response.content
content = json.loads(content)
content = content['results']
questions = 0
answers = 0
for item in content:
  #* Decode html using html.unescape('')
  question = html.unescape(item['question'])
  qtype = item['type']
  options = ['True', 'False']
  correct = html.unescape(item['correct_answer'])
  correct_id = ''
  incorrect = html.unescape(item['incorrect_answers'])
  if qtype != 'boolean':
    options = []
    options.append(correct)
    for option in incorrect:
      options.append(option)
  #* Ask the user each question.
  if qtype == 'boolean':
    print(f' True or False: {question}')
  elif qtype == 'multiple':
    print(f' Question: {question}')
    qnumber = 1
    while len(options) > 0:
      option = random.choice(options)
      index = options.index(option)
      if option == correct:
        correct_id = qnumber
      options.pop(index)
      print(f'   #{qnumber} - {option}')
      qnumber += 1
  #* Let the user answer each question.
  answer = input(f'   your answer: ')
  questions += 1
  if answer.lower() == correct.lower():
    answers += 1
  elif answer == correct_id:
    answers += 1
  print(f'   correct answer: {correct}')
#* Show the user their score.
score = round((answers / questions) * 100)
result = f'    You answered {answers} out of {questions} correct.\n   Resulting in a score of {score}%.'
print(result)
