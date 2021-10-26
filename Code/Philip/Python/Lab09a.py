'''Blackjack Advice (Lab09)
By Philip Bartoo
For PDX Code Guild'''

#Take input for three cards
card1 = input("What's your first card? ")
card2 = input("What's your second card? ")
card3 = input("What's your third card? ")

#Build a dictionary for the cards and their values
mydict= {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

#Using the card as the key, extract the dictionary value and assign it to a variable for each card
card_value1 = mydict[card1]
card_value2 = mydict[card2]
card_value3 = mydict[card3]

#Total the value of all cards and print
players_hand = card_value1 + card_value2 + card_value3
print(players_hand)

#Build the logic for whether to hit, stay, blackjack or already busted and store as a message
if players_hand < 17:
    message = 'Hit'
elif 17 <= players_hand < 21:
    message = 'Stay'
elif players_hand == 21:
    message = 'Blackjack'
else:
    message = 'Already busted'

#Print the final message
print(message)
