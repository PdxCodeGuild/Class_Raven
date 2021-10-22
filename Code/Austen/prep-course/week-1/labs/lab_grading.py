import random
# Determine rival's grade.
rival = int(random.random() * 100)
if rival < 50:
  rival *= 1.5
# User inputs grade.
grade = int(input('grade: '))
# Determine winner.
if rival > grade:
  winner = 'Your rival'
elif rival < grade:
  winner = 'You'
else:
  winner = 'Nobody'
# Determine user's letter grade
if grade < 0:
  winner = 'invalid'
  letter_grade = 'invalid'
elif grade < 60:
  letter_grade = 'F'
elif grade < 70:
  letter_grade = 'D'
elif grade < 80:
  letter_grade = 'C'
elif grade < 90:
  letter_grade = 'B'
elif grade <= 100:
  letter_grade = 'A'
else:
  winner = 'invalid'
  letter_grade = 'invalid'
# Add letter grade modifier if needed.
modifier = grade % 10
if letter_grade == 'F':
  letter_grade = letter_grade
elif grade == 100:
  letter_grade = 'A+'
elif modifier >= 7:
  letter_grade += '+'
elif modifier <=3:
  letter_grade += '-'
# Display result
print(winner + ' won. ' + 'Your grade: ' + letter_grade)