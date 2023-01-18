import random
""" blackjack advice """


playing_cards = {'a': 1, 'q': 10, 'j': 10, 'k': 10, '2': 2, '3': 3, 
'4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10
}

hand_values = []

#ask user for 3 playing cards
print('Welcome to Blackjack Advice. Enter faces as Q, J, K or A.')
while True: 
    
    #print('Welcome to Blackjack Advice. Enter faces as Q, J, K or A.')
    user_card1 = input('What\'s your first card?\n>> ').lower().strip(' ')
    if not user_card1.isalnum():
        print('Wrong input please enter only faces or integers.')
        continue
    #returns a string, I need it to return the value from the dictionary.
    if user_card1 in playing_cards:
        user_card1n = playing_cards.get(user_card1)
    
        
    user_card2 = input('What\'s your second card?\n>> ').lower().strip(' ')
    if not user_card2.isalnum():
        print('Wrong input please enter only faces or integers.')
        continue
    
    if user_card2 in playing_cards:
        user_card2n = playing_cards.get(user_card2)

    # print(user_card2)

    user_card3 = input('What\'s your third card? ').lower().strip(' ')
    if not user_card3.isalnum():
        print('Wrong input please enter only faces or integers.')
        continue
    if user_card3 in playing_cards:
        user_card3n = playing_cards.get(user_card3)

    total_card = user_card1n + user_card2n + user_card3n
    # print(f'{user_card1}\n{user_card2}\n{user_card3}')


    if total_card < 17:
        print(f'Your hand is {total_card}')
        user = input('You should hit y/n?:\n>> ')
    elif user == 'y':
        add_card = random.choice(list(playing_cards))
        add_card = playing_cards[add_card]
        print(add_card)
        total_card += add_card

    elif total_card >= 17 and total_card < 21:
        print('stay')
    elif total_card == 21:
        print('Blackjack!')
    elif total_card > 21:
        print('Already Busted')
    elif total_card > 21:
        'a' == 11
    continue





        
    
