""" blackjack advice """


playing_cards = {'a': 1, 'q': 10, 'j': 10, 'k': 10, '2': 2, '3': 3, 
'4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10
}

hand_values = []
#

# if input == 'q':
#     q = 10
#ask user for 3 playing cards
print('Welcome to Blackjack Advice. Enter faces as Q, J, K or A.')
while True: 
    
    #print('Welcome to Blackjack Advice. Enter faces as Q, J, K or A.')
    user_card1 = input('What\'s your first card? ').lower().strip(' ')
    #give error if user input isnt in the dictionary
    if not user_card1 in playing_cards:
        print('Wrong input please enter only faces or integers.')
        continue
    
    if user_card1 in playing_cards:
        user_card1n = playing_cards.get(user_card1)
    total_card = user_card1n + 0
    
    if total_card < 21:
        playing_cards['a'] = 11
    else:
        playing_cards['a'] = 1

    # print(user_card1)
        
    user_card2 = input('What\'s your second card? ').lower().strip(' ')
    if not user_card2 in playing_cards:
        print('Wrong input please enter only faces or integers.')
        continue
    
    if user_card2 in playing_cards:
        user_card2n = playing_cards.get(user_card2)
    
    total_card = user_card1n + user_card2n
    if total_card < 21:
        playing_cards['a'] = 11
    else:
        playing_cards['a'] = 1

    # print(user_card2)

    user_card3 = input('What\'s your third card? ').lower().strip(' ')
    if not user_card1 in playing_cards:
        print('Wrong input please enter only faces or integers.')
        continue
    if user_card3 in playing_cards:
        user_card3n = playing_cards.get(user_card3)
    
    total_card = user_card1n + user_card2n + user_card3n
    if total_card < 21:
        playing_cards['a'] = 11
    else:
        playing_cards['a'] = 1
    

    total_card = user_card1n + user_card2n + user_card3n
    
    print(f'Your total amount was {total_card}')

    # need to change one of the aces to 11 if the total is below 21
    # if total_card < 21:
    #     playing_cards['a'] = 11
    if total_card < 17:
        print('Hit!')
    elif total_card >= 17 and total_card < 21:
        print('stay')
    elif total_card == 21:
        print('Blackjack!')
    elif total_card > 21:
        print('Already Busted')
    
        
    continue


#print(total_card)
# def check_card(user):
#     for x in playing_cards:
#         if user == x:
#             print(x)

# check_card(user_card1)


        
    
