print("Blackjack Advisor")
import random
hand = []
hand_value = 0
card_values = {
'AD':1, '2D':2, '3D':3, '4D':4, '5D':5, '6D':6, '7D':7, '8D':8, '9D':9, '10D':10, 'JD':10, 'QD':10, 'KD':10,
'AC':1, '2C':2, '3C':3, '4C':4, '5C':5, '6C':6, '7C':7, '8C':8, '9C':9, '10C':10, 'JC':10, 'QC':10, 'KC':10,
'AS':1, '2S':2, '3S':3, '4S':4, '5S':5, '6S':6, '7S':7, '8S':8, '9S':9, '10S':10, 'JS':10, 'QS':10, 'KS':10,
'AH':1, '2H':2, '3H':3, '4H':4, '5H':5, '6H':6, '7H':7, '8H':8, '9H':9, '10H':10, 'JH':10, 'QH':10, 'KH':10, 
}
deck_of_cards=(
'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC',
'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 
)

def draw_card(deck):
    draw = random.choice(deck_of_cards)
    if draw not in hand:
        hand.append(draw)
    else:
        draw_card(deck_of_cards)
    return hand

def play_blackjack(deck):
    while len(hand) <3:
        draw_card(deck_of_cards)
    return hand

play_blackjack(deck_of_cards)
print(hand)

for card in hand:
    hand_value += card_values.get(card)
    
    print(hand_value)

if hand_value < 17:
    print(f"{hand_value} You can't win with that... 'HIT'")
elif hand_value >= 17 and hand_value < 21:
    print(f"{hand_value} Better STAY there, amigo.")
elif hand_value == 21:
    print(f"{hand_value} Heck yeah! Blackjack!")
elif hand_value > 21:
    print(f"{hand_value} Well shoot! You already Busted.  Better luck next hand.")