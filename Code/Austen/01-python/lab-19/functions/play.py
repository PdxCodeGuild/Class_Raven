def play(content):
    import html
    import random
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
    return result
