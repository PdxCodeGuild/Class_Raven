playing_cards = {    # Assigning the point value of each card individually
'A': 1, 
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
'10': 10,
'J': 10,
'Q': 10,
'K': 10
}

while True:

    p_card1 = input("What's your first card? ")
    p_card2 = input("What's your second card? ")
    p_card3 = input("What's your third card? ")

    p_card1 = playing_cards[p_card1]
    p_card2 = playing_cards[p_card2]
    p_card3 = playing_cards[p_card3]

    current_hand = p_card1 + p_card2 + p_card3
    if current_hand < 17:
        print(f"{current_hand} Hit \n")
    elif current_hand >= 17 and current_hand < 21:
        print(f"{current_hand} Stay \n")
    elif current_hand == 21:
        print(f"{current_hand} Blackjack! ")
        break
    elif current_hand > 21:
        print(f"{current_hand} Already Busted ")
        break
