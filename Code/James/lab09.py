""" blackjack advice """


playing_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]

face = ['q', 'j', 'k', 'a']

# if input == 'q':
#     q = 10
#ask user for 3 playing cards
print('Welcome to Blackjack Advice. Enter faces as Q, J, K or A.')
user_card1 = input('What\'s your first card? ').lower()
user_card1 = int(user_card1)

print(user_card1)

# user_card2 = input('What\'s your second card? ').lower()
# user_card3 = input('What\'s your third card? ').lower()
# total_card = user_card1 + user_card2 + user_card3

#print(total_card)

def face_converter(user):
    #if user enters a str I need to convert that string to the corresponding value
    if user in face:
        user = 10
    else:
        user = str
