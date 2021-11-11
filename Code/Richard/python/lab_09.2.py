print("Blackjack Advisor")
import random
hand = []
hand_value = 0
aces = ['AC', 'AD', 'AH', 'AS']
ace_count = 0
card_values = {
'AD':11, '2D':2, '3D':3, '4D':4, '5D':5, '6D':6, '7D':7, '8D':8, '9D':9, '10D':10, 'JD':10, 'QD':10, 'KD':10,
'AC':11, '2C':2, '3C':3, '4C':4, '5C':5, '6C':6, '7C':7, '8C':8, '9C':9, '10C':10, 'JC':10, 'QC':10, 'KC':10,
'AS':11, '2S':2, '3S':3, '4S':4, '5S':5, '6S':6, '7S':7, '8S':8, '9S':9, '10S':10, 'JS':10, 'QS':10, 'KS':10,
'AH':11, '2H':2, '3H':3, '4H':4, '5H':5, '6H':6, '7H':7, '8H':8, '9H':9, '10H':10, 'JH':10, 'QH':10, 'KH':10, 
} #card values to caluclate 21
deck_of_cards=(
'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC',
'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 
) #card to draw and use as keys for value

def draw_card(deck):    #function to draw one card
    draw = random.choice(deck_of_cards)
    if draw not in hand:
        hand.append(draw)
    else:
        draw_card(deck_of_cards)
    return hand

def play_blackjack(deck):   #Function to use draw_card to draw 3 cards 
    while len(hand) <3:
        draw_card(deck_of_cards)
    return hand

play_blackjack(deck_of_cards) #draw 3 cards

print(hand) #cards drawn

for card in hand: #calculate card values towards 21
    hand_value += card_values.get(card)
#    print(hand_value)

for ace in aces: #check how many aces to use the alternate 1 or 11 values tried as a function but couldn't get it working
    if ace in hand:
       ace_count+=1

#print(ace_count) #test to check how many aces in hand and offer advise accordingly 

#advise below
if hand_value < 17:
    print(f"{hand_value} You probably won't win with that... 'HIT'")
elif hand_value >= 17 and hand_value < 21:
    print(f"{hand_value} Better STAY there, amigo.")
elif hand_value == 21:
    print(f"{hand_value} Heck yeah! Blackjack!")
elif hand_value > 21 and ace_count > 0:
        if ace_count == 1:
            print(f"{hand_value} hmmmmm... we can also play this as {hand_value - 10}")
            if hand_value < 17:
                print(f"{hand_value-10}  You probably won't win with that... 'HIT'")
            elif hand_value-10 >= 17 and hand_value-10 < 21:
                print(f"{hand_value-10} Better STAY there, amigo.")
            elif hand_value-10 == 21:
                print(f"{hand_value-10} Heck yeah! Blackjack!")
        elif ace_count == 2:
            print(f"{hand_value} hmmmmm... we can also play this as {hand_value-20}")
            if hand_value-20 < 17:
                print(f"{hand_value-20}  You probably won't win with that... 'HIT'")
            elif hand_value-20 >= 17 and hand_value-20 < 21:
                print(f"{hand_value-20} Better STAY there, amigo.")
        elif ace_count == 3:
            print("Holy smokes!!! let's get over to the the poker table when we are done here.  Three Aces.  Wow!! anyway..")
            print(f"{hand_value} hmmmmm... we can also play this as {hand_value-30}")
            print("SPLIT'em and HIT'em!")
elif hand_value > 21:
    print(f"{hand_value} Well shoot! You already Busted.  Better luck next hand.")