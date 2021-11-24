def build(topics):
  import html
  print('Welcome to trivia night!\n  How many questions would you like?')
  amount = input('enter a number: ')
  url = f'https://opentdb.com/api.php?amount={amount}'

  print('Which topic would you like?')

  for topic in topics:
    name = html.unescape(topic['name'])
    print(topic['parameter'], name)
  topic = input('enter the topic number or any: ')
  url += f'&category={topic}'

  print('Easy, Medium, or Hard questions?')
  difficulty = input('enter easy, medium, hard or any: ').lower()
  url += f'&difficulty={difficulty}'

  print('Boolean (true/false) or multiple choice questions?')
  qtype = input('enter boolean, multiple, or any: ')
  url += f'&type={qtype}'
  return url
