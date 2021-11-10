def importutilities():
  import sys
  utilspath = 'X:\\pdx-code-guild\\Class_Raven\\Code\\Austen\\'
  sys.path.append(utilspath)

def lab_dad_jokes():
  import requests
  importutilities()
  from utilities.valid import answers
  url = 'https://icanhazdadjoke.com/'

  def random():
    res = requests.get(url, headers={"Accept": "application/json"})
    res = res.json()
    joke = res['joke']
    return joke

  def search(url):
    start = 'yes'
    while start == 'yes':
      term = input('enter the word you\'d like to search by \n')
      search_url = f'{url}search?term={term}'
      print(search_url)
      res = requests.get(
          search_url, headers={"Accept": "application/json"})
      res = res.json()
      resjokes = res['results']
      jokes = []
      for joke in resjokes:
        joke = joke['joke']
        jokes.append(joke)
      counter = 1
      while counter <= len(jokes):
        next = input(f'Would you like to see the first {term} joke? \n')
        while next == 'yes':
          for joke in jokes:
            print(f'\njoke {counter} of {len(jokes)}:\n {joke}\n')
            counter += 1
            if counter <= len(jokes):
                next = input(f'Would you like to see the next {term} joke? \n')
      start = input('Would you like to search again?\n')
    return jokes

  options = ['random', 'search', 'done']
  selection = input(
      'Would you like a random joke or would you like to search for something specific? \n')
  selection = answers.validate(selection, options)
  while selection != 'done':
    if selection == 'random':
      joke = random()
    if selection == 'search':
      joke = search(url)
    selection = input(
        'Would you like a random joke or would you like to search for something specific? \n')
    print(joke)
  return joke
