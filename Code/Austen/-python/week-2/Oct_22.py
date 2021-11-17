def lab_count_words():
  from requests import get
  from time import sleep

  def getdictionaryfromapi(word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    res = get(url)
    data = res.json()
    res = res.status_code
    return res, data

  def builddictionaryfromfile():
    def formatbook(path):
      import string
      with open(path, 'r', encoding='utf-8') as file:
        book = file.read()
      booklist = book.split()
      file = open(path, 'w')
      file.write('')
      file = open(path, 'a')
      for word in booklist:
        word = list(word.lower())
        formatted = ''
        for char in word:
          if char not in string.punctuation:
            formatted += char
        file.write(f'{formatted} ')

    def builddictionary(path):
      file = open(path)
      book = file.read()
      booklist = book.split()
      rawdictionary = []
      dictionary = {}
      for word in booklist:
        if word not in rawdictionary:
          rawdictionary.append(word)
          word = {word: 1}
          dictionary.update(word)
        else:
          dictionary[f'{word}'] += 1
      return dictionary

    def formatdictionary(dictionary):
      dictionary = list(dictionary.items())
      dictionary.sort(key=lambda tup: tup[0])
      return dictionary

    path = f'X:\pdx-code-guild\Class_Raven\Code\Austen\python\week-2\data\\books\\Craters of the Moon.txt'
    formatbook(path)
    dictionary = builddictionary(path)
    dictionary = formatdictionary(dictionary)
    return dictionary

  def getwordcounts(dictionary, filter):
    def gettopten(dictionary):
      dictionary.sort(key=lambda tup: tup[1], reverse=True)
      top = []
      topten = []
      exclude = ['the', 'a', 'of', 'and', 'to', 'in', 'that',
                 'is', 'on', 'this', 'as', 'by', 'it', 'are', 'from']
      for i in range(min(50, len(dictionary))):
          word = dictionary[i]
          if word[0] not in exclude:
            top.append(word)
      for worddata in top:
        word = worddata[0]
        data = getdictionaryfromapi(word)
        exists = data[0]
        if exists == 200:
          data = data[1]
          data = data[0]
          data = data['meanings']
          data = data[0]
          part = data['partOfSpeech']
          print('checking word')
          if len(topten) < 10:
            if part == 'noun':
              topten.append(worddata)
        if exists != 200:
          top.remove(worddata)

      return topten
    if filter == 'topten':
     results = gettopten(dictionary)
    return results
  dictionary = builddictionaryfromfile()
  results = getwordcounts(dictionary, 'topten')
  counter = 1
  formatted = []
  for word in results:
    result = f'The #{counter} word is: {word[0]} appearing {word[1]} times.\n'
    formatted.append(result)
    print(result)
    counter += 1
    sleep(1)
  print('That\'s all. Thanks for using the word counter. Aloha!')
  print('credits: Craters of the Moon on https://www.gutenberg.org/ebooks/62994')
  results = formatted
  return results
